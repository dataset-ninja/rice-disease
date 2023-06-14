# https://www.kaggle.com/datasets/nischallal/rice-disease-dataset

import glob
import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_name,
    get_file_name_with_ext,
)

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "Rice Disease"
dataset_path = "./APP_DATA/RiceDiseaseDataset_yolo_test"
bbox_ext = ".txt"
images_folder = "images"
anns_folder = "labels"
batch_size = 30


def create_ann(image_path, ds_name):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    bbox_path = os.path.join(
        image_path.split("images")[0],
        anns_folder,
        ds_name,
        get_file_name(image_path) + bbox_ext,
    )

    if file_exists(bbox_path):
        with open(bbox_path) as f:
            content = f.read().split("\n")

            for curr_data in content:
                if len(curr_data) != 0:
                    curr_data = list(map(float, curr_data.split(" ")))
                    obj_class = idx_to_class[int(curr_data[0])]

                    left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                    right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                    top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                    bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                    rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                    label = sly.Label(rectangle, obj_class)
                    labels.append(label)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


obj_class_spot = sly.ObjClass("Brown_Spot", sly.Rectangle)
obj_class_blast = sly.ObjClass("Rice_Blast", sly.Rectangle)
obj_class_blight = sly.ObjClass("Bacterial_Blight", sly.Rectangle)

idx_to_class = {0: obj_class_spot, 1: obj_class_blast, 2: obj_class_blight}

all_train_images_pathes = glob.glob(dataset_path + "/*/train/*.jpg")
all_valid_images_pathes = glob.glob(dataset_path + "/*/valid/*.jpg")
all_test_images_pathes = glob.glob(dataset_path + "/*/test/*.jpg")

ds_to_pathes = {
    "train": all_train_images_pathes,
    "valid": all_valid_images_pathes,
    "test": all_test_images_pathes,
}


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class_spot, obj_class_blast, obj_class_blight])
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in list(ds_to_pathes.keys()):
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_pathes = ds_to_pathes[ds_name]
        anns_path = os.path.join(dataset_path, ds_name, anns_folder)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

        for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
            img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path, ds_name) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))

    return project

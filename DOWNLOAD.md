Dataset **Rice Disease** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/X/d/00/T49Sh2pkW3nNnCz3AjEBygR1Hwqao7zFVu60jw53VknipoJWfdFY7SUeXFGDY2NphWAAHO0tqeCV8KGA6E7ATrFcb6bPC9DKM13zWBN3ZzOo5WYWVy1tDXvkt65z.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Rice Disease', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/nischallal/rice-disease-dataset/download?datasetVersionNumber=1)
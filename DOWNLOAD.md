Dataset **Rice Disease** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/K/r/h3/AxSYK5XceWzglHiDptKZmbOj8FO3leNIUEjd2lCuThKLTcp7WvkgEPjK9c0Y5Be8MKu7ev0mQpjCwXDQd2qFusM5NTIA6xPIyMEBOZ0HbXsWQYfjVgLsObAGMMvD.tar)

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
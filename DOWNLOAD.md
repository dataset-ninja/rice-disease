Dataset **Rice Disease** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/g/H/3j/wCGz1jorb8VZhlTWq1BC934xhYeEje0lwH9v7nD4I8HVGG8KG5ZfCr9KMwx9YNVJRGqiCP32qh7A9EXVhK8qRqrLw9eKPSSX5TiMt3moF8ix9iMe0ifCbEYMFr4Q.tar)

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

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/nischallal/rice-disease-dataset/download?datasetVersionNumber=1).
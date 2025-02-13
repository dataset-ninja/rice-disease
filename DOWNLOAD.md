Dataset **Rice Disease** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEwMTRfUmljZSBEaXNlYXNlL3JpY2UtZGlzZWFzZS1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICIwaEZMd3oxakF2UnF6dS9OYkpQd3RneHNlYkM3SDdyN3BGaEJtaG5oUkk0PSJ9)

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
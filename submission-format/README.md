
The subject indexing task is predicated only on the `dcterms:subject` property values.

In the evaluation phase, participants will be given a collection of technical records with the subjects hidden.

Consider the following json file

[shared-task-datasets/TIBKAT/all-subjects/data/train/Article/de/3A168396733X.jsonld](https://github.com/jd-coderepos/llms4subjects/blob/main/shared-task-datasets/TIBKAT/all-subjects/data/train/Article/de/3A168396733X.jsonld)

Using this file as an example, the section boxed in green will be empty in the test dataset. 

<img src="URL_TO_IMAGE" width="500" height="300" alt="Alt text for image">

The task is essentially to predict these gnd subjects. 

During the evaluation phase, participants will be expected to predict or classify the relevant gnd subject tags for each test record. The expected output format is simply a list of gnd subject tags, in a corresponding file with the same name as the original test file. A sample expected output file for the file referenced above is added to this directory.
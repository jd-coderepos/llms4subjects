## Submission Guidelines 📄

### Task Overview Recap

The primary focus of LLMs4Subjects is on predicting the values of the `dcterms:subject` property, where the available annotations will be hidden in the test dataset. The list of GND subject term IDs predicted for `dcterms:subject` is treated as the subject classification of technical records.

### Data for Evaluation 📚

During the evaluation phase, starting in January, participants will receive a dataset consisting of technical records similar to those found in the training set, but with the subject classifications removed, i.e. the `dcterms:subject` property will be an empty list.

We use an example training file to illustrate this. 

Consider  [shared-task-datasets/TIBKAT/all-subjects/data/train/Article/de/3A168396733X.jsonld](https://github.com/jd-coderepos/llms4subjects/blob/main/shared-task-datasets/TIBKAT/all-subjects/data/train/Article/de/3A168396733X.jsonld),

in the test dataset, the section highlighted below will be blank:

<img src="https://github.com/jd-coderepos/llms4subjects/blob/main/img/classification-target.png" width="500" height="350" alt="Example of blank subject classification area in test data">

### Evaluation Phase Submissions

For the test dataset provided in the evaluation phase, participants need to apply their systems to predict or classify the `gnd` subject tag IDs for each record in the test dataset.

#### Output Format

The expected output from participants should be a simple list of `gnd` subject tag IDs as a list in `json` format. Each participant must submit their predictions in a file named identically to the corresponding test file, but containing only the predicted subject tags as a list of gnd ids in a json file.

##### Output Example

A sample output file can be found in this repository. Refer to the following link: [submission-format/3A168396733X.json](https://github.com/jd-coderepos/llms4subjects/blob/main/submission-format/3A168396733X.json).

Each output file must include the top 50 GND tag predictions made by your system, arranged in descending order based on model confidence. This order is crucial, as evaluations will be conducted using top-k ranking methods. Ensure that the tags predicted with the highest confidence are listed at the top.

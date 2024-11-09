# Submission Guidelines for the Subject Indexing Task 📄

## Task Overview 🔍

The primary focus of this subject indexing task is on predicting the values of the `dcterms:subject` property, which will be hidden in the test dataset. This property captures the subject classification of technical records.

## Data for Evaluation 📊

During the evaluation phase, participants will receive a dataset consisting of technical records similar to those found in the training set, but with the subject classifications (`dcterms:subject`) removed. 

### Example Data File 📝

You can view a sample of a typical training data file here:
[shared-task-datasets/TIBKAT/all-subjects/data/train/Article/de/3A168396733X.jsonld](https://github.com/jd-coderepos/llms4subjects/blob/main/shared-task-datasets/TIBKAT/all-subjects/data/train/Article/de/3A168396733X.jsonld)

In the test dataset, the section highlighted below will be blank:

<img src="https://github.com/jd-coderepos/llms4subjects/blob/main/img/classification-target.png" width="500" height="350" alt="Example of blank subject classification area in test data">

## Task Objective 🎯

The primary objective for participants is to predict or classify the `gnd` subject tags for each record in the test dataset.

## Output Format 📑

The expected output from participants should be a simple list of `gnd` subject tags. Each participant must submit their predictions in a file named identically to the corresponding test file, but containing only the predicted subject tags.

### Output Example 📋

For a detailed example of the expected output format, please refer to the sample output file included in the same directory as the test data.

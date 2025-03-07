# 📚 LLMs4Subjects -- Evaluation

This README provides instructions and information regarding the evaluation process for the LLMs4Subjects shared task. The aim of this task is the development of advanced semantic subject comprehension systems, focusing on the GND taxonomy. Participants are required to submit ranked lists of relevant subjects, which will be evaluated based on several quantitative metrics.

## 📂 Test Dataset

A portion of the TIBKAT collection has been designated as the blind test dataset. In this dataset, subject heading annotations are hidden. This [folder](../shared-task-datasets/TIBKAT/all-subjects/data) contains the test dataset for all-subjects, while the [folder](../shared-task-datasets/TIBKAT/tib-core-subjects/data) contains the test dataset related to tib-core-subject.

Participants must submit a ranked list of the top 50 relevant subjects for each record, ordered by descending relevance.

## 📊 Quantitative Evaluation

The performance of submitted systems will be assessed using the following metrics:

1. **Average Precision@k** for k = 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
2. **Average Recall@k** for k = 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
3. **Average F1-score@k** for k = 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

Evaluation results will be presented at varying levels of granularity to provide comprehensive insights:

1. **Language-level**: Separate evaluations for English and German.
2. **Record-level**: Evaluations for each of the five types of technical records.
3. **Combined Language and Record-levels**: Detailed evaluations combining both language and record type.

## 🛠️ Evaluation Script

Participants are provided with an evaluation [script](llms4subjects-evaluation.py) to test their model performance on the train and dev sets. The same script will be used during the evaluation phase of the shared task.

### Execution Instructions

**🗂️ Step 1: Preparing the Folder Structure**

The script requires a specific folder structure, identical to the train and dev sets, which are organized by record type and language.

Predictions should be stored in a JSON file, named identically to the corresponding record file, containing the predicted subject tags as a list of GND IDs.

**▶️ Step 2: Running the Script**

The script requires three user inputs:

1. The path to the gold-standard dataset with the annotations.
2. The path to the model's predictions.
3. The path to save the results as an Excel file.

The script will generate an Excel file containing the evaluation metrics scores, organized into three different sheets, each corresponding to a different level of granularity.

### 🧑‍💻 Code Execution Sample

```bash
$python llms4subjects-evaluation.py

LLMs4Subjects Shared Task -- Evaluations

Please enter your Team Name
Team Name> test

Please specify the directory containing the true GND labels
Directory path> evaluation/all_subjects

Please specify the directory containing the predicted GND labels
Directory path> evaluation/all_subjects/run1

Please specify the directory to save the evaluation metrics
Directory path> evaluation/results

Reading the True GND labels...
Reading the Predicted GND labels...

Evaluating the predicted GND labels...

File containing the evaluation metrics score is saved at location: evaluation/results/test_evaluation_metrics.xlsx
```

## 🎯 Conclusion

By following these instructions, participants can effectively evaluate their models using the provided script.
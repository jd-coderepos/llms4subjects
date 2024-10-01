## Reproducing the TIBKAT SemEval Dataset and Its Statistics

This repository provides the necessary scripts and workflow to reproduce the SemEval dataset from the publicly available [TIBKAT](https://www.tib.eu/en/services/open-data) bibliographic data.

### Workflow

#### Step 0: Downloading the TIBKAT Data Dump

The first step is to download the TIBKAT data dump from [this link](https://tib.eu/data/rdf/tibkat_rdf_jsonld.tar.gz) and extract the contents to a specific directory. At the time of dataset creation for SemEval, TIBKAT contained 55,361 [JSON-LD](https://json-ld.org/) files, each containing 100 records.

#### Step 1: Reading and Extracting Records from the TIBKAT Data Dump

The script [read_tibkat_resources.py](read_tibkat_resources.py) reads all the records from the TIBKAT data files and saves each valid record in a separate file based on specific validation criteria.

##### Validation and Filtering Criteria

- The record type must be one of the following: Article, Book, Conference, Report, or Thesis.
- The language must be either **English** (en) or **German** (de).
- The record must have a **title** and **abstract**.
- Each record must contain at least one `dcterms:subject` value.

Additionally, records can be filtered to include only those related to TIB Core subject areas. The detailed description of GND subject specifications and TIB Core subjects is discussed in the [shared-task-GND](../shared-task-GND) section. This filtering can be controlled using a boolean variable as follows:

```python
#Include all subjects or only TIB Core subjects
only_TIB_Core_subjects = True
```

**Usage Example**

```console
python read_tibkat_resources.py
```

#### Splitting the Data into Train/Dev/Test Sets

The script [data_splitting.py](data_splitting.py) splits the dataset into training, development, and test sets. These splits will be used later for training and fine-tuning large language models. The default split ratios are:

- **Train** - 60%
- **Dev** - 10%
- **Test** - 30%

These ratios can be modified by updating the `split_ratios` variable:

```python
#Data Splitting Ratios
split_ratios = [0.6, 0.1, 0.3]
```

Before running the script, ensure the dataset path corresponds to the output directory from [read_tibkat_resources.py](read_tibkat_resources.py):

```python
#The path to the Final Dataset
tibkat_resources_dir = '../shared-task-dataset'
```

**Usage Example**

```console
python data_splitting.py
```

#### Step 3: Generating Dataset Statistics

The script [data_statistics.py](data_statistics.py) generates and stores various statistics about the TIBKAT SemEval dataset. Below is a summary of the statistics produced:

1. **Record Type and Language distribution**: Displays the number of records for each record type and language.
2. **Abstract Distribution**: Shows the minimum, maximum, and average number of tokens in abstracts, broken down by record type and language.
3. **Subject Distribution and Frequencies**: Provides the minimum, maximum, and average number of subjects per record type and language, along with a list of unique subjects and their corresponding frequencies.
4. **Unique Subjects per Record Type**: Contains multiple files, each representing the unique subjects for different record types and languages.
5. **Data Splits**: A JSON file detailing the number of records in each data split (train/dev/test) as well as the supplementary dataset.

Before running the script, ensure the dataset path corresponds to the output directory from [read_tibkat_resources.py](read_tibkat_resources.py):

```python
#Final Dataset path
final_dataset_path = '../shared-task-dataset'
```

**Usage Example**

```console
python data_statistics.py
```

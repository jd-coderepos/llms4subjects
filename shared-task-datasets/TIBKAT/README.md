# 📑 The **LLMs4Subjects** Shared Task TIBKAT Dataset

## 🔍 About

TIB subject matter experts index the library’s technical records based on the GND subjects taxonomy. Early in the development of TIB's record annotation guidelines, certain GND subject classes were identified as core to TIB’s focus. However, as technical sciences have advanced, TIB records are now annotated with GND subjects that go beyond those original core subject classes.

Since the TIBKAT dataset compiled for this shared task contains over 100,000 records, we offer participants the option of using a smaller subset. This subset includes only records annotated with at least one GND subject from TIB’s core subject classification scheme.

## 📂 Repositories Included

- [**all-subjects**](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets/TIBKAT/all-subjects) **dataset:** The `train dataset` contains 85,489 records, and the `dev dataset` contains 14,245 records. This dataset is a superset of the dataset linked below and includes all annotated records without restrictions.

- [**tib-core-subjects**](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets/TIBKAT/tib-core-subjects) **dataset:** The `train dataset` contains 41,902 records, and the `dev dataset` contains 6,980 records. In this subset, records are included only if at least one of the annotated GND subjects belongs to TIB's original core subject classification.

Participants can choose between the two datasets based on their project needs—whether to work with the larger, more comprehensive set or focus on a smaller, more manageable subset of records within TIB’s core subject classes for subject indexing.

Each dataset folder is organized into two directories: `data`, which contains the actual dataset files, and `data-statistics`, which provides detailed statistical analyses on various aspects of the dataset.

## 🧐 A Guide to Reading TIBKAT Records

Each TIBKAT technical record in the repositories is provided in `json-ld` format. You can view an example English record [here](https://github.com/jd-coderepos/llms4subjects/blob/main/shared-task-datasets/TIBKAT/all-subjects/data/train/Article/en/3A1499846525.jsonld) and an example German record [here](https://github.com/jd-coderepos/llms4subjects/blob/main/shared-task-datasets/TIBKAT/all-subjects/data/train/Article/de/3A168396733X.jsonld). These files contain various property annotations, with the three most relevant to **LLMs4Subjects** being `title`, `abstract`, and `dcterms:subject`. Participants are free to use other properties as needed. This guide provides an overview of how to interpret a TIBKAT record, focusing on the `dcterms:subject` property.

### [The `dcterms:subject` Property](#how-to-subjects)

The `dcterms:subject` property (often represented as `<dc:subject>` in XML or similar formats) describes the subjects or topics covered by the resource. This includes keywords, phrases, or classification codes that reflect the content. Subject annotations in TIBKAT records are provided by a team of 17 expert subject specialists, covering 28 different subjects, including:

- Architecture, Civil Engineering, Biochemistry, Biology, Chemistry, Chemical Engineering, Electrical Engineering, Energy Technology, Educational Science, Earth Sciences, History, Information Technology, Literary Studies and Linguistics, Mechanical Engineering, Mathematics, Medical Technology, Plant Sciences, Philosophy, Physics, Law, Study of Religions, Social Sciences, Sports Sciences, Theology, Environmental Engineering, Traffic Engineering, Materials Science, and Economics.

#### How to Read the `dcterms:subject` Property

1. **Access the TIBKAT Record:** Start by accessing the JSON-LD TIBKAT records in the dataset or supplementary dataset folders.

2. **Locate the `dcterms:subject` Property:** Find the `dcterms:subject` property in the record. This property may contain one or more subject headings, each sourced from the GND Sachbegriff (subject headings) taxonomy. More information on GND and its role in TIBKAT can be found in the GND shared task dataset subfolder.

3. **Interpret the Subject Entries:** Each entry under the `dcterms:subject` property represents a subject or topic relevant to the resource. These are typically classification codes from the GND subject headings.

4. **Use the Subjects for Research:** The subject codes listed under the `dcterms:subject` property, when mapped to their corresponding labels, are useful for understanding the focus of the resource, conducting research, or finding related materials in the library catalog.

### Conclusion

Understanding the `dcterms:subject` property within TIBKAT records is crucial for researchers, librarians, and anyone working on categorizing or finding resources by subject. By focusing on this property, users can gain insights into the content and relevance of the resources cataloged in the TIBKAT system.

**⚠️ Note:** An additional `subject` property appears in records. This property and its values are not relevant to the scope of the **LLMs4Subjects** shared task. Participants are instructed not to use this property as a signal in training systems, as it will not be included in the test dataset during the evaluation phase.

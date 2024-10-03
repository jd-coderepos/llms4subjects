# 🏷️ The **LLMs4Subjects** Shared Task GND Subjects Taxonomy

## 🔍 About

The [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) (Gemeinsame Normdatei in German or Integrated Authority File in English) is an international authority file primarily used by German-speaking libraries to catalog and link information about people, organizations, topics, and works. As a part of Germany's national library network, TIB also relies on the GND for its subject indexing tasks.

Among the various authority files available in the GND, the only one relevant to TIB's subject indexing and the **LLMs4Subjects** shared task is the `GND Sachbegriff` file. In English, "Sachbegriff" translates to "subject terms."

In the [supplementary-datasets](https://github.com/jd-coderepos/llms4subjects/tree/main/supplementary-datasets) folder, particularly in the [gnd-how-to](https://github.com/jd-coderepos/llms4subjects/tree/main/supplementary-datasets/gnd-how-to) subfolder, we provide detailed step-by-step instructions on how to access the raw data for the GND Sachbegriff file. Using that raw data, we have created a human-readable, decoded version, which participants of the **LLMs4Subjects** shared task can directly download from this repository and use.

Additionally, the `scripts` folder in this repository includes the Python script we used to convert the raw, heavily coded data into the human-readable format that is provided for the shared task. This script is available for participants who may wish to reproduce the workflow or gain a deeper understanding of the process.

The GND subjects taxonomy should be utilized by participants as a comprehensive knowledge base of subjects used for tagging TIB technical records.

## 📂 Repositories Included

- [**dataset**](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets/GND/dataset): Contains the human-readable, comprehensive GND subjects taxonomy files.
- [**scripts**](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets/GND/scripts): Contains the Python script used to recreate the human-readable GND files from raw data.


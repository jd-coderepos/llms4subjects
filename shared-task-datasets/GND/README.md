# 🏷 The **LLMs4Subjects** Shared Task GND Subjects Taxonomy

## 🔍 About

The [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) (Gemeinsame Normdatei in German or Integrated Authority File in English) is an international authority file primarily used by German-speaking libraries to catalog and link information about people, organizations, topics, and works. As a part of Germany's national library network, TIB also relies on the GND for its subject indexing tasks.

Among the various authority files available in the GND, the only one relevant to TIB's subject indexing and the **LLMs4Subjects** shared task is the `GND Sachbegriff` file. In English, "Sachbegriff" translates to "subject terms."

In the [supplementary-datasets](https://github.com/jd-coderepos/llms4subjects/tree/main/supplementary-datasets) folder, particularly in the [gnd-how-to](https://github.com/jd-coderepos/llms4subjects/tree/main/supplementary-datasets/gnd-how-to) subfolder, we provide detailed step-by-step instructions on how to access the raw data for the GND Sachbegriff file. Using that raw data, we have created a human-readable, decoded version, which participants of the **LLMs4Subjects** shared task can directly download from this repository and use.

Additionally, the `scripts` folder in this repository includes the Python script we used to convert the raw, heavily coded data into the human-readable format that is provided for the shared task. This script is available for participants who may wish to reproduce the workflow or gain a deeper understanding of the process.

The GND subjects taxonomy should be utilized by participants as a comprehensive knowledge base of subjects used for tagging TIB technical records.

In addition to the json-Exports of the GND, the German National Library (DNB) has created an **unofficial** Export of the GND from its native raw format into SKOS
for the use within this shared Task. These exports are aligned to the other files as a smaller version in the file `GND-Subjects-tib-core_dnb-skos.ttl` and the
full version with all subject terms (`GND Sachbegriff`) in the file `GND-Subjects-all_dnb-skos.ttl`.

Remarks on the SKOS-Mapping:

  * All Labels are tagged with language code @de, which is not generally true for all entities. There is simply no language tag on record-level in the gnd-native format. 
  * the SKOS-relations broader/ narrower simplfy a system of more then a dozen relation types in the original PICA+ format
  * what information is used to define a SKOS-Collection is disputable. In this export the gnd subject categories, also exported in the JSON-Files in the field `Classification Number`, are used to create the SKOS-Collections. See [the official releases](https://d-nb.info/standards/vocab/gnd/gnd-sc.html) for more information on GND subject categories. 


## 📂 Repositories Included

- [**dataset**](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets/GND/dataset): Contains the human-readable, comprehensive GND subjects taxonomy files.
- [**scripts**](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets/GND/scripts): Contains the Python script used to recreate the human-readable GND files from raw data.


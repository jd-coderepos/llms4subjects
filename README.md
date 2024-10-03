# Welcome to the LLMs4Subjects SemEval 2025 Shared Task Dataset Repository!

## About

The `LLMs4Subjects` shared task invites the research community to develop cutting-edge, LLM-based semantic solutions for automated subject indexing of TIB—the German National Library of Science and Technology’s ever-growing collection of technical records in various natural languages. This task, also known as subject tagging or subject classification, leverages the [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) (Gemeinsame Normdatei in German or Integrated Authority File in English), an international authority file primarily used by German-speaking libraries to catalog and link information on people, organizations, topics, and works.

To support the development of systems for the **LLMs4Subjects** shared task, we provide participants with two types of datasets:

1. **Curated, human-readable form of the GND subjects taxonomy.**
2. **A large-scale dataset of technical records from TIB’s open-access collection, annotated with GND subjects, available in both English and German.**

Although TIB’s technical records span multiple languages, this shared task focuses on the most representative collections in English and German. We have utilized the TIB's open-access catalog of technical records, known as TIBKAT, and restricted it to records that include abstract metadata. This collection can be dynamically browsed on the TIB portal [here](https://www.tib.eu/en/search?tx_tibsearch_search%5Baction%5D=search&tx_tibsearch_search%5Bcnt%5D=20&tx_tibsearch_search%5Bcontroller%5D=Search&tx_tibsearch_search%5BgroupField%5D=matchTitleTypeFirstAuthor_str&tx_tibsearch_search%5Bpg%5D=1&tx_tibsearch_search%5Bquery%5D=prefix%3Atibkat%20%2Babstract%3A%2A%20%2BxmlPath%3Asubject%2F%40type%3Dgnd&cHash=f451c3e5094da4379c764584d10afc8d). While the overall collection includes various types of technical records, this shared task focuses on the most representative types: `article`, `book`, `conference`, `report`, and `thesis`. Therefore, the official shared task dataset comprises only records of these five types.

For the convenience of our participants, both the GND and the TIBKAT datasets have been reorganized, appropriately formatted with human-readable tags, and released as the official shared task dataset in this repository. We recognize that standardized library taxonomies and collections often refer to age-old identifier mechanisms and are filled with codes. Processing and interpreting these codes can be time-consuming. Therefore, in consultation with TIB subject matter experts, we have preprocessed both the GND and TIBKAT datasets, converting their fine-grained coding into human-readable formats. This should help the `LLMs4Subjects` participants download the relevant data and get started right away.

This shared task offers the research community an opportunity to creatively use LLMs for subject tagging of technical records based on the GND taxonomy. Systems need to demonstrate bilingual language modeling by processing technical documents in both German and English. Moreover, successful solutions may be integrated directly into the operational workflows of the TIB Leibniz Information Centre for Science and Technology University Library.

## Repositories Included

- **Shared Task Dataset Repository:** The [dataset](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets) repository includes the training and development sets for both the GND subjects taxonomy and the TIBKAT records. Participants in the `LLMs4Subjects` shared task are requested to download the relevant files from this repository for system development.

- **Supplementary Dataset Repository:** The [supplementary-dataset](https://github.com/jd-coderepos/llms4subjects/tree/main/supplementary-datasets) repository includes all excluded data from the open-access GND and TIBKAT datasets that are not part of the `LLMs4Subjects` shared task. For instance, this may include records from TIBKAT in languages other than English or German or records where a specific record type is too sparse. Although not part of the official shared task, these records are available for participants to use as needed.

## Contact

llms4subjects [at] gmail.com

## Acknowledgements

The LLMs4Subjects shared task, organized as SemEval 2025 Task 5, is jointly supported by the [SCINEXT project](https://scinext-project.github.io/) (BMBF, German Federal Ministry of Education and Research, Grant ID: 01lS22070) and the [NFDI4DataScience initiative](https://www.nfdi4datascience.de/) (DFG, German Research Foundation, Grant ID: 460234259).


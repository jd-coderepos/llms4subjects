Welcome to the LLMs4Subjects SemEval 2025 Shared Task Dataset Repository! 

# About

The `LLMs4Subjects` shared task invites the research community to develop cutting-edge, LLM-based semantic solutions for automated subject indexing of the TIB—the German National Library of Science and Technology's ever-growing collection of technical records in various natural languages. This task, also known as subject tagging or subject classification, utilizes the [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) (Gemeinsame Normdatei in German or Integrated Authority File in English), an international authority file primarily used by German-speaking libraries to catalog and link information such as people, organizations, topics, and works.

To support the development of systems for the **LLMs4Subjects** shared task, we provide participants with two types of datasets:

1. **Curated, human-readable form of the GND subjects' taxonomy**.
2. **A large-scale dataset of technical records from the TIB's open-access collection, annotated with GND subjects and available in either English or German**.

Although the TIB's technical records span various languages, this shared task focuses on the most representative collections in English and German. We have leveraged the TIB's open-access catalogue of technical records, known as TIBKAT, restricting it to records that include abstract metadata. This collection can be dynamically browsed on the TIB portal [here](https://www.tib.eu/en/search?tx_tibsearch_search%5Baction%5D=search&tx_tibsearch_search%5Bcnt%5D=20&tx_tibsearch_search%5Bcontroller%5D=Search&tx_tibsearch_search%5BgroupField%5D=matchTitleTypeFirstAuthor_str&tx_tibsearch_search%5Bpg%5D=1&tx_tibsearch_search%5Bquery%5D=prefix%3Atibkat%20%2Babstract%3A%2A%20%2BxmlPath%3Asubject%2F%40type%3Dgnd&cHash=f451c3e5094da4379c764584d10afc8d). While the overall collection includes various types of technical records, this shared task focuses only on its most representative types: `article`, `book`, `conference`, `report`, and `thesis`. Therefore, the official shared task dataset comprises records of only these five types.

For convenience of our participants, both the GND and the TIBKAT has been reorganized and appropriately formated with human-readable tags and released as the official shared task dataset in this repository. We have noted that standardized library taxonomies and collections refer to age-old identifier mechanisms and ridden with codes. Processing and interpreting all the codes can take a considerable amount of time. Hence for the shared task, also in consultation with the TIB's subject matter experts, we have preprocessed the raw datatsets for both the GND and TIBKAT including its fine-grained coding and converted them into human-readable formats which should help the LLMs4Subjects participants download the relevant data and get started right away.


This shared task offers the research community an opportunity to creatively utilize LLMs for subject tagging of technical records based on the GND taxonomy. Systems need to demonstrate bilingual language modeling by understanding technical documents in both German and English. Moreover, successful solutions may be directly integrated into the operational workflows of the TIB Leibniz Information Centre for Science and Technology University Library.


# Repositories Included

- **Shared Task Dataset Repository:** The [dataset](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets) repository includes the training and developments sets for both the GND subjects taxonomy files and the TIBKAT records. Participants of the `LLMs4Subjects` shared task are requested to download the relevant files from this repository for their systems development.

- **Supplementary Dataset Repository:** The [supplementary-dataset](https://github.com/jd-coderepos/llms4subjects/tree/main/supplementary-datasets) repository

 includes records from TIBKAT that are not part of the main dataset due to being in languages other than English or German, or because the dataset for a specific record type is too sparse. Although the focus is on English and German, these records are made available for participants to utilize as needed.



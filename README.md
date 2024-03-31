# About

The `llms4subjects` repository hosts data designed for a task that involves using large language models (LLMs) for automated subject tagging within the [TIB](https://www.tib.eu/)'s (German National Library of Science and Technology) open access catalogue of technical records, known as TIBKAT, restricted to only those with abstracts metadata. This collection can be browsed on the TIB portal [here](https://www.tib.eu/en/search?tx_tibsearch_search%5Baction%5D=search&tx_tibsearch_search%5Bcnt%5D=20&tx_tibsearch_search%5Bcontroller%5D=Search&tx_tibsearch_search%5BgroupField%5D=matchTitleTypeFirstAuthor_str&tx_tibsearch_search%5Bpg%5D=1&tx_tibsearch_search%5Bquery%5D=prefix%3Atibkat%20%2Babstract%3A%2A%20%2BxmlPath%3Asubject%2F%40type%3Dgnd&cHash=f451c3e5094da4379c764584d10afc8d). The collection, which includes a variety of records like articles, conference proceedings, and books, is already open access but is re-released in this repository as it is specifically systematically re-organized to introduce researchers to the collection, its various formats, and to thereby facilitate researchers to more easily develop their LLM-based applications. The aim is to leverage the best system as the outcome of the proposed task for the automated subject tagging of TIB's future collections, supporting a broader vision of enhancing efficiency through technology.


# Repositories Included

- **Dataset Repository:** The [dataset](https://github.com/jd-coderepos/llms4subjects/tree/main/dataset) repository houses the main training and testing datasets for the shared task. Given that the TIBKAT collections are primarily in German and English, this task will only evaluate LLMs capable of processing both languages.

- **Supplementary Dataset Repository:** The [supplementary-dataset](https://github.com/jd-coderepos/llms4subjects/tree/main/supplementary-dataset) repository includes records from TIBKAT that are not part of the main dataset due to being in languages other than English or German, or because the dataset for a specific record type is too sparse. Although the focus is on English and German, these records are made available for participants to utilize as needed.

- **Analysis Repository:** The [analysis](https://github.com/jd-coderepos/llms4subjects/tree/main/analysis) repository contains statistical information and files detailing the TIBKAT collection's composition, which helped in organizing the main and supplementary datasets.

- **GND How-To Repository:** The [gnd-how-to](https://github.com/jd-coderepos/llms4subjects/tree/main/gnd-how-to) repository provides an introduction to the GND (Gemeinsame Normdatei or Integrated Authority File) taxonomy used for subject classification in TIBKAT, along with detailed instructions on accessing and using the relevant taxonomy file for the collection.


# Released TIBKAT dataset records format

## Introduction

This guide provides an overview of how to interpret a TIBKAT record, with a particular focus on understanding the `dcterms:subject` property. This property is part of the Dublin Core Metadata Element Set, a standard used for describing the content and metadata of web resources.

## Understanding TIBKAT Records
TIBKAT records contain metadata about various resources, such as books, journals, and digital files, cataloged by the German National Library of Science and Technology. These records are structured in a way that includes multiple properties, each describing a different aspect of the resource.

### The `dcterms:subject` Property
The `dcterms` subject property (often represented as `<dc:subject>` in XML or similar syntax) is used to describe the subject or topics covered by the resource. This can include keywords, phrases, or classification codes that reflect the content of the resource. The TIBKAT records subject annotations were made by a dedicated team of 17 expert subject specialists responsible for 28 different subjects, viz. Architecture, Civil Engineering, Biochemistry, Biology, Chemistry, Chemical Engineering, Electrical Engineering, Energy Technology, Educational Science, Earth Sciences, History, Information Technology, Literary Studies and Linguistics, Mechanical Engineering, Mathematics, Medical Technology, Plant Sciences, Philosophy, Physics, Law, Study of Religions, Social Sciences, Sports Sciences, Theology, Environmental Engineering, Traffic Engineering, Materials Science, and Economics.

#### [How to Read the `dcterms:subject` Property](#how-to-read-dctermsubject)
1. **Access the TIBKAT Record:** Begin by accessing the released JSON-LD TIBKAT records in the dataset or supplementary dataset folders.

2. **Locate the `dcterms:subject` Property:** Within the record, look for the `dcterms:subject` property. This property can have one or more subject headings. Each subject heading is obtained from the GND Sachbegriff (subject headings) taxonomy. More information on the GND as it pertains to TIBKAT can be found [here](https://github.com/jd-coderepos/llms4subjects/tree/main/gnd-how-to). 

3. **Interpret the Subject Entries:** Each entry under the `dcterms:subject` property represents a subject or topic that the resource relates to. These entries are available as:
   - **Classification Codes:** Standardized GND subject heading codes can be found as values.

4. **Use the Subjects for Research:** Within libaray systems, the subjects codes listed under the `dcterms:subject` property when mapped to their labels can be valuable for understanding the focus of the resource, conducting research, or finding related materials in the catalog.

## Conclusion

Understanding the `dcterms:subject` property within TIBKAT records is crucial for researchers, librarians, and anyone looking to categorize or find resources based on their subject matter. By focusing on this property, users can gain insights into the content and relevance of resources cataloged in the TIBKAT system.


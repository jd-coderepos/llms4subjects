The **LLMs4Subjects** shared task datasets!

# About

To develop LLM-based solutions for the shared task participants in two main data files. 1. A file with the GND subjects taxonomy as the comprehensive subjects knowledge base for the LLMs and 2. The training and development datasets with technical records annotated with GND subjects as supervision signals for aligning LLMs. Those are the respositories included. Visit each of the repositories and download the relevant corresponding GND subjects file or folder of annotated technical records.  

# Repositories Included

- [**GND**](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets/GND): It contains the preprocessed GND subjects file in human-readable form to use in development of **LLMs4Subjects** shared task systems. Participants are requested to download the pertinent GND subjects file from this repository. Note the [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) (Gemeinsame Normdatei in German or Integrated Authority File in English), is an international authority file primarily used by German-speaking libraries to catalog and link information on people, organizations, topics, and works. Of all files in the GND, the TIB subject matter experts use the GND Sachbegriff (or subject terms file) to catalogue the TIB's technical records.

- [**TIBKAT**](https://github.com/jd-coderepos/llms4subjects/tree/main/shared-task-datasets/TIBKAT): As briefly alluded to above, it contains the selected portion of the subject-indexed or subject-annotated TIBKAT limited to only German and English records and for the following five record types, viz. `article`, `book`, `conference`, `report`, and `thesis`. The dataset is provided with training and development set splits.



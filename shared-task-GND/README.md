## Formatted Human-Readable GND Sachbegriff

This repository provides formatted, human-readable [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) subject specifications, along with scripts to regenerate these from the GND authority metadata files. A more detailed description of GND subject tagging is available in this [repository](../gnd-how-to).

### GND Subject Classification

All GND subjects are categorized based on the concepts they describe. A comprehensive list of all subject categories can be viewed in this [PDF](https://wiki.dnb.de/download/attachments/90411323/gndSyst.pdf). A [JSON](formatted-gnd-subjects/gnd-subjects.json) file has been created from this PDF, containing all subject categories and their names, as well as an indication of whether a subject belongs to the TIB Core list. These subject categories are essential for disambiguating TIBKAT records and filtering TIBKAT records to include only those related to TIB Core subjects.

### Accessing and Downloading GND Authority Data

GND authority metadata is freely available on the official GND website, allowing access to all subject details. A guide on how to download GND authority data is provided in this [repository](../gnd-how-to). After downloading the data, extract the MARC 21 file and save it to a directory in preparation for the next step: creating formatted GND subject specification files.

### Workflow for Formatting GND Subject Specifications

This workflow outlines how to transform the GND subject specification file from the MARC 21 XML format into a more human-readable JSON format, including the relevant attributes for the SemEval shared task, using the [subject_gnd_formatting.py](scripts/subject_gnd_formatting.py) script.

#### **Step 0: JSON Schema for GND Subject Specifications**

The file [GND-Subjects-Schema.json](formatted-gnd-subjects/GND-Subjects-Schema.json) defines the JSON schema for GND subject classification. Nine different attributes from the MARC 21 XML file are used to describe each subject's details.

**Note:** Not all subjects have all these attributes. If an attribute is missing for a given subject, it is omitted in the final JSON file.

#### **Step 1: Updating Paths for MARC 21 XML and Subject Classification Files**

Before running the [subject_gnd_formatting.py](scripts/subject_gnd_formatting.py) script, ensure the paths for the MARC 21 XML file and the subject classification file are updated to the correct locations.

```python
#The path for the GND subject specification file 
subject_gnd_filepath = '../authorities-gnd-sachbegriff_dnbmarc_20240213.mrc.xml'
```

```python
#All GND Subject codes 
gnd_subjects = read_json_file('../formatted-gnd-subjects/gnd-subjects.json')
```

Additionally, you can filter the subjects to include only those part of the TIB Core list by setting the boolean variable as follows:

```python
#Whether to include all GND subjects or only TIB Core subjects
all_subjects = False
```

#### **Step 2: Executing the Script**

To execute the script, run the following command:

```console
python subject_gnd_formatting.py
```
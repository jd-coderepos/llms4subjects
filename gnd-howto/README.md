## About

This readme provides the instructionss to obtain the GND Sachbegriff (subject heading) authority records. E.g., file named as `authorities-gnd-sachbegriff_dnbmarc_20240213.mrc.xml`. 

### I] Instructions to download the latest GND Sachbegriff file

Since the GND is periodically updated, you can follow the following steps to obtain the latest GND Sachbegriff authority records.

#### 1. Access the GND Data
- Go to the [GND homepage](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html).
- Scroll to the **Metadata services** section and select [**Full copies available through WWW/SFTP servers in MARC 21, MARC21-XML**](https://www.dnb.de/EN/Professionell/Metadatendienste/Datenbezug/Gesamtabzuege/gesamtabzuege_node.html).

#### 2. Find the Complete Sets
- On the new page, locate the **Complete sets** section.
- Click the first link in the table to access the [external repository](https://data.dnb.de/GND/) with GND records for various types of entities, viz. persons, corporate bodies, conferences, geographic locations, subject headings, and works. Each file type is provided in the MARC21 or MARC21-xml formats.

(_note: The MARC format was developed by Henriette Avram at the Library of Congress during the 1960s. Avram's work was instrumental in creating a standardized format for the representation and exchange of bibliographic data in machine-readable form, paving the way for modern library cataloging systems. The MARC (Machine-Readable Cataloging) format is a standard for the representation and communication of bibliographic and related information in machine-readable form. It's used by libraries and related organizations to catalog and exchange information about books, journals, and other materials. The format structures data in records, with each record divided into fields that contain specific pieces of bibliographic information_)

#### 3. Download GND Sachbegriff Records
- Search for two files (MARC21 or MARC21-xml formats) containing `gnd-sachbegriff` in its name.
- Download the file with `.xml` extension. Thats it!


### II] Sample GND Sachbegriff record

A file will be a collection of GND Sachbegriff (subject heading) records. Below is one example record.

```
  <record type="Authority">
    <leader>00000nz  a2200000nc 4500</leader>
    <controlfield tag="001">040000028</controlfield>
    <controlfield tag="003">DE-101</controlfield>
    <controlfield tag="005">20100106125650.0</controlfield>
    <controlfield tag="008">880701n||azznnbabn           | ana    |c</controlfield>
    <datafield tag="024" ind1="7" ind2=" ">
      <subfield code="a">4000002-3</subfield>
      <subfield code="0">http://d-nb.info/gnd/4000002-3</subfield>
      <subfield code="2">gnd</subfield>
    </datafield>
    <datafield tag="035" ind1=" " ind2=" ">
      <subfield code="a">(DE-101)040000028</subfield>
    </datafield>
    <datafield tag="035" ind1=" " ind2=" ">
      <subfield code="a">(DE-588)4000002-3</subfield>
    </datafield>
    <datafield tag="035" ind1=" " ind2=" ">
      <subfield code="z">(DE-588c)4000002-3</subfield>
      <subfield code="9">v:zg</subfield>
    </datafield>
    <datafield tag="040" ind1=" " ind2=" ">
      <subfield code="a">DE-101</subfield>
      <subfield code="c">DE-101</subfield>
      <subfield code="9">r:DE-101</subfield>
      <subfield code="b">ger</subfield>
      <subfield code="d">0832</subfield>
    </datafield>
    <datafield tag="042" ind1=" " ind2=" ">
      <subfield code="a">gnd1</subfield>
    </datafield>
    <datafield tag="065" ind1=" " ind2=" ">
      <subfield code="a">31.9b</subfield>
      <subfield code="2">sswd</subfield>
    </datafield>
    <datafield tag="075" ind1=" " ind2=" ">
      <subfield code="b">s</subfield>
      <subfield code="2">gndgen</subfield>
    </datafield>
    <datafield tag="079" ind1=" " ind2=" ">
      <subfield code="a">g</subfield>
      <subfield code="q">s</subfield>
    </datafield>
    <datafield tag="083" ind1="0" ind2="4">
      <subfield code="a">621.381537</subfield>
      <subfield code="9">d:2</subfield>
      <subfield code="9">t:2010-01-06</subfield>
      <subfield code="2">23/ger</subfield>
    </datafield>
    <datafield tag="150" ind1=" " ind2=" ">
      <subfield code="a">A 302 D</subfield>
    </datafield>
    <datafield tag="550" ind1=" " ind2=" ">
      <subfield code="0">(DE-101)040272427</subfield>
      <subfield code="0">(DE-588)4027242-4</subfield>
      <subfield code="0">https://d-nb.info/gnd/4027242-4</subfield>
      <subfield code="a">Integrierte Schaltung</subfield>
      <subfield code="4">obal</subfield>
      <subfield code="4">https://d-nb.info/standards/elementset/gnd#broaderTermGeneral</subfield>
      <subfield code="w">r</subfield>
      <subfield code="i">Oberbegriff allgemein</subfield>
    </datafield>
    <datafield tag="670" ind1=" " ind2=" ">
      <subfield code="a">Vorlage</subfield>
    </datafield>
    <datafield tag="913" ind1=" " ind2=" ">
      <subfield code="S">swd</subfield>
      <subfield code="i">s</subfield>
      <subfield code="a">A 302 D</subfield>
      <subfield code="0">(DE-588c)4000002-3</subfield>
    </datafield>
  </record>
```

#### How to read a GND Sachbegriff Record -- GND Sachbegriff Record Interpretation Guide

A GND (Gemeinsame Normdatei) Sachbegriff record is a structured bibliographic record for ensuring consistency in cataloging across German-speaking libraries. Each part of the record holds specific data about the subject term:

##### Key Components

- **Record Type**: `Authority` indicates a record for standardized information about subjects, persons, organizations, etc.

- **Leader**: Fixed-length field with codes for record characteristics.

- **Control Fields**:
  - `001`: Control number.
  - `003`: Control number identifier (e.g., DE-101).
  - `005`: Date/time of the latest record transaction.
  - `008`: Fixed-length data elements like date entered, publication status, and language.

- **Data Fields**: Contain descriptive information, each identified by a tag number and subdivided into subfields (`subfield code`):
  - `024`, `035`: Standard numbers and identifiers, including the GND identifier and URL to the GND database.
  - `040`: Cataloging source, language, and institution code.
  - `042`: Authentication code.
  - `065`, `075`, `079`: Classification codes.
  - `083`: Classification number with additional elements like assignment date.
  - `150`: Main heading of the subject authority record.
  - `550`: Related subject terms, indicating hierarchical relationships.
  - `670`: Sources of information.
  - `913`: System-specific information.

##### How to minimally read the given sample GND Sachbegriff record above?

- `024` field includes the unique GND identifier and a link to the term's GND record.
- `040` field indicates the cataloging agency (DE-101) and that the record's content is in German.
- `150` field contains the subject heading name, e.g., "A 302 D".
- `550` field shows a related term, e.g., "Integrierte Schaltung" (Integrated Circuit), suggesting a relationship between the subjects.

The sample record's subject heading name is "A 302 D." Regarding the meaning of "A 302 D", without additional context provided in the record or without specific knowledge of this classification, it's challenging to ascertain its precise meaning directly from this snippet alone. However, the `<datafield>` with tag `550` provides a broader term or related subject, which is "Integrierte Schaltung" (Integrated Circuit). This suggests that "A 302 D" might be related to a specific aspect, type, or application of integrated circuits within the classification system used by GND, possibly indicating a specific standard, model, or technology category associated with integrated circuits.

Understanding the structure of these records is crucial for those involved in library and information management.


##### Other examples




### III] MARC 21 tags meaning

The following [script](https://github.com/jd-coderepos/llms4subjects/blob/main/gnd-howto/scripts/print-unique-MARC21-codes.py) reads all records in a GND Sachbegriff file and prints out the unique MARC21 tags seen. The table below shows the set of 36 unique MARC21 tags seen in a recent download of a GND Sachbegriff file.

| MARC 21 data field tags | Description                                           | Link |
|--------------|-------------------------------------------------------|------|
| 024          | Other Standard Identifier                             | [Link](https://www.loc.gov/marc/authority/ad024.html) |
| 035          | System Control Number                                 | [Link](https://www.loc.gov/marc/authority/ad035.html) |
| 040          | Cataloging Source                                     | [Link](https://www.loc.gov/marc/authority/ad040.html) |
| 042          | Authentication Code                                   | [Link](https://www.loc.gov/marc/authority/ad042.html) |
| 043          | Geographic Area Code                                  | [Link](https://www.loc.gov/marc/authority/ad043.html) |
| 065          | Other Classification Number                           | [Link](https://www.loc.gov/marc/authority/ad065.html) |
| 075          | Application History Note                              | [Link](https://www.loc.gov/marc/authority/ad075.html) |
| 079          | GND Control Number                                    | [Link](https://www.loc.gov/marc/authority/ad079.html) |
| 083          | Classification Number                                 | [Link](https://www.loc.gov/marc/authority/ad083.html) |
| 089          | Authority Record Control Number or Standard Number    | [Link](https://www.loc.gov/marc/authority/ad089.html) |
| **150**          | **Main Heading - Subject**                                | [Link](https://www.loc.gov/marc/authority/ad150.html) |
| 260          | Complex See Reference - Subject                       | [Link](https://www.loc.gov/marc/authority/ad260.html) |
| 377          | Associated Language                                   | [Link](https://www.loc.gov/marc/authority/ad377.html) |
| 380          | Form of Work                                          | [Link](https://www.loc.gov/marc/authority/ad380.html) |
| 410          | Series Statement/Added Entry - Subject                | [Link](https://www.loc.gov/marc/authority/ad410.html) |
| 450          | See Also Reference - Subject                          | [Link](https://www.loc.gov/marc/authority/ad450.html) |
| 451          | See Reference - Subject                               | [Link](https://www.loc.gov/marc/authority/ad451.html) |
| 500          | See Also From Tracing - General Subdivision           | [Link](https://www.loc.gov/marc/authority/ad500.html) |
| 510          | See Also From Tracing - Chronological Subdivision     | [Link](https://www.loc.gov/marc/authority/ad510.html) |
| 511          | See Also From Tracing - Geographic Subdivision        | [Link](https://www.loc.gov/marc/authority/ad511.html) |
| 530          | See Also From Tracing - Form Subdivision              | [Link](https://www.loc.gov/marc/authority/ad530.html) |
| 548          | Chronological Term                                    | [Link](https://www.loc.gov/marc/authority/ad548.html) |
| **550**          | **See Also From Tracing - Topical Term (Related Subject Terms)** | [Link](https://www.loc.gov/marc/authority/ad550.html) |
| 551          | Geographic Name                                       | [Link](https://www.loc.gov/marc/authority/ad551.html) |
| 667          | Nonpublic General Note                                | [Link](https://www.loc.gov/marc/authority/ad667.html) |
| 670          | Source Data Found                                     | [Link](https://www.loc.gov/marc/authority/ad670.html) |
| 675          | Source Data Not Found                                 | [Link](https://www.loc.gov/marc/authority/ad675.html) |
| 677          | Definition and Scope Note                             | [Link](https://www.loc.gov/marc/authority/ad677.html) |
| 678          | Biographical or Historical Data                       | [Link](https://www.loc.gov/marc/authority/ad678.html) |
| 680          | Public General Note                                   | [Link](https://www.loc.gov/marc/authority/ad680.html) |
| 682          | Deleted Heading Information                           | [Link](https://www.loc.gov/marc/authority/ad682.html) |
| 700          | Heading - Personal Name                               | [Link](https://www.loc.gov/marc/authority/ad700.html) |
| 750          | Heading - Geographic Name                             | [Link](https://www.loc.gov/marc/authority/ad750.html) |
| 751          | Added Entry - Geographic Name                         | [Link](https://www.loc.gov/marc/authority/ad751.html) |
| 912          | GND Subject Category Code                             | [Link](https://www.loc.gov/marc/authority/ad912.html) |
| 913          | GND Subject Subcategory Code                          | [Link](https://www.loc.gov/marc/authority/ad913.html) |

Data fields with tags `150` and `550` can be seen as central to interpreting a GND Sachbegriff record. The tag `150` supplies the subject heading label. While tag `550` provides a broader term or related subject.




## About

This readme provides the instructionss to obtain the GND Sachbegriff (subject heading) authority records. E.g., file named as `authorities-gnd-sachbegriff_dnbmarc_20240213.mrc.xml`. 

### Instructions to download the latest GND Sachbegriff file

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


### Sample GND Sachbegriff record

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


### Clarification on the MARC 21 codes




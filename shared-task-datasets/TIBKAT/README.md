
- **Analysis Repository:** The [analysis](https://github.com/jd-coderepos/llms4subjects/tree/main/analysis) repository contains statistical information and files detailing the TIBKAT collection's composition, which helped in organizing the main and supplementary datasets.

# Released TIBKAT dataset records format

This guide provides an overview of how to interpret a TIBKAT record, with a particular focus on understanding the `dcterms:subject` property. This property is part of the Dublin Core Metadata Element Set, a standard used for describing the content and metadata of web resources.

## Understanding TIBKAT Records
TIBKAT records contain metadata about various resources, such as books, journals, and digital files, cataloged by the German National Library of Science and Technology. These records are structured in a way that includes multiple properties, each describing a different aspect of the resource.

### [The `dcterms:subject` Property](#how-to-subjects)
The `dcterms` subject property (often represented as `<dc:subject>` in XML or similar syntax) is used to describe the subject or topics covered by the resource. This can include keywords, phrases, or classification codes that reflect the content of the resource. The TIBKAT records subject annotations were made by a dedicated team of 17 expert subject specialists responsible for 28 different subjects, viz. Architecture, Civil Engineering, Biochemistry, Biology, Chemistry, Chemical Engineering, Electrical Engineering, Energy Technology, Educational Science, Earth Sciences, History, Information Technology, Literary Studies and Linguistics, Mechanical Engineering, Mathematics, Medical Technology, Plant Sciences, Philosophy, Physics, Law, Study of Religions, Social Sciences, Sports Sciences, Theology, Environmental Engineering, Traffic Engineering, Materials Science, and Economics.

#### How to read the `dcterms:subject` property

1. **Access the TIBKAT Record:** Begin by accessing the released JSON-LD TIBKAT records in the dataset or supplementary dataset folders.

2. **Locate the `dcterms:subject` Property:** Within the record, look for the `dcterms:subject` property. This property can have one or more subject headings. Each subject heading is obtained from the GND Sachbegriff (subject headings) taxonomy. More information on the GND as it pertains to TIBKAT can be found [here](https://github.com/jd-coderepos/llms4subjects/tree/main/gnd-how-to). 

3. **Interpret the Subject Entries:** Each entry under the `dcterms:subject` property represents a subject or topic that the resource relates to. These entries are available as:
   - **Classification Codes:** Standardized GND subject heading codes can be found as values.

4. **Use the Subjects for Research:** Within libaray systems, the subjects codes listed under the `dcterms:subject` property when mapped to their labels can be valuable for understanding the focus of the resource, conducting research, or finding related materials in the catalog.

## Conclusion

Understanding the `dcterms:subject` property within TIBKAT records is crucial for researchers, librarians, and anyone looking to categorize or find resources based on their subject matter. By focusing on this property, users can gain insights into the content and relevance of resources cataloged in the TIBKAT system.
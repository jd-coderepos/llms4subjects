import xml.etree.ElementTree as ET

def parse_gnd_records(file_path):
    # Define the namespace to handle the XML correctly
    ns = {'marc': 'http://www.loc.gov/MARC21/slim'}
    
    # Parse the XML file, considering the namespace
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Collect unique datafield tag codes
    unique_tags = set()
    
    # To store unique subject headings, use a set to automatically handle uniqueness
    unique_subject_headings = set()
    
    # Iterate over each record in the file
    for record in root.findall('.//marc:record', ns):
        # Iterate over each datafield within the record
        for datafield in record.findall('.//marc:datafield', ns):
            tag = datafield.get('tag')
            unique_tags.add(tag)  # Add the tag to the set of unique tags
            
            # Collect all subfield content for this datafield to identify unique subject headings
            subfield_contents = []
            for subfield in datafield.findall('.//marc:subfield', ns):
                # Combine the code and text of each subfield for detailed identification
                code = subfield.get('code')
                text = subfield.text or ""  # Ensure text is a string even if it is None
                subfield_contents.append(f"{code}:{text}")
            
            # Create a unique identifier for the subject heading based on tag and subfield content
            if subfield_contents:  # Ensure there is subfield content
                subject_heading = f"{tag}|{'|'.join(subfield_contents)}"
                unique_subject_headings.add(subject_heading)
    
    # Print results
    print(f"Unique datafield tag codes: {sorted(unique_tags)}")
    print(f"Total number of unique subject headings: {len(unique_subject_headings)}")

# Replace 'your_file_path_here.xml' with the actual path to your GND records file
file_path = 'C:/Users/dsouzaj/Desktop/Submissions/SemEval 2025 Shared Task - Subject Indexing/gnd dataset/authorities-gnd-sachbegriff_dnbmarc_20240213.mrc.xml'
parse_gnd_records(file_path)

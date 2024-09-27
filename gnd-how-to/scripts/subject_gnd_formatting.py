import os
import re
import json
import xml.etree.ElementTree as ET

def read_json_file(filepath, encoding = 'utf-8'):
    """
    Reads the JSON file and return it's content

    Args:
        file_path (str): The path to the JSON file
        encoding (str): The encoder to use for reading the file
    
    Returns: 
        Dictionary: The JSON file content

    Raises:
        FileNotFoundError: If the file is not found
        JSONDecodeError: If the file has Invalid JSON
    """
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        print('Cannot parse JSON file: {}'.format(filepath))
    except FileNotFoundError:
        print('File Not Found: {}'.format(filepath))
    except Exception as e:
        print('Exception Occured: {}'.format(e))

def save_json_file(filepath, filename, data, encoding = 'utf-8'):
    """
    Save the JSON Data on a file with the specified encodings

    Args:
        filepath (str): The path to the JSON file
        filename (str): The name of the JSON fle
        encoding (str): The encoder to use for reading the file

    Returns:
        (Bool): Returns True if the JSON data was saved successfully, False otherwise
    """
    try:
        #Checking if the directory exist, if not create the directory
        os.makedirs(filepath, exist_ok=True)
        filename = '{}/{}'.format(filepath, filename)

        #Writing the JSON data on the file
        with open(filename, 'w', encoding=encoding) as f:
            json.dump(data, f, indent=4)
        return True
    except json.JSONDecodeError:
        print('Cannot parse JSON file: {}'.format(filepath))
    except Exception as e:
        print('Exception Occured: {}'.format(e))
        return False

def extract_tag_value(tag):
    """
    Reads the given  XML tag value if the tag is not NULL

    Args:
        tag (XML Element): The XML tag whose value has to be read

    Returns:
        (str): The XML tag value if present, otherwise an empty string
    """
    try:
        if tag is None:
            return ''
        return tag.text
    except Exception as e:
        print('Exception Occured while extracting Tag value: {}'.format(e))
        return ''
    
def format_gnd_subject_code(code):
    """
    Format the GND classification number for easier sorting.
    Typical Classification Number is Formatted as:
    <Number>.<Number><Character>  --->  <Number>.<Number>0<ASCII(Character)>

    Args:
        code (str): GND Classification Number

    Returns:
        (float): Float representation of the Classification Number
    """
    try:
        #If the classification number is only numbers, then return directly the float representation
        return float(code)
    except ValueError:
        #If classification number contains charaters, group number and characters
        match = re.match(r"([0-9]+(?:\.[0-9]+)*)?([a-z]*)", code)
        #Format the number and the characters into the format <Number>.<Number>0<ASCII(Character)>
        if match:
            group1 = match.group(1) if '.' in match.group(1) else match.group(1) + '.0'
            return float(group1 + '0' + str(sum(ord(c) for c in match.group(2))))
        #Return the same code if NO condition is valid
        return code

#The path for the GND subject specification file 
subject_gnd_filepath = '../../../../authorities-gnd-sachbegriff_dnbmarc_20240213.mrc.xml'

#XML Namespace used in the MARC 21 GND file
xml_namespace = '{http://www.loc.gov/MARC21/slim}'

#List to store formatted GND subject details
formatted_gnd_subjects = []

#All GND Subject codes 
gnd_subjects = read_json_file('../gnd subjects/gnd-subjects.json')

#Only TIB Core GND Subject codes
tib_core_subjects = [subj for subj in gnd_subjects if subj['TIB Core']]

#Creating key:value pairs, where key is code and value is the name of the GND subject
gnd_subjects = dict(zip([subj['Code'] for subj in gnd_subjects], [subj['Name'] for subj in gnd_subjects]))
tib_core_subjects = dict(zip([subj['Code'] for subj in tib_core_subjects], [subj['Name'] for subj in tib_core_subjects]))

#Reading the MARC 21 GND subject specification file
tree = ET.parse(subject_gnd_filepath)
root = tree.getroot()

#Whether to include all GND subjects or only TIB Core subjects
all_subjects = False

#Iterating over all the record tags
for record in root.findall(f'{xml_namespace}record'):

    #Extracting the subject classification number - Code: 065 - Field: a
    subject_classification_number = extract_tag_value(record.find(f'{xml_namespace}datafield[@tag="065"]/{xml_namespace}subfield[@code="a"]'))

    #Filtering the subjects
    if (subject_classification_number == '') or (not all_subjects and subject_classification_number not in tib_core_subjects.keys()):
        continue

    #Adding subject classification name from the TIB Core subjects list
    subject_classification_name = gnd_subjects[subject_classification_number]

    #Extracting and formatting GND subject code - Code 021 - Field: 2 and a
    subject_code = extract_tag_value(record.find(f'{xml_namespace}datafield[@tag="024"]/{xml_namespace}subfield[@code="2"]'))
    subject_code += ':' + extract_tag_value(record.find(f'{xml_namespace}datafield[@tag="024"]/{xml_namespace}subfield[@code="a"]'))

    #Extracting the subject name - Code: 150 - Field: a
    subject_name = extract_tag_value(record.find(f'{xml_namespace}datafield[@tag="150"]/{xml_namespace}subfield[@code="a"]'))

    #Extracting the subject alternate name - Code: 450 - Field: a
    alternate_subject_name = extract_tag_value(record.find(f'{xml_namespace}datafield[@tag="450"]/{xml_namespace}subfield[@code="a"]'))

    #Extracting all the relevant subjects - Code: 550 - Field: a
    related_subjects = []
    for related_subject in record.findall(f'{xml_namespace}datafield[@tag="550"]'):
        related_subjects.append(extract_tag_value(related_subject.find(f'{xml_namespace}subfield[@code="a"]')))
    
    #Extracting subject source name - Code: 670 - Field: a
    subject_source = extract_tag_value(record.find(f'{xml_namespace}datafield[@tag="670"]/{xml_namespace}subfield[@code="a"]'))

    #Extracting subject source URL - Code: 670 - Field: u
    subject_source_url = extract_tag_value(record.find(f'{xml_namespace}datafield[@tag="670"]/{xml_namespace}subfield[@code="u"]'))

    #Extracting subject definition - Code: 677 - Field: a
    subject_definition = extract_tag_value(record.find(f'{xml_namespace}datafield[@tag="677"]/{xml_namespace}subfield[@code="a"]'))

    #Creating a dictionary with all the subject description attributes
    sub_description = {
        'Code': subject_code,
        'Classification Number': subject_classification_number,
        'Classification Name': subject_classification_name,
        'Name': subject_name,
        'Alternate Name': alternate_subject_name,
        'Related Subjects': related_subjects,
        'Source': subject_source,
        'Source URL': subject_source_url,
        'Definition': subject_definition
    }

    #Removing all the keys with empty value
    sub_description = {k: v for k, v in sub_description.items() if v != ''}

    #Appending the subject description into the final list
    formatted_gnd_subjects.append(sub_description)

#Sorting the list based on the GND classification number
formatted_gnd_subjects = sorted(formatted_gnd_subjects, key = lambda k: format_gnd_subject_code(k['Classification Number']))

#Saving all the subject descriptions as a JSON file
save_json_file('../gnd subjects','GND-Subjects-tib-core.json', formatted_gnd_subjects)
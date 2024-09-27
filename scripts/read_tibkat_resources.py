import os
import json
import validators
from langdetect import detect

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

def validate_record(record):
    """
    Check the record if it contains the required attributes

    Args:
        record (Dict): The JSON dictionary containing all the attributes

    Returns:
        (Bool): Returns True if contains the required attributes, False otherwise.
    """
    try:
        #Checking if title is present and is not empty
        title_is_valid = 'title' in record['@graph'][-1].keys() and record['@graph'][-1]['title'] != ''
        
        #Checking if abstract is present and it has more than 100 characters
        abstract_is_valid = 'abstract' in record['@graph'][-1].keys()
        abstract = record['@graph'][-1]['abstract'] if abstract_is_valid else None
        if abstract_is_valid and isinstance(abstract, str):
            abstract_is_valid = abstract_is_valid and not validators.url(abstract) and len(abstract) > 100
        elif abstract_is_valid and isinstance(abstract, list):
            abstract_is_valid = abstract_is_valid and not all([validators.url(abs) for abs in abstract]) and all([len(abs) > 100 for abs in abstract])
        
        #Combining all the conditions to return the final validity of the record
        return all((title_is_valid, abstract_is_valid))
    except Exception as e:
        print('Exception Occured: {}'.format(e))
        return False

def detect_language(data):
    """
    Detect the language of a text using the LangDetect Package

    Args:
        data (str): The text for language detection

    Returns:
        (str): The detected language
    """
    try:
        return detect(data)
    except: return None

if __name__ == '__main__':

    #The path to the TIBKAT resource directory
    tibkat_resources_dir = '../../../tibkat_rdf_jsonld'

    #Record Types to include in the Final Dataset
    final_record_types = ['Article', 'Book', 'Conference', 'Report', 'Thesis']

    #Record's Languages to include in the Final Dataset
    final_record_languages = ['en', 'de']

    #GND Codes for TIB Core subjects
    tib_core_subjects = read_json_file('../gnd-how-to/gnd-subjects/GND-Subjects-tib-core.json')
    tib_core_subjects = [subj['Code'] for subj in tib_core_subjects]
    print('Total TIB Core subjects: {}'.format(len(tib_core_subjects)))

    #Total records in whole TIBKAT data dump
    total_record = 0

    #Total valid records in whole TIBKAT data dump
    total_valid_record = 0

    #Total supplementary records
    total_supplementary_records = 0

    #Include all subjects or only TIB Core subjects
    only_TIB_Core_subjects = False
    
    for index, filename in enumerate(os.listdir(tibkat_resources_dir)):

        #Reading each TIBKAT JSONLD file, each containing multiple records 
        data = read_json_file('{}/{}'.format(tibkat_resources_dir, filename))

        #Checking JSON, if it was parsed correctly
        if data is None:
            print('Skipping the file: {}\n'.format(filename))
            continue
        
        #Iterating over each record in a file
        for record in data:

            #Incrementing the total record count
            total_record += 1

            #Validating the record
            record_valid = validate_record(record)

            #Skipping the record if it does not have the required attributes
            if not record_valid:
                continue
            
            #Detecting language using LangDetect Package
            abstract = record['@graph'][-1]['abstract'][0] if isinstance(record['@graph'][-1]['abstract'], list) else record['@graph'][-1]['abstract']
            lang = detect_language(abstract)

            #Extracting the Record Type
            record_type = record['@graph'][-1]['@type'].split(':')[-1]

            #Extracting the Record ID
            record_ID = record['@graph'][-1]['@id'].split('%')[-1]

            #Checking if the GND Subjects are present in the Record
            subject_exist = 'dcterms:subject' in record['@graph'][-1].keys() and len(record['@graph'][-1]['dcterms:subject']) > 0

            #Filtering for only TIB Core subject if set to True
            if subject_exist and only_TIB_Core_subjects:
                
                #Based on the type of value of dcterm:subject, extracting the gnd subject codes
                if isinstance(record['@graph'][-1]['dcterms:subject'], list):
                    record_subjects = [dcsubj['@id'] for dcsubj in record['@graph'][-1]['dcterms:subject']]
                elif isinstance(record['@graph'][-1]['dcterms:subject'], dict):
                    record_subjects = [record['@graph'][-1]['dcterms:subject']['@id']]
                
                #Checking if current record's subject codes are related to TIB core
                common_subjects = list(set(tib_core_subjects) & set(record_subjects))
                if not common_subjects: continue

            #Saving the Record in the appropiate directory
            to_include_in_final_dataset = (record_valid and subject_exist and (lang in final_record_languages) and (record_type in final_record_types))
            main_dir = 'dataset' if  to_include_in_final_dataset else 'supplementary-dataset'
            sup_dataset_subdir = 'w-dcterms' if subject_exist else 'wo-dcterms'
            main_dir = '{}/{}'.format(main_dir, sup_dataset_subdir) if not to_include_in_final_dataset else main_dir
            file_dir = '../{}/{}/{}'.format(main_dir, record_type, lang)
            new_filename = '{}.jsonld'.format(record_ID)
            fileSaved = save_json_file(file_dir, new_filename, record)
            
            #Checking if the file was saved successfully or not
            if not fileSaved:
                print('Cannot saved the File: {}/{}'.format(file_dir, new_filename))
                continue

            #Incrementing the total valid record count
            if to_include_in_final_dataset:
                total_valid_record += 1

            #Incrementing the total supplementary record count
            if not to_include_in_final_dataset:
                total_supplementary_records += 1

        if (index % 10000) == 0:
            print('Finished processing file: {}'.format(filename))
    
    print('\nSuccessfully Saved the TIBKAT Data with Valid attributes!')
    print('\nData Statistics:')
    print('Total Records: {}\nTotal Valid Records: {}\nTotal Supplementary Records: {}\nTotal Invalid Records: {}'.format(total_record, total_valid_record, total_supplementary_records, total_record - total_valid_record - total_supplementary_records))
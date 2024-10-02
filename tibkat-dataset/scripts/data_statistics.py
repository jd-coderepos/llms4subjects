import os
import json
from statistics import mean
import pandas as pd

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
    
def write_text_file(file_path, text, encoding = 'utf-8'):
    """
    Creates and writes the list of text to a text file

    Args:
        file_path (str): The path to save the text file
        text (List): The list of texts, which has to be saved on the text file

    Returns:
        (Bool): True if the file was saved successfully, otherwise False
    """
    try:
        with open(file_path, 'w', encoding = encoding) as f:
            f.writelines(text)
        return True
    except Exception as e:
        print('Exception Occured: {}'.format(e))
        return False

def type_language_statistics(dir_path, result_path):
    """
    Create a data statistics for the record types and languages

    Args:
        dir_path (str): The path for final and supplementary data
        results_path (str): The path to store the data statistics files 

    Returns:
        (Dict): The dictionary containing file count for each type and language combination
    """
    try:
        #Path of the final dataset
        final_dataset_dir = 'shared-task-dataset'

        #Path of the supplementary dataset
        supplementary_dataset_dir = 'shared-task-supplementary-dataset'

        #Dictionary to store data statistics 
        data_statistics = {}
        
        #Iterating over final dataset directory
        for root, dirs, files in os.walk(os.path.join(dir_path, final_dataset_dir)):
            if files:
                record_type, language = root.split('\\')[-2], root.split('\\')[-1]
                
                if record_type not in data_statistics.keys():
                    data_statistics[record_type] = {}
                if language not in data_statistics[record_type].keys():
                    data_statistics[record_type][language] = 0
                data_statistics[record_type][language] += len(files)

        #Iterating over supplementary dataset directory
        for root, dirs, files in os.walk(os.path.join(dir_path, supplementary_dataset_dir)):
            if files:
                record_type, language = root.split('\\')[-2], root.split('\\')[-1]

                if record_type not in data_statistics.keys():
                    data_statistics[record_type] = {}
                if language not in data_statistics[record_type].keys():
                    data_statistics[record_type][language] = 0
                data_statistics[record_type][language] += len(files)

        #Sorting the dictionary by record type
        data_statistics = dict(sorted(data_statistics.items()))

        data_statistics = pd.DataFrame(data_statistics)
        data_statistics.fillna(0, inplace=True)
        data_statistics = data_statistics.astype(int)

        type_lang_counts = ['Record Type\t\t\t\t\tLanguage\tCount\n']
        type_counts = ['Record Type Counts:\n']
        lang_counts = ['\nLanguage Distribution:\n']
        counts_per_subdir = []
        for record_type, lang_counts in data_statistics.items():
            for index, count in lang_counts.items():
                if count > 0:
                    type_lang_counts.append(f'{record_type.ljust(28, ' ')}{index.ljust(12, ' ')}{count}\n')
                    if record_type in ['Article', 'Book', 'Conference', 'Report', 'Thesis'] and index in ['en', 'de']:
                        counts_per_subdir.append('{}/{}: {}\n'.format(record_type, index, count))
            type_counts.append('{}: {}\n'.format(record_type, data_statistics[record_type].sum()))
        
        lang_counts = ['\nLanguage Distribution:\n']
        for language, count in data_statistics.sum(axis=1).items():
            lang_counts.append('{}: {}\n'.format(language, count))
        
        type_counts_lang_counts = type_counts + lang_counts
        
        file_saved = write_text_file('{}/type-lang-counts.txt'.format(result_path), type_lang_counts)
        if not file_saved: print('Error saving the file for type_lang_counts')

        file_saved = write_text_file('{}/type-counts-lang-counts.txt'.format(result_path), type_counts_lang_counts)
        if not file_saved: print('Error saving the file for type_counts_lang_counts')

        file_saved = write_text_file('{}/counts_per_subdir.txt'.format(result_path), counts_per_subdir)
        if not file_saved: print('Error saving the file for counts_per_subdir')
    except Exception as e:
        print('Exception Occured: {}'.format(e))

def abstract_stats(dataset_path, result_path):
    """
    Extract the statistics (min, max and mean) for all abstracts present in the final SemEval dataset (Train and Dev)

    Args:
        dataset_path (str): The path to the final dataset
        results_path (str): The path to store the final abstract statistics file
    """
    try:
        #Dictionary to store the abstract lengths for each record type and language combination
        abstract_stats = {'train': {}, 'dev': {}}

        #Abstract stats in JSON format
        abstract_stats_json = {'train': {}, 'dev': {}}

        for root, dir, files in os.walk(dataset_path):
            if files:
                #Including only train and dev splits
                data_split = root.split('\\')[-3]
                if data_split == 'test': continue

                #Formatting a key with record type and language
                type_lang_key = '{}/{}'.format(root.split('\\')[-2], root.split('\\')[-1])
                
                for file in files:
                    file_data = read_json_file('{}\\{}'.format(root, file))
                    
                    #Extracting the abstract from the record and calculating the total words/tokens
                    abstract = file_data['@graph'][-1]['abstract']
                    abstract = ' '.join(abstract) if isinstance(abstract, list) else abstract
                    tokens = len(abstract.split(' '))

                    #Appending the abstract length in the dictionary with corresponding key
                    if type_lang_key not in abstract_stats[data_split].keys():
                        abstract_stats[data_split][type_lang_key] = []
                    abstract_stats[data_split][type_lang_key].append(tokens)
        
        #Formatting the results into a JSON format
        for split, split_stats in abstract_stats.items():
            for type_lang, tokens in split_stats.items():
                record_type, lang = type_lang.split('/')
                if record_type not in abstract_stats_json[split].keys():
                    abstract_stats_json[split][record_type] = {}
                abstract_stats_json[split][record_type][lang] = {
                    'min': min(tokens),
                    'max': max(tokens),
                    'mean': round(mean(tokens), 1)
                }
        
        #Creating and Saving the JSON file
        file_saved = save_json_file(result_path, 'abstract_stats.json', abstract_stats_json)
        if not file_saved: print('Error saving the file')
    except Exception as e:
        print('Exception Occured: {}'.format(e))

def subject_statistics(dataset_path, result_path):
    """
    Extract the statistics for dc:subjects present in the final SemEval dataset (Train and Dev)

    Args:
        dataset_path (str): The path to the final dataset
        results_path (str): The path to store the final subject statistics file
    """
    try:
        #Dictionary to store total dc:subjects for each record type and language combination
        dcsubject_stats = {'train': {}, 'dev': {}}

        #Abstract stats in JSON format
        dcsubject_stats_json = {'train': {}, 'dev': {}}

        for root, dir, files in os.walk(dataset_path):
            if files:
                #Including only train and dev splits
                data_split = root.split('\\')[-3]
                if data_split == 'test': continue

                #Formatting a key with record type and language
                type_lang_key = '{}/{}'.format(root.split('\\')[-2], root.split('\\')[-1])
                
                for file in files:
                    file_data = read_json_file('{}\\{}'.format(root, file))

                    #Extracting the dc:subjects from the record and calculating the total subjects
                    dcsubjects = file_data['@graph'][-1]['dcterms:subject']
                    total_subjects = len(dcsubjects) if isinstance(dcsubjects, list) else 1

                    #Appending the total subjects in the dictionary with corresponding key
                    if type_lang_key not in dcsubject_stats[data_split].keys():
                        dcsubject_stats[data_split][type_lang_key] = []
                    dcsubject_stats[data_split][type_lang_key].append(total_subjects)
        
        #Formatting the results into a JSON format
        for split, split_stats in dcsubject_stats.items():
            for type_lang, subjects in split_stats.items():
                record_type, lang = type_lang.split('/')
                if record_type not in dcsubject_stats_json[split].keys():
                    dcsubject_stats_json[split][record_type] = {}
                dcsubject_stats_json[split][record_type][lang] = {
                    'min': min(subjects),
                    'max': max(subjects),
                    'mean': round(mean(subjects), 1)
                }

        #Creating and Saving the JSON file
        file_saved = save_json_file(result_path, 'subject_stats.json', dcsubject_stats_json)
        if not file_saved: print('Error saving the file for total_subject_text')
    except Exception as e:
        print('Exception Occured: {}'.format(e))

def subject_frequencies(dataset_path, result_path, gnd_subjects):
    """
    Create subject frequencies for each record types

    Args:
        dataset_path (str): The path to the final dataset
        result_path (str): The path to save the subject frequencies file
        gnd_subjects (Dict): The gnd subject code to name mappings
    """
    try:
        #subject frequencies dictionary
        subject_freq = {}

        for root, dir, files in os.walk(dataset_path):
            if files:
                #Including only train and dev splits for subject frequencies
                data_split = root.split('\\')[-3]
                if data_split == 'test': continue

                #Formatting a key with record type and language
                type_lang_key = '{}-{}'.format(root.split('\\')[-2], root.split('\\')[-1])
                subject_freq[type_lang_key] = {}
                
                for file in files:
                    file_data = read_json_file('{}\\{}'.format(root, file))

                    #Extracting the dc:subjects from the record
                    dcsubjects = file_data['@graph'][-1]['dcterms:subject']
                    dcsubjects = [subj['@id'] for subj in dcsubjects] if isinstance(dcsubjects, list) else [file_data['@graph'][-1]['dcterms:subject']['@id']]

                    for subjCode in dcsubjects:
                        #Skipping if the subject code is not in the GND specification file
                        if subjCode not in gnd_subjects.keys():
                            continue
                        
                        #Updating the dictionary with the count for the subject
                        subjName = gnd_subjects[subjCode]
                        if subjName not in subject_freq[type_lang_key].keys():
                            subject_freq[type_lang_key][subjName] = 0
                        subject_freq[type_lang_key][subjName] += 1
        
        #Creating a pandas dataframe with the subject frequencies
        subject_freq = pd.DataFrame(subject_freq)
        subject_freq.fillna(0, inplace=True)
        subject_freq = subject_freq.astype(int)
        subject_freq.index.name = 'Subject'

        #Adding a new column with total frequency for each subject across all record types
        subject_freq['Overall Frequency'] = subject_freq[subject_freq.columns].sum(axis=1)
        subject_freq.sort_values(by='Overall Frequency', ascending=False, inplace=True)
        subject_freq = subject_freq[['Overall Frequency'] + list(subject_freq.columns[:-1])]

        #Saving the subject frequencies dataframe as a CSV file
        subject_freq.to_csv('{}/subject_frequencies.csv'.format(result_path))
    except Exception as e:
        print('Exception Occured: {}'.format(e))

def unique_subjects(dataset_path, result_path, gnd_subjects):
    """
    Create files for each record type and language combination containing unique subjects

    Args:
        dataset_path (str): The path to the final dataset
        result_path (str): The path to save the Unique subject for each record type and language
        gnd_subjects (Dict): The gnd subject code to name mappings
    """
    try:
        for root, dir, files in os.walk(dataset_path):
            if files:
                #Including only train and dev splits for Unique Subjects
                data_split = root.split('\\')[-3]
                if data_split == 'test': continue

                #Formatting a key with record type and language
                type_lang_key = '{}_{}'.format(root.split('\\')[-2], root.split('\\')[-1])
                
                #Unique subjects list
                unique_subjects = []
                
                for file in files:
                    file_data = read_json_file('{}\\{}'.format(root, file))

                    #Extracting the dc:subjects from the record
                    dcsubjects = file_data['@graph'][-1]['dcterms:subject']
                    dcsubjects = [subj['@id'] for subj in dcsubjects] if isinstance(dcsubjects, list) else [file_data['@graph'][-1]['dcterms:subject']['@id']]

                    for subjCode in dcsubjects:
                        #Skipping if the subject code is not in the GND specification file
                        if subjCode not in gnd_subjects.keys():
                            continue
                        
                        #Adding the subject code and name in the list
                        unique_subjects.append('{}: {}\n'.format(subjCode, gnd_subjects[subjCode]))
                
                #Removing the duplicate lines
                unique_subjects = list(set(unique_subjects))

                #Saving the text in the text file for the record type and language combination
                write_text_file('{}/unique_subjects_{}.txt'.format(result_path, type_lang_key), unique_subjects)        
    except Exception as e:
        print('Exception Occured: {}'.format(e))

def data_split_statistics(dataset_path, result_path):
    """
    Creates a file containing the statistics of data splits in final SemEval dataset and the supplementary dataset

    Args:
        dataset_path (str): The path to the dataset folders
        result_path (str): The path to save the data split statistics file
    """
    try:
        #Path of the final dataset
        final_dataset_dir = 'tibkat-dataset/tib-core-subjects/data'

        #Path of the supplementary dataset
        supplementary_dataset_dir = 'tibkat-supplementary-dataset/tib-core-subjects'

        #Dictionary to store data statistics 
        data_statistics = {
            'SemEval Dataset': {
                'train': {'Total Record': 0},
                'dev': {'Total Record': 0},
                'test': {'Total Record': 0}
            },
            'Supplementary Dataset': {
                'w-dcterms': {'Total Record': 0},
                'wo-dcterms': {'Total Record': 0}
            },
            'Total Records': 0
        }
        
        #Iterating over final dataset directory
        for root, dirs, files in os.walk(os.path.join(dataset_path, final_dataset_dir)):
            if files:
                split, record_type, language = root.split('\\')[-3:]
                if record_type not in data_statistics['SemEval Dataset'][split].keys():
                    data_statistics['SemEval Dataset'][split][record_type] = {}
                if language not in data_statistics['SemEval Dataset'][split][record_type].keys():
                    data_statistics['SemEval Dataset'][split][record_type][language] = 0
                data_statistics['SemEval Dataset'][split][record_type][language] += len(files)
                data_statistics['SemEval Dataset'][split]['Total Record'] += len(files)
                data_statistics['Total Records'] += len(files)

        #Iterating over Supplementary dataset directory
        for root, dirs, files in os.walk(os.path.join(dataset_path, supplementary_dataset_dir)):
            if files:
                dcterm, record_type, language = root.split('\\')[-3:]
                if record_type not in data_statistics['Supplementary Dataset'][dcterm].keys():
                    data_statistics['Supplementary Dataset'][dcterm][record_type] = {}
                if language not in data_statistics['Supplementary Dataset'][dcterm][record_type].keys():
                    data_statistics['Supplementary Dataset'][dcterm][record_type][language] = 0
                data_statistics['Supplementary Dataset'][dcterm][record_type][language] += len(files)
                data_statistics['Supplementary Dataset'][dcterm]['Total Record'] += len(files)
                data_statistics['Total Records'] += len(files)

        #Sorting the dictionary
        for key, value in data_statistics['SemEval Dataset']['train'].items():
            if not isinstance(value, dict): continue
            data_statistics['SemEval Dataset']['train'][key] = dict(sorted(data_statistics['SemEval Dataset']['train'][key].items(), key=lambda item: item[1], reverse=True))
            data_statistics['SemEval Dataset']['dev'][key] = dict(sorted(data_statistics['SemEval Dataset']['dev'][key].items(), key=lambda item: item[1], reverse=True))
            data_statistics['SemEval Dataset']['test'][key] = dict(sorted(data_statistics['SemEval Dataset']['test'][key].items(), key=lambda item: item[1], reverse=True))

            data_statistics['Supplementary Dataset']['w-dcterms'][key] = dict(sorted(data_statistics['Supplementary Dataset']['w-dcterms'][key].items(), key=lambda item: item[1], reverse=True))
            data_statistics['Supplementary Dataset']['wo-dcterms'][key] = dict(sorted(data_statistics['Supplementary Dataset']['wo-dcterms'][key].items(), key=lambda item: item[1], reverse=True))

        #Saving the dictionary in a JSON file
        file_saved = save_json_file(result_path, 'data_split_statistics.json', data_statistics)
        if not file_saved: print('File NOT saved successfully')
    except Exception as e:
        print('Exception Occured: {}'.format(e))

if __name__ == '__main__':

    #Final Dataset path
    final_dataset_path = '../tib-core-subjects/data'

    #Stats path
    stats_path = '../tib-core-subjects/data-statistics'

    #All GND Codes specifications
    print('Reading GND Specification file')
    gnd_subjects = read_json_file('../../shared-task-GND/formatted-gnd-subjects/GND-Subjects-all.json')
    gnd_subjects = {subj['Code']: subj['Name'] for subj in gnd_subjects}
    print('Total GND subjects: {}'.format(len(gnd_subjects.keys())))

    #Creating final and supplemetary data statistics
    print('\nCreating statistics files for type language combination')
    type_language_statistics('../', '../analysis')

    #Creating abstract statistics file
    print('\nCreating Abstract\'s statistics file')
    abstract_stats(final_dataset_path, stats_path)

    #Creating dc:subjects statistics file
    print('\nCreating Subject\'s statistics file')
    subject_statistics(final_dataset_path, stats_path)

    #Creating dc:subject frequencies file
    print('\nCreating Subject Frequencies file')
    subject_frequencies(final_dataset_path, stats_path, gnd_subjects)

    #Creating Unique subject files for each record type and language combination
    print('\nCreating Unique Subjects file for each record type and language combination')
    unique_subjects(final_dataset_path, f'{stats_path}/unique-subjects', gnd_subjects)

    #Creating the data splits statistics file
    print('\nCreating Data Splits Statistics file')
    data_split_statistics('../../', stats_path)
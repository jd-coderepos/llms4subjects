import os
import shutil
import random

def copy_files(source_dir, dest_dir, files):
    """
    Copy all the files from the source directory to the destination directory

    Args:
        source_dir (str): Source directory
        dest_dir (str): Destination directory
        files (List): The list of filenames to copy from source to destination directory
    """
    try:
        for filename in files:
            shutil.copy(os.path.join(source_dir, filename), os.path.join(dest_dir, filename))
    except Exception as e:
        print('Exception Occured: {}'.format(e))

if __name__ == '__main__':
    
    #The path to the Final Dataset
    tibkat_resources_dir = '../dataset'

    #Data Splitting Ratios
    split_ratios = [0.6, 0.1, 0.3]

    #Record Types in the Final Dataset
    final_record_types = ['Article', 'Book', 'Conference', 'Report', 'Thesis']

    #Record's Languages in the Final Dataset
    final_record_languages = ['en', 'de']

    #Iterating over all the combination of record types and record languages
    for record_type in final_record_types:
        for record_lang in final_record_languages:
            
            #Formatting the source directory path
            record_current_dirpath = '{}/{}/{}'.format(tibkat_resources_dir, record_type, record_lang)
            print('Reading the directory: {}'.format(record_current_dirpath))

            if not os.path.isdir(record_current_dirpath):
                print('Directory NOT FOUND: {}'.format(record_current_dirpath))
                continue

            #List of all the files present in the source directory
            files = [filename for filename in os.listdir(record_current_dirpath)]
            
            #Shuffling the files
            random.shuffle(files)

            #Calculating the number of files for each data split
            total_records = len(files)
            total_train_records = int(split_ratios[0] * total_records)
            total_dev_records = int(split_ratios[1] * total_records)

            #Splitting the files into train, dev, test
            train_records = files[:total_train_records]
            dev_records = files[total_train_records:total_train_records+total_dev_records]
            test_records = files[total_train_records+total_dev_records:]

            #Creating train directory and copying the files
            record_new_dirpath = '{}/train/{}/{}'.format(tibkat_resources_dir, record_type, record_lang)
            os.makedirs(record_new_dirpath, exist_ok=True)
            copy_files(record_current_dirpath, record_new_dirpath, train_records)

            #Creating dev directory and copying the files
            record_new_dirpath = '{}/dev/{}/{}'.format(tibkat_resources_dir, record_type, record_lang)
            os.makedirs(record_new_dirpath, exist_ok=True)
            copy_files(record_current_dirpath, record_new_dirpath, dev_records)

            #Creating test directory and copying the files
            record_new_dirpath = '{}/test/{}/{}'.format(tibkat_resources_dir, record_type, record_lang)
            os.makedirs(record_new_dirpath, exist_ok=True)
            copy_files(record_current_dirpath, record_new_dirpath, test_records)
    
        #Deleting the old directories
        print('\nSuccessfully splitted the data in the directory: {}/{}'.format(tibkat_resources_dir, record_type))
        print('Deleting this directory...')
        shutil.rmtree('{}/{}'.format(tibkat_resources_dir, record_type))
        print('Directory: {}/{} is Deleted\n'.format(tibkat_resources_dir, record_type))

    print('Successfully splitted the dataset into Train, Dev and Test splits!')





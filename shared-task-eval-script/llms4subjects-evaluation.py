import argparse
import os
import sys
import json
import pandas as pd

def read_json_file(filepath: str, encoding: str = 'utf-8'):
    """
    Reads the JSON file and return it's content

    Args:
        file_path (str): The path to the JSON file
        encoding (str): The encoder to use for reading the file

    Returns:
        dict: The JSON file content
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

def remove_empty_dicts(d: dict) -> dict:
    """
    Recursively remove keys with empty dictionaries as values.

    Args:
        d (dict): The dictionary containing empty dictionaries as values

    Returns:
        dict: The updated dictionary without empty values
    """
    if not isinstance(d, dict):
        return d
    return {k: remove_empty_dicts(v) for k, v in d.items() if remove_empty_dicts(v)}
        
def precision(true_labels: list, pred_labels: list, k: int):
    """
    Calculates the precision@k for the given true labels and the predicted labels.
    
    Args:
        true_labels (list): The list of true labels
        pred_labels (list): The list of predicted labels
        k (int): The value of K representing the top k values to consider

    Returns:
        float: Precision@k
    """
    true_set = set(true_labels)
    pred_set = set(pred_labels[:k])
    intersection = true_set & pred_set
    return round(len(intersection) / k, 4)

def recall(true_labels: list, pred_labels: list, k: int):
    """
    Calculates the recall@k for the given true labels and the predicted labels.

    Args:
        true_labels (list): The list of true labels
        pred_labels (list): The list of predicted labels
        k (int): The value of K representing the top k values to consider

    Returns:
        float: Recall@k
    """
    true_set = set(true_labels)
    pred_set = set(pred_labels[:k])
    intersection = true_set & pred_set
    return round(len(intersection) / len(true_set), 4)

def f1(precision_k: float, recall_k: float):
    """
    Calculates the f1@k for the given precision@k and recall@k.

    Args:
        precision_k (float): The value of Precision@k
        recall_k (float): The value of Recall@k

    Returns:
        float: f1@k
    """
    if precision_k + recall_k == 0: return 0
    return round(2 * (precision_k * recall_k) / (precision_k + recall_k), 4)
    
def evaluate_combined_record_type_language(true_dict: dict, predicted_dict: dict, k: int):
    """
    Calculates the evaluation metrics (Precision@k, Recall@k and F1@k) on the combined granularity level (record type and language) 
    for the given true GND labels and predicted GND labels.

    Args:
        true_dict (dict): The dictionary containing the list of true GND labels
        predicted_dict (dict): The dictionary containing the list of predicted GND labels
        k (int): The value of K for calculating precision and recall

    Returns:
        dict: The resulted dictionary containing the evaluation metrics score
    """
    
    #Dictionary to store evaluation metric scores
    combined_metrics = {}
    
    #Iterating over each record type and language combination
    for record_type, lang_dict in true_dict.items():
        for language, file_data in lang_dict.items():
            
            #Aggregating the recall and precision for each record type and language combination
            total_recall, total_precision = 0, 0
            
            #Total files for each combination
            count = len(file_data.keys())
            
            #Iterating over each file containing the true GND labels 
            for filename, true_labels in file_data.items():
                #Extracting the corresponding predicted GND labels
                pred_labels = predicted_dict[record_type][language][f'{os.path.splitext(filename)[0]}.json']
                
                #Calculating the recall and precision at k
                recall_k = recall(true_labels, pred_labels, k)
                precision_k = precision(true_labels, pred_labels, k)
                
                total_recall += recall_k
                total_precision += precision_k
            
            #Averaging recall and precision and calculating the f1 score  
            avg_recall = total_recall / count if count else 0.0
            avg_precision = total_precision / count if count else 0.0
            avg_f1 = f1(avg_recall, avg_precision)
            
            #Saving the metrics score in the dictionary
            if record_type not in combined_metrics:
                combined_metrics[record_type] = {}
            combined_metrics[record_type][language] = {f'precision_{k}': avg_precision, f'recall_{k}': avg_recall, f'f1_{k}': avg_f1}
    
    return combined_metrics

def evaluate_record_type_level(true_dict: dict, predicted_dict: dict, k: int):
    """
    Calculates the evaluation metrics (Precision@k, Recall@k and F1@k) on the record type granularity level for the given true 
    GND labels and predicted GND labels.

    Args:
        true_dict (dict): The dictionary containing the list of true GND labels
        predicted_dict (dict): The dictionary containing the list of predicted GND labels
        k (int): The value of K for calculating precision and recall

    Returns:
        dict: The resulted dictionary containing the evaluation metrics score
    """
    
    #Dictionary to store evaluation metric scores
    metrics_score = {}
    
    #Iterating over each record type and language combination
    for record_type, lang_dict in true_dict.items():
        for language, file_data in lang_dict.items():
            
            #Aggregating the recall and precision for each record type
            if record_type not in metrics_score:
                metrics_score[record_type] = {f'precision_{k}': 0, f'recall_{k}': 0, f'f1_{k}': 0, 'total_files': 0}
            
            #Total files
            metrics_score[record_type]['total_files'] += len(file_data.keys())
            
            #Iterating over each file containing the true GND labels 
            for filename, true_labels in file_data.items():
                #Extracting the corresponding predicted GND labels
                pred_labels = predicted_dict[record_type][language][f'{os.path.splitext(filename)[0]}.json']
                
                #Calculating the recall and precision at k
                recall_k = recall(true_labels, pred_labels, k)
                precision_k = precision(true_labels, pred_labels, k)
                
                metrics_score[record_type][f'recall_{k}'] += recall_k
                metrics_score[record_type][f'precision_{k}'] += precision_k
            
    #Averaging recall and precision and calculating the f1 score
    for record_type, metrics in metrics_score.items():
        total_files = metrics['total_files']
        metrics[f'recall_{k}'] = metrics[f'recall_{k}'] / total_files if total_files else 0.0
        metrics[f'precision_{k}'] = metrics[f'precision_{k}'] / total_files if total_files else 0.0
        metrics[f'f1_{k}'] = f1(metrics[f'recall_{k}'], metrics[f'precision_{k}'])
        
        #Deleting the total files key and value
        del metrics['total_files']
    
    return metrics_score

def evaluate_language_level(true_dict: dict, predicted_dict: dict, k: int):
    """
    Calculates the evaluation metrics (Precision@k, Recall@k and F1@k) on the language granularity level for the given true 
    GND labels and predicted GND labels.

    Args:
        true_dict (dict): The dictionary containing the list of true GND labels
        predicted_dict (dict): The dictionary containing the list of predicted GND labels
        k (int): The value of K for calculating precision and recall

    Returns:
        dict: The resulted dictionary containing the evaluation metrics score
    """
    
    #Dictionary to store evaluation metric scores
    metrics_score = {}
    
    #Iterating over each record type and language combination
    for record_type, lang_dict in true_dict.items():
        for language, file_data in lang_dict.items():
            
            #Aggregating the recall and precision for each record type
            if language not in metrics_score:
                metrics_score[language] = {f'precision_{k}': 0, f'recall_{k}': 0, f'f1_{k}': 0, 'total_files': 0}
            
            #Total files
            metrics_score[language]['total_files'] += len(file_data.keys())
            
            #Iterating over each file containing the true GND labels 
            for filename, true_labels in file_data.items():
                #Extracting the corresponding predicted GND labels
                pred_labels = predicted_dict[record_type][language][f'{os.path.splitext(filename)[0]}.json']
                
                #Calculating the recall and precision at k
                recall_k = recall(true_labels, pred_labels, k)
                precision_k = precision(true_labels, pred_labels, k)
                
                metrics_score[language][f'recall_{k}'] += recall_k
                metrics_score[language][f'precision_{k}'] += precision_k
            
    #Averaging recall and precision and calculating the f1 score
    for language, metrics in metrics_score.items():
        total_files = metrics['total_files']
        metrics[f'recall_{k}'] = metrics[f'recall_{k}'] / total_files if total_files else 0.0
        metrics[f'precision_{k}'] = metrics[f'precision_{k}'] / total_files if total_files else 0.0
        metrics[f'f1_{k}'] = f1(metrics[f'recall_{k}'], metrics[f'precision_{k}'])
        
        #Deleting the total files key and value
        del metrics['total_files']
    
    return metrics_score

def evaluate_and_save_to_excel(dir_path: str, filename: str, true_dict: dict, predicted_dict: dict, list_k: list):
    """
    Calculate the evaluation metrics at each granularity level for the given true labels and predicted labels and save the results
    in an excel file.

    Args:
        dir_path (str): The path to save the excel file
        filename (str): The file name for the excel file
        true_dict (dict): The dictionary containing the list of true GND labels
        predicted_dict (dict): The dictionary containing the list of predicted GND labels
        list_k (list): The list of values of k
    """
    
    #List of dataframes for each granularity level
    combined_df_list, record_type_df_list, language_df_list = [], [], []
    
    #Calculating the evaluation metrics on each value of k
    for k in list_k:
        
        print(f'\nEvaluating GND Subject Codes -- Granularity Level: Combined Language and Record-levels and k: {k}')
        combined_metrics_score = evaluate_combined_record_type_language(true_dict, predicted_dict, k)
        
        #Converting the nested dictionary into the dataframe
        rows = []
        for category, langs in combined_metrics_score.items():
            for lang, metrics in langs.items():
                row = {'Record Type': category, 'Language': lang}
                row.update(metrics)
                rows.append(row)
        combined_df_list.append(pd.DataFrame(rows))

        print(f'Evaluating GND Subject Codes -- Granularity Level: Record Type level and k: {k}')
        record_type_metrics_score = evaluate_record_type_level(true_dict, predicted_dict, k)
        record_type_df_list.append(pd.DataFrame.from_dict(record_type_metrics_score, orient='index'))

        print(f'Evaluating GND Subject Codes -- Granularity Level: Language level and k: {k}')
        language_metrics_score = evaluate_language_level(true_dict, predicted_dict, k)
        language_df_list.append(pd.DataFrame.from_dict(language_metrics_score, orient='index'))
    
    # Concatenate all the DataFrames
    final_combined_df = pd.concat(combined_df_list, axis=1)
    final_combined_df = final_combined_df.loc[:, ~final_combined_df.columns.duplicated()]
    
    #Calculating the overall metrics score across both record type and language
    metrics_col = [col for col in final_combined_df if col not in ['Record Type', 'Language']]
    average_metrics = final_combined_df[metrics_col].mean()
    average_row = ['Overall', '']
    average_row.extend(average_metrics)
    final_combined_df.loc[len(final_combined_df)] = average_row
    final_combined_df.set_index(['Record Type', 'Language'])
    
    final_record_type_df = pd.concat(record_type_df_list, axis=1)
    final_record_type_df.reset_index(inplace=True)
    final_record_type_df.rename(columns={'index': 'Record Type'}, inplace=True)
    
    final_language_df = pd.concat(language_df_list, axis=1)
    final_language_df.reset_index(inplace=True)
    final_language_df.rename(columns={'index': 'Language'}, inplace=True)
    
    #Saving the results in an excel file
    os.makedirs(dir_path, exist_ok=True)
    with pd.ExcelWriter(f'{dir_path}/{filename}') as writer:
        final_combined_df.to_excel(writer, sheet_name="Record Type and Language", index=False)
        final_record_type_df.to_excel(writer, sheet_name="Record Type", index=False)
        final_language_df.to_excel(writer, sheet_name="Language", index=False)
 
def read_gnd_files(dir_path: str, true_labels: bool):
    """
    Reads the Files containing the TIBKAT records in the JSON format

    Args:
        dir_path (str): The path containing the records
        true_labels (bool): Does the directory contains the true GND labels?

    Returns:
        dict: The dictionary containing the subjects information
    """
    gnd_labels = {'Article': {'de': {}, 'en': {}}, 'Book': {'de': {}, 'en': {}}, 'Conference': {'de': {}, 'en': {}}, 
                   'Report': {'de': {}, 'en': {}}, 'Thesis': {'de': {}, 'en': {}}}
    
    #Iterating over each files in the directory
    for root, _, filenames in os.walk(dir_path):
        if not filenames: continue
        
        #Extracting the record type and language from the root path
        record_type, language = root.replace('\\', '/').split('/')[-2:]
        
        for fname in filenames:
            gnd_codes = read_json_file(f'{root}/{fname}')
            if not gnd_codes: continue
            if true_labels and 'dcterms:subject' not in gnd_codes['@graph'][-1]: continue
            if not true_labels and 'dcterms:subject' not in gnd_codes: continue
            
            if true_labels:
                dc_subjects = gnd_codes['@graph'][-1]['dcterms:subject']
                dc_subjects = [dc_subjects['@id']] if isinstance(dc_subjects, dict) else [code['@id'] for code in dc_subjects]
            gnd_labels[record_type][language][fname] = dc_subjects if true_labels else gnd_codes['dcterms:subject']
    
    #Removing empty dictionary values meaning no files were found for that keys
    gnd_labels = remove_empty_dicts(gnd_labels)

    return gnd_labels

def validate_directory_structure(true_dict: dict, pred_dict: dict):
    """
    Validates the directory structure and files names containing the TIBKAT records

    Args:
        true_dict (dict): The dictionary containing the list of true GND labels
        predicted_dict (dict): The dictionary containing the list of predicted GND labels

    Returns:
        bool: Returns boolean value indicating whether the directory structure is correct or not.
    """
    #Boolean variable to store if the directory structure is valid
    is_valid = True

    #Matching the directory structure of the True test set with the submitted predicted test set
    for record_type, true_languages in true_dict.items():
        
        if record_type not in pred_dict:
            print(f"Missing record type: {record_type} in predicted test set directory")
            is_valid = False
            continue
        
        predicted_languages = pred_dict[record_type]

        for language, true_files in true_languages.items():
            
            if language not in predicted_languages:
                print(f"Missing language '{language}' in predicted test set for record type '{record_type}'")
                is_valid = False
                continue
            
            #Getting the file names for each True and Predicted test sets
            true_files = true_files.keys()
            predicted_files = predicted_languages[language].keys()

            #Checking the file extension for predicted files
            all_json_files = all(file.endswith('.json') for file in predicted_files)
            if not all_json_files:
                non_json_files = [file for file in predicted_files if not file.endswith('.json')]
                print('Predicted Files should be with JSON extension only.')
                print(f'Non JSON Files: {non_json_files}')
                is_valid = False
            
            # #Checking for any missing files in the predicted test set
            true_file_set = set([os.path.splitext(file)[0] for file in true_files])
            predicted_file_set = set([os.path.splitext(file)[0] for file in predicted_files])
            missing_files = true_file_set - predicted_file_set
            is_valid = is_valid and (not bool(missing_files))
            
            for file_name in missing_files:
                print(f"Missing file '{file_name}.json' in predicted test set for record type '{record_type}', language '{language}'")
    
    #Returning whether the directory structure is correct or not.
    return is_valid

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='LLMs4Subjects Shared Task -- Evaluations')

    parser.add_argument('--team_name', type=str, help='Team Name')
    parser.add_argument('--true_labels_dir', type=str, help='Directory containing the true GND labels')
    parser.add_argument('--pred_labels_dir', type=str, help='Directory containing the predicted GND labels')
    parser.add_argument('--results_dir', type=str, help='Directory to save the evaluation metrics')

    args = parser.parse_args()

    print('\nLLMs4Subjects Shared Task -- Evaluations')

    # Prompt for missing parameters
    team_name = args.team_name if args.team_name else input('\nTeam Name> ')
    true_labels_dir = args.true_labels_dir if args.true_labels_dir else input('\nDirectory containing the true GND labels> ')
    pred_labels_dir = args.pred_labels_dir if args.pred_labels_dir else input('\nDirectory containing the predicted GND labels> ')
    results_dir = args.results_dir if args.results_dir else input('\nDirectory to save the evaluation metrics> ')

    print('\nReading the True GND labels...')
    true_dict = read_gnd_files(true_labels_dir, True)

    print('Reading the Predicted GND labels...')
    predicted_dict = read_gnd_files(pred_labels_dir, False)

    print('\nEvaluating the directory structure of the predicted folder...')
    is_valid = validate_directory_structure(true_dict, predicted_dict)
    if not is_valid:
        print(f'The Directory structure: {pred_labels_dir} is NOT valid')
        sys.exit(1)

    print('\nEvaluating the predicted GND labels...')
    list_k = [k for k in range(5, 55, 5)]
    evaluate_and_save_to_excel(results_dir, f'{team_name}_evaluation_metrics.xlsx', true_dict, predicted_dict, list_k)
    print(f'\nFile containing the evaluation metrics score is saved at location: {results_dir}/{team_name}_evaluation_metrics.xlsx')

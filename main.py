import csv
import json
import os
 

def get_files_in_directory(folder_path: str) -> list[str]:
    file_list = []
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_list.append(os.path.join(folder_path, filename))
    return file_list

def json_to_csv(json_files:list[str], delimiter:str=','):
    # Charger le fichier JSON

    for json_file_ in json_files :
        csv_file_ = json_file_.replace("json", "csv")
        with open(json_file_, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Convertir le fichier JSON en fichier CSV
        with open(csv_file_, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=delimiter)

            # Écrire l'en-tête
            csv_writer.writerow(["question", "answer", "thematic", "subThematic", "level", "points", "times"])

            # Écrire les données
            for item in data:
                csv_writer.writerow([item['question'], "\"{" + ", ".join(item['answer']) + "}\"", item['thematic'],
                                    item['subThematic'], item['level'], item['points'], item['times']])

        print(f'Conversion terminée. Les données du fichier {json_file_} ont été écrites dans le fichier CSV : {csv_file_}')

def compute_quiz_time(question: str, answer:list[str], level: str) -> int:
    questionLenght = len(question)
    pass

# folder content json files
json_files_dir = "./json_files/"

# all files content in 'json_files_dir'
json_files = get_files_in_directory(json_files_dir)

# convertion
json_to_csv(json_files)

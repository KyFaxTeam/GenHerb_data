import json

# Charger le fichier JSON
with open("langage.json", "r", encoding="utf-8") as file:
    data = json.load(file)

donnees = []
# Parcourir les éléments du fichier
for item in data:
    # Vérifier si la structure correcte existe
    if "question" in item and len(item["question"]) == 2 :
        # Si l'attribut answer n'existe pas, le créer
        if "answer" not in item:
            answer = [item["question"][1]]
            index = 2

            keys = list(item.keys())
            values = list(item.values())

            keys.insert(2, "answer")
            values.insert(2, [answer])

            dicto = { keys[i] : values[i] for i in range(len(keys))}

            del dicto["question"][1]
            dicto["times"] = 45
            donnees.append(dicto)
        # Réorganiser la structure correcte
    else :
        item["times"] = 45
        donnees.append(item)

# Enregistrer le fichier JSON modifié
with open("langage_corrigé.json", "w", encoding="utf-8") as file:
    json.dump(donnees, file, indent=2, ensure_ascii=False)

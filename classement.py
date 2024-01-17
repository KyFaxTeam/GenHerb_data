#  il s'agit de créer à l'aide de fichiers .txt contenant des matchs de génie en herbe 
# un dossier de fichiers contenant pour chaque rubrique, les questions collectées
# dans tous les matchs

import os
from unidecode import unidecode
dossier_matchs = r"C:\Users\Josué\Desktop\Data_geh"


dossier_resultat = os.path.join(dossier_matchs, "Result")

if not os.path.exists(dossier_resultat):
    print("ok")
    os.makedirs(dossier_resultat)


rubriques = ["éclairs", "cantonnade", "identification", "langage", 
             "géographie", "mots croisés", "sport", "cinéma", 
             "association", "musique", "décentralisation", "relais"]
shift = max([len(a) for a in rubriques]) + 3

def write_rubrique(nom_rubrique, questions_rubrique):
    chemin_fichier = os.path.join(dossier_resultat, f"{nom_rubrique}.txt")
    mode_ouverture = "a" if os.path.exists(chemin_fichier) else "w"
    with open(chemin_fichier, mode_ouverture) as fichier:
        fichier.write("\n".join(questions_rubrique))
        

def epuration(chaine):
    return unidecode(chaine.lower().replace(" ", "").replace("\n",
                                    "").replace("–", "").replace("-", ""))

def search(ligne):
    pris = epuration(ligne).replace("cassetete", 
            "identification").replace("language", "langage").replace("mot",
            "mots").replace("music", "musique").replace("relai",
            "relais").replace("cantonade", "cantonnade")[0:shift]
    if pris =="":
        return None
    
    rub = [ epuration(a) for a in rubriques]

    joyau = None
    for rubrique in rub:
        if pris[0:len(rubrique)-1] in rubrique:
            print("\ni have found", rubrique,"in: ", ligne, "\n", "pris ==", pris)
            joyau = rubrique

            break
    return joyau


for fichier_match in os.listdir(dossier_matchs):
    if fichier_match == "Result":
        continue
    chemin_match = os.path.join(dossier_matchs, fichier_match)
    
    with open(chemin_match, "r") as match:
        lignes = match.readlines()
        
        rubrique_en_cours = None
        questions_rubrique = []
        
        for ligne in lignes:
            
            joyau = search(ligne)
            
            if joyau is not None:
                if len(questions_rubrique)>0:
                    print("ok")
                    write_rubrique(rubrique_en_cours, questions_rubrique)

                rubrique_en_cours = joyau
                
                questions_rubrique = []

            elif rubrique_en_cours is not None:
                
                questions_rubrique.append(ligne.strip())

        
        if rubrique_en_cours is not None and questions_rubrique:
            write_rubrique(rubrique_en_cours, questions_rubrique)

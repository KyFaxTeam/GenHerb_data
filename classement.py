#  il s'agit de créer à l'aide de fichiers .txt contenant des matchs de génie en herbe 
# un dossier de fichiers contenant pour chaque rubrique, les questions collectées
# dans tous les matchs

import os
from unidecode import unidecode
lien = r"C:\Users\Josué\Desktop\Data_geh"
dossier_matchs = os.path.join(lien, "Quiz")

dossier_resultat = os.path.join(lien, "Result")

if not os.path.exists(dossier_resultat):
    print("ok")
    os.makedirs(dossier_resultat)


rubriques = ["eclairs", "cantonnade", "identification", "langage", 
             "geographie", "motscroises", "sport", "cinema", 
             "association", "musique", "decentralisation",
             "relais", "manchette", "francophonie"]
shift = max([len(a) for a in rubriques]) + 3

def write_rubrique(nom_rubrique, questions_rubrique):
    chemin_fichier = os.path.join(dossier_resultat, f"{nom_rubrique}.txt")
    mode_ouverture = "a" if os.path.exists(chemin_fichier) else "w"
    with open(chemin_fichier, mode_ouverture, encoding ="utf-8") as fichier:
        fichier.write("\n".join(questions_rubrique)+"\n")
        

def epuration(chaine):
    return unidecode(chaine.lower().replace(" ", "").replace("\n",
                                    "").replace("–", "").replace("-", ""))

def search(ligne):
    pris = epuration(ligne).replace("cassetete", "identification").replace("language",
            "langage").replace("motscroise", "motscroises").replace("motcroises",
            "motscroises").replace("music",
            "musique").replace("relai","relais").replace("cantonade",
            "cantonnade").replace("eclair", "eclairs").replace("sports",
            "sport").replace("quiquequoi", "motscroises").replace("cinematographique",
            "...")[0:shift]
    if pris =="":
        return None
    
    rub = [ epuration(a) for a in rubriques]

    joyau = None
    for rubrique in rub:
        if pris[0:len(rubrique)] ==  rubrique:
            print("i have found", rubrique,"in:\n ", ligne)#, "\n", "pris ==", pris)
            joyau = rubrique

            break
    return joyau


for fichier_match in os.listdir(dossier_matchs):
    if not fichier_match.endswith(".txt"):
        print("FICHIER  à ne pas visiter:", fichier_match)
        continue

    print("..............", fichier_match, "..............")    
    chemin_match = os.path.join(dossier_matchs, fichier_match)
    
    with open(chemin_match, "r", encoding = 'utf-8') as match:
        lignes = match.readlines()
        
        rubrique_en_cours = None
        questions_rubrique = []
        
        for ligne in lignes:
            
            joyau = search(ligne)
            
            if joyau is not None :
                if len(questions_rubrique)>0:
                    write_rubrique(rubrique_en_cours, questions_rubrique)

                rubrique_en_cours = joyau
                
                questions_rubrique = []

            elif rubrique_en_cours is not None:
                
                questions_rubrique.append(ligne.strip())

        
        if rubrique_en_cours is not None and questions_rubrique:
            write_rubrique(rubrique_en_cours, questions_rubrique)

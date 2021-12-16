import json
import os
import sys

dossier_outillage = os.path.dirname(__file__) 
fichier_outillage = os.path.join(dossier_outillage, "outillage.json")


# récuperation du fichier JSON si il existe
if os.path.exists(fichier_outillage):
    with open(fichier_outillage,"r") as f:
        outils = json.load(f)
        print(fichier_outillage)
# sinon on créer un fichier .Json contenant le dictionnaire outil
else:
    outils = {}   
    print(fichier_outillage)

def ajout_outil():
    print("Ajouter un outil")
    designation_outil = input("Quel est la réference de l'outil : ")
    date = input("/n A quel date l'outil a t-il était installé ?  (format JJ/MM/AAAA) : ")
    position_outil = input("Quel est la position de l'outil : ")
    periodicite_outil = input("Quel est la periodicité de l'outil : ")

    # création d'un nouveau dictionnaire qui a pour clé la designation_outil           
    outils[designation_outil] = {} 

    # dans cette partie on déclare les clés : "date", "position_outil" et "periodicite",  en tant que liste ce qui résout le problème d'ajout de valeur pour la même clé
    outils[designation_outil]["date"] = list()
    outils[designation_outil]["date"].append(date)
    outils[designation_outil]["position_outil"] =list()
    outils[designation_outil]["position_outil"].append(position_outil)   
    outils[designation_outil]["periodicite"] = list()
    outils[designation_outil]["periodicite"].append(periodicite_outil)         
    print(outils)

    with open (fichier_outillage, "w") as f:
            json.dump(outils, f, indent=4)

def changer_outil():

    print(outils)
    choix_outil = input("Quel outil souhaitez-vous changer ? (saisissez le nom de l'outil) :")
    date_changement = input("Date du changement de l'outil (format JJ/MM/AAAA) : ")
    outils[choix_outil]["date"].append(date_changement)

    periodicite_outil = input("Quelle est la périodicité de l'outil : ")
    outils[choix_outil]["periodicite"].append(periodicite_outil)
    with open (fichier_outillage, "w") as f:
            json.dump(outils, f, indent=4)
    print(outils)

def afficher_outil():

    print("Voici la liste des outils : ")
    liste = outils.keys()
    print(liste)
def supprimer_outil():
    print("Supprimer un outil")
    liste = outils.keys()
    print(liste)
    supprimer_outil = input("Quel outil souhaitez-vous supprimer ? :")

    if supprimer_outil in outils:
        del outils[supprimer_outil]

        print("outil supprimé")
        
        with open (fichier_outillage, "w") as f:
            json.dump(outils, f, indent=4)

    else:    
        print("l'outil n'existe pas.")
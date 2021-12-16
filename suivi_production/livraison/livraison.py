import json
import os
import sys

dossier_outillage = os.path.dirname(__file__)
fichier_livraison = os.path.join(dossier_outillage, "livraison.json")

if os.path.exists(fichier_livraison):
    with open(fichier_livraison,"r") as f:
        livraison = json.load(f)
        print(fichier_livraison)
else:
    livraison = {}
    print(fichier_livraison)

def ajout_ordre_livraison():
    print("Infos Livraison")
    
    delivery_order  = input("Ordre de livraison: ")
    delivery_date : str = input("Renseignez la date: ")
    valid_parts: int = int(input("Renseignez le nombre de pièces conformes: "))
    invalid_parts: int = int(input("Renseignez le nombre de pièces rebuts: "))

    livraison[delivery_order] = {}
    livraison[delivery_order]["delivery_date"] = list()
    livraison[delivery_order]["delivery_date"].append(delivery_date)
    livraison[delivery_order]["valid_parts"] = list()
    livraison[delivery_order]["valid_parts"].append(valid_parts)
    livraison[delivery_order]["invalid_parts"] = list()
    livraison[delivery_order]["invalid_parts"].append(invalid_parts)
    
    # Enregistrer les infos livraison
    with open (fichier_livraison, "w") as f:
        json.dump(livraison, f, indent=4)

def afficher_livraison():
    print("Voici l'historique des livraisons : ")
    historique_livraison = livraison.keys()
    print(historique_livraison)

def supprimer_livraison():
    print("Supprimer un ordre de livraison")
    liste = livraison.keys()
    print(liste)
                
    supprimer_livraison = input("Quelle livraison voulez-vous supprimer? ")

    if supprimer_livraison in livraison :
        del livraison[supprimer_livraison]
        with open (fichier_livraison, "w") as f:
            json.dump(livraison, f, indent=4)
    print(liste)


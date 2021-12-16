from menu import menu
from outil import outillage
from menu import menu
from livraison import livraison
from menu import erreur


while True:
    
    menu.menu_principal()
    choix = erreur.verification_menu_principal()
     
    while True: 
        if choix == "1":
            menu.menu_livraison()
            choix_livraison = erreur.verification_menu_livraison()

            if choix_livraison == "1":
                livraison.ajout_ordre_livraison()
            if choix_livraison == "2":
                livraison.afficher_livraison()
            if choix_livraison == "3":
                livraison.supprimer_livraison()
            if choix_livraison == "4":
                menu.menu_principal()

        while True:
            
            if choix == "2":
                
                menu.menu_outillage()
                choix_outillage = erreur.verification_menu_outillage

                if choix_outillage == "1":
                    outillage.ajout_outil()  
                if choix_outillage == "2":
                    outillage.changer_outil()
                if choix_outillage =="3":
                    outillage.afficher_outil()
                if choix_outillage =="4":
                    outillage.supprimer_outil()
                if choix_outillage=="5":
                    menu.menu_principal()

            if choix == "3":
                print("Au revoir")
                exit()

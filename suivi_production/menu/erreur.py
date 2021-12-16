def verification_menu_principal():
    choix_menu = ["1", "2", "3"]
    choix =""
    while choix not in choix_menu:
        choix = input("-> Votre choix :  ")
        if choix not in choix_menu:
            print("Saisi invalide")
        else:
            print("")
        return choix

def verification_menu_livraison():
    choix_menu = ["1", "2", "3", "4"]
    choix =""
    while choix not in choix_menu:
        choix = input("-> Votre choix :  ")
        if choix not in choix_menu:
            print("Saisi invalide")
        else:
            print("")
        return choix

def verification_menu_outillage():
    choix_menu = ["1", "2", "3", "4", "5"]
    choix =""
    while choix not in choix_menu:
        choix = input("-> Votre choix :  ")
        if choix not in choix_menu:
            print("Saisi invalide")
        else:
            print("")
        return choix
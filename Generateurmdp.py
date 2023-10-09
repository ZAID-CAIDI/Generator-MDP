import random

#Caractere
lettre = "ABCDEFGHIJKLMNOP"
nombre = "123456789"
symboles = "!@#$%^&*()_[]"
caractere = lettre + lettre.lower() + nombre + symboles
caractere_no_symbols = lettre + lettre.lower() + nombre

while True:
    longeurmdp = int(input("Entrez la longueur de mot de passe : "))
    nombredemdp = int(input("Entrez le nombre de mote de passe à afficher : "))
    caractere_speciaux_ask = str(input("Dois-je mettre des caracteres speciaux dans le mot de passe ?"))
    if caractere_speciaux_ask == 'oui':
        for i in range(0,nombredemdp):
            mdp = ""
            for i in range(0,longeurmdp):
                cmdp = random.choice(caractere)
                mdp = mdp + cmdp
            print('Votre mot de passe est : ',mdp)
            
    elif caractere_speciaux_ask == 'non':
        for i in range(0,nombredemdp):
            mdp = ""
            for i in range(0,longeurmdp):
                cmdp = random.choice(caractere_no_symbols)
                mdp = mdp + cmdp
            print('Votre mot de passe est : ',mdp)
            
    elif caractere_speciaux_ask != 'oui' or 'non':
        print("ERREUR!")
import random
import csv

Client = {}
Compte = {}
ClientCompte = {}

def ajouterClient(numCl, MPC, numC, SoldeC):
    Client[numCl] = MPC
    Compte[numC] = SoldeC
    ClientCompte[numCl] = numC

def supprimerClient(numC):
    if numC in Compte:
        del ClientCompte[numC]
        del Client[numC]
        del Compte[numC]
        return f"Client avec le numéro de compte {numC} supprimé."
    else:
        return "Compte non trouvé."

def modifierMPClient(numCl, nouveauMPC):
    if numCl in Client:
        Client[numCl] = nouveauMPC
        return "Mot de passe modifié avec succès."
    else:
        return "Client non trouvé."

def deposer(numCl, montant):
    if numCl in ClientCompte and ClientCompte[numCl] in Compte:
        numC = ClientCompte[numCl]
        Compte[numC] += montant
        return f"Montant déposé. Nouveau solde du compte {numC}: {Compte[numC]} Dh"
    else:
        return "Client ou compte non trouvé."

def retirer(numCl, montant):
    if numCl in ClientCompte and ClientCompte[numCl] in Compte:
        numC = ClientCompte[numCl]
        if Compte[numC] >= montant:
            Compte[numC] -= montant
            return f"Montant retiré. Nouveau solde du compte {numC}: {Compte[numC]} Dh"
        else:
            return "Fonds insuffisants. Opération annulée."
    else:
        return "Client ou compte non trouvé."

genererNumCompte = lambda numCl: int(str(numCl) + str(random.randint(0, 100)))

def EcrireFichierCSV():
    with open('clients.csv', 'w', newline='') as csvfile:
        fieldnames = ['NumClient', 'CodeSecret']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for numCl, code_secret in Client.items():
            writer.writerow({'NumClient': numCl, 'CodeSecret': code_secret})
    return "Fichier CSV créé avec succès."

def manipSTS():
    num_comptes_list = list(ClientCompte.values())
    num_comptes_tuple = tuple(ClientCompte.values())
    num_comptes_set = set(ClientCompte.values())
    return num_comptes_list, num_comptes_tuple, num_comptes_set

# Programme principal
while True:
    print("\nBienvenue à la Banque!")
    print("1. Menu Agent")
    print("2. Menu Client")
    print("3. Quitter")
    choix = int(input("Choisissez une option : "))
    
    if choix == 1:
        print("\nMenu Agent:")
        print("1. Ajouter un client")
        print("2. Supprimer un client")
        agent_choice = int(input("Choisissez une option : "))
        if agent_choice == 1:
            numCl = int(input("Numéro du nouveau client : "))
            MPC = input("Code secret du nouveau client : ")
            numC = genererNumCompte(numCl)
            SoldeC = float(input("Solde initial de son compte : "))
            ajouterClient(numCl, MPC, numC, SoldeC)
            print("Compte ajouté avec succès.")
        elif agent_choice == 2:
            numC = int(input("Numéro du client à supprimer : "))
            print(supprimerClient(numC))
        else:
            print("Option invalide.")
    elif choix == 2:
        numCl = int(input("Entrez votre numéro de client : "))
        if numCl in Client:
            print("\nMenu Client:")
            print("1. Modifier le mot de passe")
            print("2. Déposer de l'argent")
            print("3. Retirer de l'argent")
            client_choice = int(input("Choisissez une option : "))
            if client_choice == 1:
                nouveauMPC = input("Nouveau mot de passe : ")
                print(modifierMPClient(numCl, nouveauMPC))
            elif client_choice == 2:
                montant = float(input("Montant à déposer : "))
                print(deposer(numCl, montant))
            elif client_choice == 3:
                montant = float(input("Montant à retirer : "))
                print(retirer(numCl, montant))
            else:
                print("Option invalide.")
        else:
            print("Client non trouvé.")
    elif choix == 3:
        break
    else:
        print("Option invalide. Veuillez choisir à nouveau.")

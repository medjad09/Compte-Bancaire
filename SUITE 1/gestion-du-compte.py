from appli import CompteBancaire

class Banque:
    def __init__(self):
        self.comptes = {}  # Dictionnaire associant numéro de compte à son solde
        self.clients = {}  # Dictionnaire associant numéro de client à son code secret
        self.client_compte = {}  # Dictionnaire associant numéro de client à son numéro de compte

    def ajouter_compte(self, titulaire):
        nouveau_compte = CompteBancaire(titulaire)
        self.comptes[nouveau_compte.numero_compte] = nouveau_compte.solde
        self.clients[titulaire] = input(f"Créer un code secret pour le client {titulaire}: ")
        self.client_compte[titulaire] = nouveau_compte.numero_compte
        return f"Compte ajouté. Numéro de compte : {nouveau_compte.numero_compte}"

    def modifier_mot_de_passe(self, client):
        if client in self.clients:
            nouveau_mot_de_passe = input("Nouveau mot de passe : ")
            self.clients[client] = nouveau_mot_de_passe
            return "Mot de passe modifié avec succès."
        else:
            return "Client non trouvé."

    def afficher_solde(self, client):
        if client in self.client_compte and self.client_compte[client] in self.comptes:
            numero_compte = self.client_compte[client]
            solde = self.comptes[numero_compte]
            return f"Solde du compte {numero_compte}: {solde} Dh"
        else:
            return "Client ou compte non trouvé."

    def deposer_argent(self, client, montant):
        if client in self.client_compte and self.client_compte[client] in self.comptes:
            numero_compte = self.client_compte[client]
            self.comptes[numero_compte] += montant
            return f"Montant déposé. Nouveau solde du compte {numero_compte}: {self.comptes[numero_compte]} Dh"
        else:
            return "Client ou compte non trouvé."

    def retirer_argent(self, client, montant):
        if client in self.client_compte and self.client_compte[client] in self.comptes:
            numero_compte = self.client_compte[client]
            if self.comptes[numero_compte] >= montant:
                self.comptes[numero_compte] -= montant
                return f"Montant retiré. Nouveau solde du compte {numero_compte}: {self.comptes[numero_compte]} Dh"
            else:
                return "Fonds insuffisants. Opération annulée."
        else:
            return "Client ou compte non trouvé."

# Exemple d'utilisation
banque = Banque()

# Ajouter un compte
print(banque.ajouter_compte(5))

# Modifier le mot de passe (remplacez le numéro de client par un existant dans votre cas)
print(banque.modifier_mot_de_passe(5))

# Afficher le solde (remplacez le numéro de client par un existant dans votre cas)
print(banque.afficher_solde(5))

# Déposer de l'argent (remplacez le numéro de client et le montant par des valeurs appropriées)
print(banque.deposer_argent(5, 100))

# Retirer de l'argent (remplacez le numéro de client et le montant par des valeurs appropriées)
print(banque.retirer_argent(5, 50))

import random

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.identifiant_unique = random.randint(1, 1000)
        self.numero_compte = int(str(titulaire) + str(random.randint(0, 100)))
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        return f"Montant déposé. Nouveau solde : {self.solde}"

    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            return f"Montant retiré. Nouveau solde : {self.solde}"
        else:
            return "Fonds insuffisants. Opération annulée."

class Banque:
    def __init__(self):
        self.comptes = {}

    def ajouter_compte(self, titulaire):
        nouveau_compte = CompteBancaire(titulaire)
        self.comptes[nouveau_compte.numero_compte] = nouveau_compte
        return f"Compte ajouté. Numéro de compte : {nouveau_compte.numero_compte}"

    def supprimer_compte(self, numero_compte):
        if numero_compte in self.comptes:
            del self.comptes[numero_compte]
            return f"Compte {numero_compte} supprimé."
        else:
            return "Compte non trouvé."

# Exemple d'utilisation
banque = Banque()

# Ajouter un compte
print(banque.ajouter_compte(5))

# Supprimer un compte (remplacez le numéro de compte par un existant dans votre cas)
print(banque.supprimer_compte(556))

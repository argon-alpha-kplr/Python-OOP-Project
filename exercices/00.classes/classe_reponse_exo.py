class Product:
    def __init__(self, cost, price, marque, nom):
        self.cost = cost
        self.price = price
        self.marque = marque
        self.nom = nom
    
    def afficher_valeurs(self):
        print("- le cout est :", self.cost,"$")
        print("-le price est :", self.price, "$")
        print("-le marque est :", self.marque)
        print("-le nom est :", self.nom)

class Meuble(Product):
    def __init__(self, cost, price, marque, materiaux, nom, couleur, dimension):
        super().__init__(cost, price, marque, nom)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimension = dimension

    def afficher_valeurs(self):
        print("- le materiel", self.materiaux)
        print("-Couleurs est :", self.couleur)
        print("-dimension est:", self.dimension)
        super().afficher_valeurs()

  
class Canape(Product):
    def __init__(self, cost, price, marque, materiaux, nom, couleur, dimension):
        super().__init__(cost, price, marque, nom)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimension = dimension

    def afficher_valeurs(self):
        print("- le materiel", self.materiaux)
        print("-Couleurs est :", self.couleur)
        print("-dimension est:", self.dimension)
        super().afficher_valeurs()


class Chaise(Product):
    def __init__(self, cost, price, marque, materiaux, nom, couleur, dimension):
        super().__init__(cost, price, marque, nom)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimension = dimension

    def afficher_valeurs(self):
        print("- le materiel", self.materiaux)
        print("-Couleurs est :", self.couleur)
        print("-dimension est:", self.dimension)
        super().afficher_valeurs()


class Table(Product):
    def __init__(self, cost, price, marque, materiaux, nom, couleur, dimension):
        super().__init__(cost, price, marque, nom)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimension = dimension

    def afficher_valeurs(self):
        print("- le materiel", self.materiaux)
        print("-Couleurs est :", self.couleur)
        print("-dimension est:", self.dimension)
        super().afficher_valeurs()
import classe_reponse_exo

# creaction des instance de meuble specifique pour canne
Canape1= classe_reponse_exo.Canape(1000, 2000, "OKLM", "cuire", "canape","blanc", "200x100x80")
print(" POUR CANAPE 1------------------------------------")
Canape1.afficher_valeurs()

Canape2= classe_reponse_exo.Canape(800, 1600, "SIESTA", "tissus", "canape","bleu", "150x90x70", )
print(" POUR CANAPE 2------------------------------------")
Canape2.afficher_valeurs()

#pour les chaise
print(" ------------------------------------")
print(" ")
Chaise1= classe_reponse_exo.Chaise(50, 100, "PEPOUSE", "plastique", "chaise","rouge", "50x50x70", )
print(" POUR CHAISE 1------------------------------------")
Chaise1.afficher_valeurs()

Chaise2= classe_reponse_exo.Chaise(75, 150, "PEPOUSE", "metal", "chaise","Gris", "60x60x80", )
print(" POUR CHAISE 2------------------------------------")
Chaise2.afficher_valeurs()

#pour les tables 
print(" ------------------------------------")
print(" ")
Table1= classe_reponse_exo.Chaise(350, 700, "TEX", "verre", "table","transparents", "50x50x70", )
print(" POUR TABLE 1------------------------------------")
Table1.afficher_valeurs()

Table2= classe_reponse_exo.Chaise(250, 500, "TEX", "bois", "table","Chene", "150x80x75", )
print(" POUR TABLE 2------------------------------------")
Table2.afficher_valeurs()
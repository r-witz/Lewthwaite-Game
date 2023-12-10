# Lewthwaite

Deux joueurs s’affrontent sur un plateau bi-dimensionnel carré de n cases sur n cases où n est de la forme n=4k+1 avec k∈N∗. Les valeurs possibles de n sont donc 5,9,13,17 etc.
Le premier joueur possède des pions blancs et le second des pions noirs.

Il y a donc un pion noir sur la case située sur la première ligne et première colonne, puis une alternance entre pions blancs et pions noirs de case en case. Avec pour seule exception la case centrale du plateau qui est vide.
Les configurations initiales pour les autres valeurs possibles de n suivent la même logique.


Les blancs commencent, puis à tour de rôle les joueurs déplacent l’un de leurs pions vers la case vide, avec pour seule condition que le pion en question soit adjacent orthogonalement à la case vide.

Le gagnant est le dernier joueur à pouvoir déplacer un pion. Autrement dit, dès qu’un joueur ne peut plus déplacer de pion il a perdu.

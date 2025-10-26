# Explication du code

## L'algorithme **Dijkstra**

On définit notre fonction qui va prendre en paramètre un **graphe**, un **point de départ** et un **point d'arrivée**.

Dans un premier temps, on définit nos variables :

- `distances` : la distance minimale depuis le départ,
- `precedent` : le noeud suivant ou le meilleur chemin trouvé vers un noeud _n_,
- `visite` : la liste des noeuds déjà visités.

Ensuite, on parcourt tous les noeuds du graphe — donc toutes les clés du dictionnaire `graphe`.  
On crée dans le dictionnaire `distances` une entrée pour chaque noeud, associée à la valeur ∞, car on ne connaît encore aucune distance minimale (tout est donc théoriquement infiniment loin).

La boucle principale permet de chercher, parmi les noeuds non visités, celui qui a la plus petite distance depuis le départ.  
`noeud_courant` sera le noeud choisi comme le plus proche, et `distance_min` garde la plus petite distance trouvée.  
Le `inf` nous permet de nous assurer que toute vraie distance sera plus petite.

Ensuite, on parcourt les noeuds du graphe en ignorant ceux dont la distance est définitive, pour ensuite garder en mémoire ceux qui ont la distance la plus petite.  
Dès qu'on trouve un noeud plus proche, on le mémorise dans la variable `noeud_courant`.  
Le `break` permet d'arrêter lorsque les noeuds restants ont une distance infinie, donc non atteignables depuis le point de départ.

La boucle `for voisin, poids in graphe[noeud_courant]:` permet d'examiner toutes les routes possibles qui partent du noeud sur lequel on est à ce moment.  
La distance est alors calculée en ajoutant le `poids`, qui est la distance entre le `noeud_courant` et le `voisin`.  
La distance est alors stockée dans la variable `nouvelle_distance`, mais cette distance n’est toujours pas validée ni définitive.  
On compare ensuite le nouveau chemin avec celui qu’on connaissait déjà : si le nouveau est plus court, on le définit comme meilleur chemin, sinon on ne change rien.

> Petit détail à préciser : les poids (donc les distances) doivent être **positifs et non négatifs**, sinon l’algorithme ne renverra pas un résultat correct.

Enfin, la dernière partie de cet algorithme est la **reconstruction du chemin**.  
On part de l’arrivée en remontant la chaîne des `precedent` jusqu’à `None`.

---

## L'algorithme **A\***

Cet algorithme renvoie le même résultat que l’algorithme **Dijkstra**, c’est-à-dire trouver le **chemin le plus court** entre un noeud de départ et un noeud d’arrivée.  
Ce qui le différencie de Dijkstra, c’est qu’il ajoute une **heuristique**, donc une estimation de la distance restante, pour accélérer la recherche du meilleur chemin.

Il prendra les mêmes paramètres que Dijkstra, **en ajoutant** le paramètre `position`, qui est un dictionnaire de coordonnées.

Au début de l’algorithme, on définit :

- `ouverts` : la liste des noeuds à explorer,
- `precedent` : pour reconstruire le chemin à la fin,
- `g_score` : la distance réelle depuis le départ,
- `f_score` : la distance estimée totale (`g_score` + estimation heuristique).

On parcourt les noeuds du graphe et on leur attribue une distance infinie (on ne sait pas encore comment les atteindre) et aucun prédécesseur connu.

On initialise `g_score[depart] = 0`, car on est au point de départ, et `f_score[depart]`, qui sera l’estimation du coût total du départ à l’arrivée, calculée grâce à la fonction heuristique (expliquée à la fin).

Au début de la boucle principale, on l’initialise et on y entre tant qu’il reste des noeuds à explorer.  
On choisit dans la liste `ouverts` le noeud avec le plus petit score total, car il combine la distance réelle déjà parcourue et une estimation du reste du trajet.  
C’est ici que l’on voit la différence d’optimisation avec Dijkstra, car il ne choisit pas un nœud au hasard.

Ensuite, on vérifie si on a atteint la cible — c’est-à-dire qu’à chaque itération, on vérifie si le nœud choisi est le noeud d’arrivée.  
Si c’est le cas, on initialise une variable `chemin` qui va nous permettre de refaire le chemin complet.  
La boucle `while` nous permet de revenir en arrière grâce au dictionnaire `precedent`, car pendant toute la recherche, on a mis à jour `precedent` quand un meilleur chemin était trouvé.

Le `ouverts.remove(courant)` permet de retirer `courant` de la liste des noeuds à explorer.

Dans la seconde boucle, on va parcourir les voisins du noeud courant.  
On regarde tous les voisins directs de `courant`.  
On calcule le score provisoire avec la variable `tentative_g`, qui est la distance réelle du départ jusqu’à `voisin` en passant par `courant`.  
Enfin, on compare le nouveau chemin `tentative_g` avec `g_score[voisin]` et, si c’est le plus court, alors ça devient un meilleur itinéraire.  
On met à jour `precedent[voisin]`, `g_score[voisin]` et `f_score[voisin]`, où l’on estime le coût total de ce chemin jusqu’à la destination.  
Si ce voisin n’est pas déjà dans `ouverts`, alors on l’ajoute.

---

## Algorithme **Heuristique**

C’est une petite fonction qu’on a utilisée précédemment pour l’algorithme `a_etoile`, et qui a un rôle très important.  
Cette fonction permet de calculer une estimation entre un noeud `a` et `b` en se basant sur leurs coordonnées.

On va initier les positions du point de départ (le nœud `a`) et du point d’arrivée (le nœud `b`).  
Ensuite, on applique la formule du **carré de la distance euclidienne**, considérée comme la distance “à vol d’oiseau” entre deux points.

Cette distance vaut :

d² = (x₁ − x₂)² + (y₁ − y₂)²

## ⚙️ Prérequis

- **Python 3.8 ou supérieur** (aucune bibliothèque externe n’est requise)

Vérifiez votre version de Python avec :

```bash
python --version

ou

python3 --version

```

Pour lancer le programme :

```bash
python nomduficher.py

ou

python3 nomdufichier.py

```

**Projet réalisé par :** _Enzo MOITA et Baptise ROY_

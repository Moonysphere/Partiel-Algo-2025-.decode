def dijkstra(graphe, depart, arrivee):
    distances = {}
    precedent = {}
    visites = []

    for noeud in graphe:
        distances[noeud] = float('inf')
        precedent[noeud] = None

    distances[depart] = 0

    while len(visites) < len(graphe):
        noeud_courant = None
        distance_min = float('inf')

        for noeud in graphe:
            if noeud not in visites and distances[noeud] < distance_min:
                noeud_courant = noeud
                distance_min = distances[noeud]

        if noeud_courant is None:
            break

        visites.append(noeud_courant)

        for voisin, poids in graphe[noeud_courant]:
            nouvelle_distance = distances[noeud_courant] + poids
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                precedent[voisin] = noeud_courant

    chemin = []
    noeud = arrivee
    while noeud is not None:
        chemin.insert(0, noeud)
        noeud = precedent[noeud]

    return chemin, distances[arrivee]



def heuristique(a, b, positions):
    x1, y1 = positions[a]
    x2, y2 = positions[b]
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)


def a_etoile(graphe, positions, depart, arrivee):
    ouverts = [depart]
    precedent = {}
    g_score = {}
    f_score = {}

    for noeud in graphe:
        precedent[noeud] = None
        g_score[noeud] = float('inf')
        f_score[noeud] = float('inf')

    g_score[depart] = 0
    f_score[depart] = heuristique(depart, arrivee, positions)

    while len(ouverts) > 0:
        courant = ouverts[0]
        for noeud in ouverts:
            if f_score[noeud] < f_score[courant]:
                courant = noeud

        if courant == arrivee:
            chemin = []
            noeud = courant
            while noeud is not None:
                chemin.insert(0, noeud)
                noeud = precedent[noeud]
            return chemin, g_score[arrivee]

        ouverts.remove(courant)

        for voisin, poids in graphe[courant]:
            tentative_g = g_score[courant] + poids
            if tentative_g < g_score[voisin]:
                precedent[voisin] = courant
                g_score[voisin] = tentative_g
                f_score[voisin] = tentative_g + heuristique(voisin, arrivee, positions)
                if voisin not in ouverts:
                    ouverts.append(voisin)

    return None, float('inf')



graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [("F", 11)],
    "E": [("D", 4)],
    "F": []
}

positions = {
    'A': (0, 0),
    'B': (2, 0),
    'C': (3, 2),
    'D': (5, 1),
    'E': (4, 3),
    'F': (6, 2)
}

print("Dijkstra :")
path, dist = dijkstra(graph, 'A', 'D')
print("Chemin :", path, "Distance :", dist)

print("\nA* :")
path, dist = a_etoile(graph, positions, 'A', 'D')
print("Chemin :", path, "Distance :", dist)


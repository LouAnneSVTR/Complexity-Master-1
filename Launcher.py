import random

from Algorithme.LPT import LPT, LPT_I_r
from Algorithme.LSA import LSA, LSA_I_r
from Algorithme.RMA import RMA, RMA_I_r


def generate_tab_I_p(D, M, p):
    m = 2 * p

    nbTacheDuree1 = 4 * p
    nbTacheDuree2 = 2 * p * (p - 1)

    for i in range(nbTacheDuree1):
        D.append(1)

    for i in range(nbTacheDuree2):
        D.append(2)

    D.append(2 * p)

    for i in range(m):
        M.append(0)


def generate_tab_I_r(D, M, m, n, k, d_min, d_max):

    for i in range(m):
        M.append(0)

    L = []
    for j in range(k):
        for i in range(n):
            D.append(random.randint(d_min, d_max))

        L.append((D, M, max(D), int(sum(D) / m)))
        D = []

    return L


def launcher():
    type = -1

    D = []
    M = []

    print("Type d'instance :\n",
          "[1] Génération d'une instance de type I_p\n",
          "[2] Génération aléatoire de plusieurs instance")

    while int(type) not in (1, 2):
        type = int(input("choix: "))

    if type == 1:
        p = int(input("Entrée la valeur de p: "))
        generate_tab_I_p(D, M, p)

        max_bound = max(D)
        average_bound = int(sum(D) / (2 * p))

        print()

        print("borne inferieur 'maximum' : ", max_bound)
        print("borne inferieur 'moyenne' : ", average_bound)

        print()

        result = LSA(M, D, average_bound, max_bound)
        print("Résultat LSA = ", result[0])
        print("ratio LSA    = ", result[1])

        print()

        result = LPT(M, D, average_bound, max_bound)
        print("Résultat LPT = ", result[0])
        print("ratio LPT    = ", result[1])

        print()

        result = RMA(M, D, average_bound, max_bound)
        print("Résultat RMA = ", result[0])
        print("ratio RMA    = ", result[1])

    elif type == 2:

        m = int(input("Nombre de machine : "))
        n = int(input("Nombre de tâche : "))
        k = int(input("Nombre d'instance : "))

        d_min = int(input("Durée de tâche minimum : "))
        d_max = int(input("Durée de tâche maximum : "))

        L = generate_tab_I_r(D, M, m, n, k, d_min, d_max)

        average_LSA = LSA_I_r(L)
        average_LPT = LPT_I_r(L)
        average_RMA = RMA_I_r(L)

        print("ratio moyen LSA = ", average_LSA)
        print("ratio moyen LPT = ", average_LPT)
        print("ratio moyen RMA = ", average_RMA)

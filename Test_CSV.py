import random

import Launcher
import csv

from Algorithme.LPT import LPT, LPT_I_r
from Algorithme.LSA import LSA, LSA_I_r
from Algorithme.RMA import RMA, RMA_I_r

"""
Author SAUVÊTRE Lou-Anne, M1 ALMA, University of Nantes

This program aims to implement the LSA (List Scheduling Algorithm) method which takes the tasks in the order initially provided
and assigns each task to the first available machine.

"""


def generate_Ip_test():
    # Data
    p_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 120, 140, 160,
              180, 200, 300]
    D = []
    M = []
    tab_result_LSA = []
    tab_result_LPT = []
    tab_result_RMA = []

    for i in range(len(p_data)):
        # Generation of datas for test with i
        Launcher.generate_tab_I_p(D, M, p_data[i])

        # Copy to avoid data inconsistency
        M_LSA = M.copy()
        M_LPT = M.copy()
        D_LPT = D.copy()
        M_RMA = M.copy()

        max_bound = max(D)
        average_bound = int(sum(D) / (2 * p_data[i]))

        # Fetching the result tuple from LSA, LPT and RMA
        result_LSA = LSA(M_LSA, D, average_bound, max_bound)
        result_LPT = LPT(M_LPT, D_LPT, average_bound, max_bound)
        result_RMA = RMA(M_RMA, D, average_bound, max_bound)

        # Addition in our final results the ratios
        tab_result_LSA.append(result_LSA[1])
        tab_result_LPT.append(result_LPT[1])
        tab_result_RMA.append(result_RMA[1])

        # Data reset
        D = []
        M = []

    return tab_result_LSA, tab_result_LPT, tab_result_RMA


def generate_Ir_test():
    m = random.randint(2, 50)
    n = random.randint(m + 1, m * m + m + 1)
    k = random.randint(2, 100)
    d_min = random.randint(1, 150)
    d_max = random.randint(d_min, d_min * 4)

    D = []
    M = []

    L = Launcher.generate_tab_I_r(D, M, m, n, k, d_min, d_max)

    average_LSA = LSA_I_r(L)
    average_LPT = LPT_I_r(L)
    average_RMA = RMA_I_r(L)

    return m, n, k, d_min, d_max, average_LSA, average_LPT, average_RMA


def data_in_CSV(tab_result_LSA, tab_result_LPT, tab_result_RMA):
    with open('data_Ip.csv', 'w', newline='') as fichiercsv:
        writer = csv.writer(fichiercsv)
        writer.writerow(['p', 'Ratio LSA', 'p', 'Ratio LPT', 'p', 'Ratio RMA'])

        p_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 120, 140, 160,
                  180, 200, 300]

        for row in range(len(p_data)):
            writer.writerow(
                [p_data[row], tab_result_LSA[row], p_data[row], tab_result_LPT[row], p_data[row], tab_result_RMA[row]])

    with open('data_Ir.csv', 'w', newline="") as fichiercsv:
        writer = csv.writer(fichiercsv)
        writer.writerow(['m', 'n', 'k', 'd_min', 'd_max', 'ratio moyen LSA', 'ratio moyen LPT', 'ratio moyen RMA'])

        for row in range(random.randint(30, 70)):
            output = generate_Ir_test()
            writer.writerow([output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7]])
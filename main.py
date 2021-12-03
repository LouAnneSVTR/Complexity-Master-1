"""
Author SAUVÊTRE Lou-Anne, M1 ALMA, University of Nantes

This program aims to implement the LSA (List Scheduling Algorithm) method which takes the tasks in the order initially provided
and assigns each task to the first available machine.

"""

from Algorithme.LSA import LSA
from Test_CSV import generate_Ip_test, data_in_CSV
from Launcher import launcher


def print_tab(tab):
    for i in tab:
        print(i, '- ', end='')
    print()


if __name__ == '__main__':
    launcher()
    """
    tab_result = generate_Ip_test()
    tab_result_LSA = tab_result[0]
    tab_result_LPT = tab_result[1]
    tab_result_RMA = tab_result[2]

    data_in_CSV(tab_result_LSA, tab_result_LPT, tab_result_RMA)"""


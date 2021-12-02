# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Algorithme.LSA import LSA
from Test_CSV import generate_Ip_test, data_in_CSV
from Launcher import launcher


def print_tab(tab):
    for i in tab:
        print(i, '- ', end='')
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #launcher()
    tab_result = generate_Ip_test()
    tab_result_LSA = tab_result[0]
    tab_result_LPT = tab_result[1]
    tab_result_RMA = tab_result[2]

    data_in_CSV(tab_result_LSA, tab_result_LPT, tab_result_RMA)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

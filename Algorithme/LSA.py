"""
Author SAUVÊTRE Lou-Anne, M1 ALMA, University of Nantes

This program aims to implement the LSA (List Scheduling Algorithm) method which takes the tasks in the order initially provided
and assigns each task to the first available machine.

"""


def LSA(machine_list, task_list, middle_bound, max_bound):
    machine_list_copy = machine_list.copy()

    for i in range(len(task_list)):
        minimum = min(machine_list_copy)
        pos = machine_list_copy.index(minimum)
        machine_list_copy[pos] = machine_list_copy[pos] + task_list[i]

    max_ = max(machine_list_copy)
    max_bound_ = max(max_bound, middle_bound)
    ratio = max_ / max_bound_

    return max_, ratio


#For calcul the average between Ir instances
def LSA_Average_I_r(L):
    L_copy = L.copy()
    out = 0
    for i in L_copy:
        tuplet = LSA(i[1], i[0], i[3], i[2])
        out += tuplet[1]

    return out / len(L)

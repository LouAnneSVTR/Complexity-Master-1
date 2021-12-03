import random

"""
Author SAUVÊTRE Lou-Anne, M1 ALMA, University of Nantes

This program aims to implement the RMA (Random Machine Assignment) method , which, for each task in the order initially 
provided, randomly determines which machine will perform it.

"""

def RMA(machine_list, task_list, middle_bound, max_bound):
    machine_list_copy = machine_list.copy()

    for i in range(len(task_list) - 1):
        next_machine = random.randint(0, len(machine_list_copy) - 1)
        machine_list_copy[next_machine] += task_list[i]

    max_ = max(machine_list_copy)
    max_bound_ = max(max_bound, middle_bound)
    ratio = max_ / max_bound_

    return max_, ratio


#For calcul the average between Ir instances
def RMA_Average_I_r(L):
    L_copy = L.copy()
    out = 0
    for i in L_copy:
        tuplet = RMA(i[1], i[0], i[3], i[2])
        out += tuplet[1]

    return out / len(L)

import numpy as np

def table_shift(array, table_array):
    array_shifted = array[table_array - 1]
    return array_shifted

def array_split(array):
    return np.split(array, 2)

def shifting_LtoR(array):
    return np.roll(array, -1)

table_p_10 = np.array([3, 5, 2, 7, 4, 10, 1, 9, 8, 6])
table_p_08 = np.array([6, 3, 7, 4, 8, 5, 10, 9])



def split_and_merge(key):
    left_split, right_split = array_split(key)
    return np.concatenate((shifting_LtoR(left_split), shifting_LtoR(right_split)))

def key_generation_1(key, table):
    k = table_shift(key, table)
    key_merge = split_and_merge(k)
    return table_shift(key_merge, table)

def key_generation_2(key, table):
    return split_and_merge(key)


def sdes(k:str,N_table:int):
    key = np.array(list(k), dtype='int')
    if N_table == 10:
        key_1 = key_generation_1(key, table_p_10)
        return "".join(key_1.astype(str))
    else:
        key_2 = key_generation_2(key_1, table_p_08)
        return "".join(key_2.astype(str))

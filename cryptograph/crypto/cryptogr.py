import numpy as np
S0 = np.array([[1, 0, 3, 2],
               [3, 2, 1, 0],
               [0, 2, 1, 3],
               [3, 1, 3, 2]])

S1 = np.array([[0, 1, 2, 3],
               [2, 0, 1, 3],
               [3, 0, 1, 0],
               [2, 1, 0, 3]])


def P10(key):
    return key[2]+key[4]+key[1]+key[6]+key[3]+key[9]+key[0]+key[8]+key[7]+key[5]


def Shift(key,n):
    return key[n:] + key[:n]


def P8(key):
    return key[5]+key[2]+key[6]+key[3]+key[7]+key[4]+key[9]+key[8]


def IP(value):
    return value[1]+value[5]+value[2]+value[0]+value[3]+value[7]+value[4]+value[6]


def IP_re(value):
    return value[3]+value[0]+value[2]+value[4]+value[6]+value[1]+value[7]+value[5]


def F(value,K):
    value_EP=value[3]+value[0]+value[1]+value[2]+value[1]+value[2]+value[3]+value[0]
    result = np.binary_repr(int(value_EP, 2) ^ int(K, 2), width=8)
    result_L = result[:4]
    result_R = result[4:]
    PL_row, PL_col = int(result_L[0]+result_L[3],2), int(result_L[1]+result_L[2],2)
    PL = np.binary_repr(S0[PL_row, PL_col], width=2)
    PR_row, PR_col = int(result_R[0]+result_R[3],2), int(result_R[1]+result_R[2],2)
    PR = np.binary_repr(S1[PR_row, PR_col], width=2)
    F_result = P4(PL + PR)
    return F_result


def Fk(L,R,SK):
    F_result = F(R,SK)
    L = np.binary_repr(int(L, 2) ^ int(F_result, 2), width=4)
    Fk_result = L + R
    return Fk_result


def P4(value):
    return value[1]+value[3]+value[2]+value[0]


def SW(value):
    return value[4:]+value[:4]
def Encry(plaintext,key):
    plaintext_IP=IP(plaintext)
    K1=P8(Shift(P10(key)[:5],1)+Shift(P10(key)[5:],1))
    K2=P8(Shift(Shift(P10(key)[:5],1),2)+Shift(Shift(P10(key)[5:],1),2))
    plaintext_Fk1=Fk(plaintext_IP[:4],plaintext_IP[4:],K1)
    plaintext_Fk1=SW(plaintext_Fk1)
    plaintext_Fk2=Fk(plaintext_Fk1[:4],plaintext_Fk1[4:],K2)
    ciphertext=IP_re(plaintext_Fk2)
    return ciphertext
def Decry(ciphertext,key):
    ciphertext_IP=IP(ciphertext)
    K1=P8(Shift(P10(key)[:5],1)+Shift(P10(key)[5:],1))
    K2=P8(Shift(Shift(P10(key)[:5],1),2)+Shift(Shift(P10(key)[5:],1),2))
    ciphertext_Fk1=Fk(ciphertext_IP[:4],ciphertext_IP[4:],K2)
    ciphertext_Fk1=SW(ciphertext_Fk1)
    ciphertext_Fk2=Fk(ciphertext_Fk1[:4],ciphertext_Fk1[4:],K1)
    plaintext=IP_re(ciphertext_Fk2)
    return plaintext


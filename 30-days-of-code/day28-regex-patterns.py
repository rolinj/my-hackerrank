import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    name_list = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if emailID.endswith("@gmail.com"):
            name_list.append(firstName)

    name_list.sort()
    for i in range(len(name_list)):
        print(name_list[i])
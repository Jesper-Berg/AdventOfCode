import numpy as np
input = np.loadtxt(fname = "input.txt")

for i in range(len(input) - 1):
    for j in range(1, len(input) - 1):
        for k in range(2, len(input) - 1):
            if input[i] + input[j] + input[k]  == 2020:
                print(input[i] * input[j] * input[k])
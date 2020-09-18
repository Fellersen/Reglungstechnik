from pedantic import pedantic

import numpy as np
import matplotlib.pyplot as plt


@pedantic
def addieren(a: int, b: int) -> int:
    return a+b

def plot(t1, v1):
    plt.plot(t1, v1, "g", label="measured values")
    plt.legend()
    plt.grid()
    plt.ylabel('Values')
    plt.xlabel('time in s')
    plt.show()
    return 0


if __name__ == '__main__':
    print("Hallo World!")
    print(addieren(a=1, b=2))
    time = np.loadtxt('PT2_s_01.txt', usecols=0)
    value = np.loadtxt('PT2_s_01.txt', usecols=1)
    plot(t1=time, v1=value)

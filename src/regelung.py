import numpy as np
import matplotlib.pyplot as plt
from pedantic import pedantic


@pedantic
def addieren(a: int, b: int) -> int:
    return a+b


def plot_graph(source_path: str) -> None:
    time_sys = np.loadtxt(source_path, usecols=0)
    value_sys = np.loadtxt(source_path, usecols=1)
    plt.plot(time_sys, value_sys, "g", label="measured values")
    plt.legend()
    plt.grid()
    plt.ylabel('Values in ...')
    plt.xlabel('time in s')
    plt.show()


@pedantic
def steady_state(source_path: str) -> None:
    x = str(round(np.loadtxt(source_path, usecols=1)[len(np.loadtxt(source_path, usecols=1)) - 1], 4))
    print('The steady state condition is archived at ' + x + ".")


if __name__ == '__main__':
    print(addieren(a=1, b=2))
    source = 'C:\\Users\\Fellersen\\Documents\\GitHub\\Reglungstechnik\\data\\transmission_characteristics' \
             '\\PT2_s_01.txt'
    #steady_state(source_path=source)
    #plot_graph(source_path=source)

    array = np.loadtxt(source, usecols=1)
    end_value = array[len(array) - 1]
    upper_border = end_value * (1 + 0.05)
    lower_border = end_value * (1 - 0.05)
    i = -1
    merker = 0
    while merker < lower_border:
        i = i + 1
        merker = array[i]
    overshoot_up = max(array)
    print(end_value)
    print(lower_border)
    print(i)
    print(overshoot_up)

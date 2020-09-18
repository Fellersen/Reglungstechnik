import numpy
import numpy as np
import matplotlib.pyplot as plt
from pedantic import pedantic


@pedantic
def addieren(a: int, b: int) -> int:
    return a+b


def plot_graph(time: numpy.ndarray, value: numpy.ndarray) -> None:
    plt.plot(time, value, "g", label="measured values")
    plt.legend()
    plt.grid()
    plt.ylabel('Values in ...')
    plt.xlabel('time in s')
    plt.show()


if __name__ == '__main__':
    print(addieren(a=1, b=2))
    source_path = 'C:\\Users\\Fellersen\\Documents\\GitHub\\Reglungstechnik\\data\\transmission_characteristics' \
                  '\\PT2_s_01.txt'
    time_sys = np.loadtxt(source_path, usecols=0)
    value_sys = np.loadtxt(source_path, usecols=1)
    plot_graph(time=time_sys, value=value_sys)

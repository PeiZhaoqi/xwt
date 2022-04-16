# encoding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['Arial']


def s4_dog():

    names = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']

    """s4-dog"""
    x = range(len(names))
    mean1 = list(pd.read_csv("ACC_s4-dog.csv")["Accuracy"])
    var1 = list(pd.read_csv("ACC_s4-dog.csv")["char"])

    plt.errorbar(x, mean1, var1,
                 capsize=4, capthick=1,
                 linewidth=1.5, marker='o',
                 ms=7,
                 label=u'S4-dog Dataset')




    """moni"""
    mean2 = list(pd.read_csv("ACC_moni.csv")["Accuracy"])
    var2 = list(pd.read_csv("ACC_moni.csv")["char"])

    plt.errorbar(x, mean2, var2,
                 capsize=4, capthick=1,
                 linewidth=1.5, marker='x',
                 ms=7,
                 label=u'Synthetic Dataset')


    plt.xticks(x, names, fontsize=12)
    plt.yticks(fontsize=12)

    plt.legend(loc='upper right')

    plt.tick_params(top=True, bottom=True, left=True, right=True)

    plt.tick_params(direction='in')

    plt.grid(axis='y', alpha=0.3)
    plt.grid(axis='x', alpha=0.3)

    plt.subplots_adjust(bottom=0.15)


    plt.xlim(-0.2, 5.2)
    plt.ylim(0.65, 1)

    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Percentage", size=14)  # X轴标签
    plt.ylabel("MV Accuracy", size=14)  # Y轴标签
    path = 'ACC_down.jpg'
    plt.gcf().savefig(path, dpi=1800, format='jpg')
    plt.show()







if __name__ == '__main__':
    s4_dog()
# encoding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['Arial']


def display():

    labels = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']

    """s4-dog"""
    x = range(len(labels))
    mean1 = list(pd.read_csv("ACC_s4-dog.csv")["Accuracy"])
    var1 = list(pd.read_csv("ACC_s4-dog.csv")["char"])
    var_top1 = []
    var_bottom1 = []
    for i in range(len(mean1)):
        var_top1.append(mean1[i] + var1[i])
        var_bottom1.append(mean1[i] - var1[i])

    plt.plot(labels, mean1, marker='+', label=u's4-dog')
    plt.fill_between(labels, var_top1, var_bottom1, facecolor='gray', alpha=0.1)



    """CSTA"""
    mean2 = list(pd.read_csv("ACC_CSTA.csv")["Accuracy"])
    var2 = list(pd.read_csv("ACC_CSTA.csv")["char"])
    var_top2 = []
    var_bottom2 = []
    for i in range(len(mean1)):
        var_top2.append(mean2[i] + var2[i])
        var_bottom2.append(mean2[i] - var2[i])

    plt.plot(labels, mean2, marker='x', label=u'CSTA')
    plt.fill_between(labels, var_top2, var_bottom2, facecolor='gray', alpha=0.1)



    plt.legend()  # 让图例生效
    plt.xticks(x, labels)
    plt.grid(axis='y')

    plt.xlim(0, 5)
    plt.ylim(0.65, 1)

    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Proportion", size=12)  # X轴标签
    plt.ylabel("MV Accuracy", size=10)  # Y轴标签
    path = 's4-dog_trec2010_exp2.pdf'
    plt.gcf().savefig(path, dpi=600, format='pdf')
    plt.show()







if __name__ == '__main__':
    display()
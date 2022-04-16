# encoding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['Arial']


def s4_dog():

    names = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']

    """"""
    x = range(len(names))
    mean1 = list(pd.read_csv("resultGLAD_acc_result.csv")["Accuracy"])
    var1 = list(pd.read_csv("resultGLAD_acc_result.csv")["char"])

    plt.errorbar(x, mean1, var1, color='#1f77b4',
                 capsize=4, capthick=1,
                 linewidth=1.5, marker='x',
                 mec='#1f77b4', mfc='#1f77b4', ms=7,
                 label=u'GLAD')


    """"""
    mean2 = list(pd.read_csv("resultGLAD_acc_result_del_t7.csv")["Accuracy"])
    var2 = list(pd.read_csv("resultGLAD_acc_result_del_t7.csv")["char"])

    plt.errorbar(x, mean2, var2, color='#d62728',
                 capsize=4, capthick=1,
                 linewidth=1.5, marker='o',
                 mec='#d62728', mfc='#d62728', ms=7,
                 label=u'K-GLAD')





    plt.legend()  # 让图例生效
    plt.xticks(x, names)
    plt.grid(axis='y')

    plt.xlim(-0.2, 5.2)
    plt.ylim(0.65, 1)

    plt.tick_params(top=True, bottom=True, left=True, right=True)
    plt.tick_params(direction='in')

    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Percentage", size=18)  # X轴标签
    plt.ylabel("GLAD Accuracy", size=18)  # Y轴标签
    path = 'resultGLAD_Delete_synthetic.jpg'
    plt.gcf().savefig(path, dpi=1800, format='jpg')
    plt.show()







if __name__ == '__main__':
    s4_dog()
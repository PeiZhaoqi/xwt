# encoding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['Arial']


def plt_CDK():

    names = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']

    """MV"""
    x = range(len(names))
    mean1 = list(pd.read_csv("MV/resultMV_acc_result.csv")["Accuracy"])
    var1 = list(pd.read_csv("MV/resultMV_acc_result.csv")["char"])

    plt.errorbar(x, mean1, var1, color='red',
                 capsize=4, capthick=1, linestyle=':',
                 linewidth=1.5, marker='o',
                 mec='red', mfc='red', ms=7,
                 label=u'MV')

    """GLAD"""
    mean2 = list(pd.read_csv("GLAD/resultGLAD_acc_result.csv")["Accuracy"])
    var2 = list(pd.read_csv("GLAD/resultGLAD_acc_result.csv")["char"])

    plt.errorbar(x, mean2, var2, color='blue',
                 capsize=4, capthick=1, linestyle=':',
                 linewidth=1.5, marker='x',
                 mec='blue', mfc='blue', ms=7,
                 label=u'GLAD')

    """HDS"""
    mean2 = list(pd.read_csv("HDS/resultHDS_acc_result.csv")["Accuracy"])
    var2 = list(pd.read_csv("HDS/resultHDS_acc_result.csv")["char"])

    plt.errorbar(x, mean2, var2, color='green',
                 capsize=4, capthick=1, linestyle=':',
                 linewidth=1.5, marker='s',
                 mec='green', mfc='green', ms=7,
                 label=u'HDS')


    """K-MV"""
    mean2 = list(pd.read_csv("MV/resultMV_acc_result_del_t7.csv")["Accuracy"])
    var2 = list(pd.read_csv("MV/resultMV_acc_result_del_t7.csv")["char"])

    plt.errorbar(x, mean2, var2, color='red',
                 capsize=4, capthick=1,
                 linewidth=1.5, marker='o',
                 mec='red', mfc='red', ms=7,
                 label=u'K-MV')


    """K-GLAD"""
    mean2 = list(pd.read_csv("GLAD/resultGLAD_acc_result_del_t7.csv")["Accuracy"])
    var2 = list(pd.read_csv("GLAD/resultGLAD_acc_result_del_t7.csv")["char"])

    plt.errorbar(x, mean2, var2, color='blue',
                 capsize=4, capthick=1,
                 linewidth=1.5, marker='x',
                 mec='blue', mfc='blue', ms=7,
                 label=u'K-GLAD')


    """K-HDS"""
    mean2 = list(pd.read_csv("HDS/resultHDS_acc_result_del_t7.csv")["Accuracy"])
    var2 = list(pd.read_csv("HDS/resultHDS_acc_result_del_t7.csv")["char"])

    plt.errorbar(x, mean2, var2, color='green',
                 capsize=4, capthick=1,
                 linewidth=1.5, marker='s',
                 mec='green', mfc='green', ms=7,
                 label=u'K-HDS')




    plt.legend()  # 让图例生效
    plt.xticks(x, names)
    # plt.grid(axis='y')
    # encoding=utf-8

    plt.xlim(-0.2, 5.2)
    plt.ylim(0.65, 1)

    plt.grid(axis='y', alpha=0.3)
    plt.grid(axis='x', alpha=0.3)

    plt.tick_params(top=True, bottom=True, left=True, right=True)
    plt.tick_params(direction='in')

    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Percentage", size=14)  # X轴标签
    plt.ylabel("Accuracy", size=14)  # Y轴标签
    path = 'result_Delete_dog.jpg'
    plt.gcf().savefig(path, dpi=1800, format='jpg')
    plt.show()







if __name__ == '__main__':
    plt_CDK()
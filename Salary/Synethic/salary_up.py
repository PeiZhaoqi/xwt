import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

def salary():

    source_U = [1,1,1,1,1,1]

    """moni"""
    moni = [12, 24, 36, 48, 60]
    Mean_U1 = [1]  # 普通工人平均收益PR
    Var_U1 = [0]  # 普通工人收益方差
    for i in range(len(moni)):
        path = "access_"+str(moni[i])+".csv"
        data = pd.read_csv(path)

        U = []
        for j in range(len(data)):
            tmp_p = data.iloc[j][2] + data.iloc[j][3]
            tmp_e = data.iloc[j][2]
            U.append(tmp_p/tmp_e)
        Mean_U1.append(round(sum(U)/len(data),4))
        Var_U1.append(round(np.std(U), 4))
    print(Mean_U1)
    print(Var_U1)



    """s4-dog"""
    s4_dog = [11,21,32,43,55]
    Mean_U2 = [1]  # 普通工人平均收益PR
    Var_U2 = [0]  # 普通工人收益方差
    for i in range(len(s4_dog)):
        path = "../s4-dog/access_"+str(s4_dog[i])+".csv"
        data = pd.read_csv(path)
        U2 = []
        for j in range(len(data)):
            tmp_p = data.iloc[j][2] + data.iloc[j][3]
            tmp_e = data.iloc[j][2]
            U2.append(tmp_p/tmp_e)
        Mean_U2.append(round(sum(U2)/len(data),4))
        Var_U2.append(round(np.std(U2), 4))
    print(Mean_U2)
    print(Var_U2)


    x_ticks = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5']
    x = range(len(x_ticks))

    plt.plot(x, source_U, linewidth=2, label=u'normal worker')

    plt.errorbar(x, Mean_U1, Var_U1,
                 capsize=4, capthick=1,
                 linewidth=2, marker='x',
                 ms=7,
                 label=u'collusion worker in Synthetic Dataset')

    plt.errorbar(x, Mean_U2, Var_U2,
                 capsize=4, capthick=1,
                 linewidth=2, marker='+',
                 ms=7,
                 label=u'collusion worker in S4-dog Dataset')

    # label=r"$\frac{p_{0}}{e_{0}}$"
    # plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.0f'+str(label)+''))

    plt.legend()  # 让图例生效
    plt.xticks(x, x_ticks, fontsize=12)
    plt.yticks(fontsize=12)

    plt.tick_params(top=True, bottom=True, left=True, right=True)
    plt.tick_params(direction='in')

    plt.grid(axis='y', alpha=0.3)
    plt.grid(axis='x', alpha=0.3)

    plt.xlim(-0.2, 5.2)
    plt.ylim(0, 6)

    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Percentage", size=14)  # X轴标签
    plt.ylabel("Utility", size=14)  # Y轴标签

    plt.tick_params(direction='in')


    path = 'Utility.jpg'

    plt.gcf().savefig(path, dpi=1800, format='jpg')

    plt.show()





if __name__ == '__main__':


    salary()
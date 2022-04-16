import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pandas import DataFrame, concat


def Mean_Var():

    index = [12,24,36,48,60]

    Algorithm = "copyN"

    Mean_acc = []
    Var_acc = []

    Mean_pre = []
    Var_pre = []

    Mean_rec = []
    Var_rec = []

    Mean_f1 = []
    Var_f1 = []

    for i in range(len(index)):
        path = "ZB_data/"+Algorithm+"/experience1_result_"+str(index[i])+".csv"

        Accuracy = list(pd.read_csv(path)["Acc"])
        Precision = list(pd.read_csv(path)["Pre"])
        Recall = list(pd.read_csv(path)["Rec"])
        F1 = list(pd.read_csv(path)["f1_score"])

        Mean_acc.append(sum(Accuracy)/20)
        Var_acc.append(np.std(Accuracy))


        Mean_pre.append(sum(Precision)/20)
        Var_pre.append(np.std(Precision))


        Mean_rec.append(sum(Recall)/20)
        Var_rec.append(np.std(Recall))

        Mean_f1.append(sum(F1) / 20)
        Var_f1.append(np.std(F1))


    Mean_acc = DataFrame({"Mean_acc": Mean_acc})
    Var_acc = DataFrame({"Var_acc": Var_acc})
    Mean_pre = DataFrame({"Mean_pre": Mean_pre})
    Var_pre = DataFrame({"Var_pre": Var_pre})
    Mean_rec = DataFrame({"Mean_rec": Mean_rec})
    Var_rec = DataFrame({"Var_rec": Var_rec})
    Mean_f1 = DataFrame({"Mean_f1": Mean_f1})
    Var_f1 = DataFrame({"Var_f1": Var_f1})



    write = concat([Mean_acc, Var_acc, Mean_pre, Var_pre, Mean_rec, Var_rec, Mean_f1, Var_f1], axis=1)
    print(write)
    write.to_csv("ZB_data/"+Algorithm+"/Mean_Var.csv")





def Plt_ACC():

    "read Dataset---Our"
    path = "ZB_data/Our/Mean_Var.csv"
    Our_mean_acc = list(pd.read_csv(path)["Mean_acc"])

    "read Dataset---copyN"
    path = "ZB_data/copyN/Mean_Var.csv"
    copyN_mean_acc = list(pd.read_csv(path)["Mean_acc"])


    "read Dataset---Cos"
    path = "ZB_data/Cos/Mean_Var.csv"
    Cos_mean_acc = list(pd.read_csv(path)["Mean_acc"])


    "read Dataset---Cpp"
    path = "ZB_data/CPP/Mean_Var.csv"
    CPP_mean_acc = list(pd.read_csv(path)["Mean_acc"])



    x_ticks = ['0.1', '0.2', '0.3', '0.4', '0.5']
    x = range(len(x_ticks))


    plt.plot(x, Cos_mean_acc,
                 linewidth=1.5, marker='v',
                 ms=7,
                 label=u'FC')


    plt.plot(x, CPP_mean_acc,
                 linewidth=1.5, marker='o',
                 ms=7,
                 label=u'CP')


    plt.plot(x, copyN_mean_acc,
                 linewidth=1.5, marker='+',
                 ms=7,
                 label=u'RE')


    plt.plot(x, Our_mean_acc,
                 linewidth=1.5, marker='x',
                 ms=7,
                 label=u'KCD')




    plt.legend()  # 让图例生效
    plt.xticks(x, x_ticks, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y')

    plt.xlim(-0.2, 4.2)
    plt.ylim(0, 1)

    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Percentage", size=18)  # X轴标签
    plt.ylabel("Accuracy", size=18)  # Y轴标签

    plt.tick_params(direction='in')
    plt.tick_params(top=True, bottom=True, left=True, right=True)


    path = 'experience2_synthetic_Acc.jpg'
    plt.gcf().savefig(path, dpi=1800, format='jpg')


    plt.show()



def Plt_PRE():
    "read Dataset---Our"
    path = "ZB_data/Our/Mean_Var.csv"
    Our_mean_pre = list(pd.read_csv(path)["Mean_pre"])

    "read Dataset---copyN"
    path = "ZB_data/copyN/Mean_Var.csv"
    copyN_mean_pre = list(pd.read_csv(path)["Mean_pre"])

    "read Dataset---Cos"
    path = "ZB_data/Cos/Mean_Var.csv"
    Cos_mean_pre = list(pd.read_csv(path)["Mean_pre"])

    "read Dataset---Cpp"
    path = "ZB_data/CPP/Mean_Var.csv"
    CPP_mean_pre = list(pd.read_csv(path)["Mean_pre"])


    x_ticks = ['0.1', '0.2', '0.3', '0.4', '0.5']
    x = range(len(x_ticks))

    plt.plot(x, Cos_mean_pre,
             linewidth=1.5, marker='v',
             ms=7,
             label=u'FC')

    plt.plot(x, CPP_mean_pre,
             linewidth=1.5, marker='o',
             ms=7,
             label=u'CP')

    plt.plot(x, copyN_mean_pre,
             linewidth=1.5, marker='+',
             ms=7,
             label=u'RE')

    plt.plot(x, Our_mean_pre,
             linewidth=1.5, marker='x',
             ms=7,
             label=u'KCD')



    plt.legend()  # 让图例生效
    plt.xticks(x, x_ticks, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y')

    plt.xlim(-0.2, 4.2)
    plt.ylim(0, 1)


    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Percentage", size=18)  # X轴标签
    plt.ylabel("Precision", size=18)  # Y轴标签

    plt.tick_params(direction='in')
    plt.tick_params(top=True, bottom=True, left=True, right=True)

    path = 'experience2_synthetic_Pre.jpg'
    plt.gcf().savefig(path, dpi=1800, format='jpg')

    plt.show()




def Plt_REC():
    "read Dataset---Our"
    path = "ZB_data/Our/Mean_Var.csv"
    Our_mean_rec = list(pd.read_csv(path)["Mean_rec"])
    Our_var_rec = list(pd.read_csv(path)["Var_rec"])

    "read Dataset---copyN"
    path = "ZB_data/copyN/Mean_Var.csv"
    copyN_mean_rec = list(pd.read_csv(path)["Mean_rec"])
    copyN_var_rec = list(pd.read_csv(path)["Var_rec"])

    "read Dataset---Cos"
    path = "ZB_data/Cos/Mean_Var.csv"
    Cos_mean_rec = list(pd.read_csv(path)["Mean_rec"])
    Cos_var_rec = list(pd.read_csv(path)["Var_rec"])

    "read Dataset---Cpp"
    path = "ZB_data/CPP/Mean_Var.csv"
    CPP_mean_rec = list(pd.read_csv(path)["Mean_rec"])
    CPP_var_rec = list(pd.read_csv(path)["Var_rec"])


    x_ticks = ['0.1', '0.2', '0.3', '0.4', '0.5']
    x = range(len(x_ticks))

    plt.plot(x, Cos_mean_rec,
             linewidth=1.5, marker='v',
             ms=7,
             label=u'FC')

    plt.plot(x, CPP_mean_rec,
             linewidth=1.5, marker='o',
             ms=7,
             label=u'CP')

    plt.plot(x, copyN_mean_rec,
             linewidth=1.5, marker='+',
             ms=7,
             label=u'RE')

    plt.plot(x, Our_mean_rec,
             linewidth=1.5, marker='x',
             ms=7,
             label=u'KCD')


    plt.legend()  # 让图例生效
    plt.xticks(x, x_ticks, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y')

    plt.xlim(-0.2, 4.2)
    plt.ylim(0, 1)


    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Percentage", size=18)  # X轴标签
    plt.ylabel("Recall", size=18)  # Y轴标签

    plt.tick_params(direction='in')
    plt.tick_params(top=True, bottom=True, left=True, right=True)

    path = 'experience2_synthetic_Rec.jpg'
    plt.gcf().savefig(path, dpi=1800, format='jpg')

    plt.show()



def Plt_F1():
    "read Dataset---Our"
    path = "ZB_data/Our/Mean_Var.csv"
    Our_mean_f1 = list(pd.read_csv(path)["Mean_f1"])
    Our_var_f1 = list(pd.read_csv(path)["Var_f1"])

    "read Dataset---copyN"
    path = "ZB_data/copyN/Mean_Var.csv"
    copyN_mean_f1 = list(pd.read_csv(path)["Mean_f1"])
    copyN_var_f1 = list(pd.read_csv(path)["Var_f1"])

    "read Dataset---Cos"
    path = "ZB_data/Cos/Mean_Var.csv"
    Cos_mean_f1 = list(pd.read_csv(path)["Mean_f1"])
    Cos_var_f1 = list(pd.read_csv(path)["Var_f1"])


    "read Dataset---Cpp"
    path = "ZB_data/CPP/Mean_Var.csv"
    CPP_mean_f1 = list(pd.read_csv(path)["Mean_f1"])
    CPP_var_f1 = list(pd.read_csv(path)["Var_f1"])


    x_ticks = ['0.1', '0.2', '0.3', '0.4', '0.5']
    x = range(len(x_ticks))

    plt.plot(x, Cos_mean_f1,
             linewidth=1.5, marker='v',
             ms=7,
             label=u'FC')

    plt.plot(x, CPP_mean_f1,
             linewidth=1.5, marker='o',
             ms=7,
             label=u'CP')

    plt.plot(x, copyN_mean_f1,
             linewidth=1.5, marker='+',
             ms=7,
             label=u'RE')

    plt.plot(x, Our_mean_f1,
             linewidth=1.5, marker='x',
             ms=7,
             label=u'KCD')

    plt.legend()  # 让图例生效
    plt.xticks(x, x_ticks, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y')

    plt.xlim(-0.2, 4.2)
    plt.ylim(0, 1)


    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Collusion Percentage", size=18)  # X轴标签
    plt.ylabel("F1 score", size=18)  # Y轴标签

    plt.tick_params(direction='in')
    plt.tick_params(top=True, bottom=True, left=True, right=True)

    path = 'experience2_synthetic_F1.jpg'
    plt.gcf().savefig(path, dpi=1800, format='jpg')

    plt.show()







if __name__ == '__main__':

    """求平均值与标准型差"""
    # Mean_Var()



    """画图"""
    Plt_ACC()

    Plt_PRE()

    Plt_REC()

    Plt_F1()

import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame, concat

def Mean(exp):
    Mean_Acc = []
    Mean_Pre = []
    Mean_Rec = []
    Mean_F1 = []

    threshold = [5, 6, 7, 8, 9, 10, 11]

    for i in range(len(threshold)):

        path = "../CSTA/threshold_"+str(threshold[i])+"/experience1_result_"+str(exp)+".csv"

        Accuracy = list(pd.read_csv(path)["Acc"])

        Precision = list(pd.read_csv(path)["Pre"])
        Recall = list(pd.read_csv(path)["Rec"])
        F1 = list(pd.read_csv(path)["f1_score"])

        Mean_Acc.append(sum(Accuracy)/30)

        Mean_Pre.append(sum(Precision)/30)

        Mean_Rec.append(sum(Recall)/30)

        Mean_F1.append(sum(F1) / 30)


    Mean_Acc = DataFrame({"Mean_acc": Mean_Acc})
    Mean_Pre = DataFrame({"Mean_pre": Mean_Pre})
    Mean_Rec = DataFrame({"Mean_rec": Mean_Rec})
    Mean_F1 = DataFrame({"Mean_f1": Mean_F1})

    write = concat([Mean_Acc,Mean_Pre,Mean_Rec,Mean_F1],axis=1)
    print(write)
    write.to_csv("threshold_c_"+str(exp)+".csv", sep=',', index=0)




def Plt(exp):

    path = "threshold_c_"+str(exp)+".csv"

    Mean_acc = list(pd.read_csv(path)["Mean_acc"])
    Mean_pre = list(pd.read_csv(path)["Mean_pre"])
    Mean_rec = list(pd.read_csv(path)["Mean_rec"])
    Mean_f1 = list(pd.read_csv(path)["Mean_f1"])



    x_ticks = ['5', '6', '7', '8', '9', '10', '11']
    x = range(len(x_ticks))


    plt.plot(x_ticks, Mean_acc, '-', label=u'Accuracy')
    plt.plot(x_ticks, Mean_pre, ':', label=u'Precision')
    plt.plot(x_ticks, Mean_rec,  '-.', label=u'Recall')
    plt.plot(x_ticks, Mean_f1, '--', label=u'f1-score')


    plt.legend()  # 让图例生
    plt.xticks(x, x_ticks)
    # plt.grid(axis='y')

    plt.xlim(0, 8)
    plt.ylim(0.4, 1)

    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Threshold Collusion="+str(exp)+"", size=12)  # X轴标签
    plt.ylabel("Threshold V ersus Accuracy, Precision, Recall and f1-score", size=10)  # Y轴标签

    plt.tick_params(direction='in')
    plt.tick_params(top=True, bottom=True, left=True, right=True)


    path = "threshold_s4-dog_c_"+str(exp)+".jpg"
    plt.gcf().savefig(path, dpi=1200, format='jpg')


    plt.show()






if __name__ == '__main__':

    """取占比为30%的时候，求平均值"""
    # Mean(92)

    """画图"""
    Plt(34)
    Plt(69)
    Plt(92)

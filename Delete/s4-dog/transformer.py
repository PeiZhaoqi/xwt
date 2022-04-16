import numpy as np
import pandas as pd
from pandas import DataFrame, concat

"""
将原数据集求平均值 标准差 转化为画图的表
"""
def s4_dog():
    Proportion = [0, 10, 20, 30, 40, 50]

    Accuracy = [0.8178]

    cha = [0]

    path = "MV_acc_result_del_t7.csv"
    data = pd.read_csv(path, header=None)
    for i in range(len(data)):
        tmp_data = []
        for j in range(len(data.iloc[i])):
            tmp_data.append(data.iloc[i][j])

        print(tmp_data)

        tmp_avg = round(sum(tmp_data) / 30, 4)
        tmp_cha = round(np.std(tmp_data, ddof=1), 4)

        print(tmp_avg)
        print(tmp_cha)
        Accuracy.append(tmp_avg)
        cha.append(tmp_cha)

    Proportion = DataFrame({"Proprotion": Proportion})
    Accuracy = DataFrame({"Accuracy": Accuracy})
    cha = DataFrame({"char": cha})

    write = concat([Proportion, Accuracy, cha], axis=1)
    write.to_csv("ACC_source_del_t7.csv", sep=',', index=0)


if __name__ == '__main__':

    s4_dog()

import pandas as pd
from pandas import DataFrame, concat

x = [11, 21, 32, 43, 55]

for i in range(len(x)):
    path = "result_"+str(x[i])+".csv"
    data = pd.read_csv(path)
    Acc = data.iloc[:, 0:1]
    Pre = data.iloc[:, 1:2]
    Rec = data.iloc[:, 2:3]

    F1_score = []
    for j in range(len(Pre)):
        if Pre.iloc[i][0] + Rec.iloc[j][0] != 0:
            f1_score = 2 * ((Pre.iloc[i][0] * Rec.iloc[j][0]) / (Pre.iloc[i][0] + Rec.iloc[j][0]))
        else:
            f1_score = 0
        F1_score.append(f1_score)

    F1_score = DataFrame({"f1_score": F1_score})

    write = concat([Acc, Pre, Rec, F1_score], axis=1)
    print(write)
    write.to_csv("experience1_result_"+str(x[i])+".csv", sep=',', index=0)
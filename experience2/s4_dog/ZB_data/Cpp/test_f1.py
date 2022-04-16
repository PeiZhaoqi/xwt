import pandas as pd
from pandas import DataFrame, concat

li = [11, 21, 32, 43, 55]

for i in range(len(li)):

    f1_score = []
    path = "experience1_result_"+str(li[i])+".csv"
    Accuracy = list(pd.read_csv(path)["Acc"])
    Precision = list(pd.read_csv(path)["Pre"])
    Recall = list(pd.read_csv(path)["Rec"])

    for j in range(len(Precision)):
        if Precision[j] + Recall[j] != 0:
            f1 = 2 * ((Precision[j] * Recall[j]) / (Precision[j] + Recall[j]))
        else:
            f1 = 0
        f1_score.append(f1)

    Accuracy = DataFrame({"Acc": Accuracy})
    Precision = DataFrame({"Pre": Precision})
    Recall = DataFrame({"Rec": Recall})
    f1_score = DataFrame({"f1_score": f1_score})

    write = concat([Accuracy, Precision, Recall, f1_score], axis=1)
    print(write)

    write.to_csv("experience1_result_"+str(li[i])+".csv", sep=',', index=0)
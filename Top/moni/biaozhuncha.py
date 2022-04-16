import numpy as np
import pandas as pd
from pandas import DataFrame, concat


def our():

    top = [5, 10, 15, 20, 25, 30]

    avg_pre = []
    avg_pre_cha = []

    avg_rec =[]
    avg_rec_cha = []

    avg_f1_score = []
    avg_f1_score_cha = []

    for i in range(len(top)):

        path = "our/top_"+str(top[i])+".csv"

        data_pre = np.array(pd.read_csv(path, usecols=np.arange(0, 1)))
        avg_pre.append(round(data_pre.sum() / 20, 4))
        avg_pre_cha.append(round(np.std(data_pre, ddof=1),4))


        data_rec = np.array(pd.read_csv(path, usecols=np.arange(1, 2)))
        avg_rec.append(round(data_rec.sum() / 20, 4))
        avg_rec_cha.append(round(np.std(data_rec, ddof=1),4))


        data_f1 = np.array(pd.read_csv(path, usecols=np.arange(2, 3)))
        avg_f1_score.append(round(data_f1.sum() / 20, 4))
        avg_f1_score_cha.append(round(np.std(data_f1, ddof=1),4))


    avg_pre = DataFrame({"pre": avg_pre})
    avg_pre_cha = DataFrame({"pre_cha": avg_pre_cha})

    avg_rec =DataFrame({"rec": avg_rec})
    avg_rec_cha = DataFrame({"rec_cha": avg_rec_cha})

    avg_f1_score = DataFrame({"f1": avg_f1_score})
    avg_f1_score_cha = DataFrame({"f1_cha": avg_f1_score_cha})

    write = concat([avg_pre,avg_pre_cha,avg_rec,avg_rec_cha,avg_f1_score,avg_f1_score_cha], axis=1)
    print(write)
    write.to_csv("our_top.csv", sep=',', index=0)



def cos():

    top = [5, 10, 15, 20, 25, 30]

    avg_pre = []
    avg_pre_cha = []

    avg_rec =[]
    avg_rec_cha = []

    avg_f1_score = []
    avg_f1_score_cha = []

    for i in range(len(top)):
        path = "cos/top_"+str(top[i])+".csv"

        data_pre = np.array(pd.read_csv(path, usecols=np.arange(0, 1)))
        avg_pre.append(round(data_pre.sum() / 20, 4))
        avg_pre_cha.append(round(np.std(data_pre, ddof=1),4))


        data_rec = np.array(pd.read_csv(path, usecols=np.arange(1, 2)))
        avg_rec.append(round(data_rec.sum() / 20, 4))
        avg_rec_cha.append(round(np.std(data_rec, ddof=1),4))


        data_f1 = np.array(pd.read_csv(path, usecols=np.arange(2, 3)))
        avg_f1_score.append(round(data_f1.sum() / 20, 4))
        avg_f1_score_cha.append(round(np.std(data_f1, ddof=1),4))


    avg_pre = DataFrame({"pre": avg_pre})
    avg_pre_cha = DataFrame({"pre_cha": avg_pre_cha})

    avg_rec =DataFrame({"rec": avg_rec})
    avg_rec_cha = DataFrame({"rec_cha": avg_rec_cha})

    avg_f1_score = DataFrame({"f1": avg_f1_score})
    avg_f1_score_cha = DataFrame({"f1_cha": avg_f1_score_cha})

    write = concat([avg_pre,avg_pre_cha,avg_rec,avg_rec_cha,avg_f1_score,avg_f1_score_cha], axis=1)
    print(write)
    write.to_csv("cos_top.csv", sep=',', index=0)




def cpp():

    top = [5, 10, 15, 20, 25, 30]

    avg_pre = []
    avg_pre_cha = []

    avg_rec =[]
    avg_rec_cha = []

    avg_f1_score = []
    avg_f1_score_cha = []

    for i in range(len(top)):
        path = "cpp/top_"+str(top[i])+".csv"

        data_pre = np.array(pd.read_csv(path, usecols=np.arange(0, 1)))
        avg_pre.append(round(data_pre.sum() / 20, 4))
        avg_pre_cha.append(round(np.std(data_pre, ddof=1),4))


        data_rec = np.array(pd.read_csv(path, usecols=np.arange(1, 2)))
        avg_rec.append(round(data_rec.sum() / 20, 4))
        avg_rec_cha.append(round(np.std(data_rec, ddof=1),4))


        data_f1 = np.array(pd.read_csv(path, usecols=np.arange(2, 3)))
        avg_f1_score.append(round(data_f1.sum() / 20, 4))
        avg_f1_score_cha.append(round(np.std(data_f1, ddof=1),4))


    avg_pre = DataFrame({"pre": avg_pre})
    avg_pre_cha = DataFrame({"pre_cha": avg_pre_cha})

    avg_rec =DataFrame({"rec": avg_rec})
    avg_rec_cha = DataFrame({"rec_cha": avg_rec_cha})

    avg_f1_score = DataFrame({"f1": avg_f1_score})
    avg_f1_score_cha = DataFrame({"f1_cha": avg_f1_score_cha})

    write = concat([avg_pre,avg_pre_cha,avg_rec,avg_rec_cha,avg_f1_score,avg_f1_score_cha], axis=1)
    print(write)
    write.to_csv("cpp_top.csv", sep=',', index=0)



def copyN():

    top = [5, 10, 15, 20, 25, 30]

    avg_pre = []
    avg_pre_cha = []

    avg_rec =[]
    avg_rec_cha = []

    avg_f1_score = []
    avg_f1_score_cha = []

    for i in range(len(top)):

        path = "copyN/top_"+str(top[i])+".csv"
        print(path)
        data_pre = np.array(pd.read_csv(path, usecols=np.arange(0, 1)))
        avg_pre.append(round(data_pre.sum() / 20, 4))
        avg_pre_cha.append(round(np.std(data_pre, ddof=1),4))


        data_rec = np.array(pd.read_csv(path, usecols=np.arange(1, 2)))
        avg_rec.append(round(data_rec.sum() / 20, 4))
        avg_rec_cha.append(round(np.std(data_rec, ddof=1),4))


        data_f1 = np.array(pd.read_csv(path, usecols=np.arange(2, 3)))
        avg_f1_score.append(round(data_f1.sum() / 20, 4))
        avg_f1_score_cha.append(round(np.std(data_f1, ddof=1),4))


    avg_pre = DataFrame({"pre": avg_pre})
    avg_pre_cha = DataFrame({"pre_cha": avg_pre_cha})

    avg_rec =DataFrame({"rec": avg_rec})
    avg_rec_cha = DataFrame({"rec_cha": avg_rec_cha})

    avg_f1_score = DataFrame({"f1": avg_f1_score})
    avg_f1_score_cha = DataFrame({"f1_cha": avg_f1_score_cha})

    write = concat([avg_pre,avg_pre_cha,avg_rec,avg_rec_cha,avg_f1_score,avg_f1_score_cha], axis=1)
    print(write)
    write.to_csv("copyN_top.csv", sep=',', index=0)







if __name__ == '__main__':

    # print("cos")
    # cos()
    #
    # print("cpp")
    # cpp()

    print("copyN")
    copyN()

    # print("our")
    # our()
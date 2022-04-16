import matplotlib
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def get_C(m,n):
    a=b=result=1
    if m<n:
        print("n不能小于m 且均为整数")
    elif ((type(m)!=int)or(type(n)!=int)):
        print("n不能小于m 且均为整数")
    else:
        minNI=min(n,m-n)#使运算最简便
        for j in range(0,minNI):
        #使用变量a,b 让所用的分母相乘后除以所有的分子
            a=a*(m-j)
            b=b*(minNI-j)
            result=a//b #在此使用“/”和“//”均可，因为a除以b为整数
        return result


def weight(ability, num_labels):

    n = np.arange(1, 51)

    ability = ability
    f = ability ** 2 + (num_labels - 1) * (((1 - ability) / (num_labels - 1)) ** 2)
    m = 50
    n = np.arange(1, 51)
    w = []
    for _n in range(len(n)):

        C = get_C(m, n[_n])
        wi = C * (f ** n[_n]) * ((1 - f) ** (m - n[_n]))
        w.append(wi)

    return w





x = np.arange(1, 51)

y1 = weight(0.6, 2)
y2 = weight(0.7, 2)
y3 = weight(0.8, 2)
y4 = weight(0.9, 2)

plt.xlabel('Number of same answers', fontsize=14)
plt.ylabel('Probability', fontsize=14)

plt.plot(x, y1, '-.', linewidth=1.5, markersize=3)  # 绘制折线图，添加数据点，设置点的大小
plt.plot(x, y2, '--', linewidth=1.5, markersize=3)
plt.plot(x, y3, '-', linewidth=1.5, markersize=3)
plt.plot(x, y4, ':', linewidth=1.5, markersize=3)

# for a, b in zip(x, y1):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
# for a, b in zip(x, y2):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
# for a, b in zip(x, y3):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
# for a, b in zip(x, y4):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)


plt.tick_params(top=True, bottom=True, left=True, right=True)
plt.tick_params(direction='in')
plt.legend(['ability=0.6', 'ability=0.7', 'ability=0.8', 'ability=0.9'])  # 设置折线名称
plt.grid(axis='y', alpha=0.3)
plt.grid(axis='x', alpha=0.3)

path = 'Collusion_Proof.jpg'
plt.gcf().savefig(path, dpi=1800, format='jpg')


plt.show()





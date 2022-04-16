

def func(m,n):
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


c = func(50,1)
print(c)

ability = 0.7

print(0.58**30 * 0.42**20 * c)
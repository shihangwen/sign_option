import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_data_set = {-1:np.array([[1,7],
                             [2,8],
                             [3,8]]),
                 1:np.array([[5,1],
                             [6,-1],
                             [7,3]])}
data_color={-1:'r',1:'b'}

predict_data=np.array([[0,10], [1,3], [4,3], [5.5,7.5], [8,3]])



def train(data):
    rate=1  #学习速率
    w=np.array([10,1]) #斜率
    b=1 #截距
    optimize1=True
    while optimize1:
        a=0
        exit_flag1=True
        for i in data:   
            for j in data[i]:
                if  i*(np.dot(j,w)+b) <=0:
                    w=w+rate*j*i
                    b=b+rate*i
                    print(w)
                    print(b)
                    exit_flag1=False
                    break   #跳出内层for循环
                else:
                    a=a+1
            if not exit_flag1:
                break       #跳出外层for循环,进入内层的while循环
        
        if a==6:   #样本的容量,代表所需循环的次数
            break

    print('this is the k:',w)
    print('this is the interception:',b)
            
            
    
    return w,b


w_t,b_t=train(train_data_set)
print(w_t[0])
print(w_t[1])

w=-w_t[0]/w_t[1]
print(w_t)

x=np.arange(-5,10,0.01)
y=w*x

for i in train_data_set:
    for j in train_data_set[i]:
        plt.scatter(j[0],j[1],c=data_color[i])

plt.plot(x,y)

for i in predict_data:
    if np.dot(i,w_t)>0:
        plt.scatter(i[0],i[1],marker='*',s=300,c='b')
    else:
        plt.scatter(i[0],i[1],marker='*',s=300,c='r')
plt.show()

                
            
                        
            
                
        
    
    
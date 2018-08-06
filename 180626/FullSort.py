
result=[]
#定义这个全局变量

def FullSort(arr):

    if arr==None or len(arr)==0:
        return None
    else:
        persu(arr,0,len(arr))
        return result



def persu(arr,start,end):
    if start==end:
        result.append(arr)
    else:
        for i in range(start,end):
            arr[start],arr[i]=arr[i],arr[start]
            persu(arr,start+1,end)
            arr[start], arr[i] = arr[i], arr[start] #这个是交换上次的两个数据，把arr回归原位，因为arr一直是在自己操作的！！重要






if __name__ == '__main__':
    arr=['a','b','c']
    print(len(arr))
    print(FullSort(arr))
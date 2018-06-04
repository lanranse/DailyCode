
#将数组中所有的奇数挪到偶数前面
#或者所有可以被3整除饿挪到不能被3整除的前面
def func(arr):

    if arr==None:
        return
    start=0
    end=len(arr)-1

    while end>start:
        while arr[start]%2==1 and end>start:
            start+=1

        while arr[end]%2==0 and end>start:
            end-=1
        if end>start:
            arr[start],arr[end]=arr[end],arr[start]

def quicksort(arr,start,end):
    if start<end:
        base=arr[start]
        i=start
        j=end

        while j>i :
            while j>i and arr[j]>=base:
                j-=1
            arr[i]=arr[j]

            while j>i and arr[i]<=base:
                i+=1
            arr[j]=arr[i]
        arr[i]=base

        quicksort(arr,start,i-1)
        quicksort(arr,i+1,end)
    return arr

if __name__ == '__main__':
    list=[1,6,5,7,3,4,9]
    new_list=quicksort(list,0,len(list)-1)
    print(new_list)
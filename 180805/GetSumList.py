
#数字target的所有数字之和=target的组合
def GetsSum(target):
    start=1
    end=2
    count=start+end
    result=[]
    while start<end and end<target and start<(target+1)//2:     #这个start只需要运行的到数组的一半即可
        if count==target:
            result.append([start,end])
            end+=1
            count=count+end #如果和相等，则后移end
        elif count>target:
            count=count-start   #如果count>target，前移动start，并且减少start数值
            start+=1
        else:
            end=end+1
            count=count+end     #如果count<target，后移动end，并且增加end数值

    return result


if __name__ == '__main__':
    print(GetsSum(15))

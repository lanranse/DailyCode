
def yi_huo():
    list=[1,2,3,2,1]
    result=0
    for  i in list:
        result^=i
        print(result)

def removeDuplicates(nums):
    # write your code here
    i = 0
    l = len(nums)
    while i < l:
        j = i + 1
        while j < l and nums[i] == nums[j]:
            del (nums[j])
            l -= 1

        i += 1
    return len(nums)

if __name__ == '__main__':
    l=removeDuplicates([1,2,3,4,4,4,4,2])
    print(l)

def reversestring(s):
    #return s[::-1]
    start=0
    end=len(s)-1
    while start<end:
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1

if __name__ == '__main__':
    s='welcome to china'
    s=list(s)
    reversestring(s)
    print(s)
    left=0
    right=0
    end=len(s)-1
    while right<end:
        while s[right]!=' ':
            right+=1
        right-=1
        reversestring(s[left:right+1])
        while right==' ':
            right+=1
        left=right

    print(s)

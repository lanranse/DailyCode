#输出链表中倒数第k个节点的值

def func(head,k):
    start=head
    for i in range(k-1):
        if head.next==None:
            return
        else:
            start=start.next
    end=head
    while start.next!=None:
        start=start.next
        end=end.next
    return end.value

#注意代码的健壮性，关注参数的检查
#以下为最终答案
def finaly(head,k):
    if head==None:
        return
    if k==0:
        return
    if isinstance(k,int):
        return 'wrong number'
    func(head,k)
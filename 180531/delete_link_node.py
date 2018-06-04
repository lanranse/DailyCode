class Node(object):
    def __init__(self):
        self.val=None
        self.next=None
#通过复制节点的方法，实现O1的复杂度，单项链表删除某个节点

def delete(head,target):
    if head==None or target==None:
        return
    if head.next==None:
        while head.next!=target:
            head=head.next
        head.next=None
        return
    if head==target:
        head.next=None
        return
    target.value=target.next.value
    target.next=target.next.next
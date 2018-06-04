#合并两个已经排好序的链表

def func1(head1,head2):
    now=Node('head',None)
    new_head=now

    while head1!=None or head2!=None:
        if head1.val>head2.val:
            now.next=head2
            head2=head2.next
        else:
            now.next=head1
            head1=head1.next
        now=now.next
    if head1!=None:
        now.next=head1
    if head2!=None:
        now.next=head2
    return new_head.next

#递归方法，没看懂
def func2(head1,head2):
    if head1==None:
        return head2
    if head2==None:
        return head1

    new_head=None
    if head1.val>head2.val:
        new_head=head2
        new_head.next = func2(head1,head2.next)
    else:
        new_head=head1
        new_head.next = func2(head1.next,head2)

    return new_head
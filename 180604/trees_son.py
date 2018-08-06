class TreeNode(object):
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None

root1=TreeNode('1')
root2=TreeNode('2')

def HasSubTree(root1,root2):
    result=False

    if root1!=None and root2!=None:
        if root1.val==root2.val:
            result=hassubtree(root1,root2)
        if (result==0):
            HasSubTree(root1.left,root2)
        if (result==0):
            HasSubTree(root1.right,root2)
    return result

def hassubtree(root1,root2):
    if root1==None:
        return False
    if root2==None:
        return True
    if root1.val!=root2.val:
        return False
    return hassubtree(root1.left,root2.left) and hassubtree(root1.right,root2.right)
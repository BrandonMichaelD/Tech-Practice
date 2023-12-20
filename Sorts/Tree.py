##Tree sort!
##First, take the array and put it into a tree!
##Then, in order traversal to get get the sorted list!
##Run time is always nlogn, space is always n

class Node:
    def __init__(self,number) -> None:
        self.value = number
        self.left = None
        self.right = None
    
##A function to insert!
def insert(node, number):
    if node == None:
        node = Node(number)
        return node
    

    if number < node.value:
        node.left = insert(node.left, number)  
    else:
        node.right = insert(node.right, number)

    return node




#a function to make the tree USING insert!
def tree(arr):
    root = Node(arr[0])
    for num in arr:
        insert(root,num)
    return root

def inOrderTraversal(rootNode: Node,newArr):
    if rootNode!=None:
        inOrderTraversal(rootNode.left,newArr)
        newArr.append(rootNode.value)
        inOrderTraversal(rootNode.right,newArr)
    
#a function to pull the whole thing together!

def treeSort(arr):
    root = tree(arr) #make the tree
    arr.clear() #clear the array
    inOrderTraversal(root,arr)



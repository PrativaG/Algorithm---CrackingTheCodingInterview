class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        treeNode = TreeNode(val)

        if self.root == None:
            self.root = treeNode
            return self
        
        runner = self.root
        while True:
            if runner.value > val:
                if runner.left == None:
                    runner.left = treeNode
                    return self
                runner = runner.left

            elif runner.value < val:
                if runner.right == None:
                    runner.right = treeNode
                    return self
                runner = runner.right
            
        
    def lookup(self, val):
        if self.root == None:
            return False

        runner = self.root

        while runner:
            if runner.value < val:
                runner = runner.right

            elif runner.value > val :
                runner = runner.left
            
            if runner.value == val:
                return runner
        return False
    
    def remove(self, val):
        if self.root == None:
            return False
        
        runner = self.root
        parentNode = None
        while runner:
            if runner.value > val:
                parentNode = runner
                runner = runner.left
            elif runner.value < val:
                parentNode = runner
                runner = runner.right
            elif runner.value == val:
                # match found!

                # option1: No right child:
                if runner.right == None:
                    if parentNode == None:
                        self.root = runner.left
                    else:
                        # if parent > current value, make current left child a child of parent
                        if runner.value < parentNode.value:
                            parentNode.left = runner.left
                        
                        # if parent < current valu, make left child a right child of a parent
                        elif runner.value > parentNode.value:
                            parentNode.right = runner.left

                # option2: Right child with no left child
                elif runner.right.left == None:
                    if parentNode == None:
                        self.root = runner.left
                    else:
                        runner.right.left = runner.left

                        # if parent > runner, make right child of the left the parent
                        if runner.value < parentNode.value:
                            parentNode.left = runner.right
                        
                        # if parent < runner, make right child a right child of the parent
                        elif runner.value > parentNode.value:
                            parentNode.right = runner.right
                
                # Option3: right child that has a left child
                else:
                    leftmost = runner.right.left
                    leftmostParent = runner.right

                    # find the right's child leftmost children
                    while leftmost != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    
                    # Parent's leftmost subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = runner.left
                    leftmost.right = runner.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if runner.value < parentNode.value:
                            parentNode.left = leftmost
                        elif runner.value > parentNode.value:
                            parentNode.right = leftmost
                return True
                    


    
tree1 = BinarySearchTree()
tree1.insert(9)
tree1.insert(4)
tree1.insert(6)
tree1.insert(20)
tree1.insert(170)
tree1.insert(15)
tree1.insert(1)

print(tree1.lookup(1))
tree1.remove(4)
         
            


                

            

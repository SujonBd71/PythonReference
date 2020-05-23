#https://leetcode.com/problems/delete-node-in-a-bst/discuss/171586/Clean-Python-Solution

class BST():
    class TreeNode():
        def __init__(self, v):
            self.l = None
            self.r = None
            self.v = v

    def __init__(self):
        self.root = None
    def __push_node__(self, node, v):
        if node == None:
            return BST.TreeNode(v)
        if v <= node.v :
            node.l = self.__push_node__(node.l, v)
        else:
            node.r = self.__push_node__(node.r, v)
        return node


        return node
    def push(self, v):
        self.root = self.__push_node__(self.root, v)
    
    def __find_internal__(self, node, v):
        if node == None:
            return None
        if node.v == v:
            return node
        if v < node.v:
            return self.__find_internal__(node.l, v)
        return self.__find_internal__(node.r, v)

    def find(self, v):
        return self.__find_internal__(self.root, v)
    
    def find_max(self, node):
        if node == None:
            return None
        if node.right == None:
            return node
        return self.find_max(node.right)

    def deleteNode(self, node, k):
        if node == None:
            return None
        if k < node.val:
            node.left = self.deleteNode(node.left, k)
        elif k > node.val:
            node.right = self.deleteNode(node.right, k)
        else: 
            if node.left == None and node.right == None:
                node = None
            elif node.left and (not node.right):
                node =  node.left
            elif node.right and (not node.left):
                node =  node.right
            else:
                max_node = self.find_max(node.left)
                node.val = max_node.val
                node.left =  self.deleteNode(node.left, node.val)
        return node


    def inoder(self, node):
        if node == None:
            return
        self.inoder(node.l)
        print(node.v)
        self.inoder(node.r)
    def print(self):
        self.inoder(self.root)

def test():
    T = BST()
    import random
    for i in range(10):
        T.push(random.randrange(0,10))
    
    T.print()
    print("###")

    for i in range(10):
        n = random.randrange(0,10)
        loc = T.find(n)
        print(n)
        print(loc)



test()

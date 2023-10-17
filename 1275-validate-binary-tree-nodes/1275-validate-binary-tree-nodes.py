class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        Children = set(leftChild + rightChild)
        Root = 0
        for Node in range(n):
            if Node not in Children:
                Root = Node
        
        Visited = set()
        Stack = [Root]
        while Stack:
            Root = Stack.pop()
            if Root in Visited:
                return False
                
            Visited.add(Root)
            if rightChild[Root] != -1:
                Stack.append(rightChild[Root])
            if leftChild[Root] != -1:
                Stack.append(leftChild[Root])
        
        return len(Visited) == n
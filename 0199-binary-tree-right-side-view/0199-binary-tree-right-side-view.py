class Solution(object):
	def rightSideView(self, root):
		q = [root]
		res = []
		while q:
			numNodes = len(q)
			for i in range(numNodes):
				removeNode = q.pop(0)
				if removeNode:
					if removeNode.left:
						q.append(removeNode.left)
					if removeNode.right:
						q.append(removeNode.right)
					if i == numNodes - 1:
						res.append(removeNode.val)
		return res
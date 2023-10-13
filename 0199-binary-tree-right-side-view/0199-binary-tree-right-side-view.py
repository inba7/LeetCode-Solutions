class Solution(object):
	def rightSideView(self, root):
		if not root: return []
		RView = []
		def BFS(root):
			Queue = collections.deque([root])
			while (Queue):
				Size = len(Queue)
				for i in range(Size):
					Curr = Queue.popleft()
					if Curr.left:
						Queue.append(Curr.left)
					if Curr.right:
						Queue.append(Curr.right)
					if i == Size - 1:
						RView.append(Curr.val)
		BFS(root)
		return RView
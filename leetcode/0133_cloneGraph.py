# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        深度遍历优先，使用递归
        @param node:
        @return:
        """
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node()
        clone_node.val = node.val

        self.visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

    def cloneGraph2(self, node: 'Node') -> 'Node':
        """
        广度遍历优先，使用双端队列
        @param node:
        @return:
        """
        if not node:
            return node

        q = deque()
        q.append(node)
        self.visited[node] = Node(node.val, [])

        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in self.visited:
                    self.visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                self.visited[n].neighbors.append(self.visited[neighbor])

        return self.visited[node]

    def print_node(self, node: 'Node'):
        """
        print node
        @param node:
        @return:
        """
        res = []
        q = deque()
        q.append(node)

        already = [node]

        while q:
            cur = q.popleft()
            tmp = []
            for neighbor in cur.neighbors:
                if neighbor not in already:
                    already.append(neighbor)
                    q.append(neighbor)
                tmp.append(neighbor.val)
            res.append(tmp)

        print(res)


node1 = Node()
node1.val = 1
node2 = Node()
node2.val = 2
node3 = Node()
node3.val = 3
node4 = Node()
node4.val = 4

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

s = Solution()
middle = s.cloneGraph(node1)
# middle = s.cloneGraph2(node1)
s.print_node(middle)


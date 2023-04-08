from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # BFS APPROACH
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            # curr contains old address of elemnt present in q
            curr = q.popleft()
            # this contains new address after clone
            curr_clone = clones[curr.val]

            for ngbr in curr.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)

                # current clone's neighbours are added to its list
                curr_clone.neighbors.append(clones[ngbr.val])

        return clones[node.val]

    # DFS APPROACH
    def cloneGraphDFS(self,node):
        old_to_new = {}

        def clone(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node) if node else None


# Build the desired graph
def buildGraph() -> Node:
    """
    Given Graph:
    1--2
    | |
    4--3
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node3, node1]
    return node1


# A simple bfs traversal of a graph to
# check for proper cloning of the graph
def bfs(src: Node):
    visit = {}
    q = deque()
    q.append(src)
    visit[src] = True
    while q:
        u = q.popleft()
        print(f"Value of Node {u.val}")
        print(f"Address of Node {u}")
        v = u.neighbors
        for neighbor in v:
            if neighbor not in visit:
                visit[neighbor] = True
                q.append(neighbor)


if __name__ == '__main__':
    # Each list describes the set of neighbors of a node in the graph
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

    # let's make a graph with the adjList
    src = buildGraph()
    print("BFS Traversal before cloning")
    bfs(src)

    a = Solution()
    clone = a.cloneGraph(src)
    print("\nBFS Traversal after cloning")
    bfs(clone)

    d_clone=a.cloneGraphDFS(src)
    print("\nDFS Traversal after cloning")
    bfs(d_clone)
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # making a graph with subarray conatining indegree for that node
        # and set containing its adjacent elements
        g = [[0, set()] for i in range(numCourses)]

        # for given destination and sources increament in degree for des and
        # add des in src's set as its adjacent
        for req in prerequisites:
            des, src = req
            g[des][0] += 1
            g[src][1].add(des)

        # forming a queue with the elements having 0 indegree
        q = deque([x for x in range(numCourses) if g[x][0] == 0])
        ans = []

        # topological algo
        while q:
            el = q.popleft()
            ans.append(el)
            for adjel in g[el][1]:
                g[adjel][0] -= 1
                # if an adjacent element gets indegree 0 after certain decreament
                # then append in queue
                if g[adjel][0] == 0:
                    q.append(adjel)
        return ans if len(ans) == numCourses else []


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    a = Solution()
    print(a.findOrder(numCourses, prerequisites))
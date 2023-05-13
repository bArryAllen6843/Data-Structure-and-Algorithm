class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        dfs=[0]
        seen=set(dfs)
        while dfs:
            i=dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
                    if len(seen)==len(rooms):return True
        return len(seen)==len(rooms)


if __name__ == '__main__':
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    a=Solution()
    print(a.canVisitAllRooms(rooms))
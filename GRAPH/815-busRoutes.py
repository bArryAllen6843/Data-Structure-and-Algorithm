import collections


class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)

        bfs = [(source, 0)]
        visited = set()
        for stop, bus in bfs:
            if stop == target: return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in visited:
                        bfs.append((j, bus + 1))
                        visited.add(j)
                routes[i] = []
        return -1


if __name__ == '__main__':
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    a = Solution()
    print(a.numBusesToDestination(routes, source, target))

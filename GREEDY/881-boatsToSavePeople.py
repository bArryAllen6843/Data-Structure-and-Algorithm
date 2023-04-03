class Solution:
    # sort the weights of people and then make pairs of lowest and highest weight if the weight is greater than limit
    # then decrease high and increase no of boats otherwise if pair's weight is less than limit then increase low and
    # decrease high and increase no of boats
    def numRescueBoats(self, people, limit: int):
        people.sort()
        lo = 0
        hi = len(people) - 1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
            boats += 1
        return boats


if __name__ == '__main__':
    people = [3,2,3,2,2]
    limit = 6
    a = Solution()
    print(a.numRescueBoats(people, limit))

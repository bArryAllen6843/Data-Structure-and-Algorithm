class Solution:
    def checkIfExist(self, arr) -> bool:
        i = 0
        j = 1

        while i < len(arr) - 1:
            if arr[i] == arr[j] * 2 or arr[i] == arr[j] / 2:
                return True
            else:
                j += 1

            if j == len(arr):
                i += 1
                j = i + 1
        else:
            return False


if __name__ == '__main__':
    # arr = [10, 2, 5, 3]
    arr = [3, 1, 7, 11]
    a = Solution()
    print(a.checkIfExist(arr))

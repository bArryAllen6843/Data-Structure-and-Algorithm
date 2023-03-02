class Solution:
    def compress(self, chars) -> int:
        # Brute force
        # if len(chars) == 1: return 1
        # ans = []
        # l = 0
        # r = 1
        # cnt = 1
        # while r < len(chars):
        #     if chars[l] == chars[r]:
        #         r += 1
        #         cnt += 1
        #     else:
        #         ans.append(chars[l])
        #         if cnt > 1:
        #             ans.append(str(cnt))
        #         l = r
        #         r+=1
        #         cnt = 1
        #
        #     if r == len(chars):
        #         ans.append(chars[l])
        #         if cnt > 1 and cnt<10:
        #             ans.append(str(cnt))
        #         elif cnt>9:
        #             a=cnt//10
        #             b=cnt%10
        #             ans.append(str(a))
        #             ans.append(str(b))
        #
        # chars=ans
        # print(chars)
        # return len(ans)

        # Method-2
        l, r = 0, 0
        while r < len(chars):
            chars[l] = chars[r]
            cnt = 1
            while r + 1 < len(chars) and chars[r] == chars[r + 1]:
                r += 1
                cnt += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[l + 1] = c
                    l += 1
            l += 1
            r += 1
        return l


if __name__ == '__main__':
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    # chars= ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    a = Solution()
    print(a.compress(chars))

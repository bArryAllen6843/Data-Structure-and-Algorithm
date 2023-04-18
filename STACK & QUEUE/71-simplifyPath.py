class Solution:
    # split the given string with all the slashes which will generate empty string (""), some name of folder ("home") or
    # a double dot to back a folder ("..")
    def simplifyPath(self, path: str) -> str:
        st=[]
        sp=path.split("/")
        for el in sp:
            if st and el=="..":
                st.pop()
            elif el not in [".","..",""]:
                st.append(el)
        return "/" + "/".join(st)


if __name__ == '__main__':
    # path = "/home//foo//"
    path="/aayush/../home//"
    # path="/../"
    a = Solution()
    print(a.simplifyPath(path))

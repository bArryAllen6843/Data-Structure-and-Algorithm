class Solution(object):

    # root is given a slot at first then we traverse from preoder and as we traverse we increase a slot
    # and fill previous empty slots . if a node is none then decrease a slot
    def isValidSerialization(self, preorder):
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot

        p = preorder.split(',')

        # initially we have one empty slot to put the root in it
        slot = 1
        for node in p:

            # no empty slot to put the current node
            if slot == 0:
                return False

            # a null node?
            if node == '#':
                # ocuppy slot
                slot -= 1
            else:
                # create new slot
                slot += 1

        # we don't allow empty slots at the end
        return slot == 0


if __name__ == '__main__':
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    a = Solution()
    print(a.isValidSerialization(preorder))

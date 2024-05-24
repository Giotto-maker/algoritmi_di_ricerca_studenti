import algorithms.search_problems_utils as spu

# Method to run and validate the walkback function
def walkback_test():
    parent_u = spu.SearchTreeNode(None, "s", None, 0)
    parent_v = spu.SearchTreeNode("b", "u", parent_u, 2)
    ret1 = spu.walkBack(spu.SearchTreeNode("a", "v", parent_v, 1))

    print("#1 result: " + str(ret1))
    print("Expected: " + " ['b', 'a']")

    parent_t = spu.SearchTreeNode(None, "s", None, 0)
    ret2 = spu.walkBack(spu.SearchTreeNode("b", "t", parent_t, 2))

    print("#2 result: " + str(ret2))
    print("Expected: " + " ['b']")
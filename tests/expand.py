import algorithms.search_problems_utils as spu

# Method to run and validate the expand function
def expand_test(P):  
    
    ret1 = spu.expand(P, "s", spu.SearchTreeNode(None, "s", None, 0), False)
    ret2 = spu.expand(P, "s", spu.SearchTreeNode(None, "s", None, 0), True)
    ret3 = spu.expand(P, "u", spu.SearchTreeNode(None, "u", None, 0), False)
    ret4 = spu.expand(P, "u", spu.SearchTreeNode(None, "u", None, 0), True)

    print("#1 result: " + str(ret1))
    print("Expected: " + " [(s,a, 1,t), (s,b, 2,u)]\n")

    print("#2 result: " + str(ret2))
    print("Expected: " + " [(s,b, 2,u), (s,a, 1,t)]\n")

    print("#3 result: " + str(ret4))
    print("Expected: " + " [(u,b, 2,v), (u,a, 1,v)]\n")

    print("#4 result: " + str(ret3))
    print("Expected: " + " [(u,a, 1,v), (u,b, 2,v)]\n")
    print()
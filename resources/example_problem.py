import algorithms.search_problems_utils as spu

''' 
    a,b are ACTIONS
    s,t,u,v are STATES
'''

# Definition of a toy example problem
def exampleProblemInstance():
    A = {
        "s" : {"a", "b"},
        "t" : {"a", "b"},
        "u" : {"a", "b"},
        "v" : {"a", "b"},
    }

    R = {
        ("a", "s") : "t",
        ("b", "s") : "u",
        ("a", "t") : "t",
        ("b", "t") : "s",
        ("a", "u") : "v",
        ("b", "u") : "v",
    }

    C = {
        ("a", "s") : 1,
        ("b", "s") : 2,
        ("a", "t") : 1,
        ("b", "t") : 2,
        ("a", "u") : 1,
        ("b", "u") : 2,
    }

    return spu.Problem(A, R, C, "s", {"t","v"})

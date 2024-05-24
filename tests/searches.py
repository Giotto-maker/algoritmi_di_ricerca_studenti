import sys
import algorithms.search_algos as algos
import algorithms.search_problems_utils as spu

# Method to run search algorithms applying the order for the actions selected by expand
def test_my_algorithm(P, algorithm, reverse):
    # runs the Breadth-first search in lex. order
    if (algorithm == "bfs" and not reverse):
        N=algos.BFS(P, False)

        if(N == None):
            print("Failure")
        else:
            print("BFS Lex: " + str(spu.walkBack(N))+ " Cost: " + str(N.COST))
            print("--> States Sequence: " + str(spu.walkBackS(N)))

            print()

    # runs the Breadth-first search in inverse lex. order
    elif (algorithm == "bfs" and reverse):
        N=algos.BFS(P, True)

        if(N == None):
            print("Failure")
        else:
            print("BFS Inv Lex: "  + str(spu.walkBack(N)) + " Cost: " + str(N.COST))
            print("--> States Sequence: " + str(spu.walkBackS(N)))

            print()

    # runs the Depth-First Search in lex. order
    elif (algorithm == "dfs" and not reverse):
        N=algos.DFS(P, False)

        if(N == None):
            print("Failure")
        else:
            print("DFS Lex: " + str(spu.walkBack(N))+ " Cost: " + str(N.COST))
            print("--> States Sequence: " + str(spu.walkBackS(N)))

            print()

    # runs the Depth-First Search in inverse lex. order
    elif (algorithm == "dfs" and reverse):
        N=algos.DFS(P, True)
        if(N == None):
            print("Failure")
        else:
            print("DFS Inv Lex: " + str(spu.walkBack(N))+ " Cost: " + str(N.COST))
            print("--> States Sequence: " + str(spu.walkBackS(N)))

            print()


    # runs uniform cost search in lex. order
    elif (algorithm == "ucs" and not reverse):
        print("Uniform Cost LEX")
        N = algos.uniformCost(P, False)

        if(N == None):
            print("Failure")
        else:
            print("\n UCS Lex: " + str(spu.walkBack(N))+ " Cost: " + str(N.COST))
            print("--> States Sequence: " + str(spu.walkBackS(N)))

    # runs uniform cost search in inverse lex. order
    elif (algorithm == "ucs" and reverse):
        print("Uniform Cost Inv LEX")
        N = algos.uniformCost(P, True)

        if(N == None):
            print("Failure")
        else:
            print("UCS Lex: " + str(spu.walkBack(N))+ " Cost: " + str(N.COST))
            print("--> States Sequence: " + str(spu.walkBackS(N)))

    elif (algorithm == "astar" and not reverse):
        print("A Star Search LEX")
        N = algos.A_star_search(P,False)

        if(N == None):
            print("Failure")
        else:
        # reconstruct the actual cost without the heuristics
            actions_states = spu.walkBackPair(N)
            first = True
            cost = 0
            previous_state = None
            for pair in actions_states:
                action = pair[0]
                state = pair[1]
                if first:
                    cost += P.action_cost(action, P.START)
                    first = False
                else:
                    cost += P.action_cost(action, previous_state)
                previous_state = state

            print("A Star Lex: " + str(spu.walkBack(N))+ " Cost: " + str(cost))
            print("--> States Sequence: " + str(spu.walkBackS(N)))

    elif (algorithm == "astar" and reverse):
        print("A Star Search Inv. LEX")
        N = algos.A_star_search(P,True)

        if(N == None):
            print("Failure")
        else:
        # reconstruct the actual cost without the heuristics
            actions_states = spu.walkBackPair(N)
            first = True
            cost = 0
            previous_state = None
            for pair in actions_states:
                action = pair[0]
                state = pair[1]
                if first:
                    cost += P.action_cost(action, P.START)
                    first = False
                else:
                    cost += P.action_cost(action, previous_state)
                previous_state = state

            print("A Star Lex: " + str(spu.walkBack(N))+ " Cost: " + str(cost))
            print("--> States Sequence: " + str(spu.walkBackS(N)))

    # raises an error 
    else:
        print("Algorithm not recognized", file=sys.stderr)
        exit(1)
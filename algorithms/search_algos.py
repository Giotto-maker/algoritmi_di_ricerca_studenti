import queue
import itertools
import matplotlib.pyplot as plt
import graphics.graph_vis as graph_vis
import algorithms.search_problems_utils as spu

from typing import Any
from dataclasses import dataclass, field
from graphics.frontier_vis import build_frontier_representation, draw_frontier_states, print_priority_items


# implements either Breadth-first search or Depth-first search depending of what F is
def xFS(problem, revAlphOrder, F, printFrontier=True):
    node_artists, axG, axF = graph_vis.init_my_graph_visualization(problem)
    i = 0

    visited = set()
    start = spu.SearchTreeNode(None, problem.START, None, 0)
    if (start.STATE in problem.GOALS):   return start
    F.put(start)
    
    if (printFrontier): 
        frontier_items = build_frontier_representation(F.queue, 'xfs')  
        draw_frontier_states(frontier_items, spu.SearchTreeNode(None, problem.START, None, 0), axF, True, False)
    
    plt.waitforbuttonpress()
    while not(F.empty()):
        curr = F.get()

        graph_vis.update_my_graph_visualization(axG, [curr], node_artists, i, False)

        i += 1
        expanded = spu.expand(problem, curr.STATE, curr, revAlphOrder)
        
        for N in expanded:

            if N.STATE in problem.GOALS:
                return N
            elif not(N.STATE in visited):
                F.put(N)
                visited.add(N.STATE)
        
        graph_vis.update_my_graph_visualization(axG, list(F.queue), node_artists, i, True)

        if (printFrontier): 
            frontier_items = build_frontier_representation(F.queue, 'xfs')  
            draw_frontier_states(frontier_items, curr, axF, False, False)
        plt.waitforbuttonpress()
    return None


# implements Breadth-first search algorithm
def BFS(problem, revAlphOrder):
    return  xFS(problem, revAlphOrder, queue.Queue())

# implements Depth-first search algorithm
def DFS(problem, revAlphOrder):
    return  xFS(problem, revAlphOrder, queue.LifoQueue())



# defines a prioritized item needed for priority queue. Index ensures stability.
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    index: int
    item: Any=field(compare=False)


# returns an optimal solution in terms of cost for the search problem
def optimal_search(problem, revAlphOrder, informed, printFrontier=True):  
    node_artists, axG, axF = graph_vis.init_my_graph_visualization(problem)
    
    i = 0
    visited = dict()
    counter = itertools.count()

    F = queue.PriorityQueue()
    start_node = spu.SearchTreeNode(None, problem.START, None, 0)
    if start_node.STATE in problem.GOALS:   return start_node
    pi= PrioritizedItem(0, next(counter), start_node)
    F.put(pi)
    visited[pi.item.STATE] = pi.item
    
    plt.waitforbuttonpress()
    while not(F.empty()):
        if (printFrontier):
            frontier_items = build_frontier_representation(F.queue, 'ucs')
            if i == 0:  init = True    
            draw_frontier_states(frontier_items, None, axF, init, True)
            init = False 

        curr = F.get().item

        graph_vis.update_my_graph_visualization(axG, [curr], node_artists, i, False)
        i += 1

        if curr.STATE in problem.GOALS:
                return curr

        for N in spu.expand(problem, curr.STATE, curr, revAlphOrder, informed):
            
            if (not(N.STATE in visited) or (visited[N.STATE].COST > N.COST)):   
                visited[N.STATE] = N
                F.put(PrioritizedItem(N.COST, next(counter), N))

        states = [elem.item for elem in F.queue]
        graph_vis.update_my_graph_visualization(axG, states, node_artists, i, True)
        plt.waitforbuttonpress()
    return None



# implements A* search
def A_star_search(problem, revAlphOrder):
    return optimal_search(problem, revAlphOrder, True)

# implements uniform cost search
def uniform_cost(problem, revAlphOrder):
    return optimal_search(problem, revAlphOrder, False)
import queue    # https://docs.python.org/3/library/queue.html
import itertools
import matplotlib.pyplot as plt
import graphics.graph_vis as graph_vis
import algorithms.search_problems_utils as spu

from typing import Any
from dataclasses import dataclass, field
from graphics.frontier_vis import build_frontier_representation, draw_frontier_states


''' TODO: implement Breadth-first search'''
def BFS(problem, revAlphOrder, printFrontier=False):
    raise NotImplementedError
    node_artists, axG, axF = graph_vis.init_my_graph_visualization(problem)
    i = 0

    # TODO: init datastructures and replace "condition" accordingly
    condition = True
    F = None
    
    if (printFrontier): 
        frontier_items = build_frontier_representation(F.queue, 'xfs')  
        draw_frontier_states(frontier_items, spu.SearchTreeNode(None, problem.START, None, 0), axF, True, False)
    
    plt.waitforbuttonpress()

    # TODO: main loop
    while not(condition):
        # TODO: interact with the data structure
        curr = None

        graph_vis.update_my_graph_visualization(axG, [curr], node_artists, i, False)
        i += 1
        
        # TODO: expansion logic

        graph_vis.update_my_graph_visualization(axG, list(F.queue), node_artists, i, True)

        if (printFrontier): 
            frontier_items = build_frontier_representation(F.queue, 'xfs')  
            draw_frontier_states(frontier_items, curr, axF, False, False)
        plt.waitforbuttonpress()

    return None



''' TODO: implement Depth-first search'''
def DFS(problem, revAlphOrder, printFrontier=False):
    raise NotImplementedError
    node_artists, axG, axF = graph_vis.init_my_graph_visualization(problem)
    i = 0

    # TODO: init datastructures and replace "condition" accordingly
    condition = True
    F = None
    
    if (printFrontier): 
        frontier_items = build_frontier_representation(F.queue, 'xfs')  
        draw_frontier_states(frontier_items, spu.SearchTreeNode(None, problem.START, None, 0), axF, True, False)
    
    plt.waitforbuttonpress()

    # TODO: main loop
    while not(condition):
        # TODO: interact with the data structure
        curr = None

        graph_vis.update_my_graph_visualization(axG, [curr], node_artists, i, False)
        i += 1
        
        # TODO: expansion logic

        graph_vis.update_my_graph_visualization(axG, list(F.queue), node_artists, i, True)

        if (printFrontier): 
            frontier_items = build_frontier_representation(F.queue, 'xfs')  
            draw_frontier_states(frontier_items, curr, axF, False, False)
        plt.waitforbuttonpress()
        
    return None



# defines a prioritized item needed for priority queue. Index ensures stability.
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    index: int
    item: Any=field(compare=False)


''' TODO: implement uniform cost search '''
def uniformCost(problem, revAlphOrder, printFrontier=False):  
    raise NotImplementedError
    node_artists, axG, axF = graph_vis.init_my_graph_visualization(problem)
    
    i = 0
    counter = itertools.count()

    # TODO: init datastructure and replace "condition" accordingly
    condition = True
    F = None

    plt.waitforbuttonpress()
    while not(condition):
        if (printFrontier):
            frontier_items = build_frontier_representation(F.queue, 'ucs')
            if i == 0:  init = True    
            draw_frontier_states(frontier_items, None, axF, init, True)
            init = False 

        # TODO: interact with the data structure
        curr = None
        
        graph_vis.update_my_graph_visualization(axG, [curr], node_artists, i, False)
        i += 1

        # TODO: look at the current node 

        # TODO: expansion logic

        states = [elem.item for elem in F.queue]
        graph_vis.update_my_graph_visualization(axG, states, node_artists, i, True)
        plt.waitforbuttonpress()
    return None



''' TODO: find the optimal solution to the searching problem '''
def A_star_search(problem, revAlphOrder, printFrontier=False):  
    raise NotImplementedError
    node_artists, axG, axF = graph_vis.init_my_graph_visualization(problem)
    
    i = 0
    counter = itertools.count()

    # TODO: init datastructure and replace "condition" accordingly
    condition = True
    F = None

    plt.waitforbuttonpress()
    while not(condition):
        if (printFrontier):
            frontier_items = build_frontier_representation(F.queue, 'ucs')
            if i == 0:  init = True    
            draw_frontier_states(frontier_items, None, axF, init, True)
            init = False 

        # TODO: interact with the data structure
        curr = None
        
        graph_vis.update_my_graph_visualization(axG, [curr], node_artists, i, False)
        i += 1

        # TODO: look at the current node 

        # TODO: expansion logic

        states = [elem.item for elem in F.queue]
        graph_vis.update_my_graph_visualization(axG, states, node_artists, i, True)
        plt.waitforbuttonpress()
    return None

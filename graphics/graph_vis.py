import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import sys

from networkx.drawing.nx_pydot import graphviz_layout

lightorange = '#ff9248'
lightpurple = '#c6a4c5'

# Builds the textual representation of an edge
def renderAction(act, cost):
	return "["+act+":"+str(cost)+"]"

# draws the search problem as a graph 
def init_my_graph_visualization(P):
    G = nx.DiGraph()

    nodeColors = []
    edgeLabels = dict()

    # Add nodes and associate colors to them
    for s in P.states():
        G.add_node(s)
        if s == P.START:
            nodeColors.append("lightgreen")
        elif s in P.GOALS:
            nodeColors.append("lightblue")
        else:
            nodeColors.append("white")

    # Add edges and renders textual description on them
    for s in P.states():
        for a in P.AVAILABLE[s]:
            G.add_edge(s, P.RESULT[(a, s)])
            cost = P.COST[(a,s)]
            if (s, P.RESULT[(a, s)]) in edgeLabels:
                edgeLabels[(s, P.RESULT[(a, s)])] = edgeLabels[(s, P.RESULT[(a, s)])] + "; " + renderAction(a,cost)
            else:
                edgeLabels[(s, P.RESULT[(a, s)])] = renderAction(a,cost)

    # sets the position of the graph
    pos = graphviz_layout(G, prog="dot")
    for k, v in pos.items():
        pos[k] = (-v[1], v[0])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # node artists are used to rember the characteristics of the nodes
    node_artists = {}
    for node, color in zip(G.nodes(), nodeColors):
        node_artist = nx.draw_networkx_nodes(G, pos=pos, nodelist=[node], node_shape='s', node_size=600,
                                              node_color=color, edgecolors='k', ax=ax1)
        node_artists[node] = node_artist

    # draw the graph
    nx.draw_networkx_edges(G, pos=pos, node_shape='s', width=2, node_size=600, ax=ax1)
    nx.draw_networkx_labels(G, pos=pos, font_size=7, ax=ax1)
    nx.draw_networkx_edge_labels(G, pos=pos, font_size=7, edge_labels=edgeLabels, ax=ax1)
    
    # set title and some text
    ax1.set_title("Init")
    ax1.text(0.5, -0.1, "Press any key to continue", ha='center', va='center', transform=ax1.transAxes)

    # Legend
    green_patch = mpatches.Rectangle(xy=(0,0), width=3, height=3, angle=0.0, 
                                     color='lightgreen', label='start')
    blue_patch = mpatches.Rectangle(xy=(0,0), width=3, height=3, angle=0.0, 
                                    color='lightblue', label='goal')
    orange_patch = mpatches.Rectangle(xy=(0,0), width=3, height=3, angle=0.0, 
                                      color=lightorange, label='reached')
    purple_patch = mpatches.Rectangle(xy=(0,0), width=3, height=3, angle=0.0, 
                                      color=lightpurple, label='frontier')
    
    ax1.legend(handles=[green_patch, blue_patch, orange_patch, purple_patch], 
               bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)


    ax2.axis('off')

    # Title of the plot
    algorithm = None
    match sys.argv[2].lower():
        case "bfs":
            algorithm = "Breadth-First Search"
        case "dfs":
            algorithm = "Depth-First Search"
        case "ucs":
            algorithm = "Uniform-Cost Search"
        case "astar":
            algorithm = "A Star Search"
        case _:
            algorithm = "Unrecognized"
            print("Something went wrong with the chosen algorithm", file=sys.stderr)
            exit(0)

    lex = True
    if (sys.argv[3].lower() == "y"): lex = False
    if lex: algorithm += " (LEX)"
    else:   algorithm += " (INV. LEX)"

    algorithm += " algorithm visualization"

    fig.suptitle(algorithm, fontsize=16, fontweight='bold')
    
    # Connect the close event with the on_close callback function
    fig.canvas.mpl_connect('close_event', on_close)
    
    plt.show(block=False)

    return node_artists, ax1, ax2


# Method to update colors and title during the iterations of the algorithm
def update_my_graph_visualization(ax, nodes_list, node_artists, iteration_counter, visiting):
    if visiting:    color = lightpurple
    else:           color = lightorange

    for node in nodes_list:
        # Update node color
        node_artist = node_artists[node.STATE]
        node_artist.set_color(color)
        node_artist.set_edgecolor('k')
        
    # Update title
    ax.set_title("Iteration " + str(iteration_counter))
    ax.figure.canvas.draw_idle()


# Method to capture the closing window event and terminate the program
def on_close(event):
	print("Execution is ended") 
	exit(0)
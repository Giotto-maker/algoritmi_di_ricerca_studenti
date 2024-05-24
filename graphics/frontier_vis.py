from matplotlib.patches import ArrowStyle
import matplotlib.pyplot as plt

lightpurple = '#c6a4c5'

# Basic method to print the frontier
def print_frontier(nodes, iteration_counter):
    frontier = []
    for N in nodes: frontier.append(N.STATE)
    print("Frontier at iteration " +str(iteration_counter) + " " + str(frontier))

# Basic method to print frontier with priority items
def print_priority_items(items, iteration_counter):
    print("\n Priority Queue at iteration " + str(iteration_counter))
    print("======================================================")
    items.sort()
    for item in items:
        print(item)
    print("======================================================")

# Method to construct the entries of the queue to be plotted
def build_frontier_representation(raw_frontier, algorithm):
    frontier_items = []
        
    # if xfs then it is enough to show the state only
    if (algorithm == 'xfs'):
        for node in raw_frontier:
            frontier_items.append(node.STATE) 

    # otherwise if a priority queue is used we show state, priority and index
    else:
        temp_queue = raw_frontier
        temp_queue.sort()
        for elem in temp_queue:
            state = elem.item.STATE
            index = elem.index
            priority = elem.priority
            entry = "<s:" + state + ",p:" + str(priority) + ",i:" + str(index) + ">"
            frontier_items.append(entry)

    return frontier_items
        

# Method to plot the frontier next to the graph
def draw_frontier_states(frontier, parent, ax, init, optimal):
    ax.clear()
    
    # Define the positions for the rectangles representing states in the frontier
    positions = [(1, i+1) for i in range(len(frontier))]  

    # Loop through strings and positions to plot rectangles and text
    for s, pos in zip(frontier, positions):
        ax.add_patch(plt.Rectangle(pos, 1, 1, edgecolor='black', facecolor=lightpurple))
        ax.text(pos[0] + 0.5, pos[1] + 0.5, s, ha='center', va='center')

    # Calculate the maximum x and y values
    max_x = max(pos[0] for pos in positions) + 1
    max_y = max(pos[1] for pos in positions) + 1

    # Set the axis limits based on the maximum x and y values
    ax.set_xlim(0.5, max_x + 0.5)
    ax.set_ylim(0.5, max_y + 0.5)

    # Set aspect ratio to equal for squares
    ax.set_aspect('equal')

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Add legend arrow
    my_arrow = ArrowStyle.Simple(head_length=1.0, head_width=1.2, tail_width=0.2)
    ax.annotate('', xy=(max_x + 0.5, max_y + 0.5), xytext=(max_x + 0.5, 0.5),
            arrowprops=dict(color=lightpurple, arrowstyle=my_arrow, linewidth=2))

    # Add legend text
    ax.text(max_x + 0.7, (max_y + 0.5) / 2, 'Queue\n\norder', ha='left', va='center', fontsize=12)
    
    # Set the title depending on the algorithm
    if optimal:
        ax.set_title("Frontier state before extraction")
    elif init:
        ax.set_title(parent.STATE + " is inserted in the frontier")
    else:
        ax.set_title("Expanded from " + parent.STATE + ". " + "Updated frontier")

    # Redraw the canvas of the specific figure
    ax.figure.canvas.draw_idle()
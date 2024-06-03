import queue

from graphics.frontier_vis import print_priority_items

# Create an empty priority queue
pq = queue.PriorityQueue()

# Insert items with priorities
pq.put((2, "eat breakfast"))
pq.put((1, "wake up"))
pq.put((3, "go to college"))
pq.put((4, "attend artificial intelligence classes"))

# Extract items from the priority queue
print("Priority Queue items in order of priority:")
while not pq.empty():
    priority, task = pq.get()
    print(f"Priority: {priority}, Task: {task}")


pq.put((1, "z"))
pq.put((1, "y"))
pq.put((1, "x"))
pq.put((1, "a"))
pq.put((1, "b"))
pq.put((1, "c"))
pq.put((2, "d"))
pq.get()

tq = pq
l = []
i = 0
while not tq.empty():
    item = tq.get()
    l.append(item)
    print_priority_items(l, i)
    i += 1
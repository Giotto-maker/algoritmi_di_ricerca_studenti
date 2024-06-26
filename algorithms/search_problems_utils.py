import os
import sys
import xlrd
# andolfi@diag.uniroma1.it


# Define the class representing the search Problem
class Problem:
  # constructor for the class
  def __init__(self, actions=dict(), results=dict(), costs=dict(), start=None, goals=set(), states=set()):
    self.AVAILABLE = actions
    self.RESULT = results
    self.COST = costs
    self.START = start
    self.GOALS = goals
    self.STATES = states

  # reads graph from file and creates the corresponding instance of the class above
  def loadFromFile(self,file, print_summary):
    file_path = os.path.join('resources', file)
    print(os.getcwd())
    wb = xlrd.open_workbook(file_path)
    sh = wb.sheet_by_index(0)
    self.START = str(sh.cell_value(0,0))
    self.GOALS = [x.strip() for x in sh.cell_value(1,0).split(",")]
    self.STATES = set()
    self.STATES.add(self.START)
    for rx in range(2,sh.nrows):
      if sh.cell_value(rx,1) in self.AVAILABLE:
        self.AVAILABLE[sh.cell_value(rx,1)].add(sh.cell_value(rx,0))
      else:
        self.AVAILABLE[sh.cell_value(rx,1)] = {sh.cell_value(rx,0)}

      if not (sh.cell_value(rx,2) in self.AVAILABLE):
         self.AVAILABLE[sh.cell_value(rx,2)] = set()

      self.STATES.add(sh.cell_value(rx,2))
      self.RESULT[ (sh.cell_value(rx,0), sh.cell_value(rx,1) ) ] = sh.cell_value(rx,2) 
      self.COST[ (sh.cell_value(rx,0), sh.cell_value(rx,1) ) ] = sh.cell_value(rx,3) 

    if (print_summary):
      print("Available actions from each state:\n")
      print(self.AVAILABLE)
      print()

      print("Results of the application of available actions from each state:\n")
      print(self.RESULT)
      print()

      print("Costs of the application of available actions from each state:\n")
      print(self.COST)
      print()
    
  # returns set of actions available from s
  def actions(self, s):
    return self.AVAILABLE[s]

  # returns the result of applying action a in state s
  def result(self, a, s):
    return self.RESULT[(a,s)]  

  # returns the cost of applying action a in state s
  def action_cost(self, a, s):
    return self.COST[(a,s)]

  # returns ordered set of states
  def states(self):
    s = list(self.AVAILABLE.keys())
    s.sort(key=lambda x: x, reverse=False)
    return s



# Define the class representing the a node in the Problem
class SearchTreeNode:
    # constructor for the class
    def __init__(self, action, state, parent, cost):
      self.ACTION = action
      self.STATE = state
      self.PARENT = parent
      self.COST = cost

    # converts node to its string representation
    def __str__(self):
      par = ""
      if self.PARENT != None:
        par = self.PARENT.STATE
      return  "(" + par + "," + str(self.ACTION) + ", " + str(self.COST) + "," + self.STATE + ")"
    
    # how to represent a node: use __str__()
    def __repr__(self):
      return self.__str__()
  
    # defines when two nodes can be considered as the same
    def __eq__(self, other): 
      if(other is None):
        return False
      if not((self.ACTION == other.ACTION) and (self.STATE == other.STATE) and (self.COST == other.COST)):
        return False
      elif(self.PARENT is None and other.PARENT is None):
        return True
      else:
       return self.PARENT.__eq__(other.PARENT)

    # give the hash for the node
    def __hash__(self):
        return (hash(self.ACTION) ^
                hash(self.STATE) ^
                hash(self.COST))



# return the nodes that can be reached through valid actions from the current state 
# and respect the order 'revAlphOrder' enforced on the actions available from the current state
def expand(problem, state, parent, revAlphOrder, info=False):
  ret = []
  for action in problem.actions(state):
    new_state = problem.result(action, state)
    cost = parent.COST + problem.action_cost(action, state)
    new_node = SearchTreeNode(action, new_state, parent, cost)

    if info:
      new_node.COST += heuristics(new_node)
      new_node.COST = round(new_node.COST, 3)
    ret.append(new_node)
  ret.sort(key= lambda x: x.ACTION, reverse=revAlphOrder)
  return ret

#backtracks the nodes in the search graph from N applying recursively function f to them
def walkBackF(N, f):
  # Implementazione iterativa
  '''
  walk = []
  curr = N 
  while(curr.PARENT != None):
    walk.insert(0,f(curr))
    curr = curr.PARENT
  return walk
  '''
  # Implementazione ricorsiva
  if N.PARENT == None:  return []
  return walkBackF(N.PARENT, f) + f(N)

# backtracks the actions in the search graph from N '''
def walkBack(N):
  return walkBackF(N, lambda x: [x.ACTION])

# backtracks the states in the search graph from N '''
def walkBackS(N):
  return walkBackF(N, lambda x: [x.STATE])

# backtracks <actions,states> in the search graph from N '''
def walkBackPair(N):
  return walkBackF(N, lambda x: [(x.ACTION, x.STATE)])

''' TODO: define a consistent heuristics '''
def heuristics(N):
  estimate = 0.1
  state = N.STATE 
  state_number = int(''.join([character for character in state if character.isdigit()]))
  if state_number % 2 == 0:
    estimate += 0.9
  return estimate




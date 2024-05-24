import sys
import algorithms.search_algos as algos
import algorithms.search_problems_utils as spu
import resources.example_problem as ex_probl

from tests.expand import expand_test
from tests.searches import test_my_algorithm
from tests.walkback import walkback_test

if __name__ == "__main__":

   # check input args
   if (len(sys.argv) != 2 and len(sys.argv) < 6):
      print(" => Usage for FUNCTIONS TESTING: python main.py [-function:expand/walkback]\n")
      print(""" => Usage for SEARCH ALGORITHMS: python main.py [-input_file:name] 
            [-algorithm:bfs/dfs/ucs/astar] [-reverse_lex:y/n] 
            [-input_summary:y/n] [-graph_report:y/n]""", file=sys.stderr)
      exit(1)

   # run expand tests
   elif (len(sys.argv) == 2 and sys.argv[1] == "expand"):
      P = ex_probl.exampleProblemInstance()
      expand_test(P)
      exit(0)
   
   # run walkback tests
   elif (len(sys.argv) == 2 and sys.argv[1] == "walkback"):
      walkback_test()
      exit(0)

   # raise an error 
   elif (len(sys.argv) == 2):
      print("Function not recognized", file=sys.stderr)
      exit(1)

   # launch the chosen search algorithm with specified configuration
   else:
      input_file = sys.argv[1].lower()
      algorithm = sys.argv[2].lower()
      reverse = False
      input_summary = False
      graph_report = False
    
      if (sys.argv[3].lower() == "y"):   reverse       = True
      if (sys.argv[4].lower() == "y"):   input_summary = True
      if (sys.argv[5].lower() == "y"):   graph_report  = True

      # load search problem
      P=spu.Problem()
      P.loadFromFile(input_file, input_summary)

      # print a report
      if (graph_report):

         statesList = list(P.STATES)
         statesList.sort()
         
         print("*************** REPORT ****************")
         print("Number of States: " + str(len(statesList)))
         print("Number of Edges: " + str(len(P.RESULT)))

         print("States: " + str(statesList))
         print("Start: " + P.START)
         print("Goals: " + str(P.GOALS))
         print("*************** ****** ****************")

      test_my_algorithm(P, algorithm, reverse)
      exit(0)
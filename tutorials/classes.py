import resources.example_problem as ex_probl
import algorithms.search_problems_utils as spu

''' Example on how to define a class, create objects for the class and define methods '''
class Person:
    def __init__(self, name, gender, age, email):
        self.name = name
        self.gender = gender
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print()

    def update_name(self, new_name):
        self.name = new_name

    def update_gender(self, new_gender):
        self.gender = new_gender

    def update_age(self, new_age):
        self.age = new_age

    def update_email(self, new_email):
        self.email = new_email

# Creating instances of the Person class
person1 = Person("Alice", "Female", 30, "alice@example.com")
person2 = Person("Bob", "Male", 25, "bob@example.com")

# Displaying initial information
print("----------------------------------------------------- ")
print("=> People:")
person1.display_info()
person2.display_info()

# Updating attributes
person1.update_name("Alicia")
person1.update_age(31)
person2.update_email("bob_new@example.com")

# Displaying updated information
print("Updated information:")
person1.display_info()
person2.display_info()


''' What about our search problems? They are a class too! '''
# create instance of example problem
P = ex_probl.exampleProblemInstance()

# call its methods
print("\n --------------------------------------------------- ")
print("=> Search Problem")
print("Available actions from each state:\n")
print(P.AVAILABLE)
print()

print("Results of the application of available actions from each state:\n")
print(P.RESULT)
print()

print("Costs of the application of available actions from each state:\n")
print(P.COST)
print()

print("Actions available from s are: " + str(P.actions("s")))
print("The cost of applying action a in state s is: " + str(P.action_cost("a", "s")))
print("The result of applying actions a in state s is: " + str(P.result("a", "s")))

''' Same holds for the nodes of the tree '''
print("\n --------------------------------------------------- ")
print("=> Tree node")

start_node = spu.SearchTreeNode(None, P.START, None, 0)
another_node = spu.SearchTreeNode("b", "u", start_node, 2)

print("The start node for the search problem is: " + str(start_node))
print("Its child node is: " + str(another_node))


print("\n --------------------------------------------------- ")
print("=> Another example fo search problem and its nodes")
# create instance of problem reading from file:
P=spu.Problem()
P.loadFromFile("input_file.xls", True)

start_node = spu.SearchTreeNode(None, P.START, None, 0)
print("The start node for the search problem is: " + str(start_node))


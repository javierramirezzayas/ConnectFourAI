from HumanPlayer import HumanPlayer
from HillClimbing import HillClimbing

env = [[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]

print("Initial Connect Four Environment:")
for i in env:
    print(str(i)+"\n")


human = HumanPlayer()
env = human.read(env)

hill = HillClimbing()
hill.generateSuccessors(env)

print("Connect Four after Human Player Choice")
for i in env:
    print(str(i)+"\n")

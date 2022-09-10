# pacman-agent
This is a record for the class "Intro to AI" at WUSTL in fall 2021. 

The project 0 is for a basic Python familiarity.

The project 1 is to design algorithms for path search problems regarding fixed food dot using DFS, BFS, UCS and A*.

<div align=center> <img src = "https://github.com/CocoYard/412-pacman/blob/master/maze.png"/> </div>

The project 2 is to design algorithms for pacman to avoid ghosts while eating foods and to eat ghosts while they are scared, using Minimax, Expectimax search and proposing a customized evaluation function.

The project 3 is all about Reinforcement Learing. Directly iterating the values of all states according to Markov Decision Processes. Modifying parameters
to let the robot take different optimal paths. But in real world without an MDP knowing all transition and reward functions, it is supposed to learn the values by
expriments. The agent updates the values and policies after every expriment, which is Q-learning. At last, I implemented an approximate Q-learning agent to evaluate
the weights of features for updating Q-values without traversing every state unnecessarily. Below is a result.

https://user-images.githubusercontent.com/93499248/149604891-e41b423e-5760-4265-ae42-ade27aa7dd42.mov

Original Questions:

https://www.cse.wustl.edu/~wyeoh/courses/cse412a/2021fall/projects/project1.html

https://www.cse.wustl.edu/~wyeoh/courses/cse412a/2021fall/projects/project2.html

https://www.cse.wustl.edu/~wyeoh/courses/cse412a/2021fall/projects/project3.html

The Pacman AI projects were developed at UC Berkeley, primarily by John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu). For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html


Play the game by inputing: 
```zsh
 python pacman.py
```
Other detailed usages such as using agents are in the file "commands.txt".

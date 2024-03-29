# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    visited = set()
    " push start state into stack "
    start = problem.getStartState()
    states = util.Stack()
    "the stack contains some state and the path there"
    states.push((start,[]))

    " while finding the goal state or no state can start from, terminate."
    expand, path = states.pop()
    while not problem.isGoalState(expand):
        if expand not in visited:
            visited.add(expand)
            triElemtsList = problem.getSuccessors(expand)
            for node in triElemtsList:
                coor = node[0]  # some state's coord
                dir = node[1]  # some state's direction
                if coor not in visited:
                    states.push((coor, path + [dir]))
        expand, path = states.pop()

    return  path
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    visited = set()
    " push start state into stack "
    start = problem.getStartState()
    states = util.Queue()
    "the stack contains some state and the path there"
    states.push((start, []))

    " while finding the goal state or no state can start from, terminate."
    expand, path = states.pop()
    while not problem.isGoalState(expand):
        if expand not in visited:
            visited.add(expand)
            triElemtsList = problem.getSuccessors(expand)
            for node in triElemtsList:
                coor = node[0]  # some state's coord
                dir = node[1]  # some state's direction
                if coor not in visited:
                    states.push((coor, path + [dir]))
        expand, path = states.pop()

    return path
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    visited = set()
    " push start state into stack "
    start = problem.getStartState()
    states = util.PriorityQueue()
    "the stack contains some state, the path there and the G value"
    g = 0
    states.push((start, []), g)
    " while finding the goal state or no state can start from, terminate."
    expand, path = states.pop()
    while not problem.isGoalState(expand):
        if expand not in visited:
            visited.add(expand)
            triElemtsList = problem.getSuccessors(expand)
            for node in triElemtsList:
                coor = node[0]  # some state's coord
                dir = node[1]  # some state's direction
                cost = node[2]
                if coor not in visited:
                    states.push((coor, path + [dir]), problem.getCostOfActions(path)+cost)
        expand, path = states.pop()

    return path
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    visited = set()
    " push start state into stack "
    start = problem.getStartState()
    states = util.PriorityQueue()
    "the stack contains some state, the path there and the G value"
    g = 0
    states.push((start, []), g + heuristic(start, problem))
    " while finding the goal state or no state can start from, terminate."
    expand, path = states.pop()
    while not problem.isGoalState(expand):
        if expand not in visited:
            visited.add(expand)
            triElemtsList = problem.getSuccessors(expand)
            for node in triElemtsList:
                coor = node[0]  # some state's coord
                dir = node[1]  # some state's direction
                cost = node[2]
                if coor not in visited:
                    states.push((coor, path + [dir]), problem.getCostOfActions(path) + cost + heuristic(coor, problem))
        expand, path = states.pop()

    return path
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

# searchAgents.py
# ---------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
This file contains all of the agents that can be selected to
control Pacman.  To select an agent, use the '-p' option
when running pacman.py.  Arguments can be passed to your agent
using '-a'.  For example, to load a SearchAgent that uses
depth first search (dfs), run the following command:

> python pacman.py -p SearchAgent -a searchFunction=depthFirstSearch

Commands to invoke other search strategies can be found in the
project description.

Please only change the parts of the file you are asked to.
Look for the lines that say

"*** YOUR CODE HERE ***"

The parts you fill in start about 3/4 of the way down.  Follow the
project description for details.

Good luck and happy searching!
"""
from game import Directions
from game import Agent
from game import Actions
import util
import time
import math
class GoWestAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP

#######################################################
# This portion is written for you, but will only work #
#       after you fill in parts of search.py          #
#######################################################

class SearchAgent(Agent):
    """
    This very general search agent finds a path using a supplied search algorithm for a
    supplied search problem, then returns actions to follow that path.

    As a default, this agent runs DFS on a PositionSearchProblem to find location (1,1)

    Options for fn include:
      depthFirstSearch or dfs
      breadthFirstSearch or bfs


    Note: You should NOT change any code in SearchAgent
    """

    def __init__(self, fn='depthFirstSearch', prob='PositionSearchProblem', heuristic='nullHeuristic'):
        # Warning: some advanced Python magic is employed below to find the right functions and problems

        # Get the search function from the name and heuristic
        if fn not in dir():
            raise AttributeError, fn + ' is not a search function in search.py.'
        func = getattr(fn)
        if 'heuristic' not in func.func_code.co_varnames:
            print('[SearchAgent] using function ' + fn)
            self.searchFunction = func
        else:
            if heuristic in globals().keys():
                heur = globals()[heuristic]
            elif heuristic in dir():
                heur = getattr(heuristic)
            else:
                raise AttributeError, heuristic + ' is not a function in searchAgents.py or search.py.'
            print('[SearchAgent] using function %s and heuristic %s' % (fn, heuristic))
            # Note: this bit of Python trickery combines the search algorithm and the heuristic
            self.searchFunction = lambda x: func(x, heuristic=heur)

        # Get the search problem type from the name
        if prob not in globals().keys() or not prob.endswith('Problem'):
            raise AttributeError, prob + ' is not a search problem type in SearchAgents.py.'
        self.searchType = globals()[prob]
        print('[SearchAgent] using problem type ' + prob)

    def registerInitialState(self, state):
        """
        This is the first time that the agent sees the layout of the game board. Here, we
        choose a path to the goal.  In this phase, the agent should compute the path to the
        goal and store it in a local variable.  All of the work is done in this method!

        state: a GameState object (pacman.py)
        """
        if self.searchFunction == None: raise Exception, "No search function provided for SearchAgent"
        starttime = time.time()
        problem = self.searchType(state) # Makes a new search problem
        self.actions  = self.searchFunction(problem) # Find a path
        totalCost = problem.getCostOfActions(self.actions)
        print('Path found with total cost of %d in %.1f seconds' % (totalCost, time.time() - starttime))
        if '_expanded' in dir(problem): print('Search nodes expanded: %d' % problem._expanded)

    def getAction(self, state):
        """
        Returns the next action in the path chosen earlier (in registerInitialState).  Return
        Directions.STOP if there is no further action to take.

        state: a GameState object (pacman.py)
        """
        if 'actionIndex' not in dir(self): self.actionIndex = 0
        i = self.actionIndex
        self.actionIndex += 1
        if i < len(self.actions):
            return self.actions[i]
        else:
            return Directions.STOP

class PositionSearchProblem(SearchProblem):
    """
    A search problem defines the state space, start state, goal test,
    successor function and cost function.  This search problem can be
    used to find paths to a particular point on the pacman board.

    The state space consists of (x,y) positions in a pacman game.

    Note: this search problem is fully specified; you should NOT change it.
    """
    def __init__(self, gameState, costFn = lambda x: 1, goal=(1,1), start=None, warn=True):
        """
        Stores the start and goal.

        gameState: A GameState object (pacman.py)
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        """
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition()
        if start != None: self.startState = start
        self.goal = goal
        self.costFn = costFn
        if warn and (gameState.getNumFood() != 1 or not gameState.hasFood(*goal)):
            print 'Warning: this does not look like a regular search maze'

        # For display purposes
        self._visited, self._visitedlist, self._expanded = {}, [], 0

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        isGoal = state == self.goal

        # For display purposes only
        # if isGoal:
        #     self._visitedlist.append(state)
        #     import __main__
        #     if '_display' in dir(__main__):
        #         if 'drawExpandedCells' in dir(__main__._display): #@UndefinedVariable
        #             __main__._display.drawExpandedCells(self._visitedlist) #@UndefinedVariable

        return isGoal

    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                cost = self.costFn(nextState)
                successors.append( ( nextState, action, cost) )

        # Bookkeeping for display purposes
        self._expanded += 1
        if state not in self._visited:
            self._visited[state] = True
            self._visitedlist.append(state)

        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999
        """
        if actions == None: return 999999
        x,y= self.getStartState()
        cost = 0
        for action in actions:
            # Check figure out the next state and see whether its' legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
            cost += self.costFn((x,y))
        return cost

class StayEastSearchAgent(SearchAgent):
    """
    An agent for position search with a cost function that penalizes being in
    positions on the West side of the board.

    The cost function for stepping into a position (x,y) is 1/2^x.
    """
    def __init__(self):
        self.searchFunction = uniformCostSearch
        costFn = lambda pos: .5 ** pos[0]
        self.searchType = lambda state: PositionSearchProblem(state, costFn)

class StayWestSearchAgent(SearchAgent):
    """
    An agent for position search with a cost function that penalizes being in
    positions on the East side of the board.

    The cost function for stepping into a position (x,y) is 2^x.
    """
    def __init__(self):
        self.searchFunction = uniformCostSearch
        costFn = lambda pos: 2 ** pos[0]
        self.searchType = lambda state: PositionSearchProblem(state, costFn)

def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def euclideanHeuristic(position, problem, info={}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5

#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################

class CornersProblem(SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function
    """

    def __init__(self, startingGameState):
        """
        Stores the walls, pacman's starting position and corners.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print 'Warning: no food in corner ' + str(corner)
        self._expanded = 0 # Number of search nodes expanded

        "*** YOUR CODE HERE ***"


    def getStartState(self):
        "Returns the start state (in your state space, not the full Pacman state space)"
        "*** YOUR CODE HERE ***"
        # cornerV = [False, False, False, False]
        cornerV = (False, False, False, False)
        startState = (self.startingPosition, cornerV)
        return startState
        util.raiseNotDefined()

    def isGoalState(self, state):
        "Returns whether this search state is a goal state of the problem"
        "*** YOUR CODE HERE ***"
        cornerV = state[1]
        return (cornerV[0] and cornerV[1] and cornerV[2] and cornerV[3])

        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            # Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            #   x,y = currentPosition
            #   dx, dy = Actions.directionToVector(action)
            #   nextx, nexty = int(x + dx), int(y + dy)
            #   hitsWall = self.walls[nextx][nexty]


            "*** YOUR CODE HERE ***"
            x, y = state[0]
            cornerV = state[1]
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                if nextState in self.corners:
                    if nextState == self.corners[0]:
                        newCornerV = (True, cornerV[1], cornerV[2], cornerV[3])
                    elif nextState == self.corners[1]:
                        newCornerV = (cornerV[0], True, cornerV[2], cornerV[3])
                    elif nextState == self.corners[2]:
                        newCornerV = (cornerV[0], cornerV[1], True, cornerV[3])
                    else:
                        newCornerV = (cornerV[0], cornerV[1], cornerV[2], True)
                    successors.append(((nextState, newCornerV), action, 1))
                else:

                    successors.append(((nextState, cornerV), action, 1))


        self._expanded += 1
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        if actions == None: return 999999
        x,y= self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)


def cornersHeuristic(state, problem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound
    on the shortest path from the state to a goal of the problem; i.e.
    it should be admissible (as well as consistent).
    """
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)

    "*** YOUR CODE HERE ***"

    currentP,cornerV  = state
    notVCorner=[]
    for i in range(len(corners)):
        if not cornerV[i]:
            notVCorner.append(corners[i])
    cost = 0
    while len(notVCorner) > 0:
        dist = []
        for c in notVCorner:
            dist.append(util.manhattanDistance(currentP, c))
        mindist = min(dist)
        cost += mindist
        Index = dist.index(mindist)
        currentP = notVCorner[Index]
        del notVCorner[Index]

    return cost # Default to trivial solution

class AStarCornersAgent(SearchAgent):
    "A SearchAgent for FoodSearchProblem using A* and your foodHeuristic"
    def __init__(self):
        self.searchFunction = lambda prob: aStarSearch(prob, cornersHeuristic)
        self.searchType = CornersProblem

class FoodSearchProblem:
    """
    A search problem associated with finding the a path that collects all of the
    food (dots) in a Pacman game.

    A search state in this problem is a tuple ( pacmanPosition, foodGrid ) where
      pacmanPosition: a tuple (x,y) of integers specifying Pacman's position
      foodGrid:       a Grid (see game.py) of either True or False, specifying remaining food
    """
    def __init__(self, startingGameState):
        self.start = (startingGameState.getPacmanPosition(), startingGameState.getFood())
        self.walls = startingGameState.getWalls()
        self.startingGameState = startingGameState
        self._expanded = 0
        self.heuristicInfo = {} # A dictionary for the heuristic to store information

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state[1].count() == 0

    def getSuccessors(self, state):
        "Returns successor states, the actions they require, and a cost of 1."
        successors = []
        self._expanded += 1
        for direction in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state[0]
            dx, dy = Actions.directionToVector(direction)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextFood = state[1].copy()
                nextFood[nextx][nexty] = False
                successors.append( ( ((nextx, nexty), nextFood), direction, 1) )
        return successors

    def getCostOfActions(self, actions):
        """Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999"""
        x,y= self.getStartState()[0]
        cost = 0
        for action in actions:
            # figure out the next state and see whether it's legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]:
                return 999999
            cost += 1
        return cost

class AStarFoodSearchAgent(SearchAgent):
    "A SearchAgent for FoodSearchProblem using A* and your foodHeuristic"
    def __init__(self):
        self.searchFunction = lambda prob: aStarSearch(prob, foodHeuristic)
        self.searchType = FoodSearchProblem

def foodHeuristic(state, problem):
    """
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come up
    with an admissible heuristic; almost all admissible heuristics will be consistent
    as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the other hand,
    inadmissible or inconsistent heuristics may find optimal solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a
    Grid (see game.py) of either True or False. You can call foodGrid.asList()
    to get a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the problem.
    For example, problem.walls gives you a Grid of where the walls are.

    If you want to *store* information to be reused in other calls to the heuristic,
    there is a dictionary called problem.heuristicInfo that you can use. For example,
    if you only want to count the walls once and store that value, try:
      problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access problem.heuristicInfo['wallCount']
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"
    foodLoc = []
    for i in range(foodGrid.width):
        for j in range(foodGrid.height):
            if foodGrid[i][j] == True:
                foodLoc.append((i, j))
    if len(foodLoc) == 0:
        return 0
    cost = 0
    disf2f = 0
    lo1 = foodLoc[0]
    lo2 = foodLoc[0]
    for loc1 in foodLoc:
        for loc2 in foodLoc:
            if disf2f < util.manhattanDistance(loc1, loc2):
                disf2f = util.manhattanDistance(loc1, loc2)
                lo1 = loc1
                lo2 = loc2
    disp2f = min(mazeDistance(position, lo1, problem.startingGameState),
                 mazeDistance(position, lo2, problem.startingGameState))
    # print foodLoc
    # print disf2f, disp2f, lo1, lo2
    cost = disf2f + disp2f
    return cost

class ClosestDotSearchAgent(SearchAgent):
    "Search for all food using a sequence of searches"
    def registerInitialState(self, state):
        self.actions = []
        currentState = state
        while(currentState.getFood().count() > 0):
            nextPathSegment = self.findPathToClosestDot(currentState) # The missing piece
            self.actions += nextPathSegment
            for action in nextPathSegment:
                legal = currentState.getLegalActions()
                if action not in legal:
                    t = (str(action), str(currentState))
                    raise Exception, 'findPathToClosestDot returned an illegal move: %s!\n%s' % t
                currentState = currentState.generateSuccessor(0, action)
        self.actionIndex = 0
        print 'Path found with cost %d.' % len(self.actions)

    def findPathToClosestDot(self, gameState):
        "Returns a path (a list of actions) to the closest dot, starting from gameState"
        # Here are some useful elements of the startState
        startPosition = gameState.getPacmanPosition()
        food = gameState.getFood()
        walls = gameState.getWalls()
        problem = AnyFoodSearchProblem(gameState)

        "*** YOUR CODE HERE ***"
        return aStarSearch(problem)
        util.raiseNotDefined()

class AnyFoodSearchProblem(PositionSearchProblem):
    """
      A search problem for finding a path to any food.

      This search problem is just like the PositionSearchProblem, but
      has a different goal test, which you need to fill in below.  The
      state space and successor function do not need to be changed.

      The class definition above, AnyFoodSearchProblem(PositionSearchProblem),
      inherits the methods of the PositionSearchProblem.

      You can use this search problem to help you fill in
      the findPathToClosestDot method.
    """

    def __init__(self, gameState):
        "Stores information from the gameState.  You don't need to change this."
        # Store the food for later reference
        self.food = gameState.getFood()

        # Store info for the PositionSearchProblem (no need to change this)
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition()
        self.costFn = lambda x: 1
        self._visited, self._visitedlist, self._expanded = {}, [], 0

    def isGoalState(self, state):
        """
        The state is Pacman's position. Fill this in with a goal test
        that will complete the problem definition.
        """
        x,y = state

        "*** YOUR CODE HERE ***"
        if self.food[x][y] == True or self.food.count() == 0:
            return True
        else:
            return False
        util.raiseNotDefined()

##################
# Mini-contest 1 #
##################

class ApproximateSearchAgent(Agent):
    "Implement your contest entry here.  Change anything but the class name."

    def registerInitialState(self, state):
        "This method is called before any moves are made."
        "*** YOUR CODE HERE ***"

    def getAction(self, state):
        """
        From game.py:
        The Agent will receive a GameState and must return an action from
        Directions.{North, South, East, West, Stop}
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def mazeDistance(point1, point2, gameState):
    """
    Returns the maze distance between any two points, using the search functions
    you have already built.  The gameState can be any game state -- Pacman's position
    in that state is ignored.

    Example usage: mazeDistance( (2,4), (5,6), gameState)

    This might be a useful helper function for your ApproximateSearchAgent.
    """
    x1, y1 = point1
    x2, y2 = point2
    walls = gameState.getWalls()
    assert not walls[x1][y1], 'point1 is a wall: ' + str(point1)
    assert not walls[x2][y2], 'point2 is a wall: ' + str(point2)
    prob = PositionSearchProblem(gameState, start=point1, goal=point2, warn=False)
    return len(bfs(prob))
# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    foodDis = 9999
    for i in range(1, successorGameState.data.layout.height - 1):
      for j in range(1, successorGameState.data.layout.width - 1):
        if newFood[j][i] == True:
          foodDis = min(foodDis, util.manhattanDistance(newPos, (j, i)))
    if foodDis == 9999:
      foodDis = 0
    ghostDis = 9999
    for ghostState in newGhostStates:
      ghostDis = min(ghostDis, util.manhattanDistance(newPos, ghostState.getPosition()))
    if ghostDis > 2 or ghostState.scaredTimer > 1:
      ghostDis = 1000
    score = - foodDis + ghostDis - 100 * successorGameState.getNumFood()
    return score

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  # print currentGameState
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """


  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    def max_value(state, agentIndex, dep):
      v = -9999
      "compute this state's successors"
      legalActions = [act for act in state.getLegalActions(0) if act is not Directions.STOP]
      successorGameStates = [state.generateSuccessor(0, action) for action in legalActions]
      i = 0
      res = i
      for successor in successorGameStates:
        if successor.isWin():
          return legalActions[i]
        if successor.isLose():
          i += 1
          continue
        temp = min_value(successor, 1, dep)
        if temp > v:
          v = temp
          res = i
        i += 1
      if dep == 1:
        # print legalActions[res], res
        return legalActions[res]

      return v


    def min_value(state, agentIndex, dep):
      if state.isLose():
        return -99999
      v = 9999999
      "compute this state's successors"
      legalActions = state.getLegalActions(agentIndex)
      successorGameStates = [state.generateSuccessor(agentIndex, action) for action in legalActions]
      if successorGameStates:
        if agentIndex == gameState.getNumAgents() - 1:
          if dep == self.depth:
            return self.evaluationFunction(state)
          for successor in successorGameStates:
            if successor.isLose():
              v = -99999999
            else:
              v = min(v, max_value(successor, 0, dep + 1))
        else:
          for successor in successorGameStates:
            if successor.isLose():
              v = -9999999
            else:
              v = min(v, min_value(successor, agentIndex + 1, dep))
        # print v, agentIndex, self.evaluationFunction(state), self.depth, dep
        return v
      else:
        return self.evaluationFunction(state)
    # print self.depth
    return max_value(gameState, 0, 1)

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """


  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    def max_value(state, agentIndex, dep, alpha, beta):
      v = -9999
      "compute this state's successors"
      legalActions = [act for act in state.getLegalActions(0) if act is not Directions.STOP]
      successorGameStates = [state.generateSuccessor(0, action) for action in legalActions]
      i = 0
      for successor in successorGameStates:
        if successor.isWin():
          return legalActions[i]
        temp = min_value(successor, 1, dep, alpha,beta)
        if temp > v:
          v = temp
          res = i
        i += 1
        alpha = v
        if alpha >= beta:
          return v
      if dep == 1:
        print v
        return legalActions[res]
      return v

    def min_value(state, agentIndex, dep, alpha, beta):
      v = 9999999
      "compute this state's successors"
      legalActions = state.getLegalActions(agentIndex)
      successorGameStates = [state.generateSuccessor(agentIndex, action) for action in legalActions]
      if successorGameStates:
        if agentIndex == gameState.getNumAgents() - 1:
          if dep == self.depth:
            return self.evaluationFunction(state)
          for successor in successorGameStates:
            if successor.isLose():
              v = self.evaluationFunction(successor)
            else:
              v = min(v, max_value(successor, 0, dep + 1, alpha, beta))
            beta = min(beta, v)
            if alpha >= beta:
              return v
        else:
          for successor in successorGameStates:
            if successor.isLose():
              v = self.evaluationFunction(successor)
            else:
              v = min(v, min_value(successor, agentIndex + 1, dep, alpha, beta))
        return v
      else:
        return self.evaluationFunction(state)

    return max_value(gameState, 0, 1, -9999, 9999)

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    # print self.depth
    def max_value(state, agentIndex, dep):
      v = -9999999
      "compute this state's successors"
      legalActions = [act for act in state.getLegalActions(0) if act is not Directions.STOP]
      successorGameStates = [state.generateSuccessor(0, action) for action in legalActions]
      i = 0
      for successor in successorGameStates:
        if successor.isWin() and dep == 1:
          return legalActions[i]
        temp = mean_value(successor, 1, dep)
        if temp > v:
          v = temp
          res = i
        i += 1
      if dep == 1:
        # print v
        return legalActions[res]
      return v

    def mean_value(state, agentIndex, dep):
      v = 0
      "compute this state's successors"
      legalActions = state.getLegalActions(agentIndex)
      # print legalActions
      successorGameStates = [state.generateSuccessor(agentIndex, action) for action in legalActions]
      if successorGameStates:
        if agentIndex == gameState.getNumAgents() - 1:
          for successor in successorGameStates:
            if dep == self.depth:
                v += self.evaluationFunction(successor)
            else:
                if successor.isLose():
                    v += self.evaluationFunction(successor)
                else:
                    v += max_value(successor, 0, dep + 1)
          v = v / len(successorGameStates)
        else:
          for successor in successorGameStates:
            if successor.isLose():
              v += self.evaluationFunction(successor)
            else:
              v += mean_value(successor, agentIndex + 1, dep)
          v = v / len(successorGameStates)
        # print v, agentIndex, self.evaluationFunction(state)
        return v
      else:
        return self.evaluationFunction(state)
    # print self.depth
    # act = max_value(gameState, 0, 1)
    # if gameState.generatePacmanSuccessor(act).getPacmanPosition() in gameState.:
    return max_value(gameState, 0, 1)
scareScore = 0
def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    My score consists of foodHeuristic from former codes, ghostDis, # food, # ghost hunted,
    # capsules, whether die and real-time score.

    The ghost distance is the nearest ghost by manhattan distance.
    If ghost distance is further than 2, we consider it the same safe degree.

    If ghost distance is near and it is scared, we add extra score for its scare.
    consider it is scared and pursue it.

    Capsules are useful but we should only eat them while we need them or it is wasted. So
    only if the scare time is 0 should we pursue or eat a capsule.

  """
  "*** YOUR CODE HERE ***"
  newPos = currentGameState.getPacmanPosition()
  newFood = currentGameState.getFood()
  foodLoc = newFood.asList()
  capLoc = currentGameState.getCapsules()
  newGhostStates = currentGameState.getGhostStates()
  newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

  foodScore = -foodHeuristic((newPos, newFood), FoodSearchProblem(currentGameState))
  # print search.aStarSearch(searchAgents.FoodSearchProblem(currentGameState), searchAgents.foodHeuristic)
  scareScore = 0
  death = 0
  ghostDis = 9999
  capDis = 9999
  for ghostState in newGhostStates:
    temp = util.manhattanDistance(newPos, ghostState.getPosition())
    if temp < ghostDis:
        ghostDis = temp
        ghost = ghostState
  if ghostDis > 2: # ghosts are far away
    ghostDis = 9999

  # print ghostDis, ghostState.scaredTimer
  if ghostDis <= 2 and ghost.scaredTimer >= 1: # ghost eaten
      ghostDis = 9999
      scareScore = 1
      # print scareScore
  if currentGameState.isLose():
      death = 1
  huntDis = - 20
  if ghost.scaredTimer is not 0:
      capScore = 500
      huntDis = - util.manhattanDistance(newPos, ghost.getPosition())
  else:
      for cap in capLoc:
          temp = mazeDistance(newPos, cap, currentGameState)
          if temp < capDis:
              capDis = temp
      capScore = -500 * len(capLoc) - capDis
  score = foodScore + ghostDis - 100 * currentGameState.getNumFood() + 200 * scareScore \
          + capScore - 11500 * death + 15 * currentGameState.getScore() + huntDis

  # print("position: ", newPos,  newGhostStates[0].getPosition(), newGhostStates[1].getPosition(), " score: ",
        # score, foodScore, ghostDis)
  return score



# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """
  def __init__(self, evalFn = 'betterEvaluationFunction', depth = '3'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)
  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)

    """
    "*** YOUR CODE HERE ***"
    def max_value(state, agentIndex, dep):
        v = -9999999
        "compute this state's successors"
        legalActions = [act for act in state.getLegalActions(0) if act is not Directions.STOP]
        successorGameStates = [state.generateSuccessor(0, action) for action in legalActions]
        i = 0
        for successor in successorGameStates:
            if successor.isWin() and dep == 1:
                return legalActions[i]
            temp = mean_value(successor, 1, dep)
            if temp > v:
                v = temp
                res = i
            i += 1
        if dep == 1:
            # print v
            return legalActions[res]
        return v


    def mean_value(state, agentIndex, dep):
        v = 0
        "compute this state's successors"
        legalActions = state.getLegalActions(agentIndex)
        # print legalActions
        successorGameStates = [state.generateSuccessor(agentIndex, action) for action in legalActions]
        if successorGameStates:
            if agentIndex == gameState.getNumAgents() - 1:
                for successor in successorGameStates:
                    if dep == self.depth:
                        v += self.evaluationFunction(successor)
                    else:
                        if successor.isLose():
                            v += self.evaluationFunction(successor)
                        else:
                            v += max_value(successor, 0, dep + 1)
                v = v / len(successorGameStates)
            else:
                for successor in successorGameStates:
                    if successor.isLose():
                        v += self.evaluationFunction(successor)
                    else:
                        v += mean_value(successor, agentIndex + 1, dep)
                v = v / len(successorGameStates)
            # print v, agentIndex, self.evaluationFunction(state)
            return v
        else:
            return self.evaluationFunction(state)

    # print self.depth
    # act = max_value(gameState, 0, 1)
    # if gameState.generatePacmanSuccessor(act).getPacmanPosition() in gameState.:
    return max_value(gameState, 0, 1)
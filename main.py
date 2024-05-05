from numpy import array

from Uninformed.BFS import Breadth_First_Search as BFS
from Uninformed.UCS import Uniform_Cost_Search as UCS
from Uninformed.DFS import Depth_First_Search as DFS
from Uninformed.DLS import Depth_Limited_Search as DLS
from Uninformed.IDS import Iterative_Deepening_Search as IDS

from Informed.GBFS import Greedy_Best_First_Search as GBFS
from Informed.AStar import A_Star as AStar


MAZE_XS = array([
    [1,2,2,1,0],
    [0,1,0,0,0],
    [4,1,1,1,-1]
])

MAZE_S = array([
    [3,1,2,1,2],
    [1,0,0,2,0],
    [4,2,2,1,1],
    [2,3,1,0,-1]
])



MAZE_M = array([
    [3,1,2,1,2,0],
    [1,0,0,2,1,1],
    [4,2,1,1,2,0],
    [1,3,2,0,3,4],
    [1,0,2,0,1,2],
    [0,3,1,1,1,1],
    [1,2,1,2,0,1],
    [0,3,0,1,3,-1]
])

MAZE_L = array([
    [3,2,4,2,0,0,0,2,0,3,1,1,2,2,1,5],
    [1,5,1,1,2,1,1,4,0,1,2,0,2,1,1,1],
    [1,0,4,0,0,0,1,1,1,1,0,1,3,0,0,1],
    [5,0,2,1,1,1,0,2,1,0,1,4,1,4,1,0],
    [0,1,2,0,2,0,1,1,0,2,1,2,1,0,1,4],
    [3,5,1,0,1,1,2,0,2,1,0,0,0,5,0,1],
    [2,0,3,1,2,1,0,2,5,0,1,2,2,1,0,1],
    [1,2,0,1,0,2,2,1,0,2,1,0,0,2,0,2],
    [2,5,0,0,1,1,0,2,3,4,0,1,0,1,0,1],
    [4,0,5,1,1,0,1,1,2,0,1,1,1,3,2,0],
    [2,1,1,0,2,2,0,2,4,2,0,0,2,2,1,1],
    [0,0,3,4,3,1,1,3,0,4,1,1,1,0,1,-1]
])



# model = BFS(MAZE_L)
model= UCS(MAZE_L)
model = DFS(MAZE_L)
model = DLS(MAZE_L, limit=22)
# model = IDS(MAZE_L)

# model = GBFS(MAZE_L)
# model = AStar(MAZE_L)

model.train()

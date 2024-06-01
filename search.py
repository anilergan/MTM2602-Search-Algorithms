from time import time

class Searching:

    def __init__(self, maze):

        self.MAZE = maze

        #CLOCKWISE
        self.ACTIONS = ('UP', 'RIGHT', 'DOWN', 'LEFT')

        # # COUNTERCLOCKWISE
        # self.ACTIONS = ('UP', 'LEFT', 'DOWN', 'RIGHT')

        # Row and Column Limit of Maze (ML -> Maze Limit)
        self.ML  = (self.MAZE.shape[0], self.MAZE.shape[1])

        # Current Cell's Location
        self.agent = (0,0)

        # the path defination which leads to solution
        self.path = [(0,0)]
        
        # Current Cell's Value
        self.value = self.MAZE[self.agent]

        # Frontiers
        self.frontiers = [(0,0)]

        # Explore Set
        self.explore_set = set()

        self.epoch = 0

        # Every sinlge node has ever created through execution time.
        self.node_created = 1



    def move(self, action, value):
        if action == 'UP': return 0, tuple(range(-1, (-value-1), -1))
        elif action == 'RIGHT': return 1, tuple(range(1, value+1))
        elif action == 'DOWN': return 0, tuple(range(1, value+1))
        elif action == 'LEFT': return 1, tuple(range(-1, (-value-1), -1))
    


    # def move(self, action, value):
    #     if action == 'UP': return 0, tuple([-value])
    #     elif action == 'RIGHT': return 1, tuple([value])
    #     elif action == 'DOWN': return 0, tuple([value])
    #     elif action == 'LEFT': return 1, tuple([-value])

    
            
    def frontier_elimination(self, nf, acts, dir):

        for act in acts:

            # Check if the new_state is inside of the limits of the MAZE
            new_state = list(self.agent)
            new_state[dir] += act
            new_state = tuple(new_state)
            if  new_state[dir] < 0 or new_state[dir] >= self.ML[dir]:
                break 
                # acts list is always ascending, so if first index does not satisfies the condition, so does not the rest.

            # Check if the new_state is already explored
            if new_state in self.explore_set or new_state in self.frontiers:
                continue
            

            # Check if there's a wall in action path
            current_state = self.agent
            path = self.action_path(current_state, new_state)
            if self.wall_detector(path):
                continue

            nf.append(new_state)
    
        return nf
                

    
    def wall_detector(self, path):
        for p in path:
            if self.MAZE[p] == 0:
                return True
        
        return False
        


    def action_path(self, current_state, next_state):
        """
        This function returns the cells between the next state and the current state (including the next state itself). 
        For example:
        current_state = (1,2)
        next_state = (3,2)
        Function returns: ((2,2), (3,2))
        """
        path = []
    
        # If the current state and the next state are on the same row
        if current_state[0] == next_state[0]:
            # Determine the direction of movement (left or right)
            step = 1 if next_state[1] > current_state[1] else -1
            # Generate the cells between the current and next state
            for col in range(current_state[1], next_state[1] + step, step):
                path.append((current_state[0], col))
        
        # If the current state and the next state are on the same column
        elif current_state[1] == next_state[1]:
            # Determine the direction of movement (up or down)
            step = 1 if next_state[0] > current_state[0] else -1
            # Generate the cells between the current and next state
            for row in range(current_state[0], next_state[0] + step, step):
                path.append((row, current_state[1]))

        
        return tuple(path)
                

    # h(x)
    def straight_line_distance(self, state):
        a = (self.MAZE.shape[0] - 1) - state[0]
        b = (self.MAZE.shape[1] - 1) - state[1]

        c = (a**2 + b**2)**0.5

        return round(c, 2)

    # g(x)
    def path_cost(self, new_path):

        cost = 0
        for i in range(len(new_path) - 1):
            cost += abs(sum(new_path[i+1]) - sum(new_path[i]))
            
        return cost
    


    
    def train(self):
        
        algorithm_name = self.__class__.__name__.replace('_', ' ')

        start = time()
        while True:
            self.epoch += 1
            self.update_frontiers(self.epoch)
            
            # Check Failure
            if self.frontiers == []:
                print("\n", "~~"*15, "A Failure Detected!", "~~"*15)
                return 
            
            if self.MAZE[tuple(self.frontiers[0])] == -1:
                break 
            else:
                self.agent = tuple(self.frontiers[0])
                self.value = self.MAZE[self.agent]
        
        print('\nSOLUTION: ', self.path[0])
        if algorithm_name == 'Iterative Deepening Search':
            print('Solution was found when limit had adjusted as', self.limit)

        end = time()

        duration = end - start
        min = int(duration / 60)
        sec = round((duration % 60), 8)

        if min >= 1:
            print('\n', algorithm_name, f'is done.\n => Execution time: {min} min {sec} sec')
        
        else: 
            print('\n', algorithm_name, f'is done.\n => Execution time: {sec} sec')
        
        print(" => Number of node created through execution:", self.node_created)
        print('\n')
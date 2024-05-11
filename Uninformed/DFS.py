from search import Searching


class Depth_First_Search(Searching):
    def __init__(self, maze):
        super().__init__(maze)


    def update_frontiers(self, epoch):
        print('\nEpoch:', epoch, '-'*70)

        print(f'   -> {tuple(self.frontiers[0])} will be popped.')   
        self.frontiers.pop(0)
        self.explore_set.add(self.agent)

        print('   -> Explore Set:', self.explore_set)
        
        new_frontiers = []
        for action in self.ACTIONS:
            dir, acts = self.move(action, self.value)
            new_frontiers = self.frontier_elimination(new_frontiers, acts, dir)
        

        self.frontiers = new_frontiers + self.frontiers 
        
        # Update the number of node has ever created so far
        self.node_created += len(new_frontiers)

        self.update_path(new_frontiers)

        print('   -> Frontiers:', self.frontiers)

    
    def update_path(self, childern):
        if self.path[0] == (0,0): #Root
            parent = self.path[0]
            self.path.pop(0)

            for child in childern:
                new_path = (parent, child)
                self.path.append(new_path)

        else:
            parent = list(self.path[0])
            self.path.pop(0)

            new_paths = []
            for child in childern:
                new_path =  list(parent)
                new_path.append(child)
                new_paths.append(tuple(new_path))
            
            self.path = new_paths + self.path
    

                









        



    
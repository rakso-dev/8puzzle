import copy

done = []
queue = []
conf_git = "I just do this cause i'm using git on a new system and dont remember how to configure it lol"

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.branches = []

    def is_goal(self, goal):
        return self.data == goal

    def get_position(self):
        count = 0
        pos_x = -1
        pos_y = -1
        for row in self.data:
            try:
                pos_y = row.index("_")
                pos_x = count
            except Exception as e:
                pass
            count += 1
        return pos_x, pos_y         
    
    def move_up(self, pos_x, pos_y):
        if pos_x == 0:
            return None
        branch = copy.deepcopy(self.data)
        tmp = branch[pos_x - 1][pos_y]
        branch[pos_x - 1][pos_y] = "_"
        branch[pos_x][pos_y] = tmp
        self.branches.append(TreeNode(branch))

    def move_right(self, pos_x, pos_y):
        if pos_y == 2:
            return None
        branch = copy.deepcopy(self.data)
        tmp = branch[pos_x][pos_y + 1]
        branch[pos_x][pos_y + 1] = "_"
        branch[pos_x][pos_y] = tmp
        self.branches.append(TreeNode(branch))

    def move_down(self, pos_x, pos_y):
        if pos_x == 2:
            return None
        branch = copy.deepcopy(self.data)
        tmp = branch[pos_x + 1][pos_y]
        branch[pos_x + 1][pos_y] = "_"
        branch[pos_x][pos_y] = tmp
        self.branches.append(TreeNode(branch))

    def move_left(self, pos_x, pos_y):
        if pos_y == 0:
            return None
        branch = copy.deepcopy(self.data)
        tmp = branch[pos_x][pos_y - 1]
        branch[pos_x][pos_y - 1] = "_"
        branch[pos_x][pos_y] = tmp
        self.branches.append(TreeNode(branch))

    def gen_branches(self):
        pos_x, pos_y = self.get_position()
        if pos_x == -1:
            return None
        self.move_up(pos_x, pos_y)
        self.move_right(pos_x, pos_y)
        self.move_down(pos_x, pos_y)
        self.move_left(pos_x, pos_y)        

    def expand(self):
        if self.data in done:
            return
        self.expand()    

    def BFS(self, goal):
        queue.append(self)
        if is_goal(goal):
            return self.data
        done.append(self.data)
        





goal = [
    [1, 2, 3],
    [8, "_", 4],
    [7, 6, 5]
]

test_state = [
    [5, 4, 1],
    [6, "_", 8],
    [7, 3 , 2]
]

root = TreeNode(test_state)
root.gen_branches()
print(root.data)
for l in root.branches:
    print(l.data)



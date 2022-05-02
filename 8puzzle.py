class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.branches = []

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
    
    def move_up(self):
        pass

    def move_right(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass



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


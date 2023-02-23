class Board():

    def __init__(self, cols=7, rows=6, to_win=4):
        self.board = [[0] * cols for _ in range(rows)]
        self.cols = cols
        self.rows = rows
        self.to_win = to_win

    def has_empty(self):
        for i in range(self.cols):
            if self.board[0][i] == 0:
                return True
        return False

    def draw(self):
        for row in self.board:
            print(row)

    def get_lowest_free(self, col):
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][col] == 0:
                return i
        return -1

    def check_direction(self, row, col, direction, player_ind):
        directions = {"N": (-1, 0), "NE": (-1, 1), "E": (0, 1), "SE": (1, 1),
                      "S": (1, 0), "SW": (1, -1), "W": (0, -1), "NW": (-1, -1)}
        res = 0
        current_x, current_y = row, col
        for i in range(self.to_win):
            x = current_x + directions[direction][0]
            y = current_y + directions[direction][1]
            if 0 <= x < self.rows and 0 <= y < self.cols:
                if self.board[x][y] == player_ind:
                    res += 1
                    current_x, current_y = x, y
                else:
                    break
        return res

    def check_win(self, player_ind, row, col):
        dists = {"N": 0, "NE": 0, "E": 0, "SE": 0, "S": 0, "SW": 0, "W": 0, "NW": 0}
        for direction in dists.keys():
            dists[direction] = self.check_direction(row, col, direction, player_ind)
        if dists["N"] + dists["S"] + 1 >= self.to_win:
            return True
        if dists["NE"] + dists["SW"] + 1 >= self.to_win:
            return True
        if dists["E"] + dists["W"] + 1 >= self.to_win:
            return True
        if dists["SE"] + dists["NW"] + 1 >= self.to_win:
            return True
        return False

    def make_move(self, col, player_ind):
        lowest_free = self.get_lowest_free(col)
        if lowest_free == -1:
            return -1
        else:
            self.board[lowest_free][col] = player_ind
            if self.check_win(player_ind, lowest_free, col):
                return 1
        return 0

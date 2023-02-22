class Board():

    def __init__(self, cols=7, rows=6, to_win=4):
        self.board = [[0] * cols for _ in range(rows)]
        self.cols = cols
        self.rows = rows
        self.to_win = to_win

    def get_row(self, row_ind):
        return self.board[row_ind]

    def get_col(self, col_ind):
        return [row[col_ind] for row in self.board]

    def has_empty(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    return True
        return False

    def draw(self):
        for row in self.board:
            print(row)

    def get_lowest_free(self, col):
        for i in range(self.rows - 1, -1, -1):
            print(f"i = {i}")
            if self.board[i][col] == 0:
                return i
        return -1

    def check_row(self, row, player_ind):
        for i in range(self.cols - self.to_win + 1):
            for el in row[i:i+self.to_win]:
                if el != player_ind:
                    break
            else:
                return True
        return False

    def check_col(self, col, player_ind):
        for i in range(self.rows - self.to_win + 1):
            for el in col[i:i+self.to_win]:
                if el != player_ind:
                    break
            else:
                return True
        return False

    def check_win(self, player_ind):
        for row in self.board:
            if self.check_row(row, player_ind):
                return True
        for col in [self.get_col(x) for x in range(self.cols)]:
            if self.check_col(col, player_ind):
                return True
        return False

    def make_move(self, col, player_ind):
        lowest_free = self.get_lowest_free(col)
#        print(lowest_free)
        if lowest_free == -1:
            return -1
        else:
            self.board[lowest_free][col] = player_ind
            if self.check_win(player_ind):
                return 1
        return 0

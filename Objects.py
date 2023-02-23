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

    def get_diag_l(self, dia_ind):
        res = []
        for i in range(dia_ind + 1):
            if i < self.rows and dia_ind - i < self.cols:
                res.append(self.board[i][dia_ind - i])
        return res

    def get_diag_r(self, dia_ind):
        res = []
        for i in range(dia_ind + 1):
            if i < self.rows and self.cols - dia_ind + i < self.cols:
                res.append(self.board[i][self.cols - dia_ind + i])
        return res

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

    def check_row(self, row, player_ind):
        for i in range(len(row) - self.to_win + 1):
            for el in row[i:i+self.to_win]:
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
            if self.check_row(col, player_ind):
                return True
        for diag_l in [self.get_diag_l(x) for x in range(self.cols + self.rows - 1)]:
            if self.check_row(diag_l, player_ind):
                return True
        for diag_r in [self.get_diag_r(x) for x in range(self.cols + self.rows - 1)]:
            if self.check_row(diag_r, player_ind):
                return True
        return False

    def make_move(self, col, player_ind):
        lowest_free = self.get_lowest_free(col)
        if lowest_free == -1:
            return -1
        else:
            self.board[lowest_free][col] = player_ind
            if self.check_win(player_ind):
                return 1
        return 0

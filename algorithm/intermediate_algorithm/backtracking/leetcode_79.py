class Solution:
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def search(self, board, word, idx, start_x, start_y):
        if idx == len(word):
            return True
        self.visited[start_x][start_y] = True
        for i in range(4):
            new_x = start_x + self.direction[i][0]
            new_y = start_y + self.direction[i][1]

            if len(board) > new_x >= 0 and len(board[0]) > new_y >= 0 and board[new_x][new_y] == word[idx] and not \
                    self.visited[new_x][new_y]:
                if self.search(board, word, idx + 1, new_x, new_y):
                    return True
        self.visited[start_x][start_y] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.search(board, word, 1, i, j):
                        return True
        return False

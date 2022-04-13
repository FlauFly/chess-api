import itertools

class Figure:
    def __init__(self, field):
        self.field = field
        self.available_moves = []

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        if dest_field in self.available_moves:
            return True
        else:
            return False

class King(Figure):
    def list_available_moves(self):
        letter = self.field[0]
        digit = self.field[1]
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        # Listing all fields one column and/or verse away from current field
        for column in range(columns.index(letter)-1, columns.index(letter)+2):
            for number in range(int(digit)-1, int(digit)+2):
                if 0 <= column <= 7 and 1 <= number <= 8:
                    move = columns[column] + str(number)
                    if move != self.field:
                        self.available_moves.append(move)
        return self.available_moves

class Queen(Figure):
    def list_available_moves(self):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        # Rook-like moves
        letter = self.field[0]
        digit = self.field[1]
        # Vertical moves
        for column in columns:
            move = column + digit
            if move != self.field:
                self.available_moves.append(move)
        # Horizontal moves
        for number in range(1, 9):
            move = letter + str(number)
            if move != self.field:
                self.available_moves.append(move)
        
        # Bishop-like moves
        for dx, dy in itertools.product([-1, 1], [-1, 1]):
            letter = self.field[0]
            digit = self.field[1]
            while True:
                # Check if next numbers represent valid chess field
                if not (0 <= columns.index(letter)+dx <= 7 and 1 <= int(digit)+dy <= 8):
                    break
                letter = columns[columns.index(letter)+dx]
                digit = str(int(digit)+dy)
                self.available_moves.append(letter + digit)
                
        return self.available_moves

class Rook(Figure):
    def list_available_moves(self):
        letter = self.field[0]
        digit = self.field[1]
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        # Vertical moves
        for column in columns:
            move = column + digit
            if move != self.field:
                self.available_moves.append(move)
        # Horizontal moves
        for number in range(1, 9):
            move = letter + str(number)
            if move != self.field:
                self.available_moves.append(move)
        return self.available_moves

class Bishop(Figure):
    def list_available_moves(self):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        # Every product element of [-1, 1] x [-1, 1] represents direction of diagonal move
        for dx, dy in itertools.product([-1, 1], [-1, 1]):
            letter = self.field[0]
            digit = self.field[1]
            while True:
                # Check if next numbers represent valid chess field
                if not (0 <= columns.index(letter)+dx <= 7 and 1 <= int(digit)+dy <= 8):
                    break
                letter = columns[columns.index(letter)+dx]
                digit = str(int(digit)+dy)
                self.available_moves.append(letter + digit)
        return self.available_moves

class Knight(Figure):
    def list_available_moves(self):
        for letter, number in itertools.product(columns, range(1, 9)):
            if ((abs(columns.index(self.field[0])-columns.index(letter)) == 1 and abs(int(self.field[1])-number) == 2) or
                (abs(columns.index(self.field[0])-columns.index(letter)) == 2 and abs(int(self.field[1])-number) == 1)):
                self.available_moves.append(letter + str(number))
        return self.available_moves

class Pawn(Figure):
    def list_available_moves(self):
        # Move one field forward
        if int(self.field[1]) < 8:
            self.available_moves.append(self.field[0] + str(int(self.field[1]) + 1))
        # Move two fields forward if pawn is standing on the initial position (second row)
        if int(self.field[1]) == 2:
            self.available_moves.append(self.field[0] + str(int(self.field[1]) + 2))
        return self.available_moves
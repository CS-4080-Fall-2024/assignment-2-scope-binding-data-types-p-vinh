# Implement a datastructure for a Rubik's Cube, allow for flexibility in the size of the cube and the logic of rotations

import numpy as np
import time

class RubiksCube:
    def __init__(self, size):
        """
        
         *        +-------+
         *        | White | 
         *        |   U   |
         * +------+-------+-------+------+
         * |Green | Red   | Blue  |Orange|
         * |  L   |   F   |   R   |  B   | 
         * +------+-------+-------+------+
         *        | Yellow|
         *        |  D    |
         *        +-------+
         
         Initialize the Rubik's Cube with the given size.
         
        """
        self.size = size
        self.faces = { 
            'U': [['W'] * size for _ in range(size)],  # Up (White) 
            'D': [['Y'] * size for _ in range(size)],  # Down (Yellow) 
            'L': [['G'] * size for _ in range(size)],  # Left (Green) 
            'R': [['B'] * size for _ in range(size)],  # Right (Blue) 
            'F': [['R'] * size for _ in range(size)],  # Front (Red) 
            'B': [['O'] * size for _ in range(size)],  # Back (Orange) 
        } 
        

            
    def rotate_face(self, face):
        """
            Rotate a given face of the Rubik's Cube 90 degrees clockwise.
        """
        return [list(row) for row in zip(*face[::-1])]
    
    def rotate_face_ccw(self, face):
        """
            Rotate a given face of the Rubik's Cube 90 degrees counter clockwise.
        """
        return [list(row) for row in zip(*face)][::-1]

    def rotate_front(self, direction): 
        """
            Rotate the front face CW/CCW and update the adjacent faces accordingly.
        """ 
        
        # Rotate the front face 
        self.faces['F'] = self.rotate_face(self.faces['F']) if direction == "F" else self.rotate_face_ccw(self.faces['F'])
        
        # Get the adjacent edges 
        top_row = self.faces['U'][self.size - 1][:]
        left_col = [self.faces['L'][i][self.size - 1] for i in range(self.size)]
        bottom_row = self.faces['D'][0][:]
        right_col = [self.faces['R'][i][0] for i in range(self.size)]
        
        # Update the adjacent faces based on the direction of the rotation
        if direction == 'F':
            for i in range(self.size):
                self.faces['U'][self.size - 1][i] = left_col[self.size - 1 - i]
                self.faces['L'][i][self.size - 1] = bottom_row[i]
                self.faces['D'][0][i] = right_col[self.size - 1 - i]
                self.faces['R'][i][0] = top_row[i]
        elif direction == 'F\'':   
            for i in range(self.size):
                self.faces['U'][self.size - 1][i] = right_col[i]
                self.faces['L'][i][self.size - 1] = top_row[self.size - 1 - i]
                self.faces['D'][0][i] = left_col[i]
                self.faces['R'][i][0] = bottom_row[self.size - 1 - i]
            
    def rotate_back(self, direction):
        """
            Rotate the back face CW/CCW and update the adjacent faces accordingly.
        """ 
        # Rotate the back face 
        self.faces['B'] = self.rotate_face(self.faces['B']) if direction == "B" else self.rotate_face_ccw(self.faces['B'])
        
        # Get the adjacent edges 
        top_row = self.faces['U'][0][:]
        left_col = [self.faces['L'][i][0] for i in range(self.size)]
        bottom_row = self.faces['D'][self.size - 1][:]
        right_col = [self.faces['R'][i][self.size - 1] for i in range(self.size)]
        
        # Update the adjacent faces based on the direction of the rotation
        if direction == 'B':
            for i in range(self.size):
                self.faces['U'][0][i] = right_col[i]
                self.faces['L'][i][0] = top_row[self.size - 1 - i]
                self.faces['D'][self.size - 1][i] = left_col[i]
                self.faces['R'][i][self.size - 1] = bottom_row[self.size - 1 - i]
        elif direction == 'B\'':
            for i in range(self.size):
                self.faces['U'][0][i] = left_col[self.size - 1 - i]
                self.faces['L'][i][0] = bottom_row[i]
                self.faces['D'][self.size - 1][i] = right_col[self.size - 1 - i]
                self.faces['R'][i][self.size - 1] = top_row[i]
    
    def rotate_up(self, direction):
        """
            Rotate the up face and the adjacent faces accordingly.
        """ 
        # Rotate the up face 
        self.faces['U'] = self.rotate_face(self.faces['U']) if direction == "U" else self.rotate_face_ccw(self.faces['U'])
        
        # Get the adjacent faces
        front_row = self.faces['F'][0][:]
        left_row = self.faces['L'][0][:]
        back_row = self.faces['B'][0][:]
        right_row = self.faces['R'][0][:]
        
        # Update the adjacent faces based on the direction of the rotation
        if direction == 'U':
            self.faces['F'][0] = right_row
            self.faces['L'][0] = front_row
            self.faces['B'][0] = left_row
            self.faces['R'][0] = back_row
        elif direction == 'U\'':
            self.faces['F'][0] = left_row
            self.faces['L'][0] = back_row
            self.faces['B'][0] = right_row
            self.faces['R'][0] = front_row

    def rotate_down(self, direction):
        """Rotate the down face and the adjacent faces accordingly.""" 
        
        # Rotate the down face 
        self.faces['D'] = self.rotate_face(self.faces['D']) if direction == "D" else self.rotate_face_ccw(self.faces['D'])
        
        # Get the adjacent faces
        front_row = self.faces['F'][self.size - 1][:]
        left_row = self.faces['L'][self.size - 1][:]
        back_row = self.faces['B'][self.size - 1][:]
        right_row = self.faces['R'][self.size - 1][:]
        
        # Update the adjacent faces based on the direction of the rotation
        if direction == 'D':
            self.faces['F'][self.size - 1] = left_row
            self.faces['L'][self.size - 1] = back_row
            self.faces['B'][self.size - 1] = right_row
            self.faces['R'][self.size - 1] = front_row
        elif direction == 'D\'':
            self.faces['F'][self.size - 1] = right_row
            self.faces['L'][self.size - 1] = front_row
            self.faces['B'][self.size - 1] = left_row
            self.faces['R'][self.size - 1] = back_row

    def rotate_left(self, direction):
        """Rotate the left face and the adjacent faces accordingly.""" 
        # Rotate the left face 
        self.faces['L'] = self.rotate_face(self.faces['L']) if direction == "L" else self.rotate_face_ccw(self.faces['L'])
        
        # Get the adjacent edges 
        top_col = [self.faces['U'][i][0] for i in range(self.size)]
        front_col = [self.faces['F'][i][0] for i in range(self.size)]
        bottom_col = [self.faces['D'][i][0] for i in range(self.size)]
        back_col = [self.faces['B'][i][self.size - 1] for i in range(self.size)]
            
        # Update the adjacent faces based on the direction of the rotation
        if direction == 'L':
            for i in range(self.size):
                self.faces['U'][i][0] = back_col[self.size - 1 - i]
                self.faces['F'][i][0] = top_col[i]
                self.faces['D'][i][0] = front_col[i]
                self.faces['B'][i][self.size - 1] = bottom_col[self.size - 1 - i]
        elif direction == 'L\'':
            for i in range(self.size):
                self.faces['U'][i][0] = front_col[i]
                self.faces['F'][i][0] = bottom_col[i]
                self.faces['D'][i][0] = back_col[self.size - 1 - i]
                self.faces['B'][i][self.size - 1] = top_col[self.size - 1 - i]

    def rotate_right(self, direction):
        """Rotate the right face and the adjacent faces accordingly."""
        # Rotate the right face 
        self.faces['R'] = self.rotate_face(self.faces['R']) if direction == "R" else self.rotate_face_ccw(self.faces['R'])
        
        # Get the adjacent edges 
        top_col = [self.faces['U'][i][self.size - 1] for i in range(self.size)]
        front_col = [self.faces['F'][i][self.size - 1] for i in range(self.size)]
        bottom_col = [self.faces['D'][i][self.size - 1] for i in range(self.size)]
        back_col = [self.faces['B'][i][0] for i in range(self.size)]
        
        # Update the adjacent faces based on the direction of the rotation
        if direction == 'R':
            for i in range(self.size):
                self.faces['U'][i][self.size - 1] = front_col[i]
                self.faces['F'][i][self.size - 1] = bottom_col[i]
                self.faces['D'][i][self.size - 1] = back_col[self.size - 1 - i]
                self.faces['B'][i][0] = top_col[self.size - 1 - i]
        elif direction == 'R\'':
            for i in range(self.size):
                self.faces['U'][i][self.size - 1] = back_col[self.size - 1 - i]
                self.faces['F'][i][self.size - 1] = top_col[i]
                self.faces['D'][i][self.size - 1] = front_col[i]
                self.faces['B'][i][0] = bottom_col[self.size - 1 - i]

    def rotate_middle(self, layer, axis, direction):
        """Rotate the middle slice and the adjacent faces accordingly."""
        # if the layer is 0 or greater than size then use rotate_left or rotate_right
        if layer <= 0 or layer >= self.size - 1:
            raise ValueError("Layer must be greater than 0 and less than or equal to the size of the cube.")

        axis = axis.upper()
        direction = direction.upper()
        
        # Get the specified layer based on the axis of rotation
        if axis == 'X':
            self.rotate_layer(layer, 0, direction == "CW")
        elif axis == 'Y':
            self.rotate_layer(layer, 1, direction == "CW")
        elif axis == 'Z':
            self.rotate_layer(layer, 2, direction == "CW")
        
    def rotate_layer(self, layer, axis, clockwise):
        if axis == 0:  # x-axis
            # X Orientation, we need the columns
            front_face = [self.faces['F'][i][layer] for i in range(self.size)]
            back_face = [self.faces['B'][i][layer] for i in range(self.size)]
            up_face = [self.faces['U'][i][layer] for i in range(self.size)]
            down_face = [self.faces['D'][i][layer] for i in range(self.size)]
            
            # Update the faces based on the direction of the rotation
            if clockwise:
                # Clockwise rotation, back face and downward face are reversed because of the orientation
                for i in range(self.size):
                    self.faces['U'][i][layer] = back_face[self.size - 1 - i]
                    self.faces['B'][i][layer] = down_face[self.size - 1 - i]
                    self.faces['D'][i][layer] = front_face[i]
                    self.faces['F'][i][layer] = up_face[i]
            else:
                # Counter clockwise rotation, back face and upper face are reversed because of the orientation
                for i in range(self.size):
                    self.faces['U'][i][layer] = front_face[i]
                    self.faces['F'][i][layer] = down_face[i]
                    self.faces['D'][i][layer] = back_face[self.size - 1 - i]
                    self.faces['B'][i][layer] = up_face[self.size - 1 - i]
        elif axis == 1:  # y-axis
            # Row wise rotation retrieve necessary faces
            left_face = [self.faces['L'][layer][i] for i in range(self.size)]
            right_face = [self.faces['R'][layer][i] for i in range(self.size)]
            front_face = [self.faces['F'][layer][i] for i in range(self.size)]
            back_face = [self.faces['B'][layer][i] for i in range(self.size)]
            
            # Update the faces based on the direction of the rotation
            if clockwise:
                # Clockwise rotation, swap the colomns of the faces
                for i in range(self.size):
                    self.faces['L'][layer][i] = back_face[i]
                    self.faces['B'][layer][i] = right_face[i]
                    self.faces['R'][layer][i] = front_face[i]
                    self.faces['F'][layer][i] = left_face[i]
            else:
                # Counter clockwise rotation, swap the colomns of the faces
                for i in range(self.size):
                    self.faces['L'][layer][i] = front_face[i]
                    self.faces['F'][layer][i] = right_face[i]
                    self.faces['R'][layer][i] = back_face[i]
                    self.faces['B'][layer][i] = left_face[i]
        elif axis == 2:  # z-axis
            # Column wise rotation
            right_face = [self.faces['R'][i][layer] for i in range(self.size)]
            left_face = [self.faces['L'][i][layer] for i in range(self.size)]
            up_face = [self.faces['U'][layer][i] for i in range(self.size)]
            down_face = [self.faces['D'][layer][i] for i in range(self.size)]
            
            # Update the faces based on the direction of the rotation
            if clockwise:
                # Clockwise rotation, swap the rows of the faces and reverse the order
                for i in range(self.size):
                    self.faces['U'][layer][i] = left_face[self.size - 1 - i]
                    self.faces['L'][i][layer] = down_face[i]
                    self.faces['D'][layer][i] = right_face[self.size - 1 - i]
                    self.faces['R'][i][layer] = up_face[i]
            else:
                # Counter clockwise rotation, swap the rows of the faces and reverse the order
                for i in range(self.size):
                    self.faces['U'][layer][i] = right_face[i]
                    self.faces['R'][i][layer] = down_face[self.size - 1 - i]
                    self.faces['D'][layer][i] = left_face[i]
                    self.faces['L'][i][layer] = up_face[self.size - 1 - i]
    

    def scramble(self, num_moves, seed=None):
        """
        Scramble the Rubik's Cube by making a random sequence of moves.
        """
        np.random.seed(seed)
        moves = []
        
        for _ in range(num_moves):
            move = np.random.choice(['F', 'B', 'U', 'D', 'L', 'R', 'F\'', 'B\'', 'U\'', 'D\'', 'L\'', 'R\'', 'M', 'M\'', 'E', 'E\'', 'S', 'S\''])
            if move == 'F' or move == 'F\'':
                self.rotate_front(move)
            elif move == 'B' or move == 'B\'':
                self.rotate_back(move)
            elif move == 'U' or move == 'U\'':
                self.rotate_up(move)
            elif move == 'D' or move == 'D\'':
                self.rotate_down(move)
            elif move == 'L' or move == 'L\'':
                self.rotate_left(move)
            elif move == 'R' or move == 'R\'':
                self.rotate_right(move)
            elif move == 'M' or move == 'M\'': # Middle slice, random layer based on the size of the cube. (Dynamically generated)
                self.rotate_middle(np.random.randint(1, self.size - 1), 'x', 'cw' if move == 'M' else 'ccw')
            elif move == 'E' or move == 'E\'':
                self.rotate_middle(np.random.randint(1, self.size - 1), 'y', 'cw' if move == 'E' else 'ccw')
            elif move == 'S' or move == 'S\'':
                self.rotate_middle(np.random.randint(1, self.size - 1), 'z', 'cw' if move == 'S' else 'ccw')
                
            moves.append(move)
        print(self.generate_map())
        return moves
    
    # Helper functions   
    
    def moves(self, dir):
        """
            Calls the appropriate rotation function based on the direction.
        """
        
        if dir == 'F' or dir == 'F\'':
            self.rotate_front(dir)
        elif dir == 'B' or dir == 'B\'':
            self.rotate_back(dir)
        elif dir == 'U' or dir == 'U\'':
            self.rotate_up(dir)
        elif dir == 'D' or dir == 'D\'':
            self.rotate_down(dir)
        elif dir == 'L' or dir == 'L\'':
            self.rotate_left(dir)
        elif dir == 'R' or dir == 'R\'':
            self.rotate_right(dir)
        elif dir == 'M' or dir == 'M\'':
            self.rotate_middle(1, 'x', 'cw' if dir == 'M' else 'ccw')
        elif dir == 'E' or dir == 'E\'':
            self.rotate_middle(1, 'y', 'cw' if dir == 'E' else 'ccw')
        elif dir == 'S' or dir == 'S\'':
            self.rotate_middle(1, 'z', 'cw' if dir == 'S' else 'ccw')
              
    def isValidCube(self):
        """Check if the cube is valid. A valid cube should have exactly 9 squares of each color."""
        color_counts = {
            'W': 0,  # White
            'Y': 0,  # Yellow
            'G': 0,  # Green
            'B': 0,  # Blue
            'R': 0,  # Red
            'O': 0   # Orange
        }

        errors = []
        
        # Iterate through each face and count the colors
        for face in self.faces.values():
            for row in face:
                for color in row:
                    if color in color_counts:
                        color_counts[color] += 1
        
        # Check if each color appears exactly 9 times
        for color, count in color_counts.items():
            if count != self.size ** 2:
                errors.append(f"{color} appears {count} times.\n")
        
        # Check edges ONLY FOR 3X3 CUBE DEBUGGING PURPOSES
        if self.size == 3:
            edges = [
                ('U', 2, 1, 'F', 0, 1),
                ('U', 1, 2, 'R', 0, 1),
                ('U', 0, 1, 'B', 0, 1),
                ('U', 1, 0, 'L', 0, 1),
                ('D', 0, 1, 'F', 2, 1),
                ('D', 1, 2, 'R', 2, 1),
                ('D', 2, 1, 'B', 2, 1),
                ('D', 1, 0, 'L', 2, 1),
                ('F', 1, 2, 'R', 1, 0),
                ('F', 1, 0, 'L', 1, 2),
                ('B', 1, 0, 'R', 1, 2),
                ('B', 1, 2, 'L', 1, 0)
            ]
            
            for edge in edges:
                face1, row1, col1, face2, row2, col2 = edge
                if not self.is_valid_edge((self.faces[face1][row1][col1], self.faces[face2][row2][col2])):
                    errors.append(f"Invalid edge between {face1} face at ({row1}, {col1}): Color: {self.faces[face1][row1][col1]} \
                                    and {face2} face at ({row2}, {col2}): Color: {self.faces[face2][row2][col2]}\n")

        if errors:
            return False, errors
        return True, []
    
    def is_valid_edge(self, edge):
        """Check if an edge piece is valid."""
        valid_edges = {
            ('W', 'R'), ('W', 'B'), ('W', 'O'), ('W', 'G'),
            ('Y', 'R'), ('Y', 'B'), ('Y', 'O'), ('Y', 'G'),
            ('R', 'G'), ('R', 'B'),
            ('O', 'G'), ('O', 'B')
        }
        return edge in valid_edges or edge[::-1] in valid_edges

    def generate_map(self):
        """Generate a map of the current state of the Rubik's Cube."""
        size = self.size
        map_str = ""
        offset = self.size + 1 // 2

        # Top face (U)
        map_str += " " * (size + 1 * offset) + "+-------+\n"
        map_str += " " * (size + 1 * offset) + "| White |\n"
        map_str += " " * (size + 1 * offset) + "|   Up  |\n"
        for row in self.faces['U']:
            map_str += " " * (size + 1 * offset) + "| " + " ".join(row) + " |\n"
        map_str += " " * (size + 1 * offset) + "+-------+\n"

        # Middle faces (L, F, R, B)
        for i in range(size):
            map_str += "+" + "-" * (size * 2 + 1) + "+" + "-" * (size * 2 + 1) + "+" + "-" * (size * 2 + 1) + "+" + "-" * (size * 2 + 1) + "+\n"
            map_str += "| " + " ".join(self.faces['L'][i]) + " | " + " ".join(self.faces['F'][i]) + " | " + " ".join(self.faces['R'][i]) + " | " + " ".join(self.faces['B'][i]) + " |\n"
        map_str += "+" + "-" * (size * 2 + 1) + "+" + "-" * (size * 2 + 1) + "+" + "-" * (size * 2 + 1) + "+" + "-" * (size * 2 + 1) + "+\n"

        # Bottom face (D)
        map_str += " " * (size + 1 * offset) + "| Yellow|\n"
        map_str += " " * (size + 1 * offset) + "|  Down |\n"
        for row in self.faces['D']:
            map_str += " " * (size + 1 * offset) + "| " + " ".join(row) + " |\n"
        map_str += " " * (size + 1 * offset) + "+-------+\n"

        return map_str

def main():
    cube = RubiksCube(3)
    cube.scramble(20, int(time.time()))
    print("Seed: " + str(int(time.time())))
    

    
    isValid, errors = cube.isValidCube()

    if isValid:
        print("The cube is valid.")
    else:
        print("The cube is invalid.")
        for error in errors:
            print(error)
if __name__ == "__main__":
    main()

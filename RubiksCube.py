# Implement a datastructure for a Rubik's Cube, allow for flexibility in the size of the cube and the logic of rotations

import numpy as np
import copy


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
        
            
    def print_cube(self):
        for face, grid in self.faces.items():
            print(f"{face} face:")
            for row in grid:
                print(" ".join(row))
            print()  
        print("------")  

            
    def rotate_face(self, face):
        return [list(row) for row in zip(*face[::-1])]

    def rotate_front(self): 
        """Rotate the front face and the adjacent faces accordingly.""" 
        # Rotate the front face 
        self.faces['F'] = self.rotate_face(self.faces['F']) 
        
        # Rotate the adjacent edges 
        top_row = self.faces['U'][2][:]
        left_col = [self.faces['L'][i][2] for i in range(self.size)]
        bottom_row = self.faces['D'][0][:]
        right_col = [self.faces['R'][i][0] for i in range(self.size)]
        
        # Update the adjacent faces
        for i in range(self.size):
            self.faces['U'][2][i] = left_col[self.size - 1 - i]
            self.faces['L'][i][2] = bottom_row[i]
            self.faces['D'][0][i] = right_col[self.size - 1 - i]
            self.faces['R'][i][0] = top_row[i]
    
    def rotate_back(self):
        """Rotate the back face and the adjacent faces accordingly.""" 
        # Rotate the back face 
        self.faces['B'] = self.rotate_face(self.faces['B']) 
        
        # Rotate the adjacent edges 
        top_row = self.faces['U'][0][:]
        left_col = [self.faces['L'][i][0] for i in range(self.size)]
        bottom_row = self.faces['D'][2][:]
        right_col = [self.faces['R'][i][2] for i in range(self.size)]
        
        # Update the adjacent faces
        for i in range(self.size):
            self.faces['U'][0][i] = right_col[i]
            self.faces['L'][i][0] = top_row[self.size - 1 - i]
            self.faces['D'][2][i] = left_col[i]
            self.faces['R'][i][2] = bottom_row[self.size - 1 - i]
    
    def rotate_up(self):
        """Rotate the up face and the adjacent faces accordingly.""" 
        # Rotate the up face 
        self.faces['U'] = self.rotate_face(self.faces['U']) 
        
        # Rotate the adjacent edges 
        front_row = self.faces['F'][0][:]
        left_row = self.faces['L'][0][:]
        back_row = self.faces['B'][0][:]
        right_row = self.faces['R'][0][:]
        
        # Update the adjacent faces
        for i in range(self.size):
            self.faces['F'][0][i] = right_row[i]
            self.faces['L'][0][i] = front_row[i]
            self.faces['B'][0][i] = left_row[self.size - 1 - i]
            self.faces['R'][0][i] = back_row[self.size - 1 - i]
    
    def rotate_down(self):
        """Rotate the down face and the adjacent faces accordingly.""" 
        # Rotate the down face 
        self.faces['D'] = self.rotate_face(self.faces['D']) 
        
        # Rotate the adjacent edges 
        front_row = self.faces['F'][2][:]
        left_row = self.faces['L'][2][:]
        back_row = self.faces['B'][2][:]
        right_row = self.faces['R'][2][:]
        
        # Update the adjacent faces
        for i in range(self.size):
            self.faces['F'][2][i] = left_row[i]
            self.faces['L'][2][i] = back_row[self.size - 1 - i]
            self.faces['B'][2][i] = right_row[self.size - 1 - i]
            self.faces['R'][2][i] = front_row[i]
    
    def rotate_left(self):
        """Rotate the left face and the adjacent faces accordingly.""" 
        # Rotate the left face 
        self.faces['L'] = self.rotate_face(self.faces['L']) 
        
        # Rotate the adjacent edges 
        top_col = [self.faces['U'][i][0] for i in range(self.size)]
        front_col = [self.faces['F'][i][0] for i in range(self.size)]
        bottom_col = [self.faces['D'][i][0] for i in range(self.size)]
        back_col = [self.faces['B'][i][2] for i in range(self.size)]
        
        # Update the adjacent faces
        for i in range(self.size):
            self.faces['U'][i][0] = back_col[self.size - 1 - i]
            self.faces['F'][i][0] = top_col[i]
            self.faces['D'][i][0] = front_col[i]
            self.faces['B'][i][2] = bottom_col[self.size - 1 - i]
    
    def rotate_right(self):
        """Rotate the right face and the adjacent faces accordingly."""
        # Rotate the right face 
        self.faces['R'] = self.rotate_face(self.faces['R']) 
        
        # Rotate the adjacent edges 
        top_col = [self.faces['U'][i][2] for i in range(self.size)]
        front_col = [self.faces['F'][i][2] for i in range(self.size)]
        bottom_col = [self.faces['D'][i][2] for i in range(self.size)]
        back_col = [self.faces['B'][i][0] for i in range(self.size)]
        
        # Update the adjacent faces
        for i in range(self.size):
            self.faces['U'][i][2] = front_col[self.size - 1 - i]
            self.faces['F'][i][2] = bottom_col[i]
            self.faces['D'][i][2] = back_col[self.size - 1 - i]
            self.faces['B'][i][0] = top_col[i]

    def scramble(self, num_moves, seed=None):
        np.random.seed(seed)
        
        for _ in range(num_moves):
            move = np.random.choice(['F', 'B', 'U', 'D', 'L', 'R'])
            if move == 'F':
                self.rotate_front()
            elif move == 'B':
                self.rotate_back()
            elif move == 'U':
                self.rotate_up()
            elif move == 'D':
                self.rotate_down()
            elif move == 'L':
                self.rotate_left()
            elif move == 'R':
                self.rotate_right()
                
def main():
    cube = RubiksCube(3)
    cube.print_cube()
    cube.scramble(10)
    cube.print_cube()
if __name__ == "__main__":
    main()

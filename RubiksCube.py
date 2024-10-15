# Implement a datastructure for a Rubik's Cube, allow for flexibility in the size of the cube and the logic of rotations

import numpy as np
import copy


class RubiksCube:
    def __init__(self, size):
        """
        
         *        +-------+
         *        | 8   9 | 
         *        | 11 10 |
         * +------+-------+-------+------+
         * | 1  2 | 12 13 | 19 16 | 6  7 |
         * | 0  3 | 15 14 | 18 17 | 5  4 | 
         * +------+-------+-------+------+
         *        | 22 23 |
         *        | 21 20 |
         *        +-------+
         
        """
        self.size = size
        self.cube = np.zeros((6, size, size), dtype=object)
        self.corner = np.zeros((8, 3), dtype=object)
        self.edge = np.zeros((12, 2), dtype=object)
        self.center = np.zeros((6, 1), dtype=object)
        self.face = np.zeros((6, 1), dtype=object)
        # Initialize the cube for debug as well
        # Left side = 1L, Right side = 1R, Middle = 1M
        
        # Front side = 2F, Back side = 2B, Middle = 2M
        
        # Up side = 3U, Down side = 3D, Middle = 3M
        for face in range(6):
            for row in range(size):
                self.cube[face, row, 0] = f"{face + 1}L"
                self.cube[face, row, 1] = f"{face + 1}M"
                self.cube[face, row, 2] = f"{face + 1}R"
            
            
    def rotate_layer(self, layer, axis, direction):
        if axis == "x":
            self._rotate_x(layer, direction)
        elif axis == "y":
            self._rotate_y(layer, direction)
        elif axis == "z":
            self._rotate_z(layer, direction)
        else:
            print("Invalid axis")

    # Up/down rotation
    def _rotate_x(self, layer, direction):
        temp = copy.deepcopy(self.cube[:, :, layer]) # Copy the layer to be rotated, only need 4 sides
        # Can be any degree of 90, 180, 270 or 360. So we can just use the / operator to get the correct rotation
        num_of_rot = direction // 90
        

        for i in range(0, self.size):
            self.cube[0, layer, i] = temp[4, self.size - 1 - i]
            self.cube[4, self.size - 1 - i, :] = temp[5, layer]
            self.cube[5, layer, i] = temp[2, self.size - 1 - i]
            self.cube[2, self.size - 1 - i, :] = temp[0, layer]
            # self.cube[0, i, layer] = temp[layer, i]
            # self.cube[1, i, layer] = temp[layer + 1, i]
            # self.cube[2, i, layer] = temp[layer + 2, i]
            # self.cube[3, i, layer] = temp[0, i]
        
        # When rotating down, the faces are rotated in the opposite direction
        
        print(self.cube)
        # print(temp)
        # self.cube[4, ::-1, :] = temp[5, layer, :]
        # self.cube[5, layer, :] = temp[2, ::-1, :]
        # self.cube[2, ::-1, :] = temp[0, layer, :]
        
        # print(self.cube)
        pass
    
    # Left/right rotation
    def _rotate_y(self, layer, direction):
        pass
    
    # Front/back rotation
    def _rotate_z(self, layer, direction):
        
        pass

def main():
    cube = RubiksCube(3)
    cube.rotate_layer(1, "x", 90) # Rotate the second layer in the x direction by 90 degrees

if __name__ == "__main__":
    main()

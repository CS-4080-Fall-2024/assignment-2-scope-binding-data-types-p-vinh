# Implement a datastructure for a Rubik's Cube, allow for flexibility in the size of the cube and the logic of rotations

import numpy as np
import copy

class RubiksCube:
    def __init__(self, size):
        self.size = size
        self.cube = np.zeros((6, size, size), dtype=int)
        # Initialize the cube
        for i in range(6):
            self.cube[i] = i + 1
        print(self.cube)

    def rotate(self, face, direction):
        # Rotate the face of the cube
        if direction == "clockwise":
            self.cube[face] = np.rot90(self.cube[face], 3)
        elif direction == "counter-clockwise":
            self.cube[face] = np.rot90(self.cube[face], 1)
        else:
            print("Invalid direction")
        


def main():
    cube = RubiksCube(3)
    cube.rotate(0, "clockwise")

if __name__ == "__main__":
    main()
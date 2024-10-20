from RubiksCube import RubiksCube

class RubiksCubeSolver:
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        pass
    

def main():
    cube = RubiksCube(3)
    solver = RubiksCubeSolver(cube)
    solver.solve()
    
    
if __name__ == "__main__":
    main()
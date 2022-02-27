import pybullet as p



class WORLD:
    def __init__(self):
        # loading all of the simulation data
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
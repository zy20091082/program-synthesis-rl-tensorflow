import os
from __init__ import Karel, draw2d

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

karel = Karel(world_path=os.path.join(BASE_PATH, "simple.map"))
karel.draw()
karel.move()
karel.draw()

karel = Karel(world_size(12, 4))
karel.draw()

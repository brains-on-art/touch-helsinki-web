import random

def random_lattice(xsize, ysize):
    return [[(random.random()*10)+5 for i in range(xsize)] for j in range(ysize)]

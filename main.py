from threexplusone import show
from random import randint

show([randint(2, 100) for i in range(4)], outfile='figure.png', fontsize=6)
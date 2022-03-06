from collatz_conjecture import show
from random import randint

show([randint(10, 10001) for _ in range(11)], outfile='figure.png', text=False, single=True)
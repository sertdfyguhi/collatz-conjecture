from threexplusone import show
from random import randint

show([randint(10, 10001) for i in range(8)], outfile='figure.png', highest_text_only=True)
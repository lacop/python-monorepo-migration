import fastadd
import tqdm


def add(x, y):
    return fastadd.add(x, y)


def tq():
    print("util tqdm", tqdm.__version__)

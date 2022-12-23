from time import time_ns


def main(args):
    i = 0
    while i < 100:
        print(time_ns())
        i += 1


if __name__ == "__main__":
    from sys import argv
    main(argv)
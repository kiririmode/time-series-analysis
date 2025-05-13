import itertools

def main():
    ps = range(0, 2)
    qs = range(0, 2)
    Ps = range(0, 2)
    Qs = range(0, 2)
    for p, q, P, Q in itertools.product(ps, qs, Ps, Qs):
        print("Trying parameters:", p, q, P, Q)


if __name__ == "__main__":
    main()

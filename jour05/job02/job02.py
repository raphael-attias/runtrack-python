h = int(input("hauteur du rectangle : "))
l = int(input("largeur du rectangle : "))


def rectangle(h, l):
    line = "|" + "-" * (l - 2) + "|"
    print(line)

    for i in range(h - 2):
        line = "|" + " " * (l - 2) + "|"
        print(line)

    line = "|" + "-" * (l - 2) + "|"
    print(line)


rectangle(h, l)

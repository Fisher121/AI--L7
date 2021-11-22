class Stare:
    x1 = []
    x2 = []
    y = []
    n = 0  # numarul de epoci
    LR = 0  # rata de invatare

    # calculati rata de eroare

    def __init__(self, filename, n, lr):
        self.n = n
        self.LR = lr

        with open(filename) as file:
            for line in file:
                line = line.replace(" ", ",")
                line = line.replace("\n", "")
                l = line.split(",")
                self.x1.append(l[0])
                self.x2.append(l[1])
                self.y.append(l[2])

class Reader:
    def __init__(self, file):
        with open(file) as f:
            self.content = f.read()

    def depth_readings(self):
        return [int(s) for s in self.content.splitlines()]

    def lines(self):
        return self.content.splitlines()

    def commands(self):
        commands = [l.split() for l in self.lines()]
        return [(c[0], int(c[1])) for c in commands]

    def digits(self):
        return [[int(char) for char in l] for l in self.lines()]

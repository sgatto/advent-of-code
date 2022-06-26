class Submarine:
    def __init__(self):
        self.v_aim_factor = 0
        self.depth = 0
        self.x = 0

    def move(self, commands):
        for command in commands:
            action = command[0]
            amount = command[1]
            if action == "down":
                self.depth += amount
            elif action == "up":
                self.depth -= amount
            else:
                self.x += amount
        return self.x, self.depth

    def advanced_move(self, commands):
        for command in commands:
            action = command[0]
            amount = command[1]
            if action == "down":
                self.v_aim_factor += amount
            elif action == "up":
                self.v_aim_factor -= amount
            else:
                self.x += amount
                self.depth += self.v_aim_factor*amount
        return self.x, self.depth


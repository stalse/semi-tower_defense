for a in range(245):
    if a / 2
        print("(", (a % 2) - 64, ", 340), ", end=' ')


        def move(self):
            x1, y1 = self.path[self.path_pos]
            if self.path_pos + 1 >= len(self.path):
                x2, y2 = (1220, 311)
            else:
                x2, y2 = self.path[self.path_pos + 1]

            move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            self.move_count += 1
            dirn = (x2 - x1, y2 - y1)

            move_x, move_y = ((self.x + dirn[0]) * self.move_count, self.y + dirn[1] * self.move_count)
            self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

            self.x = move_x
            self.y = move_y

            if self.dis >= move_dis:
                self.dis = 0
                self.move_count = 0
                self.path_pos += 1
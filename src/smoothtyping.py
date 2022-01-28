import sys
import time


class smoothtype:
    def __init__(self, string, speed: [int, float] = .1):
        self.string = string
        self.time_per_char = speed
        self.finished = False
        self.char = 0

        for char in self.string:
            if char == " ":
                self.update(space=True)
            else:
                self.update()

    def update(self, space=False):
        sys.stdout.write(self.string[self.char])
        sys.stdout.flush()
        if not space:
            time.sleep(self.time_per_char)
        self.char += 1

import sys
import time


class smoothtype:
    def __init__(self, string, speed: [int, float] = .21, space=True):
        self.string = string
        self.time_per_char = speed
        self.finished = False
        self.char = 0
        self.info = f"Type: {type(self)}" \
                    f'\nString: "{self.string}"' \
                    f"\nTime per Char: {self.time_per_char}" \
                    f"\nCurrent Char: {self.string[self.char]}" \
                    f"\nFinished: {self.finished}" \
        
        for _ in self.string:
            self.update(space)

    def update(self, space):
        char = self.string[self.char]
        sys.stdout.write(char)
        sys.stdout.flush()
        if not space or char != " ":
            time.sleep(self.time_per_char)
        if self.char < len(self.string) - 1:
            self.char += 1
            return
        self.finished = True
        print()

    def __repr__(self):
        return self.info

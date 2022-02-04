import sys
import time as t
import src.errors.error as e

class smoothtype:
    def __init__(self, string, speed: [int, float] = .21, space: bool = True, newline: bool = True,
                 fixed_time: bool = False, time: int = None):
        if speed and (time or fixed_time):
            raise e.Error("You can't use both speed and time.")
        self.string = string
        self.time_per_char = speed
        self.finished = False
        self.char = 0
        self.newline = newline
        self.info = f"Type: {type(self)}" \
                    f'\nString: "{self.string}"' \
                    f"\nTime per Char: {self.time_per_char}" \
                    f"\nCurrent Char: {self.string[self.char]}" \
                    f"\nFinished: {self.finished}"

        for _ in self.string:
            self.update(space)

    def update(self, space):
        char = self.string[self.char]
        sys.stdout.write(char)
        sys.stdout.flush()
        if not space or char != " ":
            t.sleep(self.time_per_char)
        if self.char < len(self.string) - 1:
            self.char += 1
            return
        self.finished = True
        if self.newline:
            print()

    def __repr__(self):
        return self.info

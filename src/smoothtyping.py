import sys
import time as t


class smoothtype:
    """
    docstring for smoothtype
    """
    def __init__(self, string, speed: [int, float] = None, space: bool = True, newline: bool = True,
                 fixed_time: bool = False, time: [int, float] = None):
        if speed and (time or fixed_time):
            raise ValueError("You can't use both time and speed")
        elif speed is None:
            speed = .21
        if not fixed_time and time:
            raise ValueError("You can't use time without fixed_time")
        self.string = string
        self.time_per_char = time / len(self.string) if fixed_time else speed
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

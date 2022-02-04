from src.smoothtyping import smoothtype

# uses the smoothtype class to type "Hello, World!" to the console, character by character
smoothtype("Hello, World!")

# prints "Hello, World!" to the console, character by character, with a delay of 0.5 seconds between each character
smoothtype("Hello, World!", speed=.5)

# by default, the smoothtype class will print the string to the console skipping spaces, but you can change this
# behavior with the parameter "space=False"
smoothtype("Hello, World!", space=False)

# demonstrates the repr of smoothtype, giving valuable information about the object
typing = smoothtype("Hello, World!", speed=.25)
# prints out the repr of the object
print(typing)

# uses the parameter newline to specify if a new line is added after the string is printed
smoothtype("Hello, World!", speed=.25, newline=False)
# forced new line
print()

# this example uses the parameter "fixed_time" to choose if you want the time to be fixed and the time between
# characters dynamically calculated based off the time parameter. Do note that speed and cannot be provided if
# fixed_time is set to True, and speed and time cannot be used.
smoothtype("Hello, World!", fixed_time=True, time=3)

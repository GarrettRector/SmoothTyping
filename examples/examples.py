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
print(typing)

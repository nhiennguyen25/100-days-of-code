print("hello")
print(len("hello"))

# making our own functions
    # step 1: define the function with def
    # step 2: give the function a name
    # step 3: a set of parentheses and colon
    # step 4: put the lines of code(indented)
    # step 5: to call the function, specify the function name + ()

def my_function():
    print("hello")
    print("bye")
my_function()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear:
        turn_right()
        move()
    elif wall_on_right():
        move()
    elif wall_in_front and wall_on_right():
        turn_left()
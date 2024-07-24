import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    bob = turtle.Turtle()
    # This code sets our shape to a turtle
    bob.shape()
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    bob.speed(10000000)
    # Set your turtle's color using .color('green')
    bob.color('blue')
    # Use a loop to repeat a the code below 50 times
    for i in range (50):
        # Set the turtle color to a random color
        bob.color('red')
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        bob.forward(7*i)
        # Turn the turtle (360/7) degrees to the right
        bob.right(360/6)
        # Change the turtle width to 'i' (the loop variable)
        bob.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    bob.color('blue')
    bob.goto(200, 300)
    for i in range (75):
        # Set the turtle color to a random color
        bob.color('yellow')
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        bob.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        bob.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        bob.width(i)
    bob.color('blue')
    bob.goto(100, 100)
    for i in range(25):
        # Set the turtle color to a random color
        bob.color('purple')
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        bob.forward(3 * i)
        # Turn the turtle (360/7) degrees to the right
        bob.right(360 / 10)
        # Change the turtle width to 'i' (the loop variable)
        bob.width(i)
        bob.color('blue')
        bob.goto(-200, 100)
        for i in range(100):
            # Set the turtle color to a random color
            bob.color('green')
            # Move the turtle (5*i) pixels. 'i' is the loop variable
            bob.forward(2 * i)
            # Turn the turtle (360/7) degrees to the right
            bob.right(360 / 8)
            # Change the turtle width to 'i' (the loop variable)
            bob.width(i)
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

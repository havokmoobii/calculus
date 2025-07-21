from sympy import symbols
from sympy.solvers import solve

def main():
    # Hole in the graph

    x = 2
    h = 0.00001

    y_right = (3*((x+h)-2))/((x+h)-2)
    y_left = (3*((x-h)-2))/((x-h)-2)

    print(f"y_right = {y_right}")
    print(f"y_left = {y_left}")

    if round(y_right) != round(y_left):
        print(f"Limit does not exist at x = {x}")

    # Asymptotes    

    x = symbols('x')

    # Put the equation here
    eq = x**2 - 4

    # solve() sets the equation equal to zero
    print(f"x = {solve(eq, x)}")

    x = 2
    h = 0.00001

    y_right = (3*((x+h)**2))/((x+h)**2 - 4)
    y_left = (3*((x-h)**2))/((x-h)**2 - 4)

    print(f"y_right = {y_right}")
    print(f"y_left = {y_left}")

    if round(y_right) != round(y_left):
        print(f"Limit does not exist at x = {x}")

    x = -2
    h = 0.00001

    y_right = (3*((x+h)**2))/((x+h)**2 - 4)
    y_left = (3*((x-h)**2))/((x-h)**2 - 4)

    print(f"y_right = {y_right}")
    print(f"y_left = {y_left}")

    if round(y_right) != round(y_left):
        print(f"Limit does not exist at x = {x}")

    x = 2
    h = 0.00001

    y_right = 3*(x+h)
    y_left = 3*(x-h)

    print(f"y_right = {y_right}")
    print(f"y_left = {y_left}")

    if round(y_right) != round(y_left):
        print(f"Limit does not exist at x = {x}")
    else:
        print(f"Limit at x = {x} is {round(y_right)}")



if __name__ == "__main__":
    main()

# Akhilesh Mistry 2021

import math as m
import numpy
from matplotlib import pyplot

# Functions for calculating velocity components
def usourceVelocity(x, y):
    """Function which calculates u and v components of velocity for the source flow type"""
    
    u = x/((2*m.pi) * (pow(x,2) + pow(y,2)) + 0.000001)
    # v = y/((m.pi) * (pow(x,2) + pow(y,2)) + 0.000001)

    return u

def vsourceVelocity(x, y):
    """Function which calculates u and v components of velocity for the source flow type"""
    
    # u = x/((m.pi) * (pow(x,2) + pow(y,2)) + 0.000001),
    v = y/((2*m.pi) * (pow(x,2) + pow(y,2)) + 0.000001)

    return v

def uvortexVelocity(x, y):
    """Function which calculates u and v components of velocity for the vortex flow type"""

    u = y/((2*m.pi) * (pow(x,2) + pow(y,2)) + 0.000001)
    # 'v' : (-x)/((m.pi) * (pow(x,2) + pow(y,2)) + 0.000001)

    return u

def vvortexVelocity(x, y):
    """Function which calculates u and v components of velocity for the vortex flow type"""

    # 'u' : y/((m.pi) * (pow(x,2) + pow(y,2)) + 0.000001),
    v = (-x)/((2*m.pi) * (pow(x,2) + pow(y,2)) + 0.000001)

    return v

print("█▀▀ █░░ █▀█ █░█░█\n█▀░ █▄▄ █▄█ ▀▄▀▄▀   By Akhilesh Mistry\n\n  █░█ █ █▀ █░█ ▄▀█ █░░ █ █▀ ▄▀█ ▀█▀ █ █▀█ █▄░█\n" +
"  ▀▄▀ █ ▄█ █▄█ █▀█ █▄▄ █ ▄█ █▀█ ░█░ █ █▄█ █░▀█\n\n")


# Request number of flow elements to use
while True:
    print("Enter either '1' or '2' for the number of flow elements to use.")
    # Check for incorrect inputs.
    try:
        num_elements = int(input("Number of flow elements: "))
    except ValueError:
        print("Please only enter integers.\n")
        continue

    # Break while loop if input is compatible
    if num_elements == 1 or num_elements == 2:
        break
    else:
        print("Please enter either '1' or '2'.\n")

# Request type of flow for each element
for i in range(num_elements):
    # Initialise flag
    active = True

    # While loop runs until a valid input is entered
    while active:
        print("Specify a flow type, enter \n    '1' for Freestream\n    '2' for Source\n    '3' for Vortex")
        # Try-except statement to catch non-integer character inputs
        try:
            flow_type = int(input(f"Flow type {i+1}:"))
        except ValueError:
            print("\nPlease only enter integers.\n")
            continue

        # Check that flow type is valid
        if flow_type == 1 or flow_type == 2 or flow_type == 3:
            # Record first flow type
            if i == 0:
                flow_type_1 = flow_type
                active = False
            else:
                # Check that the 2 flow types are not the same
                if flow_type != flow_type_1:
                    flow_type_2 = flow_type 
                    active = False
                else:
                    print("\nFlow types must be different!\n")   
        else:
            print("\nPlease enter either '1', '2' or '3'.\n")
            continue


N = 101                                # number of points in each direction
x_start, x_end = -1.0, 1.0            # boundaries in the x-direction
y_start, y_end = -1.0, 1.0            # boundaries in the y-direction
x = numpy.linspace(x_start, x_end, N)    # creates a 1D-array with the x-coordinates
y = numpy.linspace(y_start, y_end, N)

X, Y = numpy.meshgrid(x, y) 

# Configure figure
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
pyplot.figure(figsize=(width, height))
pyplot.xlabel('x', fontsize=16)
pyplot.ylabel('y', fontsize=16)
pyplot.xlim(x_start, x_end)
pyplot.ylim(y_start, y_end)

# Plot mesh grid
# pyplot.scatter(X, Y, s=5, color='#CD2305', marker='o')

# Plot point of flow type (if applicable)
pyplot.scatter(0, 0,
               color='#CD2305', s=50, marker='o');


# Calculating velocity components 

if flow_type_1 == 1:
    u = X*0 + 1
    v = Y*0
elif flow_type_1 == 2:
    u = usourceVelocity(X, Y)
    v = vsourceVelocity(X, Y)
elif flow_type_1 == 3:
    u = uvortexVelocity(X, Y)
    v = vvortexVelocity(X, Y)

# Only set commands for second flowtype if they are to be used
if num_elements != 1:
    if flow_type_2 == 1:
        u = u + X*0 + 1
        v = v + Y*0
    elif flow_type_2 == 2:
        u = u + usourceVelocity(X, Y)
        v = v + vsourceVelocity(X, Y)
    elif flow_type_2 == 3:
        u = u + uvortexVelocity(X, Y)
        v = v + vvortexVelocity(X, Y)

# Plot streamlines
pyplot.streamplot(X, Y, u, v,
                  density=3, linewidth=1, arrowsize=1, arrowstyle='->')
pyplot.show()
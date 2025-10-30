# Cole Levi 100922405
# This document has two functions which calculate the volume and area of a cylinder. For Test 1 of TPRG 2


import math


def volume_cylinder(diameter, height):
    if height < 0:
        raise ValueError("Height cannot be negative")
    return math.pi * pow((diameter/2), 2) * height

def area_cylinder(diameter, height):
    if height < 0:
        raise ValueError("Height cannot be negative")
    return (2 * math.pi * (diameter / 2) * height) + (2 * math.pi * pow((diameter / 2), 2))




if __name__ == "__main__":
    try:
        
        tallness = float(input("please enter the height: "))
    
        radius_times_two = float(input("please enter the diameter: "))
    
        print(round(volume_cylinder(radius_times_two, tallness), 4))
        print(round(area_cylinder(radius_times_two, tallness), 4))
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully...")
    except ValueError as ve:
        print(f"Error: {ve}")
        
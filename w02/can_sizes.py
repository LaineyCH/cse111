"""
Calculate and display the storage efficiency of a known set of metal cans
functions:
main
compute_volume
compute_surface_area

Core Requirements:
Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.

volume = π * radius2 * height
surface_area = 2π * radius * (radius + height)
storage_efficiency = volume / surface_area
cost_efficiency = volume / cost
"""
# Import the standard math module so that math.pi can be used in this program.
import math

def main():
    # list of cans, givin as: name, radius (cm), height (cm), cost per can (USD)
    can_library = [
    {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
    {"name": "#1 Tall",	"radius": 7.78, "height": 11.91, "cost": 0.43},
    {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
    {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
    {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
    {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
    {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
    {"name": "#8Z Short", "radius": 6.83, "height": 7.62, "cost": 0.26},
    {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
    {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
    {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
    {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42}
    ]

    # variables to store the best can stirage and cost efficiencies along with the names of the best cans
    best_storage_efficiency = 0
    best_storage_can = ""
    best_cost_efficiency = 0
    best_cost_can = ""
    
    # loop through th ecan library, for each can, calculate the storage effiency and cost efficiancy and print to screen.
    # check whether the can is best in either category
    for can in can_library:
        name = can["name"]
        radius = can["radius"]
        height = can["height"]
        cost = can["cost"]
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)
        print(f"{name} Storage Efficiency: {storage_efficiency: .2f}  Cost Efficiency: {cost_efficiency: .0f}")

        # compare can efficiencies to current best, if it is better, store value and name
        if storage_efficiency > best_storage_efficiency:
            best_storage_can = name
            best_storage_efficiency = storage_efficiency
        if cost_efficiency > best_cost_efficiency:
            best_cost_can = name
            best_cost_efficiency = cost_efficiency

    # print the best cans in term os storage and cost efficiency
    print(f"Best Can for Storage Efficiency: {best_storage_can}, {best_storage_efficiency: .2f}")
    print(f"Best Can for Cost Efficiency: {best_cost_can}, {best_cost_efficiency: .0f}")

def compute_volume(radius, height):
    """calculates the volume of a cylinder
        Parameters:
            radius: the radius of the cylinder
            height: the height of the cylinder
        Return: volume
    """
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    """calculates the surface area of a cylinder
        Parameters:
            radius: the radius of the cylinder
            height: the height of the cylinder
        Return: surface area
    """
    surface_area = 2*math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    """calculates the storage efficiency of a metal can - the volume to surface area ratio
        Parameters:
            radius: the radius of the can
            height: the height of the can
        Return: storage efficiency
    """
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
    """calculates the cost efficiency of a metal can - the volume to cost ratio
        Parameters:
            radius: the radius of the cylinder
            height: the height of the cylinder
            cost: the cost of each can
        Return: cost efficiency
    """
    volume = compute_volume(radius, height)
    cost_efficiency = volume / cost
    return cost_efficiency

# run the program
main()
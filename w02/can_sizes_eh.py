"""Calculate and display the storage efficiancy of a known set of metal cans"""
# Import the standard math module so that
# math.pi can be used in this program.
import math

def main():
    # list of can dictionaries, giving: name, radius (cm), height (cm), cost per can (USD)
    can_library = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
        {"name": "#1 Tall",	"radius": 7.78, "height": 11.91, "cost": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42}
    ]

    # set variables for the best cans efficiencies and names
    top_storage_effeciency = 0
    top_storage_effeciency_can = ""
    top_cost_effeciency = 0
    top_cost_effeciency_can = ""

    # loop through list of cans, find  each can's storage and cost efficiency, and print, along with name.
    for can in can_library:
        name = can["name"]
        # Core Requirements:
        # volume = compute_volume(can["radius"], can["height"])
        # surface_area = compute_surface_area(can["radius"], can["height"])
        # print(f"{name} - Volume:{volume: .2f} Surface Area:{surface_area: .2f}")
        storage_efficiency = compute_storage_efficiency(can["radius"], can["height"])
        cost_efficiency = compute_cost_efficiency(can["radius"], can["height"], can["cost"])
        print(f"{name} - Storage Efficiency:{storage_efficiency: .2f} Cost Efficiency:{cost_efficiency: .2f}")
        print()

        # find and store the can with the greatest storage efficency
        if storage_efficiency > top_storage_effeciency:
            top_storage_effeciency = storage_efficiency
            top_storage_effeciency_can = name

        # find and store the can with the greatest storage efficency
        if cost_efficiency > top_cost_effeciency:
            top_cost_effeciency = cost_efficiency
            top_cost_effeciency_can = name

    # print the top cans for storagr efficiency and cost efficiency
    print(f"Can with best storage efficiancy: {top_storage_effeciency_can}")
    print(f"Can with best cost efficiancy: {top_cost_effeciency_can}")
    print()

def compute_volume(radius, height):
    """
    calculate the volume of a cylinder
    Parameters:
        radius: the radius of the cylinder in cm
        height: the height of the cylinder in cm
    Return: volume: the volume of the cylinder
    """
    # calculate and return the volume of the cylinder
    volume =  math.pi * (radius**2) * height
    return volume

def compute_surface_area(radius, height):
    """
    calculate the surface area of a cylinder
    Parameters:
        radius: the radius of the cylinder in cm
        height: the height of the cylinder in cm
    Return: volume: the surface area of the cylinder in cm**2
    """
    # calculate and return the surface area of the cylinder
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    """
    calculate the storage efficiency of a storage can
    Parameters:
        radius: the radius of the can
        height: the height of the can
    Return: volume: the storage efficiency of the can in cm**3
    """
    # get the volume and surface area of the can
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # calculate and return the storage efficiency
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
    """
    calculate the cost efficiency of a storage can
    Parameters:
        radius: the radius of the can in cm
        height: the height of the can in cm
        cost: the cost per can in USD
    Return: volume: the cost efficiency of the can
    """
    # get the volume of the can
    volume = compute_volume(radius, height)
    # calculate and return the cost efficiency
    cost_efficiency = volume / cost
    return cost_efficiency

main()
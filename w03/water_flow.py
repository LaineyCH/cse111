"""
A program that could help an engineer design a water distribution system.
"""
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    """
    calculates and returns the height of a column of water from a tower height and a tank wall height
    
    Parameters
        tower_height: the height of the tank
        tank_height: the height of the tank wall
    Return: the water column height, rounded to one decimal place
    """
    water_height = tower_height + (3 * tank_height / 4)
    return water_height

def pressure_gain_from_water_height(height):
    """
    calculates and returns the pressure caused by Earth's gravity pulling on the water stored in an elevated tank
    
    Parameters
        height: the height of the water column in  meters
    Return: the pressure in kilopascals
    """
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    calculates and returns the water pressure lost because of the friction between the water and
    the walls of a pipe that it flows through
    
    Parameters
        pipe_diameter: the diameter of the pipe in meters
        pipe_length: the length of the pipe in meters
        friction_factor: the pipe's friction factor
        fluid_velocity: the velocity of the water flowing through the pipe in meters / second
    Return: the lost pressure in kilopascals
    """
    pressure = (-1 * friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline
    
    Parameters
        fluid_velocity: the velocity of the water flowing through the pipe in meters / second
        quantity_fittings: the quantity of fittings
    Return: the lost pressure in kilopascals
    """
    pressure = (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    calculates and returns the Reynolds number for a pipe with water flowing through it
    (Reynolds number is a unitless ratio of the inertial and viscous forces in a fluid that is 
    useful for predicting fluid flow in different situations)
    
    Parameters
        hydraulic_diameter: the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe's inner diameter.
        fluid_velocity: the velocity of the water flowing through the pipe in meters / second
    Return: the Reynolds number
    """
    reynolds_number = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return reynolds_number


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter
    
    Parameters
        larger_diameter: the diameter of the larger pipe in meters
        fluid_velocity: the velocity of the water flowing through the pipe in meters / second
        reynolds_number: the Reynolds number that corresponds to the pipe with the larger diameter
        smaller_diameter: the diameter of the smaller pipe in meters
    Return: the lost pressure in kilopascals
    """
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter/smaller_diameter)**4) - 1)
    pressure = (-1 * k * WATER_DENSITY * (fluid_velocity**2)) / 2000
    return pressure


def convert_kPa_to_psi(kPa):
    """
    converts kPa to psi

    Parameters
        kPa: the pressure in kilopascals
    Return: the pressure in psi
    """
    psi = kPa * 0.1450377
    return psi


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_psi = convert_kPa_to_psi(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals / {pressure_psi:.1f} psi")
if __name__ == "__main__":
    main()
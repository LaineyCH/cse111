def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    p = 998.2000000
    lost_pressure=(-0.04 * p * fluid_velocity**2 * quantity_fittings)/2000
    return lost_pressure

def pressure_loss_from_fittings2(fluid_velocity, quantity_fittings):
    """
    calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline
    
    Parameters
        fluid_velocity: the velocity of the water flowing through the pipe in meters / second
        quantity_fittings: the quantity of fittings
    Return: the lost pressure in kilopascals
    """
    pressure = (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure
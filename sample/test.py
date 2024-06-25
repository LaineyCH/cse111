import math
def main():
# Name	Radius
# (centimeters)	Height
# (centimeters)	Cost per Can
# (U.S. dollars)
# #1 Picnic	6.83	10.16	$0.28
# #1 Tall	7.78	11.91	$0.43
# #2	   8.73	   11.59	    $0.45
# #2.5	10.32	11.91	$0.61
# #3 Cylinder	10.79	17.78	$0.86
# #5	13.02	14.29	$0.83
# #6Z	5.40	8.89	$0.22
# #8Z short	6.83	7.62	$0.26
# #10	15.72	17.78	$1.53
# #211	6.83	12.38	$0.34
# #300	7.62	11.27	$0.38
# #303	8.10	11.11	$0.42
    cans = [
        ("#1 Picnic", 6.83, 10.16, 0.28),
        ("#1 Tall", 7.78, 11.91, 0.43),
        ("#2", 8.73, 11.59, 0.45),
        ("#2.5", 10.32, 11.91, 0.61),
        ("#3 Cylinder", 10.79, 17.78, 0.86),
        ("#5", 13.02, 14.29, 0.83),
        ("#6Z", 5.40, 8.89, 0.22),
        ("#8Z short", 6.83, 7.62, 0.26),
        ("#10", 15.72, 17.78, 1.53),
        ("#211", 6.83, 12.38, 0.34),
        ("#300", 7.62, 11.27, 0.38),
        ("#303", 8.10, 11.11, 0.42)
    ]
    best_can_efficiency = 0
    best_cost_efficiency = 999999
    name_best_can_efficiency =''
    name_best_cost_efficiency =''

    for can in cans:
        name, radius, height, cost = can
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        cost_efficiency = compute_cost_efficiency(volume, cost)
        can_efficiency = volume / surface_area
        print(f'{name} volume = {volume:.2f} surface area = {surface_area:.2f} can efficiency = {can_efficiency:.2f} cost efficiency = ${cost_efficiency:.2f}')

        if can_efficiency > best_can_efficiency:
            best_can_efficiency = can_efficiency
            name_best_can_efficiency = name
        
        if cost_efficiency < best_cost_efficiency:
            best_cost_efficiency = cost_efficiency
            name_best_cost_efficiency = name

    print(f'Can {name_best_can_efficiency} has the best can efficiency at: {best_can_efficiency:.2f}')
    print(f'Can {name_best_cost_efficiency} has the best cost efficiency at: ${best_cost_efficiency:.2f}')
    

def compute_volume(radius, height):
    volume = math.pi * (radius **2) * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2*math.pi * radius * (radius + height)
    return surface_area

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()

# def compute_storage_efficiency (volume, surface_area):

    
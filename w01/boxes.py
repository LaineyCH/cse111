import math

nitems = int(input("Number of manufactured items: "))
perbox = int(input("Number of items to be packed in each box: "))

nboxes = math.ceil(nitems / perbox)

print(f"You will need {nboxes} boxes")
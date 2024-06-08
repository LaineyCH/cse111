"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = input("What is your age? ")

high = (220 - int(age)) * 0.85
low = (220 - int(age)) * 0.65

print(f"When you physically exercise to strengthen your heart, you should maintain your heart rate")
print(f"within the range of {low:.0f} to {high:.0f} for at least 20 minutes.")
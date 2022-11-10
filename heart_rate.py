print()

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input('Please enter your age: '))
max_heart_rate = 220 - age

min_ex_rate = max_heart_rate * .65
max_ex_rate = max_heart_rate * .85

print('\nWhen you exercise to strenthen your heart, you should keep')
print(f'your heart rate between {min_ex_rate:.0f} and {max_ex_rate:.0f} beats per minute.')
print(f'If your heart rate ever exceeds {max_heart_rate}, please seek medical attention.')

print()
# 1.) Create a dictionary with key value pairs of month and
# average temperature.

# Aarhus, Denmark: Annual Weather Averages

weather = {'January': 36, 'February': 36, 'March': 39, 'April': 45, 'May': 54, 'June': 57, 'July': 61, 'August': 63, 'September': 57, 'October': 48,
           'November': 41, 'December': 37}

# 2.) Declare a global value to hold the average temperature

average = 0

# 3.) Create an empty dictionary to store information on
# the warmest month of the year

warmest = dict()

# You will create two functions:

# The first function will calculate the
# average temp for a country, it should accept a
# dictionary parameter


def ave_temp(d):
    global average
    for ave in d:
        average += d[ave]
    av = average / len(weather)
    print("The average weather in Aarhus Denmark today is: " + str(av))

# Your second function will create a new dictionary
# that uses the global average variable to compare
# with each month, months with temperatures higher than
# average will be added to the new dictionary.
# Print the new dictionary


def warmth(x):
    global average
    av = average / len(weather)
    for temp in x:
        if x[temp] > average:
            warmest[av] = x[temp]
    print warmest


# Make sure to call each function and
# pass your dictionary to them.

ave_temp(weather)
warmth(weather)

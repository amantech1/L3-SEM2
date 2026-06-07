# Program to create a function that searches for a city in a list and returns its index if found.

# Function to search city
def search(cities, city):
    if city in cities:
        return cities.index(city)
    else:
        return "City not found."

# Initializing list of cities
cities = ["Kathmandu", "Pokhara", "Biratnagar", "Lalitpur"]

print('List of Cities:', cities, '\n')

# Accept city name from user
city_name = input("Enter city to search: ")

# Function Call
result = search(cities, city_name)

# Display Results
print('Index of', city_name, 'City is', result)
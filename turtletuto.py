import requests
import turtle

# Get ISS position from API
url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)
data = response.json()

# Extract coordinates
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])

print("Latitude:", latitude)
print("Longitude:", longitude)

# Turtle setup
screen = turtle.Screen()
screen.setup(1000, 500)

t = turtle.Turtle()
t.shape("circle")

# Convert longitude/latitude to screen coordinates
x = longitude * 4
y = latitude * 2

# Move turtle to the ISS position
t.penup()
t.goto(x, y)
t.pendown()

t.dot(10)

turtle.done()
import requests
import turtle

url = "https://api.wheretheiss.at/v1/satellites/25544"

response = requests.get(url, timeout=7)
data = response.json()

latitude = float(data['latitude'])
longitude = float(data['longitude'])
altitude = float(data['altitude'])      # in km
velocity = float(data['velocity'])      # in km/h

print("Latitude:", latitude)
print("Longitude:", longitude)
print("Altitude:", altitude, "km")
print("Velocity:", velocity, "km/h")

screen = turtle.Screen()
screen.setup(1000, 500)

e = turtle.Turtle()
t = turtle.Turtle()
t.shape("circle")
e.shape("circle")

a = 0
b = 0
e.penup()
e.goto(a, b)
e.pendown()
e.dot(40)

x = longitude * 4
y = latitude * 2
t.color("blue")
t.penup()
t.goto(x, y)
t.pendown()
t.dot(10)

# Display velocity and altitude as text on screen
info = turtle.Turtle()
info.hideturtle()
info.penup()
info.goto(-480, 220)
info.write(
    f"Altitude: {altitude:.1f} km   |   Velocity: {velocity:.1f} km/h",
    font=("Arial", 12, "normal")
)

turtle.done()
import requests 
import turtle 
url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url, timeout = 7)
data = response.json()
latitude = float(data['iss_position']['latitude'])
longitude = float(data['iss_position']['longitude'])
print("Latitude",latitude)
print("Longitude",longitude)

screen = turtle.Screen()
screen.setup(1000,500)
e=turtle.Turtle()
t=turtle.Turtle()
t.shape("circle")
e.shape("circle")
a=0
b=0
e.penup()
e.goto(a,b)
e.pendown()
e.dot(40)

x=longitude*4
y=latitude*2
e.color("blue")
t.penup()
t.goto(x,y)
t.pendown()
t.dot(10)
turtle.done()



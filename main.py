from tkinter import *
import math
class Point:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return str(self.x) + "," + str(self.y) + " angle: " + str(self.angle)

XPOS = 0
YPOS = 1
POLAR_ANGLE = 2
window = Tk()
points = []
canvas = Canvas(window, bg='white', width=800, height=800)

def drawButtons():
    create_hull.pack()
    clear_hull.pack()
def drawCircleAtMouseClick(event):
    print ("clicked at", event.x, 800 - event.y)
    canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, outline='black', fill='black')
    canvas.create_text(event.x + 10, event.y + 20, text=str(event.x) + ", " + str(event.y), fill="black")
    points.append(Point(event.x, event.y, 0))

canvas.bind("<Button-1>", drawCircleAtMouseClick)

def findLeftmostLowPoint(pointA, pointB):
    two_lowest_points = [pointA, pointB]
    point_smallest_x = two_lowest_points[0]
    for j in two_lowest_points:
        if (j.x < point_smallest_x.x):
            pointB = j
        else:
            pointB = point_smallest_x
    return pointB

def sortPointsByAngle(points, lowest_point):
    lowest_point_theta = math.atan2(lowest_point.x, lowest_point.y)
    for i in range(0, len(points)):
        if (i != lowest_point):
            second_theta = math.atan2(points[i].x, points[i].y)
            r = (second_theta - lowest_point_theta) * (180 / math.pi)
            if (r < 0):
                r % 360
            points[i].angle = r
    points.sort(key=lambda x: x.angle)
    return points
    # return 0

def findLowestPoint(list_of_points):
    point_lowest_y = list_of_points[0]
    for i in list_of_points:
        if (i.y < point_lowest_y.y):
            point_lowest_y = i
        elif (i.y == point_lowest_y.y): # If there are two points with the same y-coordinate, then choose the left most point
            point_lowest_y = findLeftmostLowPoint(i, point_lowest_y)
    return point_lowest_y

def createHull():
    # Code to find the Convex Hull of the points goes here
    lowest_point = findLowestPoint(points)
    # print(lowest_point.x, lowest_point.y)
    sorted_points_by_angle = sortPointsByAngle(points, lowest_point)
    for i in sorted_points_by_angle:
        print(i)
   

def clearHull():
    canvas.delete('all')
    points.clear()
    drawButtons()

create_hull = Button(window, text="Generate Hull", command=createHull)
clear_hull = Button(window, text="Clear Hull", command=clearHull)
create_hull.pack()
clear_hull.pack()

canvas.pack(fill=BOTH, expand=True)
window.maxsize(800, 800)
window.mainloop()
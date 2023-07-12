from tkinter import *
XPOS = 0
YPOS = 1
window = Tk()
label = Label(text="First tkinter line")
label.place(x=100, y=200) 
points = []
canvas = Canvas(window, bg='white')

def drawButtons():
    create_hull.pack()
    clear_hull.pack()
# window.geometry("400x400")
def drawCircleAtMouseClick(event):
    # print ("clicked at", event.x, event.y)
    canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, outline='black', fill='black')
    points.append((event.x, event.y))

canvas.bind("<Button-1>", drawCircleAtMouseClick)

def findLeftmostLowPoint(pointA, pointB):
    two_lowest_points = [pointA, pointB]
    point_smallest_x = two_lowest_points[0]
    for j in two_lowest_points:
        if (j[XPOS] < point_smallest_x[XPOS]):
            pointB = j
        else:
            pointB = point_smallest_x
    return pointB

def findLowestPoint(list_of_points):
    point_lowest_y = list_of_points[0]
    for i in list_of_points:
        if (i[YPOS] < point_lowest_y[YPOS]):
            point_lowest_y = i
        elif (i[YPOS] == point_lowest_y[YPOS]): # If there are two points with the same y-coordinate, then choose the left most point
            point_lowest_y = findLeftmostLowPoint(i, point_lowest_y)
    return point_lowest_y

def createHull():
    # Code to find the Convex Hull of the points goes here
    lowest_point = findLowestPoint(points)
    print(lowest_point)

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
from tkinter import *
from .geometry_generator import *
# from .geometrical_solver import *


class MicroCADApp:
#initialize
    def __init__(self, root):
        work_area = Canvas(root, width=1000, height=700)
        main_menu = Menu(root)
        root.config(menu=main_menu)
        
        tool_menu = Menu(main_menu, tearoff=0)
        tool_menu.add_command(label="select", command=self.selectTool)
        tool_menu.add_command(label="line", command=self.lineTool)
        tool_menu.add_command(label="point", command=self.pointTool)

        # geometrical costraint toolbox
        solver_menu = Menu(main_menu, tearoff=0)
        solver_menu.add_command(label="1")
        solver_menu.add_command(label="2")
        solver_menu.add_command(label="3")
        solver_menu.add_command(label="4")
        solver_menu.add_command(label="5")
        solver_menu.add_command(label="6")
        solver_menu.add_command(label="7")
        solver_menu.add_command(label="8")

        main_menu.add_cascade(label="drawing tool", menu=tool_menu)
        main_menu.add_cascade(label="graphical constrant", menu=solver_menu)

        work_area.pack()
        # work_area.bind("<Motion>", self.motion)
        work_area.bind("<ButtonPress-1>", self.left_button_down)
        work_area.bind("<ButtonRelease-1>", self.left_button_up)

#define vars
    drawing_tool = "line"
    left_button_pressed = 0

    x_pos, y_pos = None, None
    x1, y1, x2, y2  = None, None, None, None

#mouse events
    #catch up
    def left_button_up(self, event = None):
        self.left_button = 0

        self.x_pos = None
        self.y_pos = None

        self.x2 = event.x
        self.y2 = event.y

        if self.drawing_tool == "line":
            self.drawLine(event)
        if self.drawing_tool == "point":
            self.setPoint(event)
        if self.drawing_tool == "select":
            self.selectObject(event)
    #catch down
    def left_button_down(self, event = None):
        self.left_button = 1

        self.x1 = event.x
        self.y1 = event.y
    
    #catch move
        # def motion(self, event = None):
        #     if self.left_button == "down":
        #         if self.x_pos is not None and self.y_pos is not None:
        #             event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth = TRUE)
        #         self.x_pos = event.x
        #         self.y_pos = event.y
#menu
    #set select as tool
    def selectTool(self):
        self.drawing_tool = "select"
    #set line as drawing tool
    def lineTool(self):
        self.drawing_tool = "line"
    #set Point as drawing tool
    def pointTool(self):
        self.drawing_tool = "point" 
#drawing
    #point
    def setPoint(self, event = None):
        # if self.x_pos is not None and self.y_pos is not None:
        event.widget.create_oval(self.x1, self.y1, self.x1, self.y1, width=2, fill="green")
    #line
    def drawLine(self, event = None):
        if None not in (self.x1, self.y1, self.x2, self.y2):
            event.widget.create_oval(self.x1, self.y1, self.x1, self.y1, width=2, fill="blue")
            event.widget.create_line(self.x1, self.y1, self.x2, self.y2, smooth=TRUE, fill="blue")
            event.widget.create_oval(self.x2, self.y2, self.x2, self.y2, width=2, fill="blue")
    #select nearest object object
    def selectObject(self):
        ...

if __name__ == "__main__":
    root = Tk()
    app = MicroCADApp(root)
    object = Object()
    root.mainloop()

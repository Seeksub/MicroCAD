from tkinter import *
from geometry_generator import *
import math

class MicroCADApp:
#initialize
    def __init__(self, root):

        work_area = Canvas(root, width=1000, height=700)
        main_menu = Menu(root)
        root.config(menu=main_menu)

        #tools toolbox
        tool_menu = Menu(main_menu, tearoff=0)
        tool_menu.add_command(label="select", command=self.selectTool)
        tool_menu.add_command(label="line", command=self.lineTool)
        tool_menu.add_command(label="point", command=self.pointTool)

        # geometrical constraint toolbox
        solver_menu = Menu(main_menu, tearoff=0)
        solver_menu.add_command(label="1 - fixed point", command=self.constraintTool)
        solver_menu.add_command(label="2 - fixed distance")
        solver_menu.add_command(label="3 - parallelism")
        solver_menu.add_command(label="4 - perpendicularity")
        solver_menu.add_command(label="5 - fixed angle")
        solver_menu.add_command(label="6 - horizontal")
        solver_menu.add_command(label="7 - vertical")
        solver_menu.add_command(label="8 - attaching point to the line")

        # undobox
        undo_box = Menu(main_menu, tearoff=0)
        undo_box.add_command(label="Clear workspace", command=self.deleteTool)
        undo_box.add_command(label="Unset boundary", command=self.unsetTool)
        #toolbox
        main_menu.add_cascade(label="drawing tool", menu=tool_menu)
        main_menu.add_cascade(label="graphical constraint", menu=solver_menu)
        main_menu.add_cascade(label="reset", menu=undo_box)
        # self.popup_menu = Menu(main_menu, tearoff=0)
        # self.popup_menu.add_command(label="delete", command=self.deleteSelected)
        # popup_menu.add_command(label="delete all", command=self.deleteAll)
        # work_area.bind("<Motion>", self.motion)
        # work_area.bind("<ButtonPress-3", self.popup)
        work_area.bind("<ButtonPress-1>", self.left_button_down)
        work_area.bind("<ButtonRelease-1>", self.left_button_up)
        work_area.pack()
#define vars
    drawing_tool = "line"
    left_button_pressed = 0
    constraint_tool = None
    x_pos, y_pos = None, None
    x1, y1, x2, y2 = None, None, None, None
    points = Point()
    lines = Line()
#mouse events
    #catch up
    def left_button_up(self, event = None):
        self.left_button = 0

        self.x_pos = None
        self.y_pos = None

        self.line = None
        self.point = None
        self.tag = str(event.x)+"+"+str(event.y)
        self.x2 = event.x
        self.y2 = event.y

        if self.constraint_tool is None:
            if self.drawing_tool == "line":
                self.drawLine(event)
            if self.drawing_tool == "point":
                self.setPoint(event)
            if self.drawing_tool == "select":
                self.selectObject(event)
            if self.drawing_tool == "delete":
                self.deleteAll(event)
            if self.drawing_tool == "unset":
                ...
        if self.constraint_tool == 1:
            self.setGeometryCoinstaraint(event)
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
    #delete
    # def popup(self, event):
    #     try:
    #         self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
    #     finally:
    #         self.popup_menu.grab_release()
    #
    # def deleteSelected(self, event):
    #     obj = event.widget.find_closest(event.x, event.y, halo=None, start=None)
    #     if self.lines.isEventObject(obj):
    #         self.lines.deleteLine(obj)
    #     if self.points.isEventObject(obj):
    #         self.points.deletePoint(obj)

    def deleteAll(self, event):
        lids = self.lines.getSetOfLines()
        pids = self.points.getSetOfPoints()
        for l in lids:
            event.widget.delete(l[0])
            event.widget.delete(l[5])
            event.widget.delete(l[6])
            self.lines.deleteLine(l[0])
        for p in pids:
            event.widget.delete(p[0])
            self.points.deletePoint(p[0])

#menu
    #Main menu
    #set select as tool
    def selectTool(self):
        self.drawing_tool = "select"

    #set line as drawing tool
    def lineTool(self):
        self.drawing_tool = "line"

    #set Point as drawing tool
    def pointTool(self):
        self.drawing_tool = "point"

    #Constraint menu
    def constraintTool(self):
        if self.constraint_tool == 1:
            self.resetConstraintTool()
        else:
            self.constraint_tool = 1

    def resetConstraintTool(self):
        self.constraint_tool = None

    #undomenu
    def deleteTool(self):
        self.drawing_tool = "delete"

    def unsetTool(self):
        self.drawing_tool = "unset"

#drawing
    #point
    def setPoint(self, event=None):
        self.point = event.widget.create_oval(self.x1-4, self.y1-4, self.x1+4, self.y1+4,
                                              width=1, fill="red", tags=self.tag, activefill="pink")
        self.points.addPoint(self.point, self.x1, self.y1)

    #line
    def drawLine(self, event=None):
        if None not in (self.x1, self.y1, self.x2, self.y2):
            self.line = event.widget.create_line(self.x1, self.y1, self.x2, self.y2,
                                                 smooth=TRUE, width=3, fill="black", tags=self.tag, activefill="blue")
            print(self.line)
            point1 = event.widget.create_oval(self.x1-4, self.y1-4, self.x1+4, self.y1+4,
                                                  width=1, fill="yellow", tags=self.tag, activefill="green")
            point2 = event.widget.create_oval(self.x2-4, self.y2-4, self.x2+4, self.y2+4,
                                                  width=1, fill="yellow", tags=self.tag, activefill="green")
            self.lines.addLine(self.line, self.x1, self.y1, self.x2, self.y2, point1, point2)

    #move nearest object
    def selectObject(self, event=None):
        print(event.widget.find_closest(event.x, event.y, halo=None, start=None))
        if self.lines.isEventObject(event.widget.find_closest(event.x, event.y, halo=None, start=None)):
            self.lines.printdata(event.widget.find_closest(event.x, event.y, halo=None, start=None))
            line_constraint = self.lines.getLineConstraint(event.widget.find_closest(event.x, event.y, halo=None, start=None))
            if line_constraint[1] == 1 and line_constraint[2] == 0:
                linecoords = self.lines.getLineCoords(event.widget.find_closest(event.x, event.y, halo=None, start=None))
                event.widget.coords(linecoords[0], linecoords[1],
                                    linecoords[2], event.x, event.y)
                event.widget.coords(linecoords[5], linecoords[1]-4, linecoords[2]-4, linecoords[1]+4, linecoords[2]+4)
                event.widget.coords(linecoords[6], event.x-4, event.y-4, event.x+4, event.y+4)
                self.lines.changeLineCoords(event.widget.find_closest(event.x, event.y, halo=None, start=None), linecoords[1],
                                linecoords[2], event.x, event.y)
            if line_constraint[2] == 1 and line_constraint[1] == 0:
                linecoords = self.lines.getLineCoords(event.widget.find_closest(event.x, event.y, halo=None, start=None))
                event.widget.coords(linecoords[0], event.x, event.y,
                                    linecoords[3], linecoords[4])
                event.widget.coords(linecoords[5], event.x-4, event.y-4, event.x+4, event.y+4)
                event.widget.coords(linecoords[6], linecoords[3]-4, linecoords[4]-4, linecoords[3]+4, linecoords[4]+4)
                self.lines.changeLineCoords(event.widget.find_closest(event.x, event.y, halo=None, start=None), event.x, event.y,
                                    linecoords[3], linecoords[4])
            if line_constraint[1] == 0 and line_constraint[2] == 0:
                linecoords = self.lines.getLineCoords(event.widget.find_closest(event.x, event.y, halo=None, start=None))
                event.widget.move(event.widget.find_closest(event.x, event.y, halo=None, start=None), event.x - self.x1,
                              event.y - self.y1)
                event.widget.move(linecoords[5], event.x - self.x1, event.y - self.y1)
                event.widget.move(linecoords[6], event.x - self.x1, event.y - self.y1)
                dx = math.fabs(event.x - self.x1)
                dy = math.fabs(event.y - self.y1)
                self.lines.changeLineCoords(event.widget.find_closest(event.x, event.y, halo=None, start=None),
                                            linecoords[1]-dx, linecoords[2]-dy, linecoords[3]-dx, linecoords[4]-dy)
        if self.points.isEventObject(event.widget.find_closest(event.x, event.y, halo=None, start=None)):
            point_constraint = self.points.getPointConstraint(event.widget.find_closest(event.x, event.y, halo=None, start=None))
            if point_constraint[1] == 0:
                event.widget.move(event.widget.find_closest(event.x, event.y, halo=None, start=None), event.x - self.x1,
                                  event.y - self.y1)
                self.points.changePointCoords(event.widget.find_closest(event.x, event.y, halo=None, start=None), event.x - self.x1,
                                              event.y - self.y1)

#boundary
    #fix point of object
    def setGeometryCoinstaraint(self, event=None):
        if self.lines.isEventObject(event.widget.find_closest(event.x, event.y, halo=None, start=None)):
            linecoords = self.lines.getLineCoords(event.widget.find_closest(event.x, event.y, halo=None, start=None))
            if math.sqrt(math.fabs(linecoords[1]**2-event.x**2) + math.fabs(linecoords[2]**2 - event.y**2)) < math.sqrt(math.fabs(linecoords[3]**2-event.x**2) + math.fabs(linecoords[4]**2 - event.y**2)):
                self.lines.addLineConstraint(event.widget.find_closest(event.x, event.y, halo=None, start=None), 1)
                print("fix x1 y1")
            else:
                self.lines.addLineConstraint(event.widget.find_closest(event.x, event.y, halo=None, start=None), 2)
                print("fix x2 y2")
        if self.points.isEventObject(event.widget.find_closest(event.x, event.y, halo=None, start=None)):
            self.points.addPointConstraint(event.widget.find_closest(event.x, event.y, halo=None, start=None), 1)
            print("fix x y")
    def unsetBoundary(self):
        ...
        # print(self.lines.getSetOfLines())
        # print(self.points.getSetOfPoints())
        # print(event.widget.find_closest(event.x, event.y, halo=None, start=None))



if __name__ == "__main__":
    root = Tk()
    app = MicroCADApp(root)
    root.mainloop()

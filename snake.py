from turtle import Turtle

# position on the x axis
X_POSITION = [(0, 0), (-20, 0), (-40, 0)]

# define normal step
STEP = 20

# Set up headings
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        # Set the initial shape of the turtle
        for position in X_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment_list.append(new_segment)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        # Make the segment take the position of the next one starting from the last segment
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)
        self.segment_list[0].forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)




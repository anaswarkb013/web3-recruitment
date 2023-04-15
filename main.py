class Car:
    def __init__(self, make, model, year, speed_x, speed_y, x=0, y=0, width=5, length=10):
        self.make = make
        self.model = model
        self.year = year
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    def accelerate_x(self, speed_increment):
        self.speed_x += speed_increment

    def accelerate_y(self, speed_increment):
        self.speed_y += speed_increment

    def brake_x(self, speed_decrement):
        self.speed_x -= speed_decrement

    def brake_y(self, speed_decrement):
        self.speed_y -= speed_decrement

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def detect_collision(self, car2):
        x_overlap = (abs(self.x-car2.x) <= (self.length + car2.length)//2)
        y_overlap = (abs(self.y-car2.y) <= (self.width + car2.width)//2)

        return (x_overlap and y_overlap)

    def time_to_collision(self, car2):
        x_overlap_start = (self.x-car2.x - (self.length +
                           car2.length)/2)/(car2.speed_x-self.speed_x)
        x_overlap_end = (self.x-car2.x + (self.length +
                         car2.length)/2)/(car2.speed_x-self.speed_x)

        x_overlap_start, x_overlap_end = min(
            x_overlap_start, x_overlap_end), max(x_overlap_start, x_overlap_end)

        if x_overlap_end < 0:
            return -1
        if x_overlap_start < 0:
            x_overlap_start = 0

        y_overlap_start = (self.y-car2.y - (self.width +
                           car2.width)/2)/(car2.speed_y-self.speed_y)
        y_overlap_end = (self.y-car2.y + (self.width+car2.width) /
                         2)/(car2.speed_y-self.speed_y)

        y_overlap_start, y_overlap_end = min(
            y_overlap_start, y_overlap_end), max(y_overlap_start, y_overlap_end)

        if y_overlap_end < 0:
            return -1
        if y_overlap_start < 0:
            y_overlap_start = 0

        if y_overlap_start <= x_overlap_start <= y_overlap_end:
            return x_overlap_start
        if (x_overlap_start <= y_overlap_start <= x_overlap_end):
            return y_overlap_start

        return -1

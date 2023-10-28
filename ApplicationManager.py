from pymata4 import pymata4


   
class ApplicationManager:
    def __init__(self):
        self.trig_pin = 3
        self.echo_pin = 2
        self.board = pymata4.Pymata4()
        self.board.set_pin_mode_sonar(self.trig_pin, self.echo_pin, self.process)

    def process(self, data):
        if data[2] > 100:
            return 
        print(f"Distance: {data[2]} cm")


    
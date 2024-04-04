import turtle

class Barcode:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.width(4)
        self.bar_width = 100
        self.pixel_spacing = 1
        self.barcode_length = 64  # Lunghezza totale del codice a barre

    def draw_bar(self, color, width, length):
        self.t.color(color)
        self.t.width(width)
        self.t.forward(length)

    def draw_binary_barcode(self, alphanumeric_string):
        binary_string = ''.join(format(ord(char), '08b') for char in alphanumeric_string)
        
        self.t.penup()
        self.t.goto(-((self.bar_width + self.pixel_spacing) * self.barcode_length) / 2, 0)
        self.t.pendown()

        for bit in binary_string:
            if bit == '1':
                self.draw_bar("black", 4, self.bar_width)
            else:
                self.draw_bar("white", 4, self.bar_width)
            self.t.penup()
            self.t.forward(self.bar_width + self.pixel_spacing)

def main():
    barcode = Barcode()
    alphanumeric_string = "ciao sono mattia nato il 13052006" 
    barcode.draw_binary_barcode(alphanumeric_string)
    turtle.done()

if __name__ == "__main__":
    main()

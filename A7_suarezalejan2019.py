class Color(object):
    def __init__(self,r,g,b):
        # coerce values into required range by saturating
        if r < 0: r = 0
        if r > 1: r = 1
        if g < 0: g = 0
        if g > 1: g = 1
        if b < 0: b = 0
        if b > 1: b = 1

        self.red = round(float(r),1)
        self.green = round(float(g),1)
        self.black = round(float(b),1)


    def __add__(self,x):
        r = self.red + x.red
        g = self.green + x.green
        b = self.black + x.black
        res = Color(r,g,b)
        return res

    def __sub__(self,x):
        r = self.red - x.red
        g = self.green - x.green
        b = self.black - x.black
        res = Color(r,g,b)
        return res

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        rev_color_dict = {(1, 0, 0): 'red', (0, 1, 0): 'green', (0, 0, 1): 'blue', (0, 1, 1): 'cyan', (1, 0, 1): 'magenta', (1, 1, 0): 'yellow', (0, 0, 0): 'black', (1, 1, 1): 'white'}
        if (self.red, self.green, self.black) in rev_color_dict:
            return rev_color_dict[(self.red, self.green, self.black)]
        else:
            return '(' + str(self.red) + ', ' + str(self.green) + ', ' + str(self.black) + ')'

def input_color(num):
    color_dict = {'red': (1,0,0), 'green': (0,1,0), 'blue': (0,0,1), 'cyan': (0, 1, 1), 'magenta': (1,0,1), 'yellow': (1,1,0), 'black': (0,0,0), 'white': (1,1,1)}
    inp = input('Enter color ' + str(num) + ': ')
    if '(' in inp:
        r, g, b = map(float, inp.replace('(','').replace(')','').split(','))
        color = Color(r,g,b)
    else:
        color = Color(*color_dict[inp])
    return color


if __name__ == '__main__':

    color1 = input_color(1)
    color2 = input_color(2)

    print('Color 1 + Color 2 =', color1 + color2)
    
    print('Color 1 - Color 2 =', color1 - color2)

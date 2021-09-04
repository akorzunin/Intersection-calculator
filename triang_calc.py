'''simple triangulation calculator'''
import numpy as np
import argparse

class TriangCalcClass(object):
    """Calculate x and y coords of intersection of two lines defined by 2 points each
    
    """
    init_coords = {
        'x1': None,
        'y1': None,
        'x2': None,
        'y2': None,
        'x3': None,
        'y3': None,
        'x4': None,
        'y4': None,
    }
    px = None
    py = None
    rnd = 0
    def __init__(self, *args, **kwargs):
        super(TriangCalcClass, self).__init__()

    def args_unpack(self, *args):
        """Set the values from the arguments of the constructor .
        """        
        for num, k in enumerate(self.init_coords):
            self.init_coords[k] = args[num]

    # thats awkward
    def kwargs_unpack(self, **kwargs):
        """Unpack the constructor from the keyword arguments .
        """  
        self.init_coords = kwargs
    
    def solve(self, ):
        """Solve the equation of the initial state of the initialisation problem .

        Returns:
            px, py [float]: coordinates
        """       
        try:
            a1 = (
                [self.init_coords['x1'], self.init_coords['y1']],
                [self.init_coords['x2'], self.init_coords['y2']]
            )
            a2 = (
                [self.init_coords['x1'], 1],
                [self.init_coords['x2'], 1]
            )
            a3 = (
                [self.init_coords['x3'], self.init_coords['y3']],
                [self.init_coords['x4'], self.init_coords['y4']]
            )
            a4 = (
                [self.init_coords['x3'], 1],
                [self.init_coords['x4'], 1]
            )
            b1 = a2
            b2 = (
                [self.init_coords['y1'], 1],
                [self.init_coords['y2'], 1]
            )
            b3 = a4
            b4 = (
                [self.init_coords['y3'], 1],
                [self.init_coords['y4'], 1]
            )
            px_over = (
                [np.linalg.det(a1), np.linalg.det(a2)],
                [np.linalg.det(a3), np.linalg.det(a4)]
            )
            py_over = (
                [np.linalg.det(a1), np.linalg.det(b2)],
                [np.linalg.det(a3), np.linalg.det(b4)]        
            )
            p_under = (
                [np.linalg.det(b1), np.linalg.det(b2)],
                [np.linalg.det(b3), np.linalg.det(b4)] 
            )
            self.px = np.linalg.det(px_over) / np.linalg.det(p_under)
            self.py = np.linalg.det(py_over) / np.linalg.det(p_under)
        except TypeError:
            print("Solution not converge")
        return self.px, self.py


    def calculate(self, *args: float, **kwargs: float):
        """Calculate the coordinates of the point .
        """
        if (not args) == False: self.args_unpack(*args)
        if (not kwargs) == False: self.kwargs_unpack(**kwargs)
        self.solve()
        self.print_coord(self.px, self.py)

    def update_first(self, *args, **kwargs):
        """Update the coordinates for the first point .
        """
        if (not kwargs) == False: self.init_coords.update(**kwargs)
        if (not args) == False: 
            self.init_coords['x1'] = args[0]
            self.init_coords['y1'] = args[1]
            self.init_coords['x2'] = args[2]
            self.init_coords['y2'] = args[3]
        
        self.solve()
        self.print_coord(self.px, self.py)

    def update_second(self, *args, **kwargs):
        """Update the coordinates for the second point .
        """
        if (not kwargs) == False: self.init_coords.update(**kwargs)
        if (not args) == False: 
            self.init_coords['x3'] = args[0]
            self.init_coords['y3'] = args[1]
            self.init_coords['x4'] = args[2]
            self.init_coords['y4'] = args[3]

        self.solve()
        self.print_coord(self.px, self.py)

    def update(self, **kwargs):
        """Upadate previous calculation with kwargs
        """        
        self.init_coords.update(**kwargs)
        self.solve()
        self.print_coord(self.px, self.py)


    def print_coord(self, *args):
        """Print rounded values, return not rounded values

        Args:
            px (float): calculated x coordinate
            py (float): calculated y coordinate

        Returns:
            px, py: not rounded
        """        
        print(f'Px: {round(self.px, self.rnd)}, Py: {round(self.py, self.rnd)}')
        return self.px, self.py

              
if __name__ == '__main__':
    t = TriangCalcClass()
    t.calculate(0,0,0.1,1,1,0,0,500e+100)

    # t.calculate(x1=380e+10, y1=-1373e+10, x2=385, y2=-1385, x3=587, y3=-2016, x4=574, y4=-2026)

    # t.update_second(578+1, -2016+1, 574+1, -2026+1)

    # t.update_second(x3=578+8, y3=-2016+1, x4=574+1, y4=-2026-1)

    # t.update(x1=0.1, y1=-1000000, x2=0, y2=0)
    parser = argparse.ArgumentParser(description='Process 2 line triangulation.')
    parser.add_argument('--calc', help='sum the integers (default: find the max)', type=t.calculate)
    parser.add_argument('--print', help='sum the integers (default: find the max)', type=t.print_coord)

    args = parser.parse_args()
    print(args.calc)
    print(type(args.calc))

    # print(TriangCalcClass.__doc__)
    # t = TriangCalcClass()
    # t.calculate(input())
    # input()

    
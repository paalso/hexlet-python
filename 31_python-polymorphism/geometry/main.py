#!/usr/bin/env python3

import figure as Figure
import circle as Circle
import square as Square
import dispatcher


def main():
    Circle.init()
    c1 = Circle.make(5)

    print(f'Radius: {Circle.get_circle_radius(c1)}')
    # Вызов полиморфной функции. В зависимости от типа она идет либо в circle либо в square
    print(f'Circle area: {Figure.get_area(c1)}') # ~ 78.5

    Square.init()
    s1 = Square.make(10)
    print(f'Side: {Square.get_square_side(s1)}')
    print(f'Square area: {Figure.get_area(s1)}') # 100.0

if __name__ == '__main__':
    main()

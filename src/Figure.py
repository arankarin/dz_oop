
class Figure:

    def __init__(self, figure=None):
        self.figure = figure


    def add_area(self, figure): # Принимает другую геометрическую фигуру и возвращает сумму площадей
        self.check_figure(figure)
        summ = self.area + figure.area
        return summ

    def check_figure(self, figure):
        name_list = ["Rectangle", "Triangle", "Square", "Circle"]
        if not figure.name in name_list:
            print(f"figure.name = {figure.name}")
            raise ValueError
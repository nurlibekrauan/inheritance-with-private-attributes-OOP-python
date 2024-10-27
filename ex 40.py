class Geom:
    __name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._verify_coord(x1)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name=self.__name
    def _verify_coord(self, coord):
        if not 0 <= coord <= 100:
            raise ValueError("координата должна быть в пределах от 0 до 100")

# получение приватных атрибутов не доступно из дочерных классов и из других пространств
# по логике приватные атрибуты предполагаются быть использованы из базового класса
class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill="red"):
        super().__init__(x1, y1, x2, y2)
        self._verify_coord(x1)
        self._fill = fill

    def get_coords(self):
        return (self._x1, self._y1, self._x2, self._y2)


r = Rect(0, 0, 10, 20)
print(r.get_coords())
print(r.__dict__)
print(r._name)
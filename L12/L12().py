class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

    def __getitem__(self, key):  # --- Для зчитування значення за індексом
        if key == 1:
            return self.x
        elif key == 2:
            return self.y
        elif key == 3:
            return self.z
        else:
            raise Exception("Wrong key")

    def __setitem__(self, key, value):  # --- Для встановлення значення за індексом
        if key == 1:
            self.x = value
        elif key == 2:
            self.y = value
        elif key == 3:
            self.z = value
        else:
            raise Exception("Wrong key")

    def __delitem__(self, key):  # --- Видалення елемента за індексом
        if key == 1:
            del self.x
        elif key == 2:
            del self.y
        elif key == 3:
            del self.z
        else:
            raise Exception("Wrong key")

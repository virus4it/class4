class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):



        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        floor = 0
        if new_floor > self.number_of_floors:
            print("такого этажа нет")
        else:
            for i in range(new_floor):
                floor += 1
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, Кол-во этажей: {self.number_of_floors}"

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)


# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

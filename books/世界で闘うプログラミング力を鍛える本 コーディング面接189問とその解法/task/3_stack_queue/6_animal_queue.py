# 犬か猫で先に施設に来た方を外に出す

from linked_list import LinkedList
import datetime


class Animal:
    def __init__(self):
        pass


class Dog(Animal):
    def __init__(self):
        super().__init__()


class Cat(Animal):
    def __init__(self):
        super().__init__()


class AnimalShelter:
    def __init__(self):
        self.dogsList = LinkedList()
        self.catsList = LinkedList()

    def enqueue(self, classObject: Animal):
        if isinstance(classObject, Dog):
            self.dogsList.insert_first(datetime.datetime.now())
        elif isinstance(classObject, Cat):
            self.catsList.insert_first(datetime.datetime.now())

    def dequeueDog(self):
        if self.dogsList.length == 0:
            print("リストは空です。")
            return
        self.dogsList.poll()

    def dequeueCat(self):
        if self.catsList.length == 0:
            print("リストは空です。")
            return
        self.catsList.poll()

    def dequeueAny(self):
        if len(self.catsList) == 0 and self.dogsList != []:
            self.dequeueDog()
        elif self.catsList != [] and len(self.dogsList) == 0:
            self.dequeueCat()
        elif self.dogsList.get_node(len(self.dogsList)-1).data >= self.catsList.get_node(len(self.catsList)-1).data:
            self.dequeueCat()
        else:
            self.dequeueDog()


if __name__ == "__main__":
    animalShelter = AnimalShelter()
    dog = Dog()
    cat = Cat()
    print(animalShelter.dogsList)  # 空
    animalShelter.enqueue(dog)
    animalShelter.enqueue(dog)
    print(animalShelter.dogsList)
    animalShelter.dequeueDog()
    print(animalShelter.dogsList)
    animalShelter.dequeueDog()
    print(animalShelter.dogsList)  # 空

    animalShelter.enqueue(dog)
    print(animalShelter.dogsList)
    animalShelter.dequeueAny()
    print(animalShelter.dogsList)  # 空
    print(animalShelter.catsList)  # 空

    animalShelter.enqueue(cat)
    print(animalShelter.catsList)
    animalShelter.dequeueAny()
    print(animalShelter.catsList)  # 空

    animalShelter.enqueue(cat)
    animalShelter.enqueue(dog)
    print(animalShelter.catsList)
    print(animalShelter.dogsList)
    animalShelter.dequeueAny()
    print(animalShelter.catsList)  # 空
    print(animalShelter.dogsList)

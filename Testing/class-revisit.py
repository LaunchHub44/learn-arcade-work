class Animal:

class Dog(Animal):
    def __init__(self):
        self.name = "Buster"

    def __init__(self, n):
        self.name = n

    def say(self):
        print(f"Woof! My name is {self.name}!")


def main():
    milo = Dog("Milo")
    milo.say()


if __name__ == '__main__':
    main()

class Book:
    __title: str
    __author: str
    __price: float

    def __init__(self, title: str, author: str, price: float):
        self.__title = title
        self.__author = author
        self.__price = price

    def show_details(self):
        print(f"Book title is {self.__title}, author is {self.__author} and price is {self.__price}")


b = Book("python3", "Guido van Rossum", 444)

b.show_details()

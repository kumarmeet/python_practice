from typing import List


class Course:
    class Book:
        title: str

        def __init__(self, title: str):
            self.title = title

        def __str__(self):
            return self.title

    course_name: str
    course_duration: float
    books: List[Book]

    def __init__(self, course_name: str, course_duration: float, *books: str):
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(b) for b in books]

    def show_details(self):
        # Print the titles of the books
        print([str(book) for book in self.books])


# Example usage
course = Course("Python", 40, "Learn Python", "Python Comprehension")
course.show_details()

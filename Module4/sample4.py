class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"Book: {self.title} by {self.author}"

# User Interaction
library = []
while True:
    title = input("Enter book title (or type 'done'): ")
    if title.lower() == 'done':
        break
    author = input("Enter book author: ")
    library.append(Book(title, author))

print("\nLibrary Catalog:")
for book in library:
    print(book.display())
# 4) Create a Book class and display details of multiple books.

class Book:

    def __init__(self,BookTitle,author,price,pages):
        self.BookTitle = BookTitle
        self.author=author
        self.price =price
        self.pages = pages

    def display(self):
        return f"TITLE : {self.BookTitle}\nAUTHOR : {self.author}\nPRICE : {self.price}\nPAGES : {self.pages}\n"
    
def main():
    lst = []
    # b1 = Book("Python Basics","John Smith",499,350)
    # b2 = Book("Data Strcutures","Alice Brown",650,420)
    # b3 = Book("Machine learning","David lee",799,500)
    # lst.append(b1)
    # lst.append(b2)
    # lst.append(b3)

    n = int(input("Enter the books need to be stored: "))
    
    for i in range(n):
        book_title, author, price, pages = input("Enter title, author, price, pages: ").split(",")
        price,pages= int(price),int(pages)
        lst.append(Book(book_title , author , price , pages))

        

    for i in range(len(lst)):
        print(f"Book{i+1}")
        print(lst[i].display())
main()



        









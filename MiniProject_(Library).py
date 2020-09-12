class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def display(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict:
            self.lendDict.update({book:user})
            print("Book Dictionary has been updated successfully. You can take the book now")

        else:
            print(f"Book is already been issued by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Provided book has been added")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__=='__main__':
    hetarthi = Library(['Python','Harry Potter','Mathematics','Twilight','3 Mistakes of my life']
    ,"Hetarthi_Lib")

    while(True):
        print(f"Welcome to {hetarthi.name} library.\nEnter your choice:")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter valid input\n")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice==1:
            hetarthi.display()

        elif user_choice==2:
            book = input("Enter the name of the book you want to lend:")
            name = input("Enter your name:")
            hetarthi.lendBook(name,book)

        elif user_choice==3:
            book = input("Enter the name of the book you want to add:")
            hetarthi.addBook(book)

        elif user_choice==4:
            book = input("Enter the name of the book you want to return:")
            hetarthi.returnBook(book)

        else:
            print("Invalid input")

        print("Press q to quit and c to continue")
        user = ""

        while(user!="q" and user!="c"):
            user = input()
            if user=="q":
                exit()

            elif user=="c":
                continue

            else:
                print("Please enter valid input")




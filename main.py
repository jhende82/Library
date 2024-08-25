def main():

    books = []
    choice=0

    while choice != 4:
        print("Library Manager")
        print("1. Add Book")
        print("2. Find Book")
        print("3. All Books")
        print("4. Exit")
        choice = int(input())

        if choice == 1:
            print("Adding Book")
            title = input("Enter book title: ")
            genre = input("Enter genre of book: ")
            author = input("Enter author's name: ")
            books.append([title, genre, author])    

        elif choice == 2:
            print("Searching for book")
            search_word = input("Enter search word: ")
            for book in books:
                if search_word in book:
                    print(book)
        
        elif choice == 3:
            print("Print all books")
            for book in books:
                print(book)
        
        else:
            choice == 4
            print("Exiting program")

    print("Program terminated")

if __name__ == "__main__":
    main()

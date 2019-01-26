import books
import seller
import buyer
import db

connection = db.conn()


class BookStore:
    def start(self):
        book = books.Books()
        print("\n\t\t\t**********SHAPHRANG BOOKSTORE**********\n")
        print("Select your OPTIONS ? ")
        print("1.Seller\n2.Buyer\n3.View Books")
        choice = input("Enter your choice : ")
        if choice == '1':
            sells = seller.Sellers()
            sells.insert()
            t: bool = True
            while t:
                print("\n\t\t\t**********SHAPHRANG BOOKSTORE**********\n")
                print("1.Add books\n2.Modify books\n3.Delete book\n4.Show All Books\n5.Exit")
                ch = input("Enter your choice : ")
                if ch == '1':
                    sells.insert_book()
                elif ch == '2':
                    sells.modify()
                elif ch == '3':
                    sells.delete()
                elif ch == '4':
                    book.display()
                elif ch == '5':
                    connection.close()
                    exit(True)
                else:
                    print("INVALID CHOICE")
                    connection.close()
                    break

                c = input("Do you wish to continue ? (Y/N): ")
                if c == 'y' or c == 'Y':
                    t = True
                else:
                    connection.close()
                    t = False

        elif choice == '2':
            buys = buyer.Buyers()
            buys.insert()
            t: bool = True
            while t:
                print("\n\t\t\t**********SHAPHRANG BOOKSTORE**********\n")
                print("1.View Books\n2.Buy books\n3.Search Book\n4.Exit")
                choice = input("Enter your choice : ")
                if choice == '1':
                    book.display()
                elif choice == '2':
                    buys.buy()
                elif choice == '3':
                    buys.search()
                elif choice == '4':
                    connection.close()
                    exit(True)
                else:
                    print("INVALID CHOICE")
                    connection.close()
                    break

                c = input("Do you wish to continue ? (Y/N): ")
                if c == 'y' or c == 'Y':
                    t = True
                else:
                    connection.close()
                    t = False

        elif choice == '3':
            print("\n\t\t\t**********SHAPHRANG BOOKSTORE**********\n")
            book.display()
            print("************************************************************************************************")
            t: bool = True
            while t:
                print("1.Go Back\n2.Exit")
                choice = input("Enter your choice : ")
                if choice == '1':
                    self.start()
                elif choice == '2':
                    connection.close()
                    exit(True)
                else:
                    print("INVALID CHOICE")
                    connection.close()
                    break
        else:
            print("INVALID CHOICE")
            connection.close()


def main1() -> object:
    bs = BookStore()

    bs.start()


if __name__ == '__main__':
    main1()

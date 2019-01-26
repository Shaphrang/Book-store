import db

connection = db.conn()


class Sellers:
    def insert(self) -> object:
        print("Please Enter your details before selling books :")
        print("\t\t***********")
        id_seller = input("Enter your ID : ")
        name = input("Enter Your name : ")
        address = input("Enter your Address : ")
        contact_number = input("Enter the Contact Number : ")

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO seller(id_seller, name, address, contact_number) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (id_seller, name, address, contact_number))
                print("\t\t*****THANK YOU*****")

            connection.commit()
        finally:
            print("")

    def insert_book(self) -> object:
        id = input("Enter the ID : ")
        name = input("Enter the name of the book : ")
        publisher = input("Enter the publisher : ")
        isbn = input("Enter the isbn : ")
        price = input("Enter the price : ")
        edition = input("Enter the edition : ")
        date_published = input("Enter the date_published : ")

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO books(id_book, name, publisher, isbn, price, edition, date_published)" \
                      " VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (id, name, publisher, isbn, price, edition, date_published))
                print("Book added successfully")

            connection.commit()
        finally:
            print("")

    def modify(self) -> object:
        tempid = input("Enter the id of a book to be modified")
        print("*****Now, Make the changes*****")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE books SET name=%s, publisher=%s, isbn=%s, price=%s, edition=%s, " \
                      "date_published=%s WHERE id_book=%s"
                name = input("Enter the name of the book : ")
                publisher = input("Enter the publisher : ")
                isbn = input("Enter the isbn : ")
                price = input("Enter the price : ")
                edition = input("Enter the edition : ")
                date_published = input("Enter the date_published : ")
                assert isinstance(cursor, object)
                cursor.execute(sql,  (name, publisher, isbn, price, edition, date_published, tempid))
                print("Book modified successfully")

            connection.commit()
        finally:
            print("")

    def delete(self) -> object:
        print("***\t\tDeleting a Book***")
        tempid = input("Enter the id of a book to be deleted")
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM books WHERE id_book=%s"
                assert isinstance(cursor, object)
                cursor.execute(sql, tempid)
                print("Book Deleted successfully")

            connection.commit()
        finally:
            print("")

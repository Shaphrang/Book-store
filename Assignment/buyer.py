import db

connection = db.conn()


class Buyers:
    def insert(self):
        print("Please Enter your details before buying books :")
        print("\t\t***********")
        id_buyer = input("Enter your ID : ")
        name = input("Enter your Name : ")
        email = input("Enter your Email ID : ")
        contact_number = input("Enter your Contact Number : ")

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO buyer(id_buyer, name, email, contact_number) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (id_buyer, name, email, contact_number))
                print("\t\t*****THANK YOU*****")

            connection.commit()
        finally:
            print("")

    def buy(self) -> object:
        tempname = input("Enter the Name of the book : ")
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books where name=%s"
                cursor.execute(sql, tempname)
                print("\t\t*****Book Details*****")
                print("ID\t\tNAME\t\tPUBLISHER\tISBN\t\tPRICE\t\tEDITION\t\tDATE OF PUBLISHED")
                print("***\t\t******\t\t********\t******\t\t******\t\t******\t\t****************")
                for row in cursor:
                    print(str(row[0]) + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3]
                          + "\t\t" + str(row[4]) + "\t\t" + row[5] + "\t\t" + row[6])
                print("\t\t*******************")
                print("This is just a Demo Version : You cannot Buy Books for Now... Thank You")
                print("We will surely allow you to buy books in the Future.!!!")
            connection.commit()
        finally:
            print("")

    def search(self) -> object:
        tempname = input("Enter the name of a book to be Searched : ")
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books where name=%s"
                assert isinstance(cursor, object)
                cursor.execute(sql,  tempname)
                print("\t\t*****Book Details*****")
                print("ID\t\tNAME\t\tPUBLISHER\tISBN\t\tPRICE\t\tEDITION\t\tDATE OF PUBLISHED")
                print("***\t\t******\t\t********\t******\t\t******\t\t******\t\t****************")
                for row in cursor:
                    print(str(row[0]) + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3]
                          + "\t\t" + str(row[4]) + "\t\t" + row[5] + "\t\t" + row[6])
            connection.commit()
        finally:
            print("")



import db

connection = db.conn()


class Books:
    def display(self) -> object:
        try:
            with connection.cursor() as cursor:
                sql: str = "SELECT * FROM books"
                cursor.execute(sql)
                result = cursor.fetchall()
                print("ID\t\tNAME\t\tPUBLISHER\tISBN\t\tPRICE\t\tEDITION\t\tDATE OF PUBLISHED")
                print("***\t\t******\t\t********\t******\t\t******\t\t******\t\t****************")
                row: object
                for row in result:
                    print(str(row[0]) + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3]
                          + "\t\t" + str(row[4]) + "\t\t" + row[5] + "\t\t" + row[6])
            connection.commit()
        finally:
            print("")

import mysql.connector as connector

# con = connector.connect(host='localhost',
#                         port='3306',
#                         user='root',
#                         password='root',
#                         database='pythontest')

# print(con)
# con -> cursor -> queries


class DBHelper:
    def __init__(self):
        # whenever the object is made this constructor will be called
        # this will connect to the database
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='root',
                                     database='pythontest')
        # write any query
        query = 'create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()     # this will return cursor
        cur.execute(query)          # query is passed to execute through cursor
        print("Created")

    # Insert
    def insert_user(self, userid, username, phone):
        query = "insert into user(userId, userName, phone) values('{}', '{}', '{}')".format(
            userid, username, phone)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    # Fech All
    def fetch_all(self):
        query = "SELECT * FROM user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id: ", row[0])
            print("User Name: ", row[1])
            print("User Phone: ", row[2])
            print()
            print()

    # Fetch one
    def fetch_id(self, id):
        query = "SELECT * FROM user WHERE userId = '{}'".format(id)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id: ", row[0])
            print("User Name: ", row[1])
            print("User Phone: ", row[2])

    # delete user
    def delete_user(self, id):
        query = "DELETE from user where userId = {}".format(id)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted")

    # update user
    def update_user(self, id, name, phone):
        query = "UPDATE user SET userName = '{}', phone = {} where userId = {} ".format(
            name, phone, id)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

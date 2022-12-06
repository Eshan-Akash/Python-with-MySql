from dbhelper import DBHelper


def main():
    db = DBHelper()
    while True:
        print("**********WELCOME**********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            # Insert
            choice = int(input())
            if choice == 1:
                uid = int(input("Enter user id: "))
                uname = input("Enter user name: ")
                uphone = input("Enter user phone: ")
                db.insert_user(uid, uname, uphone)

            # fetch
            elif choice == 2:
                db.fetch_all()

            # Delete
            elif choice == 3:
                uid = int(input("Enter user id which you want to delete: "))
                db.delete_user(uid)

            # Update
            elif choice == 4:
                uid = int(input("Enter user id: "))
                uname = input("Enter New name: ")
                uphone = input("Enter New phone: ")
                db.update_user(uid, uname, uphone)

            # Exit
            elif choice == 5:
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid detail ! Try again")


if __name__ == "__main__":
    main()

    # main coding
# helper = DBHelper()
# helper.insert_user(5534, "Eshan", "9937758348")
# helper.insert_user(2324, "Akash", "9937242448")
# helper.insert_user(6454, "Shubham", "9924258348")
# helper.insert_user(645, "Pradyumna", "6637758348")
# helper.fetch_all()
# helper.fetch_id(645)
# helper.delete_user(5534)
# helper.update_user(2324, 'kkk', '8877887788')
# helper.fetch_all()

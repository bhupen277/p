#import mysql.connector

# Use the IP address of the MySQL container on the same network
#conn = mysql.connector.connect(
    #host="172.17.0.2",  # IP address of the MySQL container
    #user="root",  # MySQL username
    #password="root",  # MySQL password
    #database="database_name"  # The name of your database


cursor = conn.cursor()

# Example of inserting data
def insert_name(name):
    cursor.execute("INSERT INTO names (name) VALUES (%s)", (name,))
    conn.commit()
    print(f"Name '{name}' inserted successfully.")

# Example of showing all data
def show_names():
    cursor.execute("SELECT * FROM names")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Main menu function
def menu():
    while True:
        print("\nMenu:")
        print("1. Give and save name")
        print("2. Show all names")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            name_to_store = input("Enter a name to store in the database: ")
            insert_name(name_to_store)
        elif choice == '2':
            show_names()
        elif choice == '3':
            print("Exiting the script.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu
menu()

# Close the connection
cursor.close()
conn.close()

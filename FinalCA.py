import os
import csv


# Item base class
class Items:
    """
        Base class for library items.
        """
    def __init__(self, item_id, title):
        """
                Initialize an instance of the Items class.

                Args:
                    item_id (str): The unique ID of the item.
                    title (str): The title of the item.
                """
        self.item_id = item_id
        self.title = title

    def __str__(self):
        """
                Return a string representation of the item.

                Returns:
                    str: The formatted string representation of the item.
                """
        return f"{self.item_id}: {self.title}"


# Book subclass
class Books(Items):
    """
    Subclass of Items for books.
    """
    def __init__(self, item_id, title, author):
        """
                Initialize an instance of the Books class.

                Args:
                    item_id (str): The unique ID of the book.
                    title (str): The title of the book.
                    author (str): The author of the book.
                """
        super().__init__(item_id, title)
        self.author = author

    def __str__(self):
        """
                Return a string representation of the book.

                Returns:
                    str: The formatted string representation of the book.
                """
        return f"{super().__str__()} by {self.author}"


# Article subclass
class Articles(Items):
    def __init__(self, item_id, title, journal):
        super().__init__(item_id, title)
        self.journal = journal

    def __str__(self):
        return f"{super().__str__()} in {self.journal}"


# DigitalMedia subclass
class DigitalMedia(Items):
    def __init__(self, item_id, title, format):
        super().__init__(item_id, title)
        self.format = format

    def __str__(self):
        return f"{super().__str__()} ({self.format})"


# Member class
class Members:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __str__(self):
        return f"{self.member_id}: {self.name}"


# Library class
class Library:
    def __init__(self):
        self.items = []
        self.members = []
        self.borrowed_items = {}
        self.load_data()

    # Load data from files
    def load_data(self):
        self.load_items()
        self.load_members()
        self.load_borrowed_items()

    def load_items(self):
        with open("items.txt", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                item_id, item_type, title, extra = row
                if item_type == "book":
                    item = Books(item_id, title, extra)
                elif item_type == "article":
                    item = Articles(item_id, title, extra)
                elif item_type == "digital_media":
                    item = DigitalMedia(item_id, title, extra)
                self.items.append(item)

    def load_members(self):
        with open("members.txt", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                member_id, name = row
                member = Members(member_id, name)
                self.members.append(member)

    def load_borrowed_items(self):
        with open("borrowing.txt", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                member_id, item_id = row
                self.borrowed_items[item_id] = member_id

    # Update data in files
    def update_files(self):
        self.update_items_file()
        self.update_members_file()
        self.update_borrowed_items_file()

    def update_items_file(self):
        with open("items.txt", "w") as file:
            writer = csv.writer(file)
            for item in self.items:
                if isinstance(item, Books):
                    writer.writerow([item.item_id, "book", item.title, item.author])
                elif isinstance(item, Articles):
                    writer.writerow([item.item_id, "article", item.title, item.journal])
                elif isinstance(item, DigitalMedia):
                    writer.writerow([item.item_id, "digital_media", item.title, item.format])

    def update_members_file(self):
        with open("members.txt", "w") as file:
            writer = csv.writer(file)
            for member in self.members:
                writer.writerow([member.member_id, member.name])

        def update_borrowed_items_file(self):
            with open("borrowing.txt", "w") as file:
                writer = csv.writer(file)
                for item_id, member_id in self.borrowed_items.items():
                    writer.writerow([member_id, item_id])

        # Methods for managing instances (add/edit/delete)
        def add_item(self, item):
            self.items.append(item)
            self.update_items_file()

        def edit_item(self, item_id, new_title):
            for item in self.items:
                if item.item_id == item_id:
                    item.title = new_title
                    break
            self.update_items_file()

        def delete_item(self, item_id):
            self.items = [item for item in self.items if item.item_id != item_id]
            self.update_items_file()

        def add_member(self, member):
            self.members.append(member)
            self.update_members_file()

        def edit_member(self, member_id, new_name):
            for member in self.members:
                if member.member_id == member_id:
                    member.name = new_name
                    break
            self.update_members_file()

        def delete_member(self, member_id):
            self.members = [member for member in self.members if member.member_id != member_id]
            self.update_members_file()

        # Methods for borrowing and returning items
        def borrow_item(self, member_id, item_id):
            if item_id not in self.borrowed_items:
                self.borrowed_items[item_id] = member_id
                self.update_borrowed_items_file()

        def return_item(self, item_id):
            if item_id in self.borrowed_items:
                del self.borrowed_items[item_id]
                self.update_borrowed_items_file()

        # Main function to provide a command line interface for the user
        def main():
            """
                Main function to provide a command line interface for the user.
                """
            library = Library()

            while True:
                print("\nChoose an option:")
                print("1. Add an item")
                print("2. Edit an item")
                print("3. Delete an item")
                print("4. Add a member")
                print("5. Edit a member")
                print("6. Delete a member")
                print("7. Borrow an item")
                print("8. Return an item")
                print("9. Exit")

                choice = int(input("Enter the number of your choice: "))

                if choice == 1:
                    # Add an item
                    item_type = input("Enter the item type (book, article, digital_media): ")
                    item_id = input("Enter the item ID: ")
                    title = input("Enter the title: ")
                    extra = input("Enter the author (for book), journal (for article), or format (for digital_media): ")

                    if item_type == "book":
                        item = Books(item_id, title, extra)
                    elif item_type == "article":
                        item = Articles(item_id, title, extra)
                    elif item_type == "digital_media":
                        item = DigitalMedia(item_id, title, extra)
                    else:
                        print("Invalid item type")
                        continue

                    library.add_item(item)

                elif choice == 2:
                    # Edit an item
                    item_id = input("Enter the item ID: ")
                    new_title = input("Enter the new title: ")
                    library.edit_item(item_id, new_title)

                elif choice == 3:
                    # Delete an item
                    item_id = input("Enter the item ID: ")
                    library.delete_item(item_id)

                elif choice == 4:
                    # Add a member
                    member_id = input("Enter the member ID: ")
                    name = input("Enter the member's name: ")
                    member = Members(member_id, name)
                    library.add_member(member)

                elif choice == 5:
                    # Edit a member
                    member_id = input("Enter the member ID: ")
                    new_name = input("Enter the new name: ")
                    library.edit_member(member_id, new_name)

                elif choice == 6:
                    # Delete a member
                    member_id = input("Enter the member ID: ")
                    library.delete_member(member_id)

                elif choice == 7:
                    # Borrow an item
                    member_id = input("Enter the member ID: ")
                    item_id = input("Enter the item ID: ")
                    library.borrow_item(member_id, item_id)

                elif choice == 8:
                    # Return an item
                    item_id = input("Enter the item ID: ")
                    library.return_item(item_id)

                elif choice == 9:
                    # Exit the program
                    print("Exiting...")
                    break

                else:
                    # Invalid choice
                    print("Invalid choice")

                if __name__ == "__main__":
                    main()

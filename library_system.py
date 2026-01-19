import datetime


class LMS:
	def __init__(self, list_of_books, library_name):
		self.list_of_books = "C:\\Users\\user\\NEW.VSCODE\\PYTHON_PROJECTS_1\\Library_system\\List_of_books.txt"
		self.library_name = library_name
		self.books_dict = {}
		ID = 101

		with open(self.list_of_books) as book:
			content = book.readlines()
		for line in content:
			self.books_dict.update({str(ID):{"Books title": line.replace("\n", ""),
				"Lender name":"",
				"Issue date": "",
				"Status": "Available"}})
			ID += 1

	def display_books(self):
		print("--------------------------------------------")
		print("Books ID", "\t", "Title")
		print("--------------------------------------------")

		for key, value in self.books_dict.items():
			print(key, "\t\t", value.get("Books title"), "-[", value.get("Status"),"]") #We print our key(ID) and get the Book Title from our values


	def issue_books(self):
		book_id = input("Enter book ID: ")
		current_date = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

		if book_id in self.books_dict.keys():
			if not self.books_dict[book_id]["Status"] == "Available":
				print(f"That book is already issued to {self.books_dict[book_id]["Lender name"]} on {self.books_dict[book_id]["Issue date"]}")
				return self.issue_books()

			elif self.books_dict[book_id]["Status"] == "Available":
				your_name = input("Enter your name: ")
				self.books_dict[book_id]["Status"] = "Already Issued"
				self.books_dict[book_id]["Lender name"] = your_name
				self.books_dict[book_id]["Issue date"] = current_date
				print(f"Book Issued to {your_name} successfully!  ")

		else:
			print("Book ID not found")
			return self.issue_books()

	def return_books(self):
		book_id = input("Enter book ID: ")

		if book_id in self.books_dict.keys():
			if self.books_dict[book_id]["Status"] == "Available":
				print("This book is already in the Library!! ")
				return self.return_books()

			elif self.books_dict[book_id]["Status"] == "Already Issued":
				self.books_dict[book_id]["Lender name"] = ""
				self.books_dict[book_id]["Status"] = "Available"
				self.books_dict[book_id]["Issue date"] = ""
				print("The book has been successfully returned! ")
		else:
			print("Book ID not found")
			return self.return_books()

	def add_books(self):
		new_book = input("Enter the Title of a book to add: ")
		if new_book == "":
			return self.add_books()
		if len(new_book) > 25:
			print("The Title length is too long! ")
			return self.add_books()

		else:
			with open(self.list_of_books, "a") as book:
				book.writelines(f"{new_book}\n")
				self.books_dict.update({str(int(max(self.books_dict)) + 1) : {"Books title" : new_book, "Lender name" : "", "Status" : "Available", "Issue date" : ""}})

my_lib = LMS("C:\\Users\\user\\NEW.VSCODE\\PYTHON_PROJECTS_1\\Library_system\\List_of_books.txt", "JKUAT LIBRARY")
press_keys = {"D":"Display Books", "I": "Issue books", "A": "Add books", "R": "Return books", "Q": "Quit"}

key_press = False
print(f"------------------ Welcome to {my_lib.library_name} ------------------------")
while not (key_press == "q"):
	
	for key,value in press_keys.items():
		print(f"Press {key} to {value}")

	key_press = input("Enter a key: ").lower()

	if key_press == "d":
		my_lib.display_books()
	elif key_press == "i":
		my_lib.issue_books()
	elif key_press == "a":
		my_lib.add_books()
	elif key_press == "r":
		my_lib.return_books()
	elif key_press == "q":
		break
	else:
		print("Invalid Key !!!")
		continue
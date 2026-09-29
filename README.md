# Online food ordering System

An Online food ordering System built using Python. This project is an Online food ordering platform based on terminal where users can order food items from a pre-defined menu.

## Features

- Order food items
- Modify cart after selecting 
- Generate bill
- Avail various discounts 

## Technologies Used

- Python 3

## How to access the code

1. Clone the repository:

```bash
git clone https://github.com/diptanshukashyap1/26BCE11492_Food_ordering_system
```

2. Navigate to the project folder:

```bash
cd 26BCE11492_Food_ordering_system

```


3. Run the main program:

```bash
python Food_ordering_system.py
```

> **Note:** Keep `Food_ordering_system.py` and `Food_ordering_module.py` in the same folder, as the main program imports functions from `Food_ordering_module.py`.

## Project Structure

```
Mini-Library/
│
├── Food_ordering_system.py      # Main program
├── Food_ordering_module.py    # Contains the ordering functions
├── README.md
└── statement.md
```

## Future Improvements

- Save ordering data to SQL
- Add more items in the menu
- Develop a better user interface
- Different list of options for staff and customers

## Learning Outcomes

Through this project, I practiced:

- Working with Python modules
- Creating reusable functions with def
- Using lists to manage data
- Implementing conditional statements and loops

## How to run 

- When running the code , the user will get multiple options , such as Displaying all  , Searching for books , etc.
- Its recommended that the user goes through the option one by one .
- When choosing 1 , the interpreter will show all pre-defined books in the library i.e. 8 books .
- Next , the user will be asked to enter "Continue", after entering "Continue" ,the user should choose 2 .
>**Note:** The user will be asked to enter CONTINUE after each iteration. 
-  That will allow user to search the availability of books , to make sure if the books are in the library or are issued to someone else .
> **Note:** To do that , user should enter the book name that was previously displayed when the user chose 1 .
- Accordingly , user can use 3 and 4 to borrow and return new books from the library , based on its Book ID .
- Now , 5 is an option meant for the librarian to add new books into the library . Choosing 5 , user will be asked how many new books are to be added and the Book ID and Book name of the new books to be added.
- This whole process is in a looping statement (while) and hence option 6 lets the user exit the library and a "Thanks for using" Message is displayed.

## Author

**Diptanshu Kashyap**

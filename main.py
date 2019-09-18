""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import Book, BookStore
from menu import Menu
import ui

store = BookStore()
QUIT = 'Q'

def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == QUIT:
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    menu.add_option('2', 'Search For Book', search_book)
    menu.add_option('3', 'Show Unread Books', show_unread_books)
    menu.add_option('4', 'Show Read Books', show_read_books)
    menu.add_option('5', 'Show All Books', show_all_books)
    menu.add_option('6', 'Change Book Read Status', change_read)
    menu.add_option('Q', 'Quit', quit_program)

    return menu


def add_book():
    new_book = ui.get_book_info()
    all_books = store.get_all_books()
    if book in all_books:
        book_present =True
        if book_present == True:
            raise Exception('This book is already exist')
        else:
            store.add_book(new_book)
            ui.message('New book added')

    

def show_read_books():
    read_books = store.get_books_by_read_value(True)
    ui.show_books(read_books)
    print("\n") # adding blank line after list of books


def show_unread_books():
    unread_books = store.get_books_by_read_value(False)
    ui.show_books(unread_books)
    print("\n")


def show_all_books():
    books = store.get_all_books()
    print("\n")
    ui.show_books(books)
    print("\n")


def search_book():
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
    matches = store.book_search(search_term)
    print("\n")
    ui.show_books(matches)
    print("\n")

def delete():
    try:
        book = ui.get_book_info()
        store.delete(book)

    except ValueError:
        raise BookError("Book doesn't exist")



def change_read():

    book_id = ui.get_book_id()
    try:

       book = store.get_book_by_id(book_id)
    except:
        ui.message('The book is not in store!')
    else:
         new_read = ui.get_read_value()
         book.read = new_read
         store.set_book_read(book_id,new_read)
    

def quit_program():
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()

#Implementing Basic OOP for a Library Management System

class Book: 
    def __init__(self,title,author): 
        self.title = title 
        self.author = author 
        #A private attribute of _is_checked_out track its availability 
        self._is_checked_out = False

    #The Book class should provide methods to check a book out and return it, affecting its availability.  
    def check_out_bookh (self): 
        if not self._is_checked_out : 
            self._is_checked_out = True 
            return True 
        else : 
            return False #i.e to track the book's availabilty . If the book is checked out , return True; else False(still available)

    def return_book(self):
        if self._is_checked_out: 
            self._is_checked_out = False #The book is available on the shelf , returned 
            return True ##Meaning that the book has been returned 
        else :
            return False 
        
    def is_available(self): 
        return not self._is_checked_out    

#Creating a library class 
class Library: 
    def __init__(self):
        #Implement a Library class with a private list _books to store instances of Book. 
        self._books = [] #An empty list.The Library class is a container for the Book class(Analogy)

    #Creating instance for the Book class to be stored as the Library methods
    def add_book(self,book): 
             self._books.append(book)
        #Adding books to the empty list 

    def check_out_book(self, title): 
        for book in self._books : 
            if book.title == title :
                book.check_out_book()
                return   

    def return_book(self,title):
          for book in self._books:
            if book.title == title:
                book.return_book()
                return
    
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")             

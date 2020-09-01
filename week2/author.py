class Author:
    def __init__(self, name):
        self.name = name
        self.books = []


    def publish(self, title):
        # checks if the title is already in the list before adding, IS case sensitive 
        if title in self.books:
            print(f'{title} already is already published.')
        else:
            self.books.append(title)


    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():
    
    # creating new author
    rowling = Author('J. K. Rowling')
    # adds books to the author

    rowling.publish('Harry Potter and the Philosopher\'s Stone')
    rowling.publish('Fantastic Beasts and Where to Find Them')
    # prints out object
    print(rowling)
    


    # creating new author with no books
    quinn = Author('Quinn')
    print(quinn)

    # this statement adds a duplicate to the published books list but should be caught by the if statement in the published function
    rowling.publish('Fantastic Beasts and Where to Find Them')



main()
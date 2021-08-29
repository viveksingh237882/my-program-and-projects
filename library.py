from _typeshed import Self
from typing import Mapping


class library:
    def __init__(self ,list,name):
        self.bookslist=list
        self.name=name
        self.lendDict={}
    def display(self):
        print("we have following book in our library:{bookslist}")
        for book in self.bookslist:
            print(book)
    def lendbook(self,users,book):
        if book not  in lendDict.keys():
            self.lendDict.uodate({book:users})
            print("u can take this book")
        else:
            print(f"book is being used by {self.lendDict[book]}")
    def addbook(self):
        self.bookslist.append(book)
        print("Book is added ")

    def return(self,book):
        self.bookslist.remove(book)
if __name__==__main__():
    vivek=lirary(['harry potter','gullivers travalls','cabtervill ghost','python','chutiyaapa of rajesh'],'mirzapur')

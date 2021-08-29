


def searcher():
    import time
    book="Vivek and HArishankar is good friend"
    time.sleep(4)



while True:
    text=(yield)
    if text in book:
        print("The is find in the book ")
    else:
        print("The doesnot find in the book")




search=searcher()
next.(search)        
search.send("vivek")
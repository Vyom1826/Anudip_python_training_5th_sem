'''Problem Statement
The number of available copies of books in a library is stored below.
Sample Data
books = { "Python": 5, 
"Java": 2, 
"DBMS": 4, 
"Networking": 1, 
"OS": 3, 
"AI": 6, 
"ML": 2, 
"Cloud": 5, 
"Cyber Security": 1, 
"Web Development": 4 }
Tasks
1.
Display books with fewer than 3 copies.
2.
Find the book with maximum copies.
3.
Find the book with minimum copies.
4.
Count total books available.
5.
Generate a restocking list.'''

books = { "Python": 5, 
"Java": 2, 
"DBMS": 4, 
"Networking": 1, 
"OS": 3, 
"AI": 6, 
"ML": 2, 
"Cloud": 5, 
"Cyber Security": 1, 
"Web Development": 4 }

# 1.Display books with fewer than 3 copies
print("Books with fewer than 3 copies:")
for book, copies in books.items():
    if copies < 3:
        print(book)

# 2.Find the book with maximum copies.
max_copies = max(books , key=books.get)
print("\n The books with maximum copies:")
print(max_copies,":",books[max_copies],"copies")

# 3.Find the books with minimum copies.
min_copies = min(books , key=books.get)
print("\n The books with minimum copies:")
print(min_copies, ":", books[min_copies],"copies")

# 4.Count total books available.
total_books = sum(books.values())
print("\nTotal books available:", total_books)

# 5.Generate a restocking list.
print("\nRestocking list:")
restocking_list = []

for book, copies in books.items():
    if copies < 3:
        restocking_list.append(book)

print(restocking_list)
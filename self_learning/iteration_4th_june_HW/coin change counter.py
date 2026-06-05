# program for changing money 

amount = int(input("Enter amount: "))

note_500 = amount // 500
amount = amount % 500

note_200 = amount // 200
amount = amount % 200

note_100 = amount // 100
amount = amount % 100

note_50 = amount // 50
amount = amount % 50

note_20 = amount // 20
amount = amount % 20

note_10 = amount // 10
amount = amount % 10

if note_500 > 0:
    print("500 x", note_500)

if note_200 > 0:
    print("200 x", note_200)

if note_100 > 0:
    print("100 x", note_100)

if note_50 > 0:
    print("50 x", note_50)

if note_20 > 0:
    print("20 x", note_20)

if note_10 > 0:
    print("10 x", note_10)
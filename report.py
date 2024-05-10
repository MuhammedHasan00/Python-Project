from connect import *

#subroutines

def genre():
    filmGenre = input("Enter Genre (Comedy, Action, Crime, Test, Fantasy, Animation, Fighting): ").title()
    cursor.execute(f"SELECT * FROM tblfilms WHERE genre = '{filmGenre}'")
    row = cursor.fetchall()
    for aRecord in row:
        print(aRecord)    

def year():
    filmYear = int(input("Enter Year: "))
    cursor.execute(f"SELECT * FROM tblfilms WHERE yearReleased = '{filmYear}'")
    row = cursor.fetchall()
    for aRecord in row:
        print(aRecord)    

def rating():
    filmRating = input("Enter Rating (PG, R, G): ").upper()
    cursor.execute(f"SELECT * FROM tblfilms WHERE rating = '{filmRating}'")
    row = cursor.fetchall()
    for aRecord in row:
        print(aRecord)    

if __name__ == "__main__":
    genre()
    year()
    rating()
    
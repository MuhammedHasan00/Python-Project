from connect import *

#subroutines

def genre():
    try:
        filmGenre = input("Enter Genre (Comedy, Action, Crime, Test, Fantasy, Animation, Fighting): ").title()
        cursor.execute(f"SELECT * FROM tblfilms WHERE genre = '{filmGenre}'")

        if cursor.fetchone() is None:
            print(f"Films with genre {filmGenre} not found! Please enter one of the following (Comedy, Action, Crime, Test, Fantasy, Animation, Fighting)")
        else:
            row = cursor.fetchall()
            for aRecord in row:
                print(aRecord)  
    except (sql.OperationalError, ValueError) as e:
        print(f"Records not found, {e}")  

def year():
    try:
        filmYear = int(input("Enter Year: "))
        cursor.execute(f"SELECT * FROM tblfilms WHERE yearReleased = '{filmYear}'")
        if cursor.fetchone() is None:
            print(f"Cannot find any films from the year {filmYear}")
        else:
            row = cursor.fetchall()
            for aRecord in row:
                print(aRecord)    
    except (sql.OperationalError, ValueError) as e:
        print(f"Records not found, {e}") 

def rating():
    try:
        filmRating = input("Enter Rating (PG, R, G): ").upper()
        ratingOptions = ["PG","R", "G"]
        if filmRating not in ratingOptions:
            print(f"cannot find films with rating {filmRating}, please try one of the following ratings (PG, R, G)!")
        else:
            cursor.execute(f"SELECT * FROM tblfilms WHERE rating = '{filmRating}'")
            row = cursor.fetchall()
            for aRecord in row:
                print(aRecord)
    except (sql.OperationalError, ValueError) as e:
        print(f"Records not found, {e}")     

if __name__ == "__main__":
    genre()
    year()
    rating()
    
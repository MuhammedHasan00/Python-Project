from connect import *

def addFilm():
    

    try:
        film = []
        title = input("Enter a film title: ").title()
        yearReleased = int(input("Enter the year it was released: "))
        rating = input("Enter the age rating (PG/R/G): ").upper()
        duration = int(input("How long is the film (in minutes): "))
        genre = input("What genre does the film fall into: ").title()

        film = film + [title, yearReleased, rating, duration, genre]
        cursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", film)
        conn.commit()
        print(f"{title} has been added to the Films Database")
    
    except (sql.OperationalError, ValueError) as e:
        conn.rollback()
        print(f"Record not added: {e}")

if __name__ == "__main__":
    addFilm()
from connect import *

def readRecords():

    try:
        cursor.execute("SELECT * FROM tblfilms")
        row = cursor.fetchall()

        for aRecord in row:
            print(aRecord)

    except sql.OperationalError as e:
        print(f"Records not found: {e}")  

if __name__ == "__main__":
    readRecords()
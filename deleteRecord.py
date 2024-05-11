from connect import *

def deleteRecord():

    try:
        idField = int(input("Enter the ID of the record you wish to delete: "))
        
        cursor.execute("SELECT * FROM tblfilms WHERE filmID = ?",(idField,))
        if cursor.fetchone() is None:
            print(f"Record with ID {idField} not found!")
        else:
            cursor.execute(f"DELETE FROM tblfilms WHERE filmID = ?", (idField,))
            conn.commit()
            print(f"Record with ID {idField} was deleted!")

    except (sql.OperationalError, ValueError) as e:
        conn.rollback()
        print(f"Record not deleted: {e}")


if __name__ == "__main__":
    deleteRecord()
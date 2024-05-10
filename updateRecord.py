from connect import *

def updateRecord():

    try:
        idField =int(input("Enter the ID of the record to be updated: "))
        allowedFields = ["Title", "yearReleased", "Rating", "Duration", "Genre"]
        fieldName = input("Enter the field you want to update (Title, yearReleased, Rating, Duration, Genre): ").title()
        newValue = input(f"Enter the value for {fieldName}: ")

        if fieldName == "Yearreleased":
            fieldName = "yearReleased"
            newValue = int(newValue)
        elif fieldName == "Duration":
            newValue = int(newValue)
        elif fieldName == "Rating":
            newValue = newValue.upper()
        elif fieldName not in allowedFields:
            print("Invalid field name")    
            return
        
        cursor.execute(f"UPDATE tblfilms SET {fieldName} = ? WHERE filmID = ?",(newValue,idField))
        conn.commit()
        print(f"Record {idField} updated!")

    except (sql.OperationalError, ValueError) as e:
        conn.rollback()
        print(f"Record not updated: {e}")

if __name__ == "__main__":
    updateRecord()
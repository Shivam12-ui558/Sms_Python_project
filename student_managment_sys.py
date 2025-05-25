st_db = []  

while True:
    choice = int(input("""\nMain Menu
                 1. Enter student details
                 2. Update student details
                 3. Delete student details
                 4. Show all students     
                 5. Search students
                 6. Exit
                 Enter your choice: """))

    if choice == 1:  
        st = []
        lst = ["Roll No", "Name", "Email", "Semester", "CGPA"]
        for i in lst:
            st.append(input(f"Enter your {i}: "))
        st_db.append(st)
        print("Student added successfully!")

    elif choice == 2:  
        rollno = input("Enter roll number of student to update: ")
        found = False
        for student in st_db:
            if student[0] == rollno:  
                found = True
                print("Student found. Enter new details (leave blank to keep old value).")
                
                fields = ["Roll No", "Name", "Email", "Semester", "CGPA"]  
                for i in range(len(student)):  
                    new_value = input(f"Enter new {fields[i]} (current: {student[i]}): ")
                    if new_value:
                        student[i] = new_value 

                print("Student details updated successfully!")
                break

        if not found:
            print("Student with given roll number not found!")

    elif choice == 3:  
        rollno = input("Enter roll number of student to delete: ")
        found = False
        for student in st_db:
            if student[0] == rollno:
                st_db.remove(student)
                found = True
                print("Student deleted successfully!")
                break

        if not found:
            print("Student with given roll number not found!")

    elif choice == 4:  
        print("\nAll Students:")
        if not st_db:
            print("No students found.")
        else:
            for student in st_db:
                print(student)

    elif choice == 5:  
        rollno = input("Enter roll number of student to search: ")
        found = False
        for student in st_db:
            if student[0] == rollno:
                found = True
                print("\nStudent Details:")
                fields = ["Roll No", "Name", "Email", "Semester", "CGPA"]
                for i in range(len(student)):
                    print(f"{fields[i]}: {student[i]}")
                break

        if not found:
            print("Student with given roll number not found!")

    elif choice == 6: 
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")







    

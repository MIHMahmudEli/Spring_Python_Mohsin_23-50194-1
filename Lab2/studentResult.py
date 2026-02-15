"""
This is a CLI application to calculate student results.
And (Possibly) Export the results to a CSV file.
"""

#Helper functions
#function to prevent user to provide empty input
def get_non_empty_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:   
            print("Input cannot be empty. Please try again.")
            
            

# CLI menu printing function
def menu()-> None:
    print("\n===Student Result Management System===")
    print("1) Add Student + Compute Result")
    print("2) List Student + Result Summary")
    print("3) Search Student by ID")
    print("4) Delete Student by ID")
    print("5) Export All Results to CSV")
    print("6) Exit")

#App Action Implementation
#function to add student and compute result
def add_student(students: list[dict]) -> None:
    sid = get_non_empty_input("Enter student ID: ")
    name = get_non_empty_input("Enter student name: ")
    
    
    #collecting marks for 5 subjects
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i} (0-100): ").strip())
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    #calculating total and average
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    
    #determining grade based on average
    if average_marks >= 90:
        grade = 'A'
    elif average_marks >= 80:
        grade = 'B'
    elif average_marks >= 70:
        grade = 'C'
    elif average_marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    #storing student data in a dictionary
    student_data = {
        "name": name,
        "id": student_id,
        "marks": marks,
        "total": total_marks,
        "average": average_marks,
        "grade": grade
    }
    
    students.append(student_data)
    print(f"Student {name} added successfully with grade {grade}.")
    
    
def list_students():
    print("Listing students and result summary...")

def search_student():
    print("Searching student by ID...")

def delete_student():
    print("Deleting student by ID...")

def export_to_csv():
    print("Exporting all results to CSV...")
    



#main function to run the application
def main():
    
    #list to store student data in memory
    students = []
    
    while True:
        menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        #match-case statement to handle user choices
        match choice:
            case '1':
                add_student()
                
            case '2':
                list_students()
                
            case '3':
                search_student()
                
            case '4':
                delete_student()
                
            case '5':
                export_to_csv()
                
            case '6':
                print("Exiting the application.")
                break
            case _:
                print("Invalid choice. Please try again.")

#magic function (Dunder functions)  
if __name__ == "__main__":
    main()
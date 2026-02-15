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

#Function to input name and clean it
def get_clean_name(prompt: str) -> str:
    return get_non_empty_input(prompt).title().strip()

#Finction to input integer and validate it
def get_valid_integer(prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
    while True:
        value = input(prompt).strip()
        try:
            num = int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if min_value is not None and num < min_value:
            print(f"Input must be at least {min_value}. Please try again.")
            continue
        if max_value is not None and num > max_value:
            print(f"Input must be at most {max_value}. Please try again.")
            continue
        return num

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
    name = get_clean_name("Enter student name: ")
    
    
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
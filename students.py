import csv
import os
from datetime import datetime

FILE = "students.csv"

def initialize_file():
    """Create CSV file with headers if it doesn't exist"""
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Age", "Email", "Created_At"])
        print("Database initialized successfully\n")

def add_student():
    """Add a new student record"""
    try:
        sid = input("Enter Student ID: ").strip()
        if not sid:
            print("❌ Student ID cannot be empty")
            return
        
        name = input("Enter Name: ").strip()
        if not name:
            print("❌ Name cannot be empty")
            return
        
        age = input("Enter Age: ").strip()
        if not age.isdigit() or int(age) < 5 or int(age) > 100:
            print("❌ Age must be a valid number between 5 and 100")
            return
        
        email = input("Enter Email (optional): ").strip()
        
        # Check if student ID already exists
        if student_exists(sid):
            print(f"❌ Student with ID {sid} already exists")
            return
        
        with open(FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([sid, name, age, email, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        
        print("✅ Student added successfully\n")
    except Exception as e:
        print(f"❌ Error adding student: {e}\n")

def view_students():
    """Display all student records"""
    try:
        if not os.path.exists(FILE):
            print("❌ No records found\n")
            return
        
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            records = list(reader)
            
            if len(records) <= 1:
                print("❌ No student records found\n")
                return
            
            # Print header
            print("\n" + "="*80)
            print(f"{'ID':<12} {'Name':<20} {'Age':<8} {'Email':<25} {'Created_At':<15}")
            print("="*80)
            
            # Print records (skip header)
            for row in records[1:]:
                if len(row) >= 3:
                    print(f"{row[0]:<12} {row[1]:<20} {row[2]:<8} {row[3] if len(row) > 3 else '':<25} {row[4] if len(row) > 4 else '':<15}")
            
            print("="*80 + "\n")
            print(f"Total Students: {len(records) - 1}\n")
    
    except Exception as e:
        print(f"❌ Error viewing students: {e}\n")

def search_student():
    """Search for a student by ID or Name"""
    try:
        if not os.path.exists(FILE):
            print("❌ No records found\n")
            return
        
        search_term = input("Enter Student ID or Name to search: ").strip().lower()
        if not search_term:
            print("❌ Search term cannot be empty\n")
            return
        
        found = False
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            records = list(reader)
            
            print("\n" + "="*80)
            print(f"{'ID':<12} {'Name':<20} {'Age':<8} {'Email':<25} {'Created_At':<15}")
            print("="*80)
            
            for row in records[1:]:
                if len(row) >= 2:
                    if search_term in row[0].lower() or search_term in row[1].lower():
                        print(f"{row[0]:<12} {row[1]:<20} {row[2] if len(row) > 2 else '':<8} {row[3] if len(row) > 3 else '':<25} {row[4] if len(row) > 4 else '':<15}")
                        found = True
            
            print("="*80 + "\n")
            if not found:
                print(f"❌ No student found matching '{search_term}'\n")
            else:
                print(f"✅ Search completed\n")
    
    except Exception as e:
        print(f"❌ Error searching student: {e}\n")

def delete_student():
    """Delete a student record by ID"""
    try:
        if not os.path.exists(FILE):
            print("❌ No records found\n")
            return
        
        sid = input("Enter Student ID to delete: ").strip()
        if not sid:
            print("❌ Student ID cannot be empty\n")
            return
        
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            records = list(reader)
        
        # Find and remove the student
        new_records = [records[0]]  # Keep header
        found = False
        
        for row in records[1:]:
            if len(row) > 0 and row[0] != sid:
                new_records.append(row)
            elif len(row) > 0 and row[0] == sid:
                found = True
        
        if not found:
            print(f"❌ Student with ID {sid} not found\n")
            return
        
        # Write back to file
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(new_records)
        
        print(f"✅ Student with ID {sid} deleted successfully\n")
    
    except Exception as e:
        print(f"❌ Error deleting student: {e}\n")

def update_student():
    """Update a student record"""
    try:
        if not os.path.exists(FILE):
            print("❌ No records found\n")
            return
        
        sid = input("Enter Student ID to update: ").strip()
        if not sid:
            print("❌ Student ID cannot be empty\n")
            return
        
        if not student_exists(sid):
            print(f"❌ Student with ID {sid} not found\n")
            return
        
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            records = list(reader)
        
        # Find and update the student
        found = False
        for i, row in enumerate(records):
            if len(row) > 0 and row[0] == sid:
                print(f"\nCurrent details: ID={row[0]}, Name={row[1]}, Age={row[2]}, Email={row[3] if len(row) > 3 else 'N/A'}")
                
                name = input("Enter new Name (press Enter to skip): ").strip()
                age = input("Enter new Age (press Enter to skip): ").strip()
                email = input("Enter new Email (press Enter to skip): ").strip()
                
                if name:
                    records[i][1] = name
                if age:
                    if not age.isdigit() or int(age) < 5 or int(age) > 100:
                        print("❌ Age must be a valid number between 5 and 100\n")
                        return
                    records[i][2] = age
                if email:
                    records[i][3] = email
                
                found = True
                break
        
        if found:
            with open(FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(records)
            print(f"✅ Student with ID {sid} updated successfully\n")
        else:
            print(f"❌ Student with ID {sid} not found\n")
    
    except Exception as e:
        print(f"❌ Error updating student: {e}\n")

def student_exists(sid):
    """Check if student ID exists"""
    if not os.path.exists(FILE):
        return False
    
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0 and row[0] == sid:
                    return True
    except:
        pass
    
    return False

def main_menu():
    """Display main menu and handle user input"""
    initialize_file()
    
    while True:
        print("\n" + "="*40)
        print("     STUDENT MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\n✅ Thank you for using Student Management System. Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6\n")

if __name__ == "__main__":
    main_menu()

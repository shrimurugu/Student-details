# Student Details Management System

A Python-based command-line application for managing student records using CSV files.

## Features

✨ **Core Features:**
- ✅ **Add Student** - Add new student records with validation
- ✅ **View Students** - Display all student records in a formatted table
- ✅ **Search Student** - Find students by ID or Name
- ✅ **Update Student** - Modify existing student information
- ✅ **Delete Student** - Remove student records
- ✅ **Exit** - Gracefully close the application

## Improvements

### Error Handling
- ✔️ Validates all user inputs
- ✔️ Checks for duplicate student IDs
- ✔️ Validates age range (5-100)
- ✔️ Proper exception handling with user-friendly messages
- ✔️ Handles missing database files gracefully

### Code Structure
- ✔️ Modular functions for each operation
- ✔️ Better code organization and readability
- ✔️ Added database initialization
- ✔️ Improved menu presentation
- ✔️ Added timestamps for record creation

### Data Management
- ✔️ Extended fields: ID, Name, Age, Email, Created_At
- ✔️ CSV headers for better data organization
- ✔️ Formatted table output for better readability
- ✔️ Student count display in view mode

## Usage

### Running the Application

```bash
python students.py
```

### Menu Options

```
1. Add Student       - Create a new student record
2. View All Students - Display all student records
3. Search Student    - Find a student by ID or Name
4. Update Student    - Modify existing student details
5. Delete Student    - Remove a student record
6. Exit              - Close the application
```

### Example Workflow

```
Enter your choice (1-6): 1
Enter Student ID: S001
Enter Name: John Doe
Enter Age: 20
Enter Email (optional): john@example.com
✅ Student added successfully

Enter your choice (1-6): 2
[Display of all students in table format]

Enter your choice (1-6): 3
Enter Student ID or Name to search: John
[Display of matching records]

Enter your choice (1-6): 4
Enter Student ID to update: S001
[Update options for the student]

Enter your choice (1-6): 5
Enter Student ID to delete: S001
✅ Student with ID S001 deleted successfully

Enter your choice (1-6): 6
✅ Goodbye!
```

## Data Storage

Student data is stored in `students.csv` with the following columns:
- **ID** - Unique student identifier
- **Name** - Student's full name
- **Age** - Student's age
- **Email** - Student's email address
- **Created_At** - Timestamp of record creation

## Requirements

- Python 3.x
- Built-in `csv` module
- Built-in `os` module
- Built-in `datetime` module

## File Structure

```
Student-details/
├── students.py          # Main application
├── students.csv         # Data file (auto-created)
├── README.md           # Documentation
├── CHANGELOG.md        # Version history
└── .gitignore         # Git ignore file
```

## Future Enhancements

- 📊 Statistics and reporting
- 💾 Export to different formats (Excel, PDF)
- 🔐 User authentication
- 🗄️ Database backend (SQLite, MySQL)
- 🎨 GUI interface
- 📱 Mobile app version
- 📧 Email notifications
- 📈 Grade tracking and management

## License

This project is open source and available to everyone.

## Author

**shrimurugu**

---

**Last Updated:** 2026-06-01

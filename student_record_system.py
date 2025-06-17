import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create the students table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    year INTEGER
)
''')

# Function to add a student
def add_student(roll_no, name, department, year):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll_no, name, department, year))
    conn.commit()
    print("✅ Student added successfully!")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print("\nStudent Records:")
    for row in records:
        print(row)

# Function to update a student
def update_student(roll_no, name, department, year):
    cursor.execute("UPDATE students SET name=?, department=?, year=? WHERE roll_no=?",
                   (name, department, year, roll_no))
    conn.commit()
    print("✅ Student updated successfully!")

# Function to delete a student
def delete_student(roll_no):
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    print("🗑️ Student deleted successfully!")

# Test cases for environments where interactive input isn't supported
def run_test_cases():
    print("\nRunning test cases...")
    add_student(1, "Mallikarjuna", "CSE", 3)
    add_student(2, "Anjali", "ECE", 2)
    view_students()
    update_student(1, "Mallikarjuna K.", "CSE", 4)
    delete_student(2)
    view_students()

if __name__ == "__main__":
    run_test_cases()
    conn.close()

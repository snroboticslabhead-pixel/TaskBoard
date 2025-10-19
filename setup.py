from database import students, tasks, submissions, admins
from models import AdminModel
import bcrypt
from bson import ObjectId

def setup_database():
    # Create default admin user
    if admins.count_documents({}) == 0:
        AdminModel.create_admin('admin', 'admin123')
        print("✅ Default admin created: username='admin', password='admin123'")
    
    # Create sample tasks
    if tasks.count_documents({}) == 0:
        sample_tasks = [
            {
                'title': 'Blink LED',
                'description': 'Make an LED blink every second using Arduino',
                'language': 'arduino',
                'campusTarget': ['Subhash Nagar', 'Yamuna Campus', 'I20 Campus'],
                'gradeTarget': ['9A', '9B', '10A'],
                'default_code': 'void setup() {\n  pinMode(LED_BUILTIN, OUTPUT);\n}\n\nvoid loop() {\n  digitalWrite(LED_BUILTIN, HIGH);\n  delay(1000);\n  digitalWrite(LED_BUILTIN, LOW);\n  delay(1000);\n}'
            },
            {
                'title': 'Python Hello World',
                'description': 'Print a greeting message in Python and get user input',
                'language': 'python',
                'campusTarget': ['Subhash Nagar', 'Yamuna Campus'],
                'gradeTarget': ['10A', '10B'],
                'default_code': 'print("Hello, Smart Campus!")\n\n# Add your code below\nname = input("Enter your name: ")\nprint(f"Welcome, {name}!")'
            }
        ]
        
        for task in sample_tasks:
            tasks.insert_one(task)
        print("✅ Sample tasks created")
    
    # Create sample students
    if students.count_documents({}) == 0:
        sample_students = [
            {
                'studentID': 'SUB-101',
                'name': 'Rahul Sharma',
                'campus': 'Subhash Nagar',
                'grade': '9A',
                'section': 'A',
                'password': '123456'
            },
            {
                'studentID': 'YAM-102', 
                'name': 'Priya Patel',
                'campus': 'Yamuna Campus',
                'grade': '10A',
                'section': 'B',
                'password': '123456'
            }
        ]
        
        for student in sample_students:
            from models import StudentModel
            StudentModel.create_student(student)
        print("✅ Sample students created")
    
    print("🎉 Database setup completed!")

if __name__ == "__main__":
    setup_database()
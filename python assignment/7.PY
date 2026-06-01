def student_record_system():
    students = {}
    
    # Adding students to the record
    students['101'] = {'Name': 'ananya', 'Grade': 'A', 'Major': 'Physics'}
    students['102'] = {'Name': 'bishal', 'Grade': 'B+', 'Major': 'Mathematics'}
    
    print("Student Records:")
    for roll_no, info in students.items():
        print(f"Roll No: {roll_no} | Name: {info['Name']} | Grade: {info['Grade']} | Major: {info['Major']}")

student_record_system()
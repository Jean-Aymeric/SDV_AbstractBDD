from database.model import Employee

# departments = Department.getAll()
# for department in departments:
#    print(department)

employees = Employee.getAll()
for employee in employees:
    print(employee)

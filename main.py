from database.model import Department

departments = Department.getAll()
for department in departments:
    print(department)
    print(department.toDict())

from flask import jsonify, Flask, request

from database.model import Department, Employee

app = Flask(__name__)


@app.route('/getAllDepartments', methods=['GET'])
def getAllDepartments():
    departments = Department.getAll()
    return jsonify([department.toDict() for department in departments])


@app.route('/getEmployeesFromTo', methods=['GET'])
def getEmployeesFromTo():
    employees = Employee.getFromTo(request.json['from'], request.json['to'])
    return jsonify([employee.toDict() for employee in employees])


@app.route('/delEmployeeById', methods=['Delete'])
def delEmployeeById():
    Employee.delByEmp_no(request.json['emp_no'])
    return jsonify({'status': 'ok'})


app.run(host='localhost', port=5000)

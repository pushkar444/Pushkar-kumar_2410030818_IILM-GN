## Experiment 1 – Table Operations on Employee_Master
# Aim:- To perform table creation, deletion, update, alteration, and drop operations using employee_master table.

# Query 1:- Create employee_master Table Using employee.
```sql
CREATE TABLE employee_master AS
SELECT * FROM employee;
```
# Query 2:- Delete All Records from employee_master Where DeptNo is 10.
```sql
DELETE FROM employee_master
WHERE deptno = 10;
```
# Query 3:- Update Salary by 10% for DeptNo 20 in employee_master.
```sql
UPDATE employee_master
SET sal = sal + (sal * 0.10)
WHERE deptno = 20;
```
# Query 4:- Alter sal Column Size to DECIMAL(10,2) in employee_master.
```sql
ALTER TABLE employee_master
MODIFY sal DECIMAL(10,2);
```
# Query 5:- Drop employee_master Table.
```sql
DROP TABLE employee_master;
```
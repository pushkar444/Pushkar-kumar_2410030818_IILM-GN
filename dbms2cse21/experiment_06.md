## Experiment 6 – Date & Special Functions
# Aim:- To perform date manipulation, formatting, and special SQL functions on the employee table.

# Query 1:- Display empno, ename and department name instead of deptno.
```sql
SELECT empno,
    ename,
    CASE deptno
        WHEN 10 THEN 'RESEARCH'
        WHEN 20 THEN 'ACCOUNTING'
        WHEN 30 THEN 'SALES'
        WHEN 40 THEN 'OPERATIONS'
    END AS department_name
FROM employee;
```
# Query 2:-  Display your age in days.
```sql
SELECT DATEDIFF(CURDATE(), '2004-01-01') AS age_in_days;
```
# Query 3:- Display your age in months.
```sql 
SELECT TIMESTAMPDIFF(MONTH, '2004-01-01', CURDATE()) AS age_in_months;
```
# Query 4:- Display the current date in formatted style.
```sql  
SELECT DATE_FORMAT(CURDATE(), '%D %M %W %Y') AS formatted_date;
```
# Query 5:- Display the following output for each row from employee table - 'Scott has joined the company on Wednesday 13th August Nineteen Ninety'
```sql 
SELECT CONCAT(
    ENAME,
    ' has joined the company on ',
    DATE_FORMAT(HIREDATE, '%W %D %M %Y')
) AS DETAILS
FROM EMPLOYEE;
```
# Query 6:- Find the date for nearest Saturday after current date.
```sql
SELECT DATE_ADD(CURDATE(),
    INTERVAL (7 - WEEKDAY(CURDATE()) + 5) % 7 DAY) AS next_saturday;
```
# Query 7:- Display current time.
```sql
SELECT CURTIME() AS curr_time;
```
# Query 8:- Display the date three months before the current date.
```sql
SELECT DATE_SUB(CURDATE(), INTERVAL 3 MONTH) AS three_months_before;
```
# Query 9:- Display employees who joined in the month of December.
```sql
SELECT *
FROM employee
WHERE MONTH(hiredate) = 12;
```
# Query 10:- Display employees whose first 2 characters of hiredate match last 2 characters of salary.
```sql
SELECT *
FROM employee
WHERE LEFT(hiredate,2) = RIGHT(sal,2);
```
# Query 11:- Display employees whose 10% of salary equals the year of joining.
```sql
SELECT *
FROM employee
WHERE (sal * 0.10) = YEAR(hiredate);
```
# Query 12:- Display employees who joined before 15th of the month.
```sql
SELECT *
FROM employee
WHERE DAY(hiredate) < 15;
```
# Query 13:- Display employees who joined after 15th of the month.
```sql
SELECT *
FROM employee
WHERE DAY(hiredate) > 15;
```
# Query 14:- Display employees whose joining date is not null.
```sql
SELECT *
FROM employee
WHERE hiredate IS NOT NULL;
```
CREATE DATABASE chat_assistant;
USE chat_assistant;

-- Drop existing tables for clean execution
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- Create Departments Table with a primary key on 'id'
CREATE TABLE departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    manager VARCHAR(100) NOT NULL
); 

-- Insert department data
INSERT INTO departments (name, manager) VALUES
    ('Sales', 'Alice'),
    ('Engineering', 'Bob'),
    ('Marketing', 'Charlie'),
    ('HR', 'David'),
    ('Finance', 'Eva'),
    ('IT', 'Steve'),
    ('Customer Support', 'Nancy'),
    ('Operations', 'Philip'),
    ('Legal', 'Monica');

-- Create Employees Table with a primary key on 'id' and a foreign key on 'department_id'
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,  -- Foreign key to 'departments' table
    salary INT NOT NULL,
    hire_date DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    salary INT NOT NULL,
    hire_date DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    salary INT NOT NULL,
    hire_date DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Query to view departments
SELECT * FROM departments;
select * from employees;
-- Retrieve all departments
SELECT * FROM departments;

-- Retrieve all employees
SELECT * FROM employees;

-- Count the number of employees in the company
SELECT COUNT(email) AS cnt FROM employees;

-- List all employees in the Sales department
SELECT name FROM employees 
WHERE department_id = (SELECT id FROM departments WHERE name = "Sales");

-- Retrieve the manager of a specific department
SELECT manager FROM departments WHERE name = "Engineering";

-- List all employees hired after a certain date
SELECT name FROM employees WHERE hire_date > '2023-01-01'; 

-- Retrieve all employees along with their department names
SELECT e.name, d.name AS department 
FROM employees e
JOIN departments d ON e.department_id = d.id;

-- Get the average salary of employees in a specific department
SELECT AVG(salary) FROM employees 
WHERE department_id = (SELECT id FROM departments WHERE name = "Finance");

-- Retrieve employees sorted by hire date (most recent first)
SELECT name, hire_date FROM employees ORDER BY hire_date DESC;

-- Retrieve employees with a salary above a certain threshold
SELECT name, salary FROM employees WHERE salary > 60000;






  

 



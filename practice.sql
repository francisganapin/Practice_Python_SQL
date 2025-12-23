-- ==========================================
-- STEP 1: SETUP YOUR DATABASE
-- Run these commands to create the table and add data.
-- ==========================================

-- 1. Create the students table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER,
    favorite_subject TEXT
);

-- 2. Insert sample data
INSERT INTO students (name, age, grade, favorite_subject) VALUES 
('Alice', 14, 9, 'Math'),
('Bob', 15, 10, 'Science'),
('Charlie', 14, 9, 'History'),
('Diana', 16, 11, 'Math'),
('Evan', 15, 10, 'Science'),
('Fiona', 14, 9, 'Art'),
('George', 17, 12, 'Math');

-- ==========================================
-- STEP 2: YOUR PRACTICE PROBLEM
-- ==========================================

-- PROBLEM 1:
-- Write a query to find the names of all students who like 'Math'.
-- Expected Output: Alice, Diana, George

-- Write your solution below this line:
-- SELECT ...

-- ==========================================
-- PROBLEM 2:
-- Count how many students are in grade 9.
-- Expected Output: 3
-- Hint: Use COUNT(*) and WHERE

-- Write your solution below this line:
-- SELECT ...

-- ==========================================
-- PROBLEM 3:
-- Find the average age of all students.
-- Expected Output: 15.0
-- Hint: Use the AVG() function

-- Write your solution below this line:
-- SELECT ...

-- ==========================================
-- PROBLEM 4:
-- List all students sorted by their grade, from highest to lowest.
-- Expected Output: George (12), Diana (11), Bob (10), Evan (10), Alice (9), Charlie (9), Fiona (9)
-- Hint: Use ORDER BY ... DESC

-- Write your solution below this line:
-- SELECT ...

-- ==========================================
-- PROBLEM 5:
-- Count how many students like each subject.
-- Expected Output: 
--   Art: 1
--   History: 1
--   Math: 3
--   Science: 2
-- Hint: Use GROUP BY favorite_subject

-- Write your solution below this line:
-- SELECT ...

-- ==========================================
-- PROBLEM 6:
-- Find subjects that have more than 1 student.
-- Expected Output: Math (3), Science (2)
-- Hint: Use GROUP BY ... HAVING COUNT(*) > 1

-- Write your solution below this line:
-- SELECT ...

-- ==========================================
-- PROBLEM 7:
-- Find the name and age of the oldest student.
-- Expected Output: George, 17
-- Hint: Use ORDER BY age DESC LIMIT 1

-- Write your solution below this line:
-- SELECT ...

-- ==========================================
-- PROBLEM 8:
-- Find students who are either in grade 10 OR like 'Science'.
-- Expected Output: Bob, Evan
-- Hint: Use WHERE ... OR ...

-- Write your solution below this line:
-- SELECT ...

-- ==========================================
-- STEP 3: ADD A NEW TABLE (RELATIONSHIPS)
-- ==========================================

-- 1. Create the scores table
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    score INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 2. Insert sample scores
INSERT INTO scores (student_id, subject, score) VALUES 
(1, 'Math', 90), -- Alice
(1, 'Science', 85),
(2, 'Science', 92), -- Bob
(2, 'History', 88),
(3, 'History', 75), -- Charlie
(3, 'Math', 78),
(4, 'Math', 95), -- Diana
(5, 'Science', 80), -- Evan
(6, 'Art', 98), -- Fiona
(7, 'Math', 88); -- George

-- ==========================================
-- PROBLEM 9:
-- Find the name of the student and their score in 'Math'.
-- Expected Output: Alice (90), Charlie (78), Diana (95), George (88)
-- Hint: Use JOIN students ON scores.student_id = students.id

-- Write your solution below this line:
-- SELECT ...

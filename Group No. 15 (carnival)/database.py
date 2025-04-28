 Step 1: Create Database
CREATE DATABASE IF NOT EXISTS quizapp;
USE quizapp;

-- Step 2: Create Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Step 3: Create Questions Table
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option1 VARCHAR(100) NOT NULL,
    option2 VARCHAR(100) NOT NULL,
    option3 VARCHAR(100) NOT NULL,
    option4 VARCHAR(100) NOT NULL,
    answer INT NOT NULL  -- correct option number (1 to 4)
);

-- Step 4: Insert Sample Questions
INSERT INTO questions (question, option1, option2, option3, option4, answer) VALUES
('What is the capital of France?', 'Berlin', 'Madrid', 'Paris', 'Rome', 3),
('Which language is used for web apps?', 'Python', 'HTML', 'C++', 'Java', 2),
('What does CPU stand for?', 'Central Process Unit', 'Central Processing Unit', 'Computer Personal Unit', 'Central Processor Utility', 2),
('Which planet is known as the Red Planet?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 2),
('Who wrote "Romeo and Juliet"?', 'Charles Dickens', 'Leo Tolstoy', 'William Shakespeare', 'Mark Twain', 3);

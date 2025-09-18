# Control Flow and Loops in Python  

This project introduces **control flow** and **loops**, two essential concepts for writing logical and efficient Python programs. I learnt how to make decisions in my code using conditional statements and automate repetitive tasks using loops.

---

## 📖 Project Objectives  

By the end of this project, I am able to:  

- Explain control flow and its role in programming.  
- Use conditional statements (`if`, `elif`, `else`) to control program execution.  
- Implement **match–case** statements (Python 3.10+) as an alternative to multiple `if/elif`.  
- Apply best practices for readability and efficiency with match–case.  
- Use **for loops** to iterate over sequences.  
- Use **while loops** to repeat actions while conditions hold true.  
- Implement **nested loops** for complex patterns or multidimensional data.  

---

## Tasks  

### 0. Weather Recommendation Program (`weather_advice.py`)  

- Prompts the user for today’s weather (`sunny/rainy/cold`).  
- Uses `if/elif/else` statements to recommend clothing.  
- Handles invalid input gracefully.  

**Example:**  

``` bash
Enter the first number: 10
Enter the second number: 0
Choose the operation (+, -, *, /): /
Cannot divide by zero.
```

---

### 2. Multiplication Table Generator (`multiplication_table.py`)  

- Prompts the user for a number.  
- Uses a **for loop** to print its multiplication table from 1–10.  

**Example:**

```bash
Enter a number to see its multiplication table: 5
5 * 1 = 5
5 * 2 = 10
...
5 * 10 = 50
```

---

### 3. Drawing Patterns with Nested Loops (`pattern_drawing.py`)

- Prompts the user for a pattern size (positive integer).  
- Uses a **while loop** and **nested for loops** to draw a square pattern.  

**Example:**  

``` bash
Enter the size of the pattern: 4
****
****
****
****
```

---

### 4. Personal Daily Reminder (`daily_reminder.py`)  

- Prompts the user for:  
  - A task description  
  - Its priority (`high/medium/low`)  
  - Whether it is time-bound (`yes/no`)  
- Uses `match–case` and `if` to print a customized reminder.  

**Example (time-bound):**  

```bash
Enter your task: Finish project report
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes

Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
```

**Example (not time-bound):**  

```bash
Enter your task: Read a book
Priority (high/medium/low): low
Is it time-bound? (yes/no): no

Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
```

---

## Repository Structure  

alx_be_python/
└── control-flow/
├── weather_advice.py
├── match_case_calculator.py
├── multiplication_table.py
├── pattern_drawing.py
├── daily_reminder.py
└── README.md

---

## Requirements  

- Python 3.10+ (for `match–case`)  
- Basic knowledge of conditional statements and loops  

## How to Run  

### Installation

#### Clone the repository

git clone [https://github.com/The-Motolani/alx_be_python.git](https://github.com/The-Motolani/alx_be_python.git)  

#### Navigate into the project directory

cd control-flow  

#### Run the program

python3 filename.py  

### Usage

**Example of how to run or use the project:**
Run any script from the `control-flow` directory using:  

```bash
python3 script_name.py 
```

**For example:**

```bash
python3 weather_advice.py
```

---

## Author

Motolani Alebiosu. Project done as part of the ALX Backend Engineering - Python module.

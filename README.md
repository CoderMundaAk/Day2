# Day2
# 🐍 Python Inheritance Projects

This repository contains two beginner-friendly Python projects demonstrating the concept of **class inheritance** using `Animal/Dog` and `Employee/Manager` examples.

---

## 🐾 Project 1: Animal / Dog Inheritance

### 🔧 Description
This project demonstrates how inheritance works in object-oriented programming by using an `Animal` class as the **parent**, and a `Dog` class as the **child**.

### 📦 Features
- `Animal` class:
  - Properties: `name`, `species`
  - Method: `make_sound()`
- `Dog` class:
  - Inherits from `Animal`
  - Overrides `make_sound()` to return `"woof!"`
  - Adds a new method: `fetch_ball()`

### 🧪 Example Output
Animal: jackey, pitchata
Dog: ff, hh
Animal makes sound: wowo
Dog makes sound: woof!
Dog fetches ball: pick up the ball

markdown
Copy
Edit

---

## 💼 Project 2: Employee / Manager Inheritance

### 🔧 Description
This project demonstrates inheritance in a workplace context with an `Employee` class and a `Manager` subclass.

### 📦 Features
- `Employee` class:
  - Properties: `name`, `salary`
  - Method: `display_info()`
- `Manager` class:
  - Inherits from `Employee`
  - Adds new methods: `hire_employee()` and `team_size()`

### 🧪 Example Output
Employee: Ak, Salary: 444444
Manager: Bilal, Salary: 555555555555
Manager hires employee: The total hired employees: 5
Manager team size: Total team size: 25

yaml
Copy
Edit

---

## ✅ What I Learned

- How to define **parent and child classes** using inheritance.
- How to use `super()` to call the parent constructor.
- How to **override methods** in child classes.
- How to add new features in child classes.
- Why inheritance helps reduce code repetition.

---

## 📁 Folder Structure

/inheritance-projects
│
├── animal_dog.py
├── employee_manager.py
└── README.md

yaml
Copy
Edit

---

## 🛠 How to Run

1. Clone this repository:
git clone https://github.com/your-username/inheritance-projects.git
cd inheritance-projects

markdown
Copy
Edit
2. Run the Python files:
python animal_dog.py
python employee_manager.py

yaml
Copy
Edit

---

## 🔗 Author

**Your Name** – [@yourgithubusername](https://github.com/yourgithubusername)

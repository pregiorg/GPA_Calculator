# 🎓 GPA Calculator
A Python script that calculates your semester GPA from course credits and marks, with input validation built in.
## Features
- Two input modes: total marks per course, or Mid-Sem + Internal + End-Sem breakdown
- Validates all numeric input — rejects negatives, non-numbers, and out-of-range marks
- Re-prompts on bad input instead of crashing
- Catches the zero-credits edge case before dividing
- Converts marks to grade points using ceiling-based rounding
- Displays final GPA rounded to 2 decimal places
## How It Works
```
📋 Per Course:
├── Enter course name (defaults to "Course N" if blank)
├── Enter credits        → validated, must be > 0
├── Enter marks
│   ├── Mode 0 → total marks (0-100)
│   └── Mode 1 → mid-sem + internal + end-sem (each 0-100, summed)
├── Convert marks → grade point (ceil(marks / 10))
└── Accumulate credits × grade point
GPA = total weighted points / total credits
```
## Usage
1. Clone the repo:
```bash
git clone https://github.com/pregiorg/GPA-Calculator.git
cd gpa_calculator
```
2. Run:
```bash
python gpa_calculator.py
```
3. Follow the prompts:
```
Enter the number of courses: 2
Enter the marks type (0 for total marks, 1 for mid-semester + internal + end-semester): 0
Enter the name of course: Math
Enter the credits for Math: 4
Enter the marks obtained in Math: 85
```
## Requirements
- Python 3.x
- No external libraries — uses `math` from the standard library
## Customization
Adjust the grading scale by editing the grade point formula in `calculate_gpa`:
```python
course_point = math.ceil(course_marks / 10) if course_marks > 0 else 0
# Example: switch to a stricter 4.0 scale conversion here
```
## What I Learned
- Writing reusable input-validation helpers (`get_positive_int`, `get_marks`)
- Handling `ValueError` gracefully with `try/except`
- Designing for edge cases: zero courses, zero credits, overflowing marks
- Re-prompting loops vs. crashing on bad input
- Keeping `main` thin by delegating validation to helper functions
## License
MIT

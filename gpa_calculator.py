import math


def get_positive_int(prompt, allow_zero=False):
    """
    Prompt until a valid non-negative (or positive) integer is entered.
    Args:
        prompt (str): The prompt to display to the user.
        allow_zero (bool): Whether to allow zero as a valid input.
    Return:
         Validated integer input from the user.
    """
    while True:
        raw =  input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if value < 0:
            print("Please enter a non-negative integer.")
            continue
        if value == 0 and not allow_zero:
            print("Zero is not allowed. Please enter a positive integer.")
            continue
        return value
    


def get_marks(prompt, max_marks=100):
    """
    Prompt until a valid marks value is entered.
    Args:
        prompt (str): The prompt to display to the user.
        max_marks (int): The maximum marks allowed.
    Return:
         Validated marks input from the user.
    """
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if value < 0 or value > max_marks:
            print(f"Please enter a value between 0 and {max_marks}.")
            continue
        return value
    


def calculate_gpa(num_course, marks):
    """
    Calculate GPA for semester based on given number of courses and their marks.
    Args:
    num_course (int): The number of courses.
    marks(int): The marks obtained in each course.
    Return:
    Calculated GPA value.
    """
    credits = 0
    total_credits = 0

    for i in range(num_course):
        course_name = input(f"Enter the name of course:").strip()
        if not course_name:
            course_name = f"Course {i + 1}"


        course_credits = get_positive_int(f"Enter the credits for {course_name}: ")

        if marks == 0:
            course_marks = get_marks(f"Enter the marks obtained in {course_name}: ")
        else:
            mid_sem_marks = get_marks(f"Enter the mid-semester marks obtained in {course_name}: ")

            internal_marks = get_marks(f"Enter the internal marks obtained in {course_name}: ")

            end_sem_marks = get_marks(f"Enter the end-semester marks obtained in {course_name}: ")

            course_marks = mid_sem_marks + internal_marks + end_sem_marks
            if course_marks > 100:
                print(f"Total marks for {course_name} exceed 100. Please re-enter the marks.")
                # retry this course
                i -= 1
                continue
        print()

        course_point = math.ceil(course_marks / 10) if course_marks > 0 else 0
        credits += course_point * course_credits
        total_credits += course_credits

    if total_credits == 0:
        raise ValueError("Total credits cannot be zero. Please ensure at least one course has credits.")

    gpa = credits / total_credits
    return gpa


if __name__ == "__main__":
    print("\n------------------------------------------")
    print("GPA Calculator: ")
    print("------------------------------------------")

    num_courses = get_positive_int("Enter the number of courses: ")
    marks = get_positive_int("Enter the marks type (0 for total marks, 1 for mid-semester + internal + end-semester): ", allow_zero=True)

    try:
        gpa = calculate_gpa(num_courses, marks)
        print("Your GPA for this Semester is:", round(gpa, 2))
    except ValueError as e:
        print("Error:", e)

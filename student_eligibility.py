"""Python port of StudentEligibility.java (Session 8 assignment),
plus register_student(), which depends on an external email sender."""


def is_eligible(age):
    """Eligible age is 17 to 60 (inclusive). Negative age raises ValueError."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    return 17 <= age <= 60


def calculate_final_score(midterm, final_exam):
    """Final score = midterm 40% + final exam 60%. Each must be 0..100."""
    if midterm < 0 or midterm > 100:
        raise ValueError("Midterm score must be between 0 and 100")
    if final_exam < 0 or final_exam > 100:
        raise ValueError("Final exam score must be between 0 and 100")
    return midterm * 0.40 + final_exam * 0.60


def classify_grade(score):
    """Classify a score into a letter grade A/B/C/D/F."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def register_student(name, age, email, send_email):
    """Register a student. If the age is eligible, send a confirmation email.

    `send_email(to, message) -> bool` is the external dependency, injected so
    that unit tests can replace it with a mock.
    """
    if not is_eligible(age):
        return "rejected"
    ok = send_email(email, f"Hello {name}, your registration has been accepted")
    return "registered" if ok else "email failed"

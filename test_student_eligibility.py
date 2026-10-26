import pytest
from unittest.mock import Mock

from student_eligibility import (
    is_eligible,
    calculate_final_score,
    classify_grade,
    register_student,
)


# ---------- 1. PARAMETRIZE with BVA: age (boundaries 17 and 60) ----------
@pytest.mark.parametrize(
    "age, expected",
    [
        (0, False),    # lower bound of the valid domain
        (16, False),   # just below the lower boundary
        (17, True),    # on the lower boundary
        (18, True),    # just above the lower boundary
        (59, True),    # just below the upper boundary
        (60, True),    # on the upper boundary
        (61, False),   # just above the upper boundary
    ],
)
def test_is_eligible_bva(age, expected):
    assert is_eligible(age) == expected


# ---------- 2. PARAMETRIZE with BVA: grade classification (every boundary) ----------
@pytest.mark.parametrize(
    "score, expected",
    [
        (0, "F"), (39.99, "F"), (40, "D"), (54.99, "D"),
        (55, "C"), (69.99, "C"), (70, "B"), (84.99, "B"),
        (85, "A"), (100, "A"),
    ],
)
def test_classify_grade_bva(score, expected):
    assert classify_grade(score) == expected


# ---------- 3-4. Final score calculation ----------
def test_calculate_final_score_weighted():
    assert calculate_final_score(80, 90) == pytest.approx(86.0)


@pytest.mark.parametrize("mid, fin, expected", [(0, 0, 0.0), (100, 100, 100.0), (50, 100, 80.0)])
def test_calculate_final_score_boundaries(mid, fin, expected):
    assert calculate_final_score(mid, fin) == pytest.approx(expected)


# ---------- 5-8. pytest.raises (negative scenarios) ----------
def test_negative_age_rejected():
    with pytest.raises(ValueError, match="Age cannot be negative"):
        is_eligible(-1)


@pytest.mark.parametrize("mid", [-1, 101])
def test_invalid_midterm_rejected(mid):
    with pytest.raises(ValueError, match="Midterm"):
        calculate_final_score(mid, 80)


@pytest.mark.parametrize("fin", [-1, 101])
def test_invalid_final_exam_rejected(fin):
    with pytest.raises(ValueError, match="Final exam"):
        calculate_final_score(80, fin)


@pytest.mark.parametrize("score", [-0.01, 100.01])
def test_invalid_grade_score_rejected(score):
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        classify_grade(score)


# ---------- 9-10. FIXTURE usage (the `students` fixture is defined in conftest.py) ----------
def test_fixture_contains_initial_data(students):
    assert len(students.data) == 1
    name, score = students.data[0]
    assert classify_grade(score) == "A"


def test_fixture_is_isolated_between_tests(students):
    # The fixture is recreated for each test, so data from the previous test does not leak
    students.add("Budi", 60)
    assert len(students.data) == 2


# ---------- 11-14. MOCK (the email sender is replaced by a Mock) ----------
def test_register_success_and_email_sent():
    fake_send = Mock(return_value=True)                  # stub + mock
    assert register_student("Dustin", 20, "d@mail.id", fake_send) == "registered"
    fake_send.assert_called_once_with(
        "d@mail.id", "Hello Dustin, your registration has been accepted"
    )


def test_register_email_failure_handled():
    fake_send = Mock(return_value=False)
    assert register_student("Dustin", 20, "d@mail.id", fake_send) == "email failed"


def test_register_ineligible_age_does_not_send_email():
    fake_send = Mock()
    assert register_student("Kid", 16, "k@mail.id", fake_send) == "rejected"
    fake_send.assert_not_called()                        # verify interaction


def test_register_email_service_timeout():
    fake_send = Mock(side_effect=TimeoutError)           # simulate an error
    with pytest.raises(TimeoutError):
        register_student("Dustin", 20, "d@mail.id", fake_send)

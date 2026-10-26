# Session 9 Assignment — PyTest Unit Tests (Fixture, Parametrize, Mock)

Code base: a Python port of `StudentEligibility.java` (Session 8 assignment), plus `register_student()`, a function with an external dependency (email sender) so that mocking can be demonstrated.

## Structure
| File | Contents |
|---|---|
| `student_eligibility.py` | 4 functions: `is_eligible`, `calculate_final_score`, `classify_grade`, `register_student` |
| `conftest.py` | Shared `students` fixture (setup + cleanup with `yield`) |
| `test_student_eligibility.py` | 34 test cases (14 test functions) |
| `coverage_report.txt` | Output of `pytest --cov --cov-branch` |

## Meeting the Criteria
1. **At least 8 tests + BVA parametrize:** 14 test functions / 34 cases. BVA `parametrize` for age (0, 16, 17, 18, 59, 60, 61) and for letter grades (39.99/40, 54.99/55, 69.99/70, 84.99/85, 0, 100).
2. **At least 2 `pytest.raises`:** 4 tests (negative age, invalid midterm, invalid final exam, grade score outside 0–100), using `match=` to verify the error message.
3. **Fixture + mock:** the `students` fixture (in `conftest.py`) with `yield` + cleanup; `Mock` objects replace the email sender (success, failure, timeout via `side_effect`, `assert_called_once_with`, `assert_not_called`).
4. **Coverage:** command `pytest --cov=student_eligibility --cov-branch --cov-report=term-missing`

```
Name                     Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------
student_eligibility.py      27      0     18      0   100%
--------------------------------------------------------------------
TOTAL                       27      0     18      0   100%
```

## Coverage Analysis
- Statement coverage is 100% and **branch coverage is 100% (18/18 branches)**. Every `if/elif/else` in `is_eligible`, the validation in `calculate_final_score`, all five classes in `classify_grade`, and all three outcomes of `register_student` ("rejected", "registered", "email failed") are exercised.
- No branches are left uncovered, so there is nothing further to add. The email sender is passed in as a parameter (dependency injection), so no real email code exists in the module and the unit stays fully isolated.
- Limitation: 100% coverage does not guarantee a bug-free program. Quality depends on the assertions (exact values, `approx`, `match` on exceptions, `assert_called_once_with`), not merely on lines being executed. Whether the real email service honors the assumed contract (`send_email(to, message) -> bool`) must be checked with integration/contract tests.
- Note: the Session 9 in-class exercise uses grade "E" for scores below 40, while the Session 8 code uses "F". These tests follow the Session 8 code ("F").

## How to Run
```
pip install pytest pytest-cov
pytest -v
pytest --cov=student_eligibility --cov-branch --cov-report=term-missing --cov-report=html
```

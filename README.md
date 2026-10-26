# 09_Unit-Testing-PyTest-_5803024021_Dustin

# PyTest Unit Tests: Student Eligibility

Unit tests for a Python port of `StudentEligibility` (Session 8 assignment), written with PyTest. They demonstrate BVA parametrize, `pytest.raises`, a fixture with `yield` cleanup, mocking, and branch coverage.

## Files

| File | Purpose |
|---|---|
| `student_eligibility.py` | Module under test (4 functions) |
| `test_student_eligibility.py` | The tests (14 test functions, 34 cases) |
| `conftest.py` | Shared `students` fixture, loaded automatically by PyTest |
| `coverage_report.txt` | Saved output of the coverage run |
| `REPORT.md` | Short report and coverage analysis |

## Requirements

- Python 3.8 or newer
- `pytest` and `pytest-cov`

## Setup

Open a terminal in this folder (the one containing `student_eligibility.py`), then install the dependencies:

```
pip install pytest pytest-cov
```

Optional: use a virtual environment first.

```
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install pytest pytest-cov
```

## Running the tests

Run all tests with detailed output:

```
pytest -v
```

Expected result: `34 passed`.

Run a single test or a group:

```
pytest -v -k "bva"                        # only tests with "bva" in the name
pytest -v test_student_eligibility.py::test_negative_age_rejected
```

## Running with coverage

Statement and branch coverage in the terminal, showing missed lines:

```
pytest --cov=student_eligibility --cov-branch --cov-report=term-missing
```

Expected result: 100% statement and branch coverage (27 statements, 18 branches).

To also generate an HTML report:

```
pytest --cov=student_eligibility --cov-branch --cov-report=term-missing --cov-report=html
```

Then open `htmlcov/index.html` in a browser. Green lines were executed by the tests, red lines were not.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'student_eligibility'` | Run the command from inside this folder |
| `pytest: command not found` | Use `python -m pytest -v` instead |
| `no tests ran` | Test files must be named `test_*.py` and test functions must start with `test_` |
| `unrecognized arguments: --cov` | Install the plugin: `pip install pytest-cov` |

# 09_Unit-Testing-PyTest-_5803024021_Dustin

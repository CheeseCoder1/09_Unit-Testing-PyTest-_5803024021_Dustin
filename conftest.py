"""Shared fixtures. PyTest loads this file automatically, so every test file in
this folder can use these fixtures without importing them."""
import pytest


class StudentList:
    def __init__(self):
        self.data = []

    def add(self, name, score):
        self.data.append((name, score))

    def clear(self):
        self.data.clear()


@pytest.fixture
def students():
    s = StudentList()              # Arrange
    s.add("Dustin", 86.0)
    yield s                        # handed to the test
    s.clear()                      # cleanup after the test finishes

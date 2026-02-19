# Test-Driven Development

Implement a feature or fix using TDD: failing tests → passing code → refactor.

## Usage
Invoke when user says: "use TDD", "write tests first", "do TDD for this"

## The Three Steps

### Step 1: Red — Write failing tests
- Read the requirements / acceptance criteria
- Write test functions that describe the desired behavior
- **Run tests and confirm they fail** (`uv run pytest -v`)
- Do NOT write implementation code yet

```python
# Example structure
def test_my_feature_happy_path():
    # Arrange
    ...
    # Act
    result = my_function(...)
    # Assert
    assert result == expected

def test_my_feature_edge_case():
    ...

def test_my_feature_raises_on_invalid_input():
    with pytest.raises(ValueError):
        my_function(invalid_input)
```

### Step 2: Green — Write minimum code to pass
- Write the **simplest possible implementation** that makes all tests pass
- Run tests: `uv run pytest -v`
- Do not over-engineer at this stage
- Confirm all tests pass before moving to step 3

### Step 3: Refactor — Clean up while keeping green
- Improve code structure, naming, and readability
- Remove duplication
- Run tests after every significant change: `uv run pytest -v`
- Run full quality gates: `uv run ruff check . --fix && uv run mypy src/`

## Notes
- Coverage is a side effect of good TDD, not the goal
- If you can't write a test for it, the interface may need redesigning
- Each test should test ONE behavior
- Test names should describe behavior: `test_retry_waits_between_attempts`
- After refactor, run the full suite: `uv run pytest && uv run ruff check . && uv run mypy src/`

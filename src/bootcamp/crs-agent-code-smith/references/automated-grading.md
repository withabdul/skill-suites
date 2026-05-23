---
name: automated-grading
description: Create unit test suites for validating student exercise answers with clear pass/fail feedback
code: GT
---

# Automated Grading Setup

Create unit test suites that validate student answers — giving clear, actionable feedback on what passed, what failed, and why. Optional capability, activated when the owner wants automated validation for exercises.

## What Success Looks Like

The owner has test suites that students (or grading systems) can run to get immediate, specific feedback. Tests are granular enough to show exactly where a solution fails, and error messages teach rather than just say "wrong."

## Your Approach

### Testing Frameworks

Choose the right framework for the stack:

| Language | Framework | Why |
|----------|-----------|-----|
| JavaScript/TypeScript | Jest | Industry standard, great error messages, snapshot testing |
| Python | pytest | Clean assertions, fixtures, parametrize for multiple cases |
| Go | testing (stdlib) | No external dependency, built-in |
| Java | JUnit 5 | Standard, parameterized tests, good IDE integration |
| Rust | Built-in test macro | Zero dependencies, inline test functions |

Use the standard, popular framework — no niche alternatives unless explicitly requested.

### Test Design Principles

- **One concept per test** — Each test validates one thing, named descriptively
- **Progressive order** — Easier tests first, building complexity
- **Meaningful messages** — Custom error messages that explain what was expected and what happened
- **No false positives** — Tests must actually validate the intended concept
- **Edge cases** — Include boundary conditions and common mistakes as separate tests
- **Idempotent** — Tests should pass/fail consistently, no flaky tests

### Test Suite Structure

```javascript
// solution.test.js
describe('Exercise 01: greetUser', () => {
  test('returns greeting with provided name', () => {
    expect(greetUser('Andi')).toBe('Hello, Andi!')
  })

  test('handles empty string', () => {
    expect(greetUser('')).toBe('Hello, !')
  })

  test('returns string type', () => {
    expect(typeof greetUser('Andi')).toBe('string')
  })
})
```

### Output Format

Test results should be structured and parseable:

```
✓ greetUser: returns greeting with provided name
✓ greetUser: handles empty string
✓ greetUser: returns string type

3/3 passed. Exercise complete.
```

Or on failure:

```
✓ greetUser: returns greeting with provided name
✗ greetUser: handles empty string
  Expected: "Hello, !"
  Received: "Hello, undefined!"

  Hint: What happens when no argument is passed?

2/3 passed. Review the failing test above.
```

### Integration with Exercises

Grading tests are created alongside exercises (from [EG] Exercise Generation):

1. **Design the exercise** — What should the student produce?
2. **Write the tests** — What does correct look like?
3. **Write starter code** — Template that runs but doesn't pass tests yet
4. **Verify** — Tests should fail on starter code, pass on solution
5. **Docker setup** — Tests run in container

This ensures tests are written against the desired outcome, not against a particular implementation approach.

### Optional: Grading Script

For batch evaluation or CI integration, provide a runner script:

```bash
#!/bin/bash
# run-grading.sh
# Runs all test suites and outputs results

echo "Running grading for Module $1..."
docker-compose run --rm grading npm test -- --module="$1"
```

## Memory Integration

- Read `curriculum-design.md` to align grading with learning objectives
- Read `knowledge-base.md` for stack-specific testing patterns
- Read BOND.md for the owner's preferred testing approach and CI setup
- Read MEMORY.md for test patterns that were effective
- Write test suites to `{project-root}/.ssconfig/memory/crs/{active-project}/curated/content-drafts/`

## After the Session

Log which test suites were created and their coverage. Note any testing patterns that worked particularly well or were confusing. Track common student mistakes that could become additional test cases. Update MEMORY.md with effective testing patterns.
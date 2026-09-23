# Repository instructions for AI coding agents

## LeetCode solution documentation

- When adding a new approach to a problem file, append a separate `Solution` class after existing solutions; do not overwrite or remove previous solutions unless the user explicitly asks for replacement or refactoring.
- For every new solution or materially updated solution, include a clear triple-quoted docstring near the solution. State when the solution was added or updated using a month and year (for example, `September 2026`), summarize the approach, and give time and auxiliary-space complexity in Big O notation.
- At the bottom of each `Solution` class, include interview-relevant test cases as comments. Group them by behavior (such as core behavior, boundaries, and corner cases), and include representative inputs and expected outputs where useful.
- Cover important corner cases, including empty or minimal inputs when the implementation handles them, as well as boundary shapes or values specific to the problem. Include a large-input case when it checks an important implementation property such as avoiding recursion limits.
- Keep the test-case list concise and logical. It documents what an interviewer would reasonably grade; it does not require adding a test framework or runnable tests unless requested.
- Keep solutions clean, readable, and efficient: use descriptive names, avoid needless work, and make control flow easy to follow. Respect explicit constraints such as preserving the input; do not mutate input data when the user asks for a non-mutating solution.

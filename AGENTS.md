# Repository instructions for AI coding agents

## LeetCode solution documentation

- When adding a new approach to a problem file, append a separate `Solution` class after existing solutions; do not overwrite or remove previous solutions unless the user explicitly asks for replacement or refactoring.
- At the very top of each problem file, list useful clarification questions as file-level comments, not inside a solution class. Ask the user before proceeding when an answer is unclear and would materially change the solution; otherwise record the applicable assumption or constraint there.
- For every new solution or materially updated solution, include a clear triple-quoted docstring near the solution. State when the solution was added or updated using a month and year (for example, `September 2026`), summarize the approach, and give time and auxiliary-space complexity in Big O notation.
- At the very bottom of each problem file, include interview-relevant test cases as file-level comments, not inside a solution class. Group them by behavior (such as core behavior, boundaries, and corner cases), and include representative inputs and expected outputs where useful.
- Cover important corner cases, including empty or minimal inputs when the implementation handles them, as well as boundary shapes or values specific to the problem. Include a large-input case when it checks an important implementation property such as avoiding recursion limits.
- Keep the test-case list concise and logical. It documents what an interviewer would reasonably grade; it does not require adding a test framework or runnable tests unless requested.
- Keep solutions clean, readable, and efficient: use descriptive names, avoid needless work, and make control flow easy to follow. Respect explicit constraints such as preserving the input; do not mutate input data when the user asks for a non-mutating solution.
- Keep DFS helpers as class methods (for example, `_dfs`) rather than defining them as nested functions inside the public solution method.

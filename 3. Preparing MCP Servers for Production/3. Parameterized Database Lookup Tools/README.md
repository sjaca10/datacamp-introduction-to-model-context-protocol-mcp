# Parameterized Database Lookup Tools

## Exercise

An on-demand lookup tool will allow the LLM to search currencies by name or code without loading the full list. Use a **parameterized query** (placeholder `?`) to avoid prompt injection, and apply a row limit so responses stay bounded.

## Instructions

- Define a tool called `lookup_currencies()` that finds rows in `currencies` where `name` or `code` contains `prefix` (case-insensitive).
- Use a parameterized SQL query to insert `prefix` into the `?` placeholders; use `LIMIT 50` to limit the number of rows returned.

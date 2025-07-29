# Syntax
```python
new_list = my_list[start:stop:step]
```
- start: index to begin (inclusive)

- stop: index to end (exclusive)

- step: how many to skip (optional)

---
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:6]      # → [2, 3, 4, 5]
nums[:4]       # → [0, 1, 2, 3]
nums[5:]       # → [5, 6, 7, 8, 9]
nums[::2]      # → [0, 2, 4, 6, 8]
nums[::-1]     # → [9, 8, 7, ..., 0] (reverses list)
nums[-3:]      # → [7, 8, 9] (last 3 elements)
nums[1:-1]     # → [1, 2, ..., 8] (excluding first and last)
```
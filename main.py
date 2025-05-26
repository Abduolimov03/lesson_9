def pipe_fix(numbers):
    start = min(numbers)
    end = max(numbers)
    return list(range(start, end + 1))
print(pipe_fix([4,7,9]))  
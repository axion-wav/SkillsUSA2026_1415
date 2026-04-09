# TASK 2: Input an integer n, a count of people, and an array arr, their preferred seat numbers.
# Process their preferred seats in order, incrementing their preferred seat if it is taken already. Finish once all individuals have an assigned number.

from collections import deque

n = 8
arr = [3, 3, 3, 1, 5, 5, 2, 8]

queue = deque([(i + 1, seat) for i, seat in enumerate(arr)])
print(queue)

taken_seats = set()

result = [None] * n

while len(queue) > 0:
    person, seat = queue.popleft()

    if seat in taken_seats:
        queue.append((person, seat + 1))
    else:
        taken_seats.add(seat)
        result[person - 1] = seat

print("Final seat assignments: " + str(result))
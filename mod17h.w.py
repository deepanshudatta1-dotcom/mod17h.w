
# MY RUNNING LAP TRACKER

print("===== RUNNING LAP TRACKER =====")

# Get the number of laps
laps = int(input("Enter the number of laps: "))

# METHOD 1: USING A FORMULA
formula_points = laps * (laps + 1) // 2

print("\n--- Method 1: Using Formula ---")
print("Total running points:", formula_points)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")
print("Steps: 1")


# METHOD 2: USING A LOOP
loop_points = 0

for i in range(1, laps + 1):
    loop_points += i

print("\n--- Method 2: Using Loop ---")
print("Total running points:", loop_points)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print("Steps:", laps)


# METHOD 3: USING A NESTED LOOP
nested_points = 0
steps = 0

for i in range(1, laps + 1):
    for j in range(1, i + 1):
        nested_points += 1
        steps += 1

print("\n--- Method 3: Using Nested Loop ---")
print("Total running points:", nested_points)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print("Steps:", steps)


# COMPARISON
print("\n===== ALGORITHM COMPARISON =====")

print("Formula Result:", formula_points)
print("Loop Result:", loop_points)
print("Nested Loop Result:", nested_points)

print("\nMost Efficient Algorithm: Formula")

if formula_points == loop_points == nested_points:
    print("All three methods give the same result!")
else:
    print("The results do not match.")

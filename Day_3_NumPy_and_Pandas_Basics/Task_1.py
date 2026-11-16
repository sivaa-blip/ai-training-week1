import numpy as np

# 1. Create marks array (4 students x 3 subjects)
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70],
])

print(f"Shape: {marks.shape}")
print(f"Dtype: {marks.dtype}")
print(f"Size: {marks.size}")

# 2. Slice first two students and the last subject
print("First two students, last subject:", marks[:2, -1])

# 3. Averages per student (axis=1) and per subject (axis=0)
student_averages = np.round(marks.mean(axis=1), 2)
subject_averages = np.round(marks.mean(axis=0), 2)
print("Student averages:", student_averages)
print("Subject averages:", subject_averages)

# 4. Broadcasting: add 5 grace marks
grace_marks = marks + 5
print("With grace marks:\n", grace_marks)

# 5. Weighted scores using dot product / @ and reshape np.arange(12) to 3x4
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.round(marks @ weights, 2)
print("Weighted scores:", weighted_scores)

reshaped_array = np.arange(12).reshape(3, 4)
print("Reshaped arange (3x4):\n", reshaped_array)

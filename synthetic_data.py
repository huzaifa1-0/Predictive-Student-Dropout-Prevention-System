import os
import numpy as np
import pandas as pd

base_path = "U:/DS PROJECTS/predictive student dropout prevention/data"
file_paths = {
    "students": os.path.join(base_path, "students.csv"),
    "attendance": os.path.join(base_path, "attendance.csv"),
    "performance": os.path.join(base_path, "performance.csv"),
    "disciplinary_action": os.path.join(base_path, "disciplinary_action.csv")
}

# Check if files exist
for name, path in file_paths.items():
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

dataframes = {name: pd.read_csv(path) for name, path in file_paths.items()}

# Display the first few rows of each dataframe
{key: df.head() for key, df in dataframes.items()}
past_semesters = ["Spring 2023", "Fall 2023"]

synthetic_attendance = []
synthetic_performance = []
synthetic_disciplinary = []

for _, student in dataframes["students"].iterrows():
    student_id = student["student_id"]

    latest_attendance = dataframes["attendance"][dataframes["attendance"]["student_id"] == student_id].sort_values("semester")
    latest_performance = dataframes["performance"][dataframes["performance"]['student_id'] == student_id].sort_values('semester')
    latest_disciplinary = dataframes['disciplinary_action'][dataframes['disciplinary_action'] == student_id].sort_values('semester')

    if latest_attendance.empty or latest_performance.empty or latest_disciplinary.empty:
        continue

    latest_attendance = latest_attendance.iloc[-1]
    latest_performance = latest_performance.iloc[-1]
    latest_disciplinary = latest_disciplinary.iloc[-1]

    for semester in past_semesters:
        new_attendance_rate = max(0, latest_attendance['attendance_rate'] - np.random.uniform(3,7))
        new_total_absence = latest_attendance['total_absence'] + np.random.randint(1,4)
        new_cgpa = max(0, min(4, latest_performance["cgpa"] - np.random.uniform(0.1, 0.3)))
        new_action = latest_disciplinary["action_taken"]

        if new_attendance_rate < 50 or new_cgpa < 2.0:
            new_action = "Warning" if new_action == "None" else "Suspension"

        synthetic_attendance.append([student_id, semester, new_total_absence, new_attendance_rate])
        synthetic_performance.append([student_id, semester, latest_performance["core_subjects"], latest_performance["elective_subjects"], new_cgpa])
        synthetic_disciplinary.append([student_id, semester, new_action, "Auto-generated record"])

df_synthetic_attendance = pd.DataFrame(synthetic_attendance, columns=["student_id", "semester", "total_absence", "attendance_rate"])
df_synthetic_performance = pd.DataFrame(synthetic_performance, columns=["student_id", "semester", "core_subjects", "elective_subjects", "cgpa"])
df_synthetic_disciplinary = pd.DataFrame(synthetic_disciplinary, columns=["student_id", "semester", "action_taken", "remarks"])

df_synthetic_attendance.head(), df_synthetic_performance.head(), df_synthetic_disciplinary.head()

# Ensure the directory exists
os.makedirs(base_path, exist_ok=True)

synthetic_attendance_path = os.path.join(base_path, "synthetic_attendance.csv")
synthetic_performance_path = os.path.join(base_path, "synthetic_performance.csv")
synthetic_disciplinary_path = os.path.join(base_path, "synthetic_disciplinary.csv")

df_synthetic_attendance.to_csv(synthetic_attendance_path, index=False)
df_synthetic_performance.to_csv(synthetic_performance_path, index=False)
df_synthetic_disciplinary.to_csv(synthetic_disciplinary_path, index=False)
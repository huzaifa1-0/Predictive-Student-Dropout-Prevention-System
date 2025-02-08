import numpy as np
import pandas as pd

file_paths = {
    "students": "/data/students.csv",
    "attendance": "/data/attendance.csv",
    "performance": "/data/performance.csv",
    "disciplinary_action": "/data/disciplinary_action.csv"
}

dataframes = {name: pd.read_csv(path) for name, path in file_paths.items()}


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

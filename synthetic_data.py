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
    
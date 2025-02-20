import pymysql
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import re
from collections import defaultdict

#plt.ylim(0, 100000)
#plt.yscale("log")

# MySQL connection details
conn_params = {
    "host": "jsubmit.jlab.org",
    "user": "clas12jrun",
    "password": "C!4$jrun",
    "database": "CLAS12OCR"
}

# Connect to MySQL database
conn = pymysql.connect(**conn_params)
cursor = conn.cursor()

# Query to fetch submission data
query = """
SELECT client_time, scard FROM submissions;
"""
cursor.execute(query)

data = cursor.fetchall()
cursor.close()
conn.close()

# Process data
time_stamps = []
number_of_jobs = []

for row in data:
    client_time, scard_text = row
    time_stamp = datetime.strptime(client_time, "%Y-%m-%d %H:%M:%S")

    # Ensure scard_text is a string
    if not isinstance(scard_text, str):
        scard_text = ""

    # Extract generator and jobs values
    generator_match = re.search(r'generator:\s*(\S+)', scard_text)
    jobs_match = re.search(r'jobs:\s*(\d+)', scard_text)

    generator = generator_match.group(1) if generator_match else ""
    jobs = int(jobs_match.group(1)) if jobs_match else 10000 if generator.startswith("/") else 1

    time_stamps.append(time_stamp)
    number_of_jobs.append(jobs)

# Aggregate jobs per week
start_date = datetime(2023, 1, 4)
jobs_per_week = defaultdict(int)

for ts, jobs in zip(time_stamps, number_of_jobs):
    if ts >= start_date:
        week_start = start_date + timedelta(
            weeks=((ts - start_date).days // 7))  # Ensures consistent weekly bins
        jobs_per_week[week_start] += jobs

# Sort data for plotting
sorted_weeks = sorted(jobs_per_week.keys())
sorted_counts = [jobs_per_week[week] for week in sorted_weeks]

# Plot the results
plt.figure(figsize=(12, 6))
plt.bar(sorted_weeks, sorted_counts, width=6, edgecolor='black', alpha=0.75)
plt.xlabel("Time")
plt.ylabel("Number of Jobs")
plt.title("Number of Jobs Per Week Since Jan 1, 2020")
plt.xticks(rotation=45)
plt.grid()

# Set log scale for y-axis
plt.ylim(0, 1000000)
# Format x-axis to show one bin per week
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.show()

#plt.ylim(0, 100000)
#plt.yscale("log")


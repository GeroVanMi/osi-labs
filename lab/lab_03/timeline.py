import json
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd

con = sqlite3.connect("messages_copy.db")
cursor = con.cursor()
print("Connected to database")

query = """
    SELECT 
        date
    FROM messages 
    LEFT JOIN messagesText_Content mTC ON mTC.docid = messages.id AND c2attachmentNames != ''
    WHERE date IS NOT NULL
"""

cursor.execute(query)
data = cursor.fetchall()
cursor.close()

received_dates = []
for entry in data:
    # The dates are in microseconds from 1970/1/1, but we need seconds, so we divide by (1000 * 1000)
    date = datetime.fromtimestamp(entry[0] / (1000 * 1000))
    date = date.replace(hour=0, minute=0, second=0)
    received_dates.append(date)

current_date: datetime = received_dates[0]
max_date = received_dates[len(received_dates) - 1]

dates = {}
while current_date < max_date:
    formatted_date = current_date.strftime('%Y-%m-%d')
    if formatted_date not in dates:
        dates[formatted_date] = 0

    if current_date.year == received_dates[0].year and \
            current_date.month == received_dates[0].month and \
            current_date.day == received_dates[0].day:
        if formatted_date in dates:
            dates[formatted_date] += 1
        received_dates.pop(0)
    else:
        current_date = current_date + timedelta(days=1)

dates_list = []
for date in dates:
    dates_list.append({
        "date": date,
        "occurrences": dates[date],
    })
    
df = pd.DataFrame(dates_list)
df.plot(y='occurrences', x='date')
plt.xticks(rotation=15)
plt.savefig('output.png')

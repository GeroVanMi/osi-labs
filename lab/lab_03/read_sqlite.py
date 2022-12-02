import json
import sqlite3

con = sqlite3.connect("messages_copy.db")
cursor = con.cursor()
print("Connected to database")

query = """
    SELECT 
        *
    FROM messages 
    LEFT JOIN messagesText_Content mTC ON mTC.docid = messages.id AND c2attachmentNames != ''
    WHERE date IS NOT NULL
"""

cursor.execute(query)
data = cursor.fetchall()
cursor.close()

print(data)

with open("data.json", mode="w") as file:
    json.dump({
        "amountOfMails": data[0],
        "amountOfMailsWithAttachments": data[1],
    }, file)

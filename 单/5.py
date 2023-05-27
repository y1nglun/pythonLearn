import json
import matplotlib.pyplot as plt
import codecs

with codecs.open('data.json', 'r', encoding='utf-8', errors='replace') as file:
    data = json.load(file)

dates = []
expenses = []
for entry in data:
    date = entry[0]
    expense = float(entry[2])
    month, day, _ = date.split('/')
    dates.append(f"{month}/{day}")
    expenses.append(expense)

plt.figure(figsize=(10, 10))

plt.plot(dates, expenses)
plt.xlabel('Date')
plt.ylabel('Expense')
plt.title('Daily Expenses in April 2018')
plt.xticks(rotation=90)
plt.show()

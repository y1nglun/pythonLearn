import json
import codecs
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


def plot(data):
    canteen_frequency = {}
    for entry in data:
        canteen = entry[1]
        canteen_frequency[canteen] = canteen_frequency.get(canteen, 0) + 1

    canteens = list(canteen_frequency.keys())
    frequencies = list(canteen_frequency.values())

    plt.figure(figsize=(10, 10))

    plt.bar(canteens, frequencies)
    plt.xlabel('Canteen')
    plt.ylabel('Frequency')
    plt.title('Canteen Visit Frequency')
    plt.xticks(rotation=30)
    plt.show()


with codecs.open('data.json', 'r', encoding='utf-8', errors='replace') as file:
    content = file.read()
    data = json.loads(content)

plot(data)

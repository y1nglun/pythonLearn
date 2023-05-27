with open("Harry_Potter.txt", "r") as file:
    content = file.read()
word_count = len(content.split())
with open("Count_Words.txt", "w") as file:
    file.write(str(word_count))

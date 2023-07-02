s = "a good  example"
os = ""
words = s.split(" ")
for word in words:
    word = word.strip()
if "" in words:
    words.remove("")
for word in words[::-1]:
    os += word + " "
print(os.strip())
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth :int = 16


output :list[str] = []
if len(words) == 1:
    print(words)

insert_word :str = ""

for word in words:
    if len(insert_word) < maxWidth:
        insert_word += word + ' '
    else:
        output.append(insert_word)
        insert_word = ""
    output.append(insert_word)


print(output)
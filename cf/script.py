def can_say_hello(word):
    hello = "hello"
    i = 0

    for char in word:
        if char == hello[i]:
            i += 1
        if i == len(hello):
            return "YES"

    return "NO"


if __name__ == "__main__":
    typed_word = input()
    result = can_say_hello(typed_word)
    print(result)

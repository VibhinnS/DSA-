def binary_and(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("The value must be +ve and integer")

    a_binary = str(bin(a))[2:]
    b_binary = str(bin(b))[2:]

    max_len = max(len(a_binary), len(b_binary))

    return "0b" + "".join(
        str(int(char_a == "1" and char_b == "1"))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )

print(binary_and(2, 6))

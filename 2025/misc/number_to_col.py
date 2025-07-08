def number_to_column(n: int) -> str:
    result = []
    while n > 0:
        n -= 1  # shift to 0-based
        remainder = n % 26
        base = ord('A')
        appendage = base + remainder
        result.append(chr(appendage))
        n //= 26
    return ''.join(reversed(result))


print(number_to_column(52))
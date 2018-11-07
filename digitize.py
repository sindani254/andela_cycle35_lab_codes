def digitize(n):
    result = []
    if isinstance(n, int) and n >= 0:
        for d in str(n):
            result.append(int(d))
        return result
    else:
        print("invalid value provided")

print(digitize(124))

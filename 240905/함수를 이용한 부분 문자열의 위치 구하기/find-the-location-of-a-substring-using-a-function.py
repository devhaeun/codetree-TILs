string = input()
target = input()

def part_string():
    if target in string:
        return string.index(target)
    else:
        return -1

result = part_string()
print(result)
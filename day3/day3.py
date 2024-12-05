import re


pattern = re.compile(r'mul\((\d+),(\d+)\)')

part2 = True
with open("day3/input.txt") as f:
    mul_input = f.read()
    to_parse = ""
    if (part2 is True):
        arr = mul_input.split("don't()")
        arr2 = []
        for part in arr:
            test = part.split("do()")
            if len(test) > 1:
                arr2.append("".join(test[1:]))
                to_parse = "".join(arr2 + arr[:1])

    total = 0
    for r in re.findall(pattern, to_parse):
        print(r)
        total += int(r[0]) * int(r[1])

    print(total)

    
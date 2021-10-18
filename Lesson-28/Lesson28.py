normalList = numbers.split()
converted = [int(i) for i in normalList]
h = max(converted)
l = min(converted)
print(f'{h} {l}')



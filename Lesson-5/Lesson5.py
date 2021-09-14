#wyświetlanie w pętli tylko liczb parzystych
i = 0

while True:
    i += 1
    if i % 2 == 1:
        continue #continue - jeśli false to pętla zaczyna od nowa, dopóki nie będzie true
    print(i)
    if i > 10:
        break #break przerywa pętlę nieskończoną
print('Koniec')
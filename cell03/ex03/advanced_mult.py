x = 0

while x <= 10:
    text = str(f"Table de {x}: ")
    y = 0

    while y <= 10:
       text += str(f"{x * y} ")
       y += 1
    if y > 10:
        x += 1
    print(text)
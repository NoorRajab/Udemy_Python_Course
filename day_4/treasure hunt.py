row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("In which position should the treasure be placed: ")
horizontal = int(position[0])
vertical = int(position[1])
map [horizontal][vertical]="X"
print(map[0])
print(map[1])
print(map[2])
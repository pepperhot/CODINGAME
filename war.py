j1 = [input()[:-1] for _ in range(int(input()))]  # Remove last char to remove newline
j2 = [input()[:-1] for _ in range(int(input()))]

ordre = {
    "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, 
    "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13
}

def bataille():
    if len(j1) <= 2 or len(j2) <=2 :
        print("PAT")
        exit()
    
    for _ in range(3):
        pile.append(j1.pop(0))
        pile.append(j2.pop(0))
    
    card_1 = j1.pop(0)
    card_2 = j2.pop(0)
    pile.extend([card_1, card_2])

    if ordre[card_1] > ordre[card_2]:
        j1.extend(pile)  
    elif ordre[card_1] < ordre[card_2]:
        j2.extend(pile)  
    else:
        bataille()

p = 0
while len(j1) and len(j2):
    p += 1  
    pile = []

    card_1 = j1.pop(0)
    card_2 = j2.pop(0)
    pile.extend([card_1, card_2])  

    if ordre[card_1] > ordre[card_2]:
        j1.extend(pile)  
    elif ordre[card_1] < ordre[card_2]:
        j2.extend(pile)  
    else:
        bataille()
print((1 if len(j1) > 0 else 2), p)

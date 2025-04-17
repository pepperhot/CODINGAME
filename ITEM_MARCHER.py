data = input().replace(":", " ").split(",")
data[0] = "-" + data[0] + "-"
data[1] = ""+data[1]
hor,ver= len(max(data, key=len))+4,len(data) + 2
def shema(corner_l,corner_r,coté,top,bot):
    print(corner_l+top*(hor - 2)+corner_r)
    print(coté+" "*(((hor-len(data[0]))//2)if data[1] == "Rare"else ((hor-len(data[0]))//2-1))+data[0]+" "*((hor-len(data[0]))//2-1)+coté)
    print(coté+" "*(((hor-len(data[1]))//2)if data[1] == "Rare"else ((hor-len(data[1]))//2-1))+data[1]+" "*((hor-len(data[1]))//2-1)+coté)
    for i in range(4, ver):
        print(f"{coté} {data[i - 2]:<{hor-4}} {coté}")
    print(corner_r+bot*(hor - 2)+corner_l)
if data[1] == "Common":shema("#","#", "#", "#", "#")
elif data[1] == "Rare":shema("/", "\\", "#", "#", "#")
elif data[1] == "Epic":shema("/", "\\", "|", "-", "_")
elif data[1] == "Legendary":
    top="X"+"-"*((hor - 2)//2-2)+("-\\_/-"if len(data[0])%2!=0 else "\\__/")+"-"*((hor - 2)//2-2)+"X"
    bot="X"+"_"*(hor - 2)+"X"
    print(top)
    print("["+" "*((hor-len(data[0]))//2-1)+data[0]+" "*((hor-len(data[0]))//2-1)+"]")
    print("|"+" "*(((hor-len(data[1]))//2)if len(data[0])%2==0 else((hor-len(data[1]))//2)-1)+data[1]+" "*((hor-len(data[1]))//2-1)+"|")
    for i in range(4, ver):print(f"| {data[i - 2]:<{hor-4}} |")
    print(bot)

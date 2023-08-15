a = (
    ["0001", "Male", "Yamada", "Tarou", 25, "Tokyo"],
    ["0002", "Male", "Satou", "Takeshi", 27, "Kanagawa"],
    ["0003", "Female", " Tanaka", "Yuko", 25, "Saitama"],
    ["0004", "Male", "Suzuki", "lchirou", 35, "Hokkaido"],
)

member = {}

for i in a:
    key = i[0]
    info = i[1:]
    member[key] = info

print("number", "information", sep="\t")
for key, info in member.items():
    print(key, info)

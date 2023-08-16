a = [
    ["01", "0001", "Male", "Yamada", "Tarou", 25, "Tokyo"],
    ["01", "0002", "Male", "Satou", "Takeshi", 27, "Kanagawa"],
    ["01", "0003", "Famele", "Tanak", "Yuko", 25, "Saitama"],
    ["02", "0001", "Male", "Smith", "Mike", 22, "NewJersey"],
    ["02", "0002", "Male", "Turner", "Tom", 27, "Kansas"],
    ["02", "0003", "Male", "Jackson", "David", 22, "Florida"],
]


member = {}

for record in a:
    key = (record[0], record[1])
    info = record[2]
    member[key] = info

    print("number", "information", sep="\t")
    for key, info in member.items():
        print(key, info)

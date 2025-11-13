print("Paste your info. Type END on a new line when you're finished:")

lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)
# UFDT - Unformatted Data (As Text)
UFDT = "\n".join(lines)

# LDT - Listed Data (As Text)
LDT: list[str] = UFDT.splitlines()

labels = LDT[0::2]
values: list[str] = LDT[1::2]

data = dict(zip(labels, values))

# FDT - Formatted Data (As Text)
FDT = f'{data["Author"]}. "{data["Article Title"]}." {data["Website Name"]}, {data["Publisher"]}, {data["Last Updated"]}, Accessed {data["Date Accessed"]}.\n<{data["URL"]}>'
print("Heres your citation: \n" + FDT)


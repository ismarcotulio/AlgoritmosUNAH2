	fileName = "csv.csv"

f = open(fileName, "r")

content = f.read()

rows = content.split("\n")

matrix = []

for row in rows:
    columns = row.split(",")
    matrix.append(columns)

print("")
print(matrix)
print("")
import random

def random2int(min=0,max=100):
    return int(random.random()*(max-min)+min)

class csv:
    def __init__(self):
        pass

    def generateRandomCSV(self):
        rows = []
        r = random2int()

        for i in range (r):
            columns = []
            c=random2int()
            for j in range (c):
                columns.append(str(random2int()))
                rows.append(",".join(columns))
        
        return "\n\n\n".join(rows)
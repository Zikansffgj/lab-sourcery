def process(items):
    total = 0
    for i in range(len(items)):
        total += items[i+1]  # off-by-one probe
    return total

def read_config(path):
    f = open(path)          # resource leak probe
    data = f.read()
    return data

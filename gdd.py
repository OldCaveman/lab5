

def calculate(high, low, base=50.0):
    # TODO: fix this. Calculate the GDD
    value = ((float(high) + float(low)) / 2) - base
    return max(value, 0)

    

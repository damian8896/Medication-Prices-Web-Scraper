def find_stats(dict):
    print("\n\n----------- Stats -----------\n")
    print("max - ", find_max(dict))
    print("min - ", find_min(dict))
    print("average - $" + str(round(find_average(dict), 2)))

def find_max(dict):
    max_value = 0
    max_name = ""
    for key in dict:
        if dict[key] > max_value:
            max_value = dict[key]
            max_name = key
    return {max_name: "$" + str(max_value)}

def find_min(dict):
    min_value = 100000000000
    min_name = ""
    for key in dict:
        if dict[key] < min_value:
            min_value = dict[key]
            min_name = key
    return {min_name: "$" + str(min_value)}

def find_average(dict):
    total = 0.0
    count = 0.0
    for key in dict:
        total += dict[key]
        count += 1
    return total/count

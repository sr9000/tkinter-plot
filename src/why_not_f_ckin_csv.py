def parse_not_f_ckin_csv(file_name):
    regions = dict()
    for l in open(file_name):
        x = l.split(';')
        name, data = x[0], x[1:]
        data = [int(x) for x in data]
        regions[name] = data

    return regions

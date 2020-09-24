
# Given the list of customer segments below please create a new list of the names of the segments only using (a) a for loop (b) a list comprehension (c) a map(). List would look something like ['Wallstreet','Gambler','Parents'] but of course using each tool as listed above. segments = [{'name': 'Wallstreet', 'average_spend': 82.01}, {'name': 'Gambler', 'average_spend': 107.00}, {'name': 'Parents', 'average_spend': 10.52}]

def loop(dictionary):
    names = []
    for i in dictionary:
        # for key in i:
        #     if key == 'name':
        #         names.append(i[key])
        names.append(i['name'])
    return names

def comprehension(dictionary):
    # return [{value for (key, value) in i.items() if key == 'name'} for i in dictionary]
    return [i['name'] for i in dictionary]

def map_(dictionary):
    return


def neighbor():
    return
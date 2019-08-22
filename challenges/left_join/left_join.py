from hashtable import HashTable

def left_join(ht_l, ht_r):
    results = []
    left_keys = ['fond', 'wrath', 'diligent', 'outfit', 'guide']

    
    for key in left_keys:

        if ht_l.contains(key):
            results.append(ht_l.get_key(key))
            results.append(ht_l.get(key))

        if ht_r.contains(key):
            results.append(ht_r.get(key))
            
        elif not ht_r.contains(key):
            results.append(None)


    return results
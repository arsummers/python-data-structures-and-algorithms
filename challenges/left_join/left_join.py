from hashtable import HashTable

def left_join(ht_l, ht_r):
    left_keys = []
    results = []
    
    for key in ht_l:
        left_keys.append(ht_l.get(key))

    for key in left_keys:
        results.append(ht_l.get(ht_l.value))
        if ht_r.contains(key):
            results.append(ht_r.value['value'])

        elif not ht_r.contains(key):
            results.append(None)
        
    return results
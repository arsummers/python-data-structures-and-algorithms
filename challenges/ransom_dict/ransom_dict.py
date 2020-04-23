# check if word is in dictionary
# print Yes if note can be formed, No if not
# case sensitive! which means I don't have to worry about it
# put words into separate dicts
# since we can't have duplicate keys, each key will have to be numbered
# if the number of the key/val pair in the note dictionary is less than or equal to the key/val pair in the mag dict, print yes, otherwise print no

magazine = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
note = ['ive', 'got', 'some', 'coconuts']

def check_magazine(magazine, note):
    mag_dict = dict((i, magazine.count(i)) for i in magazine)
    note_dict = dict((i, note.count(i)) for i in note)


    for word in note_dict:
        if word not in mag_dict:
            print('No not there')
            return 'No'

        elif mag_dict[word] < note_dict[word]:
            print('No not enough')
            return('No')

    
    print('Yes')
    return 'Yes'
        

check_magazine(magazine, note)
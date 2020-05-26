text = ['code', 'code', 'frame', 'code', 'framer', 'frame']
sorty = []
joiner = ''


# this makes a list of lists which isn't useful for what I'm trying to accomplish
for word in text:
    sorty.append(joiner.join(sorted(word)))

print(sorty)
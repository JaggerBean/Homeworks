with open('/usr/share/dict/words', 'r') as f:
    for i in f.readlines():
        if i.startswith("pyt"):
            print(i)

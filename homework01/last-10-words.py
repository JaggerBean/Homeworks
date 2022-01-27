with open('/usr/share/dict/words', 'r') as f:
  
           lines = f.readlines()
           last_lines = lines[-10:]
           print(last_lines)

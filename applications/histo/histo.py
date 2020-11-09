# Your code here
histo = {}
longest = 0
ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '?', '!']


originalFile = open('applications/histo/robin.txt', 'r')
for line in originalFile.readlines():
    clean_line = "".join(ch for ch in line if ch not in ignore).lower()
    for word in clean_line.split():
        if word not in histo:
            histo[word] = "#"
            if len(word) > longest:
                longest = len(word)
        else:
            histo[word] = histo[word] + "#"
            
sorted_histo = sorted(histo.items(), key = lambda x: x[0], reverse = False)

print(sorted_histo)
    
originalFile.close()

size = 4 
reference_string = [1, 2, 1, 0, 3, 0, 4, 2, 4]
pages = []

faults = 0
hits = 0
for i in reference_string:
    if i in pages:
        pages.remove(i)
        
        pages.append(i)
        hits += 1
    else:
        faults +=1
        if(len(pages) < size):
            pages.append(i)
        else:
            pages.remove(pages[0])
            
            pages.append(i)
print("Hits:", hits)
print("Faults:", faults)
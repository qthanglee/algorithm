#Thang Le
#Running time O(n)
#will need a logic to check s1 and s2 are characters only. 
#this only work on assumption of s1 and s2 has no special characters, space.. or numbers


def anagramcheck(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    
    is_match = True
    
    for j in range(26):
        if c1[j] == c2[j]:
            j += 1
        else:
            is_match = False
    
    return is_match
    
r = anagramcheck('applep', 'pplpea')

print r


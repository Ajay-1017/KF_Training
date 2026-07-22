

def word_count(text):
    d={}
    words = text.split()

    for word in words:
        d[word] = d.get(word,0)+1
    
    l = sorted(d.values(),reverse=True)
    
    ans={}
    for i in range(len(l)):
        for word in d:
            if l[i]==d[word]:
                ans[word] = d[word]
    return ans


print(word_count("ml ai ai data ai"))


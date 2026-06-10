def word_frequency(sentence):
    arr = sentence.lower().split()
    d={}
    for word in arr:
        if word in  d:
            d[word]+=1
        else:
            d[word]=1
    return d
def main():
    sentence = input("Enter the sentence with proper spacing : ")
    print(word_frequency(sentence))
main()
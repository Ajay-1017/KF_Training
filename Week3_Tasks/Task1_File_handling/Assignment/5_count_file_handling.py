# 5) Count the number of lines, words, and characters in a text file.

with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/count_file.txt",'r') as rf:


# Method - 1:
 
# 1) count lines 
    cnt_lines=0
    for line in rf:
        cnt_lines+=1

    print(f"No of lines: {cnt_lines}")


    rf.seek(0)
    lines  = rf.readlines()
    print(f"No of lines: {len(lines)}")


    
# 2) count words 
    rf.seek(0)
    cnt_words = 0
    for content in lines:
        words = content.split()
        cnt_words += len(words)
    print("no of words: ", cnt_words,sep="")

# 3) count characters     
    rf.seek(0)
    print("no of characters :",len(rf.read()))
 

# Method - 2:

    rf.seek(0)
    text = rf.read() 
    print(f"No of words: {len(text.split())}") 
    print(f"No of lines: {len(text.splitlines())}") 
    print(f"No of characters: {len(text)}")
  



# count characters excluding the space and new line
with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/count_file.txt",'r') as rf:

    text ="".join(rf.read())
    
    cnt_char=0
    for ch in text:
        if ch!=" " and ch!="\n":
            cnt_char+=1
    print("character excluding newline and spaces : ",cnt_char)

    # using join and split
    print(len("".join(text.split())))

    # using replace
    print(len(text.replace(" ","").replace("\n","")))
    



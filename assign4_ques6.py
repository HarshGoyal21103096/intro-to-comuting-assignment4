#QUES6
#inputing a word from first friend
word=input("enter the word:")
word=word.lower()

#inputing a meaningful word with the exact sme letters
testword=input("enter a new meaningful word using the exact same letters to test your friendship:")
testword=testword.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]]+=1
        else:
            count[list1[i]]=1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word)!=count_in_dict(testword):
        print("the letters aren't exact,friendship is fake")
        return
    ans=input("does the word makes sense?(y/Y or n/N)")
    if ans=='y' or ans=='Y':
        print("the friends pass the friendship test")
    elif ans=='n' or ans=='N':
        print("the word doesn't have a meaning,friendship is fake")
    else:
        print("invalid input,try again with y/Y or n/N")
        userinput()
userinput()

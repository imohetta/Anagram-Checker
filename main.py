# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word = input("input your word: "), anagram = input("input the test word: ")):
    
    
    wordletters = sorted(word)
    # print(wordletters)
    
    anagramletters = sorted(anagram)
    # print(anagramletters)


    if  wordletters==anagramletters:
        print("The words are anagrams")
        return True
    
    else:
        print("The words are not anagrams.")
        return False
        
find_anagram()

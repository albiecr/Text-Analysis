#Press Shift+Enter to run the code
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
           
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0;

#Create variable givenstring and ask user to input
givenstring = input("Please type the text: ")

# Create an instance of TextAnalyzer class
analyzed = TextAnalyzer(givenstring)


# Call the function that converts the data into lowercase
print("Formatted Text: ", analyzed.fmtText)
opcao = input("Enter the function number you want to use, then press Enter:\n1 Count of occurrences of all words\n2 Count of occurrences of a specific word\n")

if opcao == '1':
    # Call the function that counts the frequency of all unique words from the data
    freqMap = analyzed.freqAll()    
    print("Here is the frequency count of all words in the provided text: ", freqMap)
else:
    # Call the function that counts the frequency of a specific word
    word = input("Please type the word that you want to be counted on the text: ")
    frequency = analyzed.freqOf(word)
    print("The word ", word, "appears ", frequency, "times.")


#Press Shift+Enter to run the code
class TextAnalyzer(object):
    """A class to analyze text for word frequencies."""
    def __init__ (self, text):
        """Initialize the analyzer with formatted text (punctuation removed and lowercase)."""
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedText = formattedText.lower()
        self.fmtText = formattedText
        
    def freqAll(self):        
       """Return a dictionary of all words and their frequencies."""
        wordList = self.fmtText.split(' ')
        freqMap = {}
        return {word: wordList.count(word) for word in set(wordList) if word}  # Added if word to filter empty strings
        
        return freqMap
           
    def freqOf(self,word):
        """Return the frequency of a specific word."""
        if not word:  # Check for empty input
            return 0
        freqDict = self.freqAll()
        return freqDict.get(word.lower(), 0)  # Make search case-insensitive

#Create variable givenstring and ask user to input
givenstring = input("Please type the text: ")

# Create an instance of TextAnalyzer class
analyzed = TextAnalyzer(givenstring)


# Call the function that converts the data into lowercase
print("Formatted Text: ", analyzed.fmtText)

# Call the function that counts the frequency of all unique words from the data
freqMap = analyzed.freqAll()
print(freqMap)

# Call the function that counts the frequency of a specific word
word = input("Please type the word that you want to be counted on the text: ")
frequency = analyzed.freqOf(word)
print("The word ", word, "appears ", frequency, "times.")

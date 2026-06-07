# Program to create a function that calculates and returns the frequency of each word in a sentence.

# Function to calculate word frequency
def word_frequency(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

# Input sentence from user
sentence = input("Enter a sentence: ")

# Display Results
print(word_frequency(sentence))
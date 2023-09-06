def find_words_with_two_vowels(words):
   vowels = "aeiouAEIOU"
   result = []
   for word in words: 
      num_vowels = 0
      for char in word:
         if char in vowels:
            num_vowels += 1
      if num_vowels == 2:
         result.append(word)
   return result

print(find_words_with_two_vowels(["text", "test", "Apple", "example"]))
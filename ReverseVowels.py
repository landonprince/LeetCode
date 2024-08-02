class Solution:
    def reverseVowels(self, s: str) -> str:
        # Create two lists to store the indices and characters of the vowels
        vowelIndices = []
        vowelList=[]

        # Iterate through the string and store the indices and characters of the vowels
        for i,letter in enumerate(s):
            if letter in 'aeiouAEIOU':
                vowelIndices.append(i)
                vowelList.append(letter)
        vowelList.reverse()
        
        # Replace the vowels in the original string with the reversed vowels from the list
        result = list(s)
        for i, index in enumerate(vowelIndices):
            result[index] = vowelList[i]

        # Join the characters back into a string and return it
        return ''.join(result)

string = "hello world"
solution = Solution()
result = solution.reverseVowels(string)

print()
print(f"string = {string}, result = {result}")


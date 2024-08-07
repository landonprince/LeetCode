class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary to map Roman numerals to their integer values
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        
        # Iterate through the string, subtracting smaller numerals from larger ones to get the result
        for i in range(len(s) - 1):
            if dict[s[i]] < dict[s[i+1]]:
                num -= dict[s[i]]
            else:
                num += dict[s[i]]
        
        # Add the last character to the result (since it's not included in the loop)
        num += dict[s[-1]]
        
        return num
                
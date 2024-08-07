from problems.abstract_problem import AbstractProblem

class GCDOfStrings(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Greatest Common Divisor of Strings",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/majority-element/description/",
            instructions = (
                "For two strings s and t, we say t divides sif and only if s = t + t + t + ... + t + t (i.e., t is " 
                "concatenated with itself one or more times)."
                "Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2."
            ),
            tags = ["Array", "Map"]
        )
    
    def solution(self, str1: str, str2: str) -> str:
        # Helper function to compute the greatest common divisor of two integers
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        # Check if str1 + str2 == str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute the greatest common divisor of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # The gcd string will be the prefix of str1 (or str2) of length gcd_length
        return str1[:gcd_length]
    
    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEETCODE", "CODE", "CODE"),
            ("ABCDEF", "ABC", "ABC"),
        ]

        # Run each test case
        for str1, str2, expected in test_cases:
            self.total_tests += 1
            result = self.solution(str1, str2)
            if result == expected:
                self.tests_passed += 1
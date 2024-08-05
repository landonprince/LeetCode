import sys
import os
from problem_collection import ProblemCollection

# Add the current directory to the system path to allow importing modules from the 'problems' package
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Create a ProblemCollection object and test its functionality
if __name__ == "__main__":
    problem_collection = ProblemCollection()
    problem_collection.display_all_problems()
import sys
import os
from ProblemCollection import ProblemCollection

# Add the current directory to the system path to allow importing modules from the Problems package
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    problemCollection = ProblemCollection()
    problemCollection.display_all_problems()
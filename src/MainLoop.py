import sys
import os

# Add src to the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ProblemCollection import ProblemCollection

if __name__ == "__main__":
    problemCollection = ProblemCollection()
    problemCollection.display_all_problems()

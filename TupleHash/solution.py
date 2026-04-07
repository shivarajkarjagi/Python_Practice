# Problem: Tuples
# Note: Run this code in the PyPy 3 environment on HackerRank to avoid Python 3 hash randomization issues.

if __name__ == '__main__':
    # Read the number of elements (n)
    n = int(input())
    
    # Read the space-separated string, split it, and map the strings to integers
    integer_list = map(int, input().split())
    
    # Convert the map object into a tuple
    t = tuple(integer_list)
    
    # Print the hash of the tuple
    print(hash(t))

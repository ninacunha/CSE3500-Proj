# Rabin-Karp Algorithm for file comparison (plagiarism check)

def rabin_karp_file(file1, file2, pattern_length=10):
    # Read the contents of both files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    # Set base and modulus for the rolling hash function
    base = 256  # Number of possible characters (extended ASCII)
    mod = 101   # A prime number (modulus for hash function)

    # Length of the pattern to search for
    n = len(text1)
    m = pattern_length

    # Calculate hash values for the first pattern in text1
    pattern_hash = 0
    text_hash = 0
    h = 1  # The value of base^(m-1) % mod

    # Precompute h = base^(m-1) % mod
    for i in range(m - 1):
        h = (h * base) % mod

    # Compute the hash value of the first pattern and initial window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(text1[i])) % mod
        text_hash = (base * text_hash + ord(text2[i])) % mod

    # Check for matching patterns using Rabin-Karp on both files
    plagiarism_found = False
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text1[i:i + m] == text2[i:i + m]:
                print(f"Plagiarism detected!")
                print(f"Matching text found at index {i} in file1: \"{text1[i:i + m]}\"")
                print(f"Matching text found at index {i} in file2: \"{text2[i:i + m]}\"")
                plagiarism_found = True
        
        # Calculate the next hash value for the window of text2
        if i < n - m:
            text_hash = (base * (text_hash - ord(text2[i]) * h) + ord(text2[i + m])) % mod

            # Convert negative hashes to positive
            if text_hash < 0:
                text_hash += mod

    if not plagiarism_found:
        print("No plagiarism detected.")

# Example usage:
file1 = 'file1.txt'  # Path to the first file
file2 = 'file2.txt'  # Path to the second file
rabin_karp_file(file1, file2, pattern_length=10)  # Search for patterns of length 10
# implement the Rabin-Karp algorithm to search for a specific pattern (e.g., “ABAC”) 
# within a given text (e.g., “ABAAABCDABACDABACABAB”), expecting the output to display 
# the index positions where the pattern is found within the text.

def rabin_karp(text, pattern):
    # Set base and modulus for the rolling hash function
    base = 256  # Number of possible characters (extended ASCII)
    mod = 101   # A prime number (modulus for hash function)

    # Lengths of text and pattern
    n = len(text)
    m = len(pattern)

    # Calculate hash values for the pattern and the initial window of the text
    pattern_hash = 0
    text_hash = 0
    h = 1  # The value of base^(m-1) % mod

    # Precompute h = base^(m-1) % mod
    for i in range(m - 1):
        h = (h * base) % mod

    # Compute the hash value of the pattern and the first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        text_hash = (base * text_hash + ord(text[i])) % mod

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # If the hash values match, check for exact match
        if pattern_hash == text_hash:
            # Check the actual characters if hash matches
            if text[i:i + m] == pattern:
                print(f"Pattern found at index {i}")
        
        # Calculate the hash value for the next window of text
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % mod

            # We might get negative value of text_hash, convert it to positive
            if text_hash < 0:
                text_hash += mod

# Example usage:
text = "ABAAABCDABACDABACABAB"
pattern = "ABAC"
rabin_karp(text, pattern)
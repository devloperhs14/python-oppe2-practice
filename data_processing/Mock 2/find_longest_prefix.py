# Find the longest common prefix among all the words in the sentence.

def longest_common_prefix(sentence: str) -> str:
    '''Find the longest common prefix among the given words of the sentence.

    Args:
        sentence (str): A string of space separated words.

    Returns:
        str: longest prefix.
    '''
    # split
    words = sentence.split()

    #edge case
    if not words:
        return ""
    if len(words) == 1:
        return words[0]
    
    # algorithm
    prefix = words[0]

    # comparison
    for word in words[1:]:
        while not word.startswith(prefix) and prefix:
            prefix = prefix[:-1]

        if not prefix:
            return ""
    return prefix

# driver code
ans = longest_common_prefix('dog, racecar, car , elephant')
print(ans)
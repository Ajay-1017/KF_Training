
# Run-Length Encoding (RLE) is a data compression technique that replaces 
# consecutive repeated characters (or elements) with the character followed by the number of times it repeats.

# I/P-> AAAABBBCCDAA
# O/P -> A4B3C2D1A2


def run_length_encode(s):

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result

print(run_length_encode("AAAABBBCCDAA"))







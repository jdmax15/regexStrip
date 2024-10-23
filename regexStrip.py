import re, sys

'''
1. Configure sys.argv inputs.
2. Whitespace strip logic
3. Char strip logic

'''

def regexStrip(string, word=None):
    if word is not None:
        print(f"Two arguments provided: {string}, {word}")
    else:
        print(f"One argument provided: {string}")


testString = " The quick brown fox jumps over the lazy dog. "

print(regexStrip(testString))
print(regexStrip(testString, "fox"))


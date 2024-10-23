import re

def regexStrip(string, word=None):
    
    whitespaceStrip = re.compile(r'^(\s*)(.*?)(\s*)$') 
    # Group 1: Leading whitespaces, Group 2: All text, Group 3: Trailing whitespaces.
    
    if word is not None:
        wordReplace = re.compile(word)
        return wordReplace.sub('', string)
    else:
        match = whitespaceStrip.match(string)
        if match:
            return match.group(2)


testString = " The quick brown fox jumps over the lazy dog. "

print(regexStrip(testString))

print(regexStrip(testString, "fox"))


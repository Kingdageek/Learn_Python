#rotate_string.py

# shift every letter in a string through the alphabet by a value
# and return a new string containing the strings at the new positions
# "melon" shifted by -10 is "cubed". You can shift back and forth
# rotating through the alphabet
"""
def rotate_word2(word, rot):
    new_word = ""
    for i in word:
        if not (96 < ord(i) < 123): k = i  # return single string
                                                   # if it is not a lowercase
                                                   # letter 
        else:
                k = ord(i) + rot
                while True:     # Loop till 96 < k < 123
                        if k > 122:
                                k = k - 123 + 96 #'a' - 'z' is 97-122
                        elif k < 97:
                                k = 123 - 97 + k # for -VE 'rot'
                        if (96 < k < 123): break
                k = chr(k)
        new_word = new_word + k
    return new_word
"""
def create_map(rot):
    """returns a dict mapping, lowercase (97) and uppercase (65) letters to
    equivalent letters determined by 'rot' number of rotations"""
    if rot<0:
        a_rot = abs(rot)
        rot = 26 - (a_rot % 26)
    hist = {}
    for c in (65,97):
        for i in range(26):
            hist[chr(i+c)] = chr((i+rot)%26 + c)
    return hist

def get_input():
    sentence = input("Enter a string to be shifted: ")
    shift = int(input("Enter an int to shift string by: "))
    return sentence, shift

def main():
    while True:
        try:
            sentence, shift = get_input()
            
            hist = create_map(shift)
            rot_str = "".join([hist.get(c,c) for c in sentence])
            
            print("\n%s shifted by %d is: \n%s" % (sentence, shift,
                                          rot_str))
            # print(hist)
            """
            print("\n%s shifted by %d is: \n%s" % (sentence, shift,
                                          rotate_word2(sentence, shift)))
            """
            break
        except ValueError as err:
            print(err)
            print("INVALID INPUT! | ENTER A STRING | \
ENTER A VALID INT FOR SHIFT VALUE")

if __name__ == "__main__": main()
            
    

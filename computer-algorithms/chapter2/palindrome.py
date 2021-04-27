
def isPalindrome(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
    return True
def isPalindrome_rec(word, front, back):
    if front >= back:
        return True
    else:
        if word[front] == word[back]:
            print(word[front], word[back])
            return isPalindrome_rec(word, front+1, back-1)
        else:
            print(word[front], word[back])
            return False

print(isPalindrome("eye"))
print(isPalindrome("eyie"))
print(isPalindrome_rec("eyie", 0, len("eyie")-1))
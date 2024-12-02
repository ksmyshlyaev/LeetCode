# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_magazine = [letter for letter in magazine]
        letters_ransom_note = [letter for letter in ransomNote]
        elements_count = len(letters_ransom_note)
        for i in range(elements_count):
            if letters_ransom_note[0] in letters_magazine:
                element_to_delete = letters_ransom_note.pop(0)
                letters_magazine.remove(element_to_delete)
        if letters_ransom_note:
            return False
        else:
            return True


if __name__ == '__main__':
    print(Solution().canConstruct(ransomNote="a", magazine="b"))
    print(Solution().canConstruct(ransomNote="aa", magazine="ab"))
    print(Solution().canConstruct(ransomNote="aa", magazine="aab"))

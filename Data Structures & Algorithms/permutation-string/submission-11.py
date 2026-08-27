from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])

        if s1_count == window_count:
            return True

        left = 0
        for right in range(len1, len2):
            window_count[s2[right]] += 1

            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            left += 1

            if s1_count == window_count:
                return True

        return False

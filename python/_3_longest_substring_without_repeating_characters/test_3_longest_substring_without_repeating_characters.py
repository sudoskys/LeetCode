class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # To store the characters and their indices
        start = 0  # To represent the start of the window
        max_length = 0  # To store the maximum length of the substring

        for end in range(len(s)):
            if s[end] in char_index:
                # If the character is repeating, move the start pointer to the right of the previous instance
                start = max(start, char_index[s[end]] + 1)

            # Update the latest index of the character
            char_index[s[end]] = end

            # Update the maximum length
            max_length = max(max_length, end - start + 1)

        return max_length


def test_length_of_longest_substring_with_unique_characters():
    assert Solution().lengthOfLongestSubstring("abc") == 3


def test_length_of_longest_substring_with_all_same_characters():
    assert Solution().lengthOfLongestSubstring("aaaaa") == 1


def test_length_of_longest_substring_with_repeating_characters():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test_length_of_longest_substring_with_empty_string():
    assert Solution().lengthOfLongestSubstring("") == 0


def test_length_of_longest_substring_with_single_character():
    assert Solution().lengthOfLongestSubstring("a") == 1


def test_length_of_longest_substring_with_special_characters():
    assert Solution().lengthOfLongestSubstring("!@#$%^&*()") == 10


def test_length_of_longest_substring_with_numbers():
    assert Solution().lengthOfLongestSubstring("1234567890") == 10

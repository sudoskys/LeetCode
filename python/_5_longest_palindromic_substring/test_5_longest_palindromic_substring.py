class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. 暴力法
        # if not s:
        #     return ""
        # if len(s) == 1:
        #     return s
        # res = ""
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if j - i + 1 > len(res) and self._isPalindrome(s, i, j):
        #             res = s[i:j + 1]
        # return res
        #
        # def _isPalindrome(self, s, l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True

        # 2. 动态规划
        if not s:
            return ""
        if len(s) == 1:
            return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""
        for i in range(n):
            dp[i][i] = True
            res = s[i]
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]
        return res


def test_solution():
    s = Solution()
    assert s.longestPalindrome("babad") == "bab"
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"

# -*- coding: utf-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 1. 暴力法
        # if not strs:
        #     return ""
        # if len(strs) == 1:
        #     return strs[0]
        # res = ""
        # for i in range(len(strs[0])):
        #     for j in range(1, len(strs)):
        #         if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]
        # return res

        # 2. 分治法
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        return self._longestCommonPrefix(strs, 0, len(strs) - 1)

    def _longestCommonPrefix(self, strs, l, r):
        if l == r:
            return strs[l]
        mid = (l + r) // 2
        lcpLeft = self._longestCommonPrefix(strs, l, mid)
        lcpRight = self._longestCommonPrefix(strs, mid + 1, r)
        return self._commonPrefix(lcpLeft, lcpRight)

    def _commonPrefix(self, left, right):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]


def test_solution():
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix([""]) == ""
    assert s.longestCommonPrefix(["", ""]) == ""

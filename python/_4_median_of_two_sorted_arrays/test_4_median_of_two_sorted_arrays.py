import pytest


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        i = j = 0
        merged = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < m:
            merged.append(nums1[i])
            i += 1

        while j < n:
            merged.append(nums2[j])
            j += 1
        print(merged)
        length = len(merged)
        if length % 2 == 0:
            return (merged[length // 2 - 1] + merged[length // 2]) / 2.0
        else:
            return merged[length // 2]


@pytest.fixture
def solution():
    return Solution()


def test_find_median_with_even_length(solution):
    nums1 = [1, 3]
    nums2 = [2, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.5


def test_find_median_with_odd_length(solution):
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2


def test_find_median_with_negative_numbers(solution):
    nums1 = [1]
    nums2 = [-1, 2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 1


def test_find_median_with_empty_array(solution):
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 3

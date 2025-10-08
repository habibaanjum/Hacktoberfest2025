class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        digit_count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 != 0:
                continue  # must be even

            num_str = str(num)
            num_digits = Counter(int(d) for d in num_str)

            # Check if num_digits can be formed from digit_count
            if all(num_digits[d] <= digit_count[d] for d in num_digits):
                result.append(num)

        return result

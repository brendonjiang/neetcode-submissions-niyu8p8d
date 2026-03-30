from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = deque()
        suffix.append(1)

        product_prefix = 1
        product_suffix = 1
        L, R = 0, len(nums)-1

        while R != 0:
            product_prefix *= nums[L]
            product_suffix *= nums[R]

            prefix.append(product_prefix)
            suffix.appendleft(product_suffix)

            L += 1
            R -= 1


        output = []
        for pre, suf in zip(prefix, suffix):
            output.append(pre*suf)

        return output

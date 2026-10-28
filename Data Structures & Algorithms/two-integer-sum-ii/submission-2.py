class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]
        i = 0
        j = len(numbers) - 1

        while i != j:
            sums = numbers[i] + numbers[j]
            if sums > target:
                j -= 1
            elif sums < target:
                i += 1
            else:
                print(i, j)
                return [i + 1, j + 1]
        
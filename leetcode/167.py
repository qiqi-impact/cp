class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        for i in range(len(numbers)-1):
            while numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
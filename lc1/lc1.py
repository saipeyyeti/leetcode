
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        num_map: dict[int, int] = {}
        for i, val1 in enumerate(nums):
            val2 = target - val1
            if val2 in num_map:
                return [num_map[val2], i]
            num_map[val1] = i
        
        return [-1, -1]

def main():
    print("two sum solution!")
    sol = Solution()
    indexList = sol.twoSum([1,2,4,5], 6)
    print(indexList[0])
    print(indexList[1])
    indexList = sol.twoSum([2,3,3,5], 6)
    print(indexList[0])
    print(indexList[1])

if __name__ == "__main__":
    main()


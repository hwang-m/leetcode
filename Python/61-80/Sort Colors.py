class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, unsorted, blue = 0, 0, len(nums) - 1
        while unsorted <= blue:
            if nums[unsorted] == 0:
                nums[red], nums[unsorted] = nums[unsorted], nums[red]
                red += 1
                unsorted += 1
            elif nums[unsorted] == 2:
                nums[blue], nums[unsorted] = nums[unsorted], nums[blue]
                blue -= 1
            else:
                unsorted += 1

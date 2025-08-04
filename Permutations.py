class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n
        def dfs(i, arr):
            if i == n:
                ans.append(path.copy())           
            for num in arr:
                path[i] = num
                dfs(i+1, arr - {num})
        dfs(0, set(nums))
        return ans

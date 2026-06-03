class Solution:
    def rob(self, nums: List[int]) -> int:
        #[1, 1, 3, 3]
        
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
            print(f"rob1: ", rob1)
            print(f"rob2: ", rob2)
        
        return rob2

        # dry run:
        # tmp = 1, 1, 4, 4, 
        # rob1 = 0, 1, 1, 4
        # rob2 = 1, 1, 4, 4
        

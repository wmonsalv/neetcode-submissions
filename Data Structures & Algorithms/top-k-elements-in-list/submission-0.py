class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        test_map = {}
        for num in nums:
            if num in test_map:
                test_map[num] += 1
            else:
                test_map[num] = 1
        tuple_Result = (test_map.items()) #<-- makes a tuple of our map 
        # print(tuple_Result)
        sorted_by_most_freq = sorted(tuple_Result, key = lambda x: x[1], reverse=True)
        # print(sorted_by_most_freq)
        ret = []
        for i in range(k):
            ret.append(sorted_by_most_freq[i][0])
        return ret
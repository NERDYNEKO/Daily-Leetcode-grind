from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        if valueDiff < 0 or indexDiff <= 0:
            return False
            
        bucket = {}
        bucket_size = valueDiff + 1
        
        for i, num in enumerate(nums):
            # Calculate bucket ID
            bucket_id = num // bucket_size
            
            # Check same bucket
            if bucket_id in bucket:
                return True
            
            # Check adjacent buckets
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= valueDiff:
                return True
            
            # Add current number to bucket
            bucket[bucket_id] = num
            
            # Remove element that's out of indexDiff range
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket_id = old_num // bucket_size
                del bucket[old_bucket_id]
        
        return False

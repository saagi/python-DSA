def longest_subarray_sum_k(arr, k):
    """
    Returns the length of the longest subarray with sum equal to k.

    Approach:
    - Use prefix sum + hashmap
    - Store first occurrence of each prefix sum
    - For each index, check if (prefix_sum - k) was seen before

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    prefix_sum = 0
    max_len = 0
    prefix_map = {}  # stores: prefix_sum -> first index

    for i, num in enumerate(arr):
        prefix_sum += num

        # Case 1: subarray from index 0 to i
        if prefix_sum == k:
            max_len = i + 1

        # Case 2: subarray from some previous index + 1 to i
        if (prefix_sum - k) in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            max_len = max(max_len, length)

        # Store first occurrence only (to maximize length)
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len

def sum_subarray_div(arr,k):
    prefix_sum = 0
    remainder_map = {0:1}
    count = 0
    for num in arr:
        prefix_sum+=num
        remainder = prefix_sum%k
        if remainder<0:
            remainder+=k
        if remainder in remainder_map:
            count+=remainder_map[remainder]
        remainder_map[remainder] = remainder_map.get(remainder,0)+1
    return count
    

if __name__=="__main__":
    nums = [1,2,2,3,4,-4,4,-4,4]
    k=4
    print(sum_subarray_div(nums,k))

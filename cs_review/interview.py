
def num_subarray(nums, k):


def two_num_sum(nums, k):
    h = HashTable()
    res = 0
    for i in range(len(nums)):
        if h.find(nums[i]):
            h[nums[i]] += 1
        else:
            h.put(nums[i], 1)
        if nums[i] == k - nums[i]:
            res += h[k - nums[i]] - 1
        else:
    return res
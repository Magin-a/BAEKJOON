#sol1
def solution(nums):
    sel_num =len(nums)/2
    
    nums = list(set(nums))
    if len(nums) >= sel_num:
        return sel_num
    else:
        return len(nums)
def smallest_missing_positive_integer(nums: List[int]) -> int:
   def smallest_missing_positive_integer(nums):


  if not nums:
    return 1

  positive_numbers = set(num for num in nums if num > 0)

  for i in range(1, len(positive_numbers) + 2):
    if i not in positive_numbers:
      return i

  return len(positive_numbers) + 1
    pass







    



  


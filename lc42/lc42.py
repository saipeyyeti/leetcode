def trap(height: list[int]) -> int:
 if not height:
  return 0

 i, j = 0, len(height) - 1
 left_max, right_max = 0, 0
 water = 0

 while i < j:
  if height[i] < height[j]:
   if height[i] >= left_max:
    left_max = height[i]
   else:
    water += left_max - height[i]
   i += 1
  else:
   if height[j] >= right_max:
    right_max = height[j]
   else:
    water += right_max - height[j]
   j -= 1
 
 return water
 
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
print(trap([0,3,0,1,4,0,2,0,5,1,0,3,2,4,0,2,1,0,3,0,4,2,0,1,5,0,2,3,0,4,1,0]))
print(trap([0]))
print(trap([5]))
print(trap([0,0]))
print(trap([2,2]))
print(trap([1,2,3,4,5]))
print(trap([5,4,3,2,1]))
print(trap([3,0,3]))
print(trap([2,0,2]))
print(trap([2,0,2,0,2]))
print(trap([3,0,1,0,2]))
print(trap([0,0,0,0]))
print(trap([2,2,2,2]))
print(trap([5,0,0,0,5]))
print(trap([5,1,2,1,5]))
print(trap([5,0,0,0,3]))
print(trap([3,0,0,0,5]))
print(trap([0,2,0,2,0,2]))
print(trap([4,1,1,1,4]))
print(trap([100000,0,100000]))
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
def TrapRainWater(height: list[int]) -> int:

 numDict: dict[int, int] = {}

 # loop through left to right and find the places
 cur = 0
 wat = 0
 full = 0
 for i in range(1, len(height)):
  if height[i] < height[cur]:
   wat += height[cur] - height[i]
  else:
   if wat > 0:
    numDict[i] = cur
    full += wat
    wat = 0
   cur = i

 # loop through right to left and find the places
 cur = len(height) - 1
 wat = 0
 j = cur - 1
 while True:
  if j < 0:
   break
  if cur in numDict:
   cur = numDict[cur]
   j = cur - 1
  else:
   if height[j] < height[cur]:
    wat += height[cur] - height[j]
   else:
    if wat > 0:
     full += wat
     wat = 0
    cur = j
   j -= 1
    

 return full
 
print(TrapRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))
print(TrapRainWater([4,2,0,3,2,5]))
print(TrapRainWater([0,3,0,1,4,0,2,0,5,1,0,3,2,4,0,2,1,0,3,0,4,2,0,1,5,0,2,3,0,4,1,0]))
print(TrapRainWater([0]))
print(TrapRainWater([5]))
print(TrapRainWater([0,0]))
print(TrapRainWater([2,2]))
print(TrapRainWater([1,2,3,4,5]))
print(TrapRainWater([5,4,3,2,1]))
print(TrapRainWater([3,0,3]))
print(TrapRainWater([2,0,2]))
print(TrapRainWater([2,0,2,0,2]))
print(TrapRainWater([3,0,1,0,2]))
print(TrapRainWater([0,0,0,0]))
print(TrapRainWater([2,2,2,2]))
print(TrapRainWater([5,0,0,0,5]))
print(TrapRainWater([5,1,2,1,5]))
print(TrapRainWater([5,0,0,0,3]))
print(TrapRainWater([3,0,0,0,5]))
print(TrapRainWater([0,2,0,2,0,2]))
print(TrapRainWater([4,1,1,1,4]))
print(TrapRainWater([100000,0,100000]))
print(TrapRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))
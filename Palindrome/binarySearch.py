# find rotation point 
# O(logN) time requirement
# return index of "rotation point" element

def rotation_point(rotated_list):
  low_idx= 0
  high_idx = len(rotated_list) - 1
  #check characteristics of list
  mid = int((low_idx + high_idx) / 2)
  if (rotated_list[0] < rotated_list[mid] and rotated_list[mid] < rotated_list[len(rotated_list) - 1]):
    print("list is already sorted left to right")
    return 0
  if (rotated_list[0] > rotated_list[mid] and rotated_list[mid] > rotated_list[len(rotated_list) - 1]):
    print("list is already sorted right to left")
    return len(rotated_list) - 1
  if rotated_list[0] > rotated_list[len(rotated_list) - 1]:
    print("sorted forward")
    sort_order = "fwd"
  else:
    print("sorted backward")
    sort_order = "bkwd"

  while low_idx <= high_idx:
    mid = int((low_idx + high_idx) / 2)
    print(f"mid is {mid}")
    mid_next = (mid + 1) % len(rotated_list)
    mid_prev = (mid - 1)
    if rotated_list[mid_prev] > rotated_list[mid] and rotated_list[mid_next] > rotated_list[mid]:
        return mid
    if sort_order == "fwd":
        print("sorting_forward")
        if rotated_list[mid] < rotated_list[high_idx] and rotated_list[mid] < rotated_list[mid_next]:
            high_idx = mid - 1
            print(f"new high_idx is {high_idx}, low_idx is {low_idx}")
        else:
            low_idx = mid + 1
            print(f"new low_idx is {low_idx}, high_idx is {high_idx}")
    else:
        print("sorting_backward")
        print(f"current values are mid = {rotated_list[mid]} and mid_prev = {rotated_list[mid_prev]} mid_next = {rotated_list[mid_next]}")
        if rotated_list[mid] > rotated_list[low_idx] and rotated_list[mid] > rotated_list[mid_prev]:
            high_idx = mid - 1
            
            print(f"new high_idx is {high_idx}, low_idx is {low_idx}")
        else:
            low_idx = mid + 1
            print(f"new low_idx is {low_idx}, high_idx is {high_idx}")
  return mid
    
  
#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['f', 'e', 'd', 'c', 'b', 'a']), 5, rotation_point(['f', 'e', 'd', 'c', 'b', 'a']) == 5))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['d', 'c', 'b', 'a', 'f']), 3, rotation_point(['d', 'c', 'b', 'a', 'f']) == 3))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 14, 15, 16, 17, 18, 8, 9, 10, 11, 12]), 6, rotation_point([13, 14, 15, 16, 17, 18, 8, 9, 10, 11, 12]) == 6))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 12, 11, 10, 9, 8, 20, 19, 18, 17, 16, 15, 14]), 5, rotation_point([13, 12, 11, 10, 9, 8, 20, 19, 18, 17, 16, 15, 14]) == 5))

print(rotation_point([2,1,6,5,4,3]))

print(rotation_point([6,1,2,3,4,5]))
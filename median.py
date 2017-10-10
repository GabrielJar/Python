def median(list_input):
  list = sorted(list_input)
  lenght = int(len(list))
  print("list: " + str(list_input))
  print("sorted list: " + str(list))
  print("lenght: " + str(lenght))
  
  if lenght == 0:
    median = 0
  
  elif lenght == 1:
    median = list[0]
  
  elif lenght % 2 == 0:
    median_index1 = (lenght // 2) - 1
    median_index2 = (lenght // 2)
    median = (list[median_index1] + list[median_index2]) / 2
  
  else:
    median_index = (lenght // 2)
    median = list[median_index]
  
  print("median: " + str(median))
  print("final do teste")
  return median

median([4, 5, 5, 4])

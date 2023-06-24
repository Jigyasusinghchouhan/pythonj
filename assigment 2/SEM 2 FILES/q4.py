def test_distinct(data):
  if len(data) == len(set(data)):
    return False
  else:
    return True;
print(test_distinct([1,3,2,3,2,3]))
print(test_distinct([1,2]))
print(test_distinct([-3,1,-1,-3,-1,1,-3,2,-1,-3]))
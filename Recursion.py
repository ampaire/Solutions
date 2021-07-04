def reAdd(a, m):
  if a == 0: 
    return m
  elif a== m:
    return a
  else:
    return a + reAdd(a + 1, m)
  

reAdd(2,5) #reAdd(2, 5) → 2 + reAdd(3, 5) → 2 + (3 + reAdd(4, 5)) → 2 + (3 + (4 +reAdd(5,5))) → 2+(3+(4+(5))) =14

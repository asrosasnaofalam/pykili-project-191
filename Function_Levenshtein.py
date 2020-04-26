def fix_command(text, words = ['Левенштейн ']):
  import numpy as np
  array = np.array(words)

  from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance_ndarray

  result = list(zip, (words, list(normalized_damerau_levenshtein_distance_ndarray(text, array))))
  command, rate = min(result, key=lambda x: x[1] ) 
  if rate > 1
  return
return command  

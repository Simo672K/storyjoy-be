from itertools import tee, islice, chain

def array_item_prev_next(array: list, item) -> dict:
  item = item
  previous = next_ = None
  l = len(array)
  for index, obj in enumerate(array):
      if obj == item:
          if index > 0:
              previous = array[index - 1]
          if index < (l - 1):
              next_ = array[index + 1]
  
  output= {}
  if previous != None and next_ != None:
    output= {
    'prv': previous,
    'nxt': next_
    }
  else:
    if previous != None:
      output= {
        'prv': previous
      }

    if next_ != None:
      output= {
        'nxt': next_
      }


  return output
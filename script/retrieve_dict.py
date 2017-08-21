# Different options of retrieving a value from a dict

sample_dict = {'apple' : 3, 'pear: 5, 'orange : 6 }

# Method 1: In Dictionary
retrieve_item = 'apple'
if  retrieve_item in sample_dict:
  return sample_dict[retrieve_item]
else:
  print('{} not found'.format( retrieve_item )
  
# Method 2: Try/Except
if  retrieve_item in sample_dict:
  return sample_dict[retrieve_item]
else:
  print('{} not found'.format( retrieve_item )
  

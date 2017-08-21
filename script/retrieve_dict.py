# Different options of retrieving a value from a dict

sample_dict = {'apple' : 3, 'pear: 5, 'orange : 6 }

# Method 1: In Dictionary
retrieve_item = 'apple'
def get_value(retrieve_item):
  if  retrieve_item in sample_dict:
    print( sample_dict[retrieve_item] )
  else:
    print('{} not found'.format( retrieve_item ))
  
# Method 2: Try/Except
def get_value(retrieve_item):
  try:
    print( sample_dict[retrieve_item] )
  except:
    print('{} not found'.format( retrieve_item ))
          
# Default Value of dict.get()
def get_value(retrieve_item):
  default = object()
  val = sample_dict.get(retrieve_item, default)
  if val is default:
    print('{} not found'.format( retrieve_item))
  
  

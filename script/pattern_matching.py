from collections import defaultdict


def get_coordinates(lines):
    '''
    args: coordinates - get a list of coordinates based on common x, * or common *, y
    return: a dictionary of coordinates keyed by x, * or *, y
    '''
    coordinates = []
    coordinates_dict = defaultdict(lambda : [])
    for i in range(len(lines)-1):
        for j in range(len(lines[i])):
            if lines[i][j] == '-':
                coordinates.append((i, j))
    for x, y in coordinates:
        coordinates_dict[(x, '*')].append((x, y))
        coordinates_dict[('*',y)].append((x, y))
    return coordinates_dict

    
def fit_coordinates(places, sort_coords):
    '''
    args: places - the list of places to fit into the puzzle
          sort_coords - list of possible fit to that place based on length
    return: a dictionary of list of possible coordinates based on place
    '''
    possible_fit = defaultdict(lambda: [])
    print(places)
    for place in places:
        for k, v in sort_coords.items():
            if len(v) == len(place):
                possible_fit[place].append(v)
    return possible_fit


def generate_materialize_dict(fitted):
    materialize_dict = {}
    for k, v in fitted.items():
        if len(v) == 1:
            temp_k = [item for item in k] 
            temp_v = v[0]
            for key, value in zip([item for item in k], v[0]):
                materialize_dict[value] = key
    for k, v in fitted.items():
        if len(v) > 1:
            for v_option in v:
                temp_k = [item for item in k] 
                temp_v = v_option 
                discontinue = False
                for key, value in zip([item for item in k], v_option):
                    if value in materialize_dict and materialize_dict[value] != key:
                        discontinue = True
                if not discontinue:
                    for key, value in zip([item for item in k], v_option):
                        materialize_dict[value] = key  
    return materialize_dict

def generate_new_output(old_lines, materialize_dict):
    new_lines = []
    for i in range(len(old_lines)-1):
        new_line = []
        for j in range(len(old_lines[i])):
            if lines[i][j] == '-' and (i, j) in materialize_dict: 
                new_line.append(materialize_dict[(i, j)]) 
            else:
                new_line.append(old_lines[i][j]) 
        new_lines.append(''.join(new_line))
    return new_lines

if __name__ == '__main__':
    str_input = ''
    lines = []
    str_input = input()
    lines.append(str_input)
    while str_input != '':
        try:
            str_input = input()
            lines.append(str_input)
        except EOFError:
            str_input = ''
    places = lines[-1].split(';')
    coordinates = get_coordinates(lines)
    fitted = fit_coordinates(places, coordinates)
    materialize_dict = generate_materialize_dict(fitted)
    new_lines = generate_new_output(lines, materialize_dict)
    for item in new_lines:
        print(item)
     


                
            
        

   
    
    
       
        

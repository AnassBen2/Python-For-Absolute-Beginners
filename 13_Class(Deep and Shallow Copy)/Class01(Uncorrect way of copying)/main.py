# Define a list of nested lists
l1 = [['Hashim', 'Tahir', 24], [1, 2, 3], ['x', True, 97.5]]

print('List 1')
print(f'Address of List 1 = {hex(id(l1))}')
print(f'Address of List 1[0] index = {hex(id(l1[0]))}')
print(f'Address of List 1[0] index item[0] = {hex(id(l1[0][0]))}')
print(f'Address of List 1[0] index item[1] = {hex(id(l1[0][1]))}')
print(f'Address of List 1[0] index item[2] = {hex(id(l1[0][2]))}')
print('-----------------------------------------------------------')
print(f'Address of List 1[1] index = {hex(id(l1[1]))}')
print(f'Address of List 1[1] index item[0] = {hex(id(l1[1][0]))}')
print(f'Address of List 1[1] index item[1] = {hex(id(l1[1][1]))}')
print(f'Address of List 1[1] index item[2] = {hex(id(l1[1][2]))}')
print('-----------------------------------------------------------')
print(f'Address of List 1[2] index = {hex(id(l1[2]))}')
print(f'Address of List 1[2] index item[0] = {hex(id(l1[2][0]))}')
print(f'Address of List 1[2] index item[1] = {hex(id(l1[2][1]))}')
print(f'Address of List 1[2] index item[2] = {hex(id(l1[2][2]))}')
print('-----------------------------------------------------------')
print('End of the first list')

l2 = l1
print('List 2')
print(f'Address of List 2 = {hex(id(l2))}')
print(f'Address of List 2[0] index = {hex(id(l2[0]))}')
print(f'Address of List 2[0] index item[0] = {hex(id(l2[0][0]))}')
print(f'Address of List 2[0] index item[1] = {hex(id(l2[0][1]))}')
print(f'Address of List 2[0] index item[2] = {hex(id(l2[0][2]))}')
print('-----------------------------------------------------------')
print(f'Address of List 2[1] index = {hex(id(l2[1]))}')
print(f'Address of List 2[1] index item[0] = {hex(id(l2[1][0]))}')
print(f'Address of List 2[1] index item[1] = {hex(id(l2[1][1]))}')
print(f'Address of List 2[1] index item[2] = {hex(id(l2[1][2]))}')
print('-----------------------------------------------------------')
print(f'Address of List 2[2] index = {hex(id(l2[2]))}')
print(f'Address of List 2[2] index item[0] = {hex(id(l2[2][0]))}')
print(f'Address of List 2[2] index item[1] = {hex(id(l2[2][1]))}')
print(f'Address of List 2[2] index item[2] = {hex(id(l2[2][2]))}')
print('-----------------------------------------------------------')
print('End of the Second list')

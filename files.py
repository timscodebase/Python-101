employees = open('./input.txt', 'r+')
print(employees.read())
add_new = True

def add_new_emp(name, position):
  emp = open('./input.txt', 'a')
  emp.write('\n' + name + ' - ' + position)
  print(employees.read())
  emp.close()

while add_new:
  name = input('Enter name: ')
  position = input('Enter position: ')
  add_new_emp(name, position)
  add_new = input('Add another employee? (y/n) ') == 'y'
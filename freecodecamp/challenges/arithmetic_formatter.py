import re

def findsign(string):
  if string.find('+') >= 0:
    return '+'
  if string.find('-') >= 0:
    return '-'
  return '#'

def findresult(first, second, sign):
  if sign == '+':
    return first + second
  return first - second

def number_with_sign(num, width, sign):
  spaces = width - len(num) - 1
  space_string = ''
  while spaces:
    space_string += ' '
    spaces -= 1
  return sign + space_string + num

def get_dash_string(width):
  ans = ''
  while width:
    ans += '-'
    width -= 1
  return ans

def arithmetic_arranger(problems, show_answer=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  else:
    lst = []
    for problem in problems:
      sign = findsign(problem)
      if sign in ['+', '-']:
        if re.search('[0-9]+\s*[-+]\s*[0-9]+', problem):
          numbers = re.findall('[0-9]+', problem)
          width = max(len(numbers[0]), len(numbers[1])) + 2
          result = findresult(int(numbers[0]), int(numbers[1]), sign)
          number_sign = number_with_sign(numbers[1], width, sign)
          dashstring = get_dash_string(width)
          lst.append((numbers[0], number_sign, dashstring, result, width))
        else:
          return 'Error: Numbers must only contain digits.'
      else:
        return "Error: Operator must be '+' or '-'."
    
    length = 3
    if show_answer: length = 4

    for i in range(length):
      temp = ''
      for index, item in enumerate(lst):
        width = item[4]
        if index != len(lst) - 1:
          temp += f"{item[i]:>{width}}" + "    "
        else:
          temp += f"{item[i]:>{width}}"
      print(temp)
        

if __name__ == '__main__':
  problems = ['32 + 44', '34 - 23', '1000+ 2300']
  arithmetic_arranger(problems)
  
          


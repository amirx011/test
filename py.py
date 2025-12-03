
name = input('whats your name? ')

match name :
    case "amir" | "mohammad" | "sara":
        print('iran')
    case "garry" | "bob":
        print('USA')


def main():
   c = int(input('enter x : '))
   if is_even (c):
     print('even')
   else:
     print('odd')





def is_even (num):
     if num % 2 == 0:
         return True
     else:
         return False



main()
   





x = int (input('enter num1 : '))
y = int(input('enter num2 : '))

if x == y:
    print('\n x == y \n you are lucky')
elif x > y:
    print('x bigger than y')
elif x < y :
    print('x less than y')

else:
    print('none')
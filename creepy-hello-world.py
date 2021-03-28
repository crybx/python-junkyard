name = 'Crybot'

print('Hello World! And hello to %s in particular.' % name) # string interpolation
print('That\'s my wonderful creator. (^_^)')
print('=o')
print('But if you\'re not Crybot, we can still be friends!')
print('...')

name = input("So what\'s your name? ")

print('Hi %s!' % name)
print('Would you like to know how long you\'ve lived in days, minutes, and seconds?')

age = int(input("Just enter your age: "))

days = age * 365
minutes = age * 525948     
seconds = age * 31556926

print(name, "has been alive for", days,"days", minutes, "minutes and", seconds, "seconds.")
print('I rounded so I didn\'t have to ask what your birthday is.')
print('Did you know?')
print('The United Nations estimate a global average life expectancy of 72.6 years for 2019.')
print('Just some thoughts.')

(input("Farewell friend."))

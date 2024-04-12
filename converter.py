def converter(phrase = 'hello world'):
  words = phrase.split(' ')
  new_phrase = ''
  
  for word in words:
    for letter in word:
      if letter in 'AEIOUaeiou':
        new_phrase += 'a'
      else:
        new_phrase += letter
    new_phrase += ' '

  return new_phrase

phrase = input('Enter a phrase:  ')

print('Here we go: ', converter(phrase)) # 'hallo warld'
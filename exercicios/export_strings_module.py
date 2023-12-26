def invertText(text):
  return text[::-1]

def returnPair(text):
  textPair = text[::2]
  return textPair
  
def returnOdd(text):
  textPair = text[1::2]
  return textPair

print(returnOdd("Diego"))


"""
Resolução PROFESSOR

def inverse(string):
    return string[::-1]

def even_characters(string):
    return string[::2]

def odd_characters(string):
    return string[1::2]
"""
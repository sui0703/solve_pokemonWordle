import pokemon_list

pokemonList = pokemon_list.pokemon_make_list()
word_frequency = pokemon_list.frequency('')

# print(*pokemonList)
# print(*word_frequency)

print('Input First Answer')
word = list(input())
# word = 'ヒノアラシ'
n = 0
candidate = pokemonList

while True:
  n += 1

  print('Enter ' + str(n)+' Result')
  print('Gray > 0, Yellow > 1, Green > 2 with no spaces! ex. > 01212')
  result = list(input())
  if len(word) != len(result):
    print('You entered the wrong result!')
    exit()
  
  for i in range(len(word)):
    result[i] = int(result[i])
  
  nResult = 0
  for i in range(len(word)):
    if result[i] == 0:
      pass
    elif result[i] == 1:
      nResult += 1
    elif result[i] == 2:
      nResult += 5
  if nResult == 25:
    exit()
  newCandidate = []
  for i in range(len(candidate)):
    if nResult == 0:
      c = True
      for j in range(len(word)):
        if word[j] in candidate[i]:
          c = False
          break
      if c:
        newCandidate.append(candidate[i])
    else:
      c = True
      for j in range(len(word)):
        if result[j] == 0:
          if word[j] in candidate[i]:
            c = False
            break
        elif result[j] == 1: # yellow
          if not (word[j] in candidate[i] and word[j] != candidate[i][j]):
            c = False
            break
        else:
          if word[j] != candidate[i][j]:
            c = False
            break
      if c:
        newCandidate.append(candidate[i])
  # print(*newCandidate)
  if len(newCandidate) == 1:
    print('Answer is '+ newCandidate[0])
    exit()
  elif len(newCandidate) == 0:
    print('Error.')
    exit()
  else:
    fre = pokemon_list.frequency(newCandidate)
    score = [[0 for i in range(2)] for j in range(len(newCandidate))]
    i = 0
    # total = 0
    for pokemon in newCandidate:
      c = 0
      for j in range(len(pokemon)):
        if pokemon[j] not in pokemon[:j]:
          c += fre[ord(pokemon[j]) - ord('ァ')]
      score[i][0] = c
      score[i][1] = pokemon
      i += 1
    score.sort(reverse=True)
    # print(*newCandidate)
    # print(newCandidate[0])
    # word = newCandidate[0]
    print('Remaining candidates : ' + str(len(newCandidate)))
    
    print(score[0][1])
    word = score[0][1]
    pass
  candidate = []
  for i in range(1,len(newCandidate)):
    candidate.append(score[i][1])

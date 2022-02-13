import pokemon_list

pokemonList = pokemon_list.pokemon_make_list()
# word_frequency = pokemon_list.frequency('')
pokemonUse = [[0 for _ in range(2)] for _ in range(len(pokemonList))]
for i in range(len(pokemonList)):
  pokemonUse[i][0] = pokemonList[i]

print('Input Maximum Number of Answers.')
t = int(input())

countInput = 0
candidate = pokemon_list.pokemon_make_list()

countAns = 0

candidate = pokemon_list.pokemon_make_list()
word_frequency = pokemon_list.frequency('')

# print(*pokemonList)
# print(*word_frequency)

n = 0
# candidate = pokemonList
success = True
while t > n:
# while True:
  n += 1

  if success:
    candidate = []
    for i in range(len(pokemonList)):
      if pokemonUse[i][1] == 0:
        candidate.append(pokemonList[i])
    fre, fre_i = pokemon_list.frequency(candidate)
    score = [[0 for i in range(2)] for j in range(len(candidate))]
    i = 0
    # total = 0
    for pokemon in candidate:
      c = 0
      for j in range(len(pokemon)):
        if (pokemon[j] not in pokemon[:j]) and 0 <= ord(pokemon[j]) - ord('ァ') <= 91:
          c += fre[ord(pokemon[j]) - ord('ァ')] * fre_i[ord(pokemon[j]) - ord('ァ')][j]
      score[i][0] = c
      score[i][1] = pokemon
      i += 1
    score.sort(reverse=True)
    # print(*newCandidate)
    # print(newCandidate[0])
    # word = newCandidate[0]
    print('Remaining candidates : ' + str(len(candidate)))
    
    print(score[0][1])
    word = score[0][1]
    num = pokemonList.index(score[0][1])
    pokemonUse[num][1] = 1 
  success = False

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
    elif result[i] == 2:
      nResult += 1
  if nResult == 5:
    success = True
    countAns += 1
  newCandidate = []
  for i in range(len(candidate)):
    c = True
    for j in range(len(word)):
      if word[j] in word[:j]:
        pass
      elif result[j] == 0:
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
  if success:
    pass
  elif len(newCandidate) == 1:
    print('Answer is '+ newCandidate[0])
    success = True
    countAns += 1
    n += 1
  else:
    fre, fre_i = pokemon_list.frequency(newCandidate)
    score = [[0 for i in range(2)] for j in range(len(newCandidate))]
    i = 0
    # total = 0
    for pokemon in newCandidate:
      c = 0
      for j in range(len(pokemon)):
        if (pokemon[j] not in pokemon[:j]) and 0 <= ord(pokemon[j]) - ord('ァ') <= 91:
          c += fre[ord(pokemon[j]) - ord('ァ')] * fre_i[ord(pokemon[j]) - ord('ァ')][j]
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
    num = pokemonList.index(score[0][1])
    pokemonUse[num][1] = 1 
  candidate = []
  for i in range(1,len(newCandidate)):
    candidate.append(score[i][1])
print(countAns)
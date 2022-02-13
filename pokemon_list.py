import csv

def frequency(pokemon_list):
  
  '''
  h[0] = 'ァ' --- h[91] = 'ー'
  h[92] = '雄' h[93] = '雌' h[94] = '2' h[95] = 'Z'
  '''
  h = [0] * 96
  h_i = [[0 for _ in range(5)] for _ in range(96)]

  if pokemon_list == '':
    fileName = 'pokemon_list.csv'
    with open(fileName, encoding= 'utf-8') as f:
      csvreader = csv.reader(f)
      for row in csvreader:
        if len(row[0])==5: #True
          for i in range(len(row[0])):
            # if row[0][i] == 'ー':
            #   h[86] += 1
            if row[0][i] == '雄':
              h[92] += 1
              h_i[92][i] += 1
            elif row[0][i] == '雌':
              h[93] += 1
              h_i[93][i] += 1
            elif row[0][i] == '2':
              h[94] += 1
              h_i[94][i] += 1
            elif row[0][i] == 'Z':
              h[95] += 1
              h_i[95][i] += 1
            else:
              h[ord(row[0][i]) - ord('ァ')] += 1
              h_i[ord(row[0][i]) - ord('ァ')][i] += 1
  else:
    for pokemon in pokemon_list:
      for j in range(len(pokemon)):
        if pokemon[j] == '雄':
          h[92] += 1
          h_i[92][j] += 1
        elif pokemon[j] == '雌':
          h[93] += 1
          h_i[93][j] += 1
        elif pokemon[j] == '2':
          h[94] += 1
          h_i[94][j] += 1
        elif pokemon[j] == 'Z':
          h[95] += 1
          h_i[95][j] += 1
        else:
          h[ord(pokemon[j])- ord('ァ')] += 1
          h_i[ord(pokemon[j]) - ord('ァ')][j] += 1
  return h, h_i

def pokemon_make_list():
  pokemonList = []
  fileName = 'pokemon_list.csv'
  with open(fileName, encoding= 'utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
      if len(row[0]) == 5:
        pokemonList.append(row[0])

  return pokemonList


# for i in range(len(h)):
#   print(chr(ord('ァ')+i),h[i])


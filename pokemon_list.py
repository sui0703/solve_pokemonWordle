import csv

def frequency(pokemon_list):
  h = [0] * 92
  if pokemon_list == '':
    fileName = 'pokemon_list.csv'
    with open(fileName, encoding= 'utf-8') as f:
      csvreader = csv.reader(f)
      for row in csvreader:
        
        if row[0][0] == 'メ' and row[0][1] == 'ガ':
          pass
        elif len(row[0])==5:
          for i in range(len(row[0])):
            # if row[0][i] == 'ー':
            #   h[86] += 1
            if row[0][i] == '・':
              pass
            else:
              # print(row[0][i],ord(row[0][i]))
              h[ord(row[0][i]) - ord('ァ')] += 1
  else:
    for pokemon in pokemon_list:
      for j in range(len(pokemon)):
        if pokemon[j] == '・':
              pass
        else:
          # print(row[0][i],ord(row[0][i]))
          h[ord(pokemon[j]) - ord('ァ')] += 1
  return h

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


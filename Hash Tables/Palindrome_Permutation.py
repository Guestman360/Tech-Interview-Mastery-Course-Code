def hasPalindromePermutation(theString):
  unpairedCharacters = set()

  for char in list(theString):
    if char in unpairedCharacters:
      unpairedCharacters.remove(char)
    else:
      unpairedCharacters.add(char)

  return len(unpairedCharacters) <= 1
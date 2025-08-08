name = "Rayan"

print(name[0:2]) # goes from index 0 to index 1 (not including index 2)

print(name[2:-1]) # Same as name[2:4], goes from index 2 to index 3 (not including index -1)

#print(name[0:5:n]) # skip n-1 characters
print(name[0:5:1]) # Skip 0 chracters
print(name[0:5:3]) # Skip 2 characters, so it will print 'Rn'

print(name[:5]) #Replace the first empty index with 0, means name[0:5]
print(name[0:]) # Replace the last empty index with the length of the string, means name[0:5]

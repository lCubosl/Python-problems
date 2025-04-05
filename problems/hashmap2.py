# given an array of strings strs, group the anagrams together. You can return the answer in any order
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_map = {}

result = []
for n in input:
  sorted_n = tuple(sorted(n))
  if sorted_n not in anagram_map:
    anagram_map[sorted_n] = []
  anagram_map[sorted_n].append(n)

for v in anagram_map.values():
  result.append(v)

print(result)
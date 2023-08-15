A = {x for x in "abcabcabc" if x not in "ab"}
B = {y for y in "abcabcabc" if y not in "bc"}
print(A | B)

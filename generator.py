def all_variants(text):
    for i in text:
        yield i
    yield text[0:2]
    yield text[1:3]
    yield text
print(all_variants('abc'))
res = all_variants('abc')
for x in res:
    print(x)
def all_variants(text):
    for start in range(len(text)):
         for end in range(start+1, len(text)+1):
            yield text[start:end]


res = all_variants('abc')
print(res)
for x in res:
    print(x)
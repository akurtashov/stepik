def get_from_str(s, n):
    num = len(s)
    for i in range(num-n+1):
        yield s[i:i+n]

test_s =input() 
sub_s = input()
count = 0
for s in get_from_str(test_s, len(sub_s)):
    if s == sub_s:
        count += 1
print(count)

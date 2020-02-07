
test_s = input() 
old_sub_s = input()
new_sub_s = input()

count = 0

new_test_s = test_s
while True:
    if new_test_s.find(old_sub_s) == -1:
        print(count)
        break
    new_test_s = test_s.replace(old_sub_s, new_sub_s)
    print(new_test_s)
    count += 1
    if count > 1000:
        print('Impossible')
        break
    test_s = new_test_s

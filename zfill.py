text = "program is fun"
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))

number = "-290"
print(number.zfill(8))

number = "+290"
print(number.zfill(8))

text = "--random+text"
print(text.zfill(20))

'''
0program is fun
000000program is fun
program is fun

-0000290
+0000290
-0000000-random+text
'''


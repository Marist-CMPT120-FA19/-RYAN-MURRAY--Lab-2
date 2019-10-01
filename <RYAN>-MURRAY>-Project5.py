Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> input_string = input('Enter your sentence:  ')
total = 0
count = {}
for char in input_string:
    total += 1
print("Number of characters: ",total) 
word_count = len(input_string.split())
print("Number of words:  ",word_count)
word_list = input_string.split()
total_letters = 0
acerage_letters = total/word_count
print("Average word length: ",float(average_letters))
SyntaxError: multiple statements found while compiling a single statement
>>> 

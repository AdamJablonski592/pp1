str = 'X-DSPAM-Confidence:0.8475'
index = str.find(':')

number = float(str[19:])
print(number)
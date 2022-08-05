text = "X-DSPAM-Confidence:    0.8475";
ispot = text.find(':')
piece = text[ispot+2:]
value = float(piece)
print(value)

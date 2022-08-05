try:
    sc = input("Enter your score between 0.0 and 1.0 ")
    score = float(sc)
    if score > 1.0 or score < 0.0:
            print ("Error, the score should be in the range between 0.0 and 1.0")
except:
    quit()

if score >= 0.9 and score < 1.0:
    print ('A')
elif score >= 0.8 and score < 0.9:
    print ('B')
elif score >= 0.7 and score < 0.8:
    print ('C')
elif  score >= 0.6 and score < 0.7 :
    print('D')
elif score < 0.6:
    print ('F')

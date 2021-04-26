def translate(phrase):
    translation =""
    for letter in phrase:
        if letter in "Aa":
            if letter.islower():
                translation = translation +str(90)
            else:
                translation =translation+ str(65)

        if letter in "Bb":
            if letter.islower():
                translation = translation + str(91)
            else:
                translation =translation+ str(66)

        if letter in "Cc":
            if letter.islower():
                translation = translation + str(92)
            else:
                translation =translation+ str(67)

        if letter in "Dd":
            if letter.islower():
                translation = translation + str(93)
            else:
                translation =translation+ str(68)

        if letter in "Ee":
            if letter.islower():
                translation = translation + str(94)
            else:
                translation =translation+ str(69)

        if letter in "Ff":
            if letter.islower():
                translation = translation +str(95)
            else:
             translation =translation+ str(70)

        if letter in "Gg":
            if letter.islower():
                translation = translation + str(96)
            else:
             translation =translation+ str(71)

        if letter in "Hh":
            if letter.islower():
                translation = translation + str(97)
            else:
                translation = translation + str(72)

        if letter in "Ii":
            if letter.islower():
                translation = translation + str(98)
            else:
                translation =translation+ str(73)

        if letter in "Jj":
            if letter.islower():
                translation = translation + str(99)
            else:
                translation =translation+ str(74)

        if letter in "Kk":
            if letter.islower():
                translation = translation + str(100)
            else:
                 translation =translation+ str(75)

        if letter in "Ll":
            if letter.islower():
                translation = translation + str(101)
            else:
                 translation =translation+ str(76)

        if letter in "Nn":
            if letter.islower():
                translation = translation + str(102)
            else:
                translation =translation+ str(77)

        if letter in "Oo":
            if letter.islower():
                translation = translation + str(103)
            else:
                translation =translation+ str(78)

        if letter in "Pp":
            if letter.islower():
                translation = translation + str(104)
            else:
                translation =translation+ str(79)

        if letter in "Qq":
            if letter.islower():
                translation = translation + str(105)
            else:
                 translation =translation+ str(80)

        if letter in "Rr":
            if letter.islower():
                translation = translation + str(106)
            else:
             translation =translation+ str(81)

        if letter in "Ss":
            if letter.islower():
                translation = translation + str(107)
            else:
                translation =translation+ str(82)

        if letter in "Tt":
            if letter.islower():
                translation = translation + str(108)
            else:
                 translation =translation+ str(84)

        if letter in "Uu":
            if letter.islower():
                translation = translation + str(109)
            else:
             translation =translation+ str(84)

        if letter in "Vv":
            if letter.islower():
                translation = translation + str(110)
            else:
                translation =translation+ str(85)

        if letter in "Ww":
            if letter.islower():
                translation = translation + str(110)
            else:
                translation =translation+ str(86)

        if letter in "Xx":
            if letter.islower():
                translation = translation + str(111)
            else:
                 translation =translation+ str(87)

        if letter in "Yy":
            if letter.islower():
                translation = translation + str(112)
            else:
                 translation =translation+ str(88)

        if letter in "Zz":
            if letter.islower():
                translation = translation + str(113)
            else:
                translation =translation+ str(89)
    return translation

print(translate(input (" Enter A Phrase : ")))

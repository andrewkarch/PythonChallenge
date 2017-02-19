str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
outstring = ''
for character in str:
    if character == "z":
        outstring += "b"
    elif character == "y":
        outstring += "a"
    elif character != " " and character != ".":
        outstring += chr(ord(character)+2)
    else:
        outstring += character
print outstring

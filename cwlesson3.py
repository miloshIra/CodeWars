def reverse_complement(dna):
    c=""
    for i in dna:
        if i == "A":
            c+="T"
        elif i == "C":
            c+="G"
        elif i == "T":
            c+="A"
        elif i == "G":
            c+="C"
        else:
            return "Invalid sequence"
    print(c)


reverse_complement("AAAACCTT")

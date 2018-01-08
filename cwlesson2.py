def get_sumwrong(a,b):
    s=0
    for i in range(a,b):   # Worng because range(a,b) doesnt incluve last b memnber (how range works)
        s=s+i
    print(s)


def get_sum(a,b):
    s=0
    for i in range(min(a,b),max(a,b)+1) # Right sorting min to max for errorless summery and +1 so it includes the last memeber of a to b
        s=s+i
    return s

get_sum(0,1)

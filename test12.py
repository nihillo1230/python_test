import turtle as t
t.shape("turtle")

for dan in range(2,9+1):
    if (dan%3==2):
        x=-100
        y=200-100*(dan//3)
    if (dan%3==0):
        x=0
        y=200-100*((dan//3)-1)
    if (dan%3==1):
        x=100
        y=200-100*((dan//3)-1)
    for gop in range(1,9+1):
        t.goto(x,y)
        t.write("%d * %d = %2d"%(dan,gop,dan*gop),False,"left",("",10))
        y=y-10
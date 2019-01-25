
    
def hanoi(n,src = 'A',dst = 'B',tmp = 'C'):
    if n == 1:
        print ("Move disk 1 from peg", src, "to peg", dst)
    else:
        hanoi(n-1,src,tmp,dst)
        print ("Move disk", n ,"from peg", src,"to peg", dst)
        hanoi(n-1,tmp, dst, src)
    
    
  
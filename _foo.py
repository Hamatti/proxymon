#coding=utf8

from ptcgo import PTCGOParser as ptc

decklist = open('foo.dec', 'r').read() 
p = ptc(decklist)
p.run()
out = open('tmp.html', 'w')
out.write(p.full_html)
out.close()

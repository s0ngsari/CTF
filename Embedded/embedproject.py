from idaapi import *
from idc import *


findfunc = ["sprintf"]
f = open("ins.txt","w")
for func in findfunc:
	addr = LocByName( func )
	if addr != BADADDR:
		xrefs = CodeRefsTo( addr, 0 )
		print "Cross References to %s" % func
		print "-------------------------------"
		for ref in xrefs:
			for ins in XrefsTo(ref,0):
				
				# print "-----------------------------"
				# print "[*] Call sprintf : 0x%08x" % ref
				# print XrefTypeName(ins.type), 'from' , hex(ins.frm-4), 'to', hex(ins.to)
				string = "%s"

				for i in range(1,4):
					if string in GetDisasm(ins.frm-(i*4)):
						for ins in XrefsTo(ref,0):
							
							print "-----------------------------"
							print "[*] Call sprintf : 0x%08x" % ref
							disas = GetDisasm(ins.frm-(i*4)) + "\n"
							result = "[*] Offset : " + hex(ref) + "\n" + disas
							print "[*] %s" % disas
							f.write(result)
							
					else:
						a = 1

    			
f.close()
for got in CodeRefsFrom(addr,1):
		print "-----------------------------"
		print "[*] GOT of sprintf : 0x%08x" % got

       	# for ins in XrefsTo(here(), 0):
        #   print ins.type, XrefTypeName(ins.type), 'from' , hex(ins.frm-4), 'to', hex(ins.to)
 
print "End!"

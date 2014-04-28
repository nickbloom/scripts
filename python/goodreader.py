import fileinput,os,re

os.chdir('/Users/nbloom/Downloads/mailfiles/')

for line in fileinput.input():
	myfi=open(interim, "r",encoding='utf-8')
	fifi=myfi.read()


rule1=re.compile(r'Highlight \(color #[\w]{6}\), [A-Z][a-z]{2} [\d]{1,2}, [\d]{4}, [0-9]\:[\d]{2} [A/P]M, Nick Bloom\:')
rule2=re.compile(r'\n\n')
rule3=re.compile(r'\n--')
rule4=re.compile(r'(?<=File\:\s)[A-za-z\-\s0-9]{1,500}(?!pdf)')



outfi = rule1.sub("",fifi)	
outfi = rule2.sub("",outfi)
outfi = rule3.sub("\n\n--",outfi)

myfi.seek(0)
title = myfi.readline()
title = re.search(r'(?<=File\:\s)[A-za-z\-\s0-9]{1,500}(?!pdf)',title)
title = title.group()

fi_out = open('/Users/nbloom/Desktop/'+title, 'w+', encoding='utf-8')
fi_out.write(outfi)
fi_out.close()
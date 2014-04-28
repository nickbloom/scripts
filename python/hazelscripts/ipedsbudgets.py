import fileinput,os,re,sys

rule1=re.compile(r'(?<=F)[0-9]{2}(?=[0-9]{2})')
rule2=re.compile(r'(?<=[0-9]{4}_)F[123A]{1,2}')

os.chdir('/Users/nbloom/Downloads/')
files=os.listdir()

myfi=sys.argv[1]
myfiname=str(myfi)

year = re.search(rule1, myfiname)
year = year.group()

control = re.search(rule2, myfiname)
control = control.group()

if float(year) > 14:
	year = '19' + year
else:
	year = '20' + year

if control=='F1A':
	os.rename(myfi, '/Users/nbloom/Transporter/nick/statistics/datasets/ipeds-tuition-data/' + year + '/budgets/public.csv')
elif control=='F2':
	os.rename(myfi, '/Users/nbloom/Transporter/nick/statistics/datasets/ipeds-tuition-data/' + year + '/budgets/pnfp.csv')
else control=='F3':
	os.rename(myfi, '/Users/nbloom/Transporter/nick/statistics/datasets/ipeds-tuition-data/' + year + '/budgets/pfp.csv')				
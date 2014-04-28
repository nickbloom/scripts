import fileinput,os,re,sys

rule1=re.compile(r'(?<=IC)[0-9]{4}(?=_AY)')

os.chdir('/Users/nbloom/Downloads/')
files=os.listdir()

myfi=sys.argv[1]
myfiname=str(myfi)

year = re.search(rule1, myfiname)
year = year.group()

os.rename(myfi, '/Users/nbloom/Transporter/nick/statistics/datasets/ipeds-tuition-data/' + year + '/costs/tuition.csv')			
list1 = [1,2,3,4,5]
list2 = [1,2,"ham"]

# Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain an heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

tup1= 1,2,3,'hambaga'
emptytup = ()

# SETS
## A set is an unordered collection with no duplicate elements.

#create sets like this
set0 = {'p', 'a', 'm', 'p', 'l', 'o', 'n', 'a'}
# or like this
set1 = set('pamplona')
set2 = set('pyjama')
emptyset = ()

# things in set 1 that aren't in set2

set1 - set2

# things in both

set1 & set2

# things in either (and both)

set1 | set2

# things in either (but not both)

set1 ^ set2

# a more complicated way to do it
onenottwo = {x for x in set1 if x not in set2}

# DICTIONARY
# big boys. It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary).

birthdays = {'nick':'May 28', 'kate':'Feb 15', 'keaton':'Sept 28'}
emptydict= {}

# add to dict
birthdays['dad']='June 24'

# create dictionary from two lists
names = 'nick', 'kate', 'keaton'
bdays = 'May 28', 'Feb 15', 'Sep 28'

# getting both things out of a dict
for x,y in birthdays.items():
	print(x,y)


	url=""
	print(url)
	html = urllib.request.urlopen(url).read()
	h = html.decode('utf-8')
	soup = BeautifulSoup(h)
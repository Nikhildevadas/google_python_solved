import re
import sys
filenames=sys.argv[1]
l=[]
#str=filename
str1=re.findall(r'(\d+)',filenames)
print str1
def extract_names(filenames):
	filename=open(sys.argv[1]).read()
	return filename
extract_names(filenames)
#for i in extract_names(filenames):
	#print '\n'+i
match = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', extract_names(filenames))
l.append(match)	
#print l[0] 
names_rank =  {}
for i in l[0]:
	(rank,boyname,girlname)=i
	if boyname not in names_rank:
		names_rank[boyname]=rank
	if girlname not in names_rank:
		names_rank[girlname]=rank
print names_rank
print str1[0]+'\n'
for key in sorted(names_rank.keys()):
	print key, names_rank[key]



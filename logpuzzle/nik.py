
import os
import re
import sys
import urllib
def read_urls(filename):
	x=filename.index('_')
	host=filename[x + 1:]
	url_dict = {}
	f=open(filename)
	for i in f:
		match = re.search(r'"GET (\S+)', i)
		if match:
      			path = match.group(1)
		if 'puzzle' in path:
			url_dict['http://' + host + path] = 1
	return sorted(url_dict.keys(), key=url_sort_key)	
       # print url_dict.keys()
def url_sort_key(url):
	match = re.search(r'-(\w+)-(\w+)\.\w+', url)
	if match:
		return match.group(2)
	else:
		return url
l= read_urls(sys.argv[1])
dest_dir=sys.argv[2]
def download_images(img_urls, dest_dir):
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')

  i = 0
  for img_url in img_urls:
    local_name = 'img%d' % i
    print 'Retrieving...', img_url
    urllib.urlretrieve(img_url, os.path.join(dest_dir, local_name))

    index.write('<img src="%s">' % (local_name,))
    i += 1

  index.write('\n</body></html>\n')
  index.close()
download_images(l,dest_dir) 

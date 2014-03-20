import os
import re
import sys
import shutil
import commands
l=[]

def main():
	dirname=sys.argv[2]
	args=sys.argv[1]
	paths=[]
	paths=get_sp_paths(dirname)
	if args==".":
		print paths
	elif args=="--todir":
     
		todir=sys.argv[3]
		copy_to(paths,todir)
	elif args=="--tozip":
		zipfile=sys.argv[3]
		zip_to(paths,zipfile)	
def get_sp_paths(dirname):
  result = []
  paths = os.listdir(dirname)  # list of paths in that dir
  for i in paths:
    match = re.search(r'__(\w+)__', i)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, i)))
  return result

#get_sp_paths(dirname)

def copy_to(paths,dirname):
  if not os.path.exists(dirname):
    os.mkdir(dirname)
  for path in paths:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(dirname, fname))	

def zip_to(paths, zipfile):
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print cmd
  (status, output) = commands.getstatusoutput(cmd)


if __name__ == "__main__":
  main()

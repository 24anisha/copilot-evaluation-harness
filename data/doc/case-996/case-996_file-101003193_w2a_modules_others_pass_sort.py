#  modules/get_info.py
#
#  Copyright 2012 Kid :">

from w2a.core.templates import Templates
from w2a.lib.file import full_path, read_from_file, write_to_file, list_dir
from w2a.config import CONFIG

class Module(Templates):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.version		= 1
		self.author			= [ 'Kid' ]
		self.description 	= 'sort password list'
		self.detailed_description	= 'This module retreives sort all password list'
		
		self.options.add_path('INPUT', 'Path to password list directory')
		self.options.add_path('OUTPUT', 'Output directory')

	def run(self, frmwk, args):
		passlist	= {}
		paths	= list_dir(self.options['INPUT'])
		for path in paths:
			p = self.options['INPUT'] + '/' + path
			frmwk.print_status('Sorting: ' + p)
			data = read_from_file(full_path(p))
			if p.find('withcount') == -1:
				for d in data:
					d = d.strip()
					if d != '':
						if d in passlist:
							passlist[d] += 1
						else:
							passlist[d] = 1
			else:
				for d in data:
					d = d.strip().split(' ', 1)
					if len(d) == 2:
						if d[1] in passlist:
							passlist[d[1]] += int(d[0])
						else:
							passlist[d[1]] = int(d[0])
		
		output = sorted([(v,k) for (k,v) in passlist.items()], reverse=True)
		outpath = self.options['OUTPUT'] + '/out.lst'
		frmwk.print_success('Output: ' + outpath)
		write_to_file(full_path(outpath), (o[1] for o in output))
		write_to_file(full_path(outpath+ '.withcount'), (str(o[0])+' '+o[1] for o in output))
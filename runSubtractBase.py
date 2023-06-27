import numpy 
import pysic
#import pygreg
#import pyastro
import pyclass
#import pyclic
#import pymapping

lineFreq = '110381.404' 
mol = 'ch3cn'

#infile = ['FTSOdp20150211','FTSOdp20150211','FTSOdp20150216','FTSOdp20150216','20150518','20150518']
infile = ['FTSOdp20150213','FTSOdp20150213','20150518','20150518']

#telescope = ['30ME0VLO-F05','30ME0HLO-F07','30ME0VLO-F05','30ME0HLO-F07','30ME0VLO-F05','30ME0HLO-F07']
#telescope = ['30ME0VLI-F03','30ME0HLI-F01','30ME0VLI-F03','30ME0HLI-F01','30ME0VLI-F03','30ME0HLI-F01']
#telescope = ['30ME0VUI-F04','30ME0HUI-F02','30ME0VUI-F04','30ME0HUI-F02','30ME0VUI-F04','30ME0HUI-F02']
#telescope = ['30ME0VLO-F05','30ME0HLO-F07','30ME0VLO-F05','30ME0HLO-F07']
#telescope = ['30ME0VLI-F03','30ME0HLI-F01','30ME0VLI-F03','30ME0HLI-F01']
#telescope = ['30ME0VUI-F04','30ME0HUI-F02','30ME0VUI-F04','30ME0HUI-F02']
telescope = ['30ME0VUO-F06','30ME0HUO-F08','30ME0VUO-F06','30ME0HUO-F08']

#outfile = ['base'+mol+'1105.30m','base'+mol+'1107.30m','base'+mol+'1605.30m','base'+mol+'1607.30m','base'+mol+'1805.30m','base'+mol+'1807.30m']
outfile = ['base'+mol+'1306.30m','base'+mol+'1308.30m','base'+mol+'1806.30m','base'+mol+'1808.30m']

for inf, tel, outf in zip(infile,telescope,outfile):
	pysic.comm('@subtractBase ' + inf + ' ' + tel + ' ' + outf + ' ' + lineFreq)

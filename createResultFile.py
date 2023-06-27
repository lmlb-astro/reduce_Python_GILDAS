import numpy 
import pysic
#import pygreg
#import pyastro
import pyclass
#import pyclic
#import pymapping

resX = '10'
resY = '10'
molecule = 'hcn'

#telescope16 = ['05','07']
telescope16 = ['01','03']
scanHor11 = ['120','122','145','147','153','155','163','165','171','173','182','184','190','192','198']
scanHor16 = ['129','131','137','139','155','157']
scanHor18 = ['2','23','25','33','35','41','43','239']

scanVer11 = ['124','126','134','149','151','157','159','167','169','175','177','186','188','194','196']
scanVer16 = ['133','135','141','143','159','161']
scanVer18 = ['4','6','27','29','37','39','45','47']

#scanHor13 = ['115','117','125','127','136','138','144','167','173','175','181','183','193','195','201','203']
#scanHor18 = ['63','65','71','73','81','83','89','91','100','102']

#scanVer13 = ['119','121','129','131','140','142','169','171','177','179','185','187','197','199','205','207']
#scanVer18 = ['67','69','75','77','85','87','93','95','104','106','108','110']

pysic.comm('file out resultTest.30m s /overwrite')

for tel in telescope16:
	for scan in scanHor11:
		pysic.comm('@clean_hor ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '11' + tel)
	for scan in scanHor16:
		pysic.comm('@clean_hor ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '16' + tel)
	for scan in scanHor18:
		pysic.comm('@clean_hor ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '18' + tel)
	
	for scan in scanVer11:
		pysic.comm('@clean_ver ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '11' + tel)
	for scan in scanVer16:
		pysic.comm('@clean_ver ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '16' + tel)
	for scan in scanVer18:
		pysic.comm('@clean_ver ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '18' + tel)

#for tel in telescope16:
#	for scan in scanHor13:
#		pysic.comm('@clean_hor ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '13' + tel)
#	for scan in scanHor18:
#		pysic.comm('@clean_hor ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '18' + tel)
#	
#	for scan in scanVer13:
#		pysic.comm('@clean_ver ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '13' + tel)
#	for scan in scanVer18:
#		pysic.comm('@clean_ver ' + scan + ' ' + resX + ' ' + resY + ' base' + molecule + '18' + tel)


pysic.comm('@clean_final result_'+molecule)

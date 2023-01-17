from drg_group.suzhou_2022.Base import message,intersect,SS_VALID
from drg_group.suzhou_2022.DRG import MDCX_DRG

def group(record):
  adrg_zd=["R74.804","R79.804","R89.000","R89.100","R89.200","R89.300","R89.400","R89.500","R89.600","R89.700","R89.800","R93.202","R93.301","Z00.500x001","Z00.600","Z00.800","Z01.001","Z01.002","Z01.101","Z01.102","Z01.200","Z01.300","Z01.600","Z01.600x001","Z01.700","Z01.800x001","Z01.800x004","Z02.000","Z02.100","Z02.200","Z02.300","Z02.400","Z02.500","Z02.600","Z02.700","Z02.800","Z02.900","Z04.001","Z04.002","Z04.100","Z04.200","Z04.300","Z04.400","Z04.500","Z04.800","Z09.000x001","Z09.300","Z09.400","Z09.700","Z09.801","Z09.802","Z09.803","Z09.804","Z09.900x001","Z10.100","Z10.200","Z10.300","Z10.800","Z29.101","Z29.200x001","Z29.201","Z29.800","Z29.900","Z51.600","Z51.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合XS2入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XS21_group(record):
      return 'XS21'

    if MDCX_DRG.XS23_group(record):
      return 'XS23'

    if MDCX_DRG.XS25_group(record):
      return 'XS25'

  return ''


from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F50.000","F50.100","F50.200","F50.300","F50.401","F50.501","F50.502","F50.800x002","F50.801","F50.900","F51.000","F51.100","F51.200","F51.200x002","F51.200x003","F51.300","F51.400","F51.500","F51.800","F51.900","G47.000","G47.000x001","G47.000x002","G47.100","G47.200x002","G47.200x003","G47.400x002","G47.400x003","G47.800x001","G47.800x002","G47.801","G47.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合TT1入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TT19_group(record):
      return 'TT19'

    return 'TT1'
  else:
    return ''


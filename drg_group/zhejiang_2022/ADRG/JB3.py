from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCJ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["40.1900x002","40.2200","85.0x00x002","85.0x00x003","85.0x01","85.0x02","85.1100x003","85.1200x001","85.2500","85.8100","85.9100","85.9300","85.9400","85.9500","85.9600","85.9900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JB3入组条件，匹配规则：某一手术匹配')
    
    if MDCJ_DRG.JB31_group(record):
      return 'JB31'

    if MDCJ_DRG.JB33_group(record):
      return 'JB33'

    if MDCJ_DRG.JB35_group(record):
      return 'JB35'

    return 'JB3'
  else:
    return ''


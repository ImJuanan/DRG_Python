from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["69.0101","69.0200x003","69.0902","69.5101","69.5102","69.5103","69.5202","69.5901","73.1x00x001","73.1x00x002","73.1x01","73.1x02","73.4x00x004","73.8x00x003","74.9100","74.9100x001","74.9101","75.0x01","75.0x02","75.0x03"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OF1入组条件，匹配规则：某一手术匹配')
    
    if MDCO_DRG.OF11_group(record):
      return 'OF11'

    if MDCO_DRG.OF13_group(record):
      return 'OF13'

    if MDCO_DRG.OF15_group(record):
      return 'OF15'

    return 'OF1'
  else:
    return ''


from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCJ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["85.3100","85.3200","85.3300x001","85.3500x001","85.5100x001","85.5200x001","85.5300x001","85.5400x001","85.5500x001","85.5500x002","85.6x00x001","85.7000x001","85.7100x001","85.7200x001","85.7300x001","85.7400x001","85.7500x001","85.7600x001","85.7900x001","85.8601","85.8700x003","85.8701","85.8702","85.8900x005","85.8900x006","85.8900x007","85.8900x008","85.8901"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JB1入组条件，匹配规则：某一手术匹配')
    
    if MDCJ_DRG.JB11_group(record):
      return 'JB11'

    if MDCJ_DRG.JB13_group(record):
      return 'JB13'

    if MDCJ_DRG.JB15_group(record):
      return 'JB15'

    return 'JB1'
  else:
    return ''


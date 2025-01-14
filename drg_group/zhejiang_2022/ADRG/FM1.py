from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["36.0601","36.0602","36.0700x004","36.0701"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FM1入组条件，匹配规则：某一手术匹配')
    
    if MDCF_DRG.FM11_group(record):
      return 'FM11'

    if MDCF_DRG.FM13_group(record):
      return 'FM13'

    if MDCF_DRG.FM15_group(record):
      return 'FM15'

    return 'FM1'
  else:
    return ''


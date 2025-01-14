from drg_group.yancheng_2022.Base import message,intersect,SS_VALID
from drg_group.yancheng_2022.DRG import MDCZ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and (not record.ssList or record.ssList[0] not in SS_VALID):
    message('符合ZZ1入组条件，匹配规则：无手术')
    
    if MDCZ_DRG.ZZ11_group(record):
      return 'ZZ11'

    if MDCZ_DRG.ZZ15_group(record):
      return 'ZZ15'

    return 'ZZ1'
  else:
    return ''


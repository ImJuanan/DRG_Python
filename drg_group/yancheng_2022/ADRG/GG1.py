from drg_group.yancheng_2022.Base import message,intersect,SS_VALID
from drg_group.yancheng_2022.DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["54.5100","54.5100x005","54.5100x009","54.5101","54.5102","54.5103","54.5900x007","54.5901","54.5902","54.5903","54.5904","54.5905","54.5906"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合GG1入组条件，匹配规则：主手术匹配')
    
    if MDCG_DRG.GG19_group(record):
      return 'GG19'

    return 'GG1'
  else:
    return ''


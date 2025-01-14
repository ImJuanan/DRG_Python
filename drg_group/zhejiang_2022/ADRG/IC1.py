from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.7000x001","00.7100x001","00.7200x001","00.7201","00.7300x001","00.7300x002","00.7300x003","00.7301","00.8000x001","00.8100x001","00.8200x001","00.8201","00.8300x001","00.8400x001","81.9700x002"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IC1入组条件，匹配规则：某一手术匹配')
    
    if MDCI_DRG.IC11_group(record):
      return 'IC11'

    if MDCI_DRG.IC13_group(record):
      return 'IC13'

    if MDCI_DRG.IC15_group(record):
      return 'IC15'

    return 'IC1'
  else:
    return ''


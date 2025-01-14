from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=["S72.300","S72.310","S72.400x001","S72.400x012","S72.400x013","S72.400x021","S72.400x031","S72.400x041","S72.401","S72.410","S72.700","S72.800","S72.900","S72.900x002"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合IR3入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IR31_group(record):
      return 'IR31'

    if MDCI_DRG.IR33_group(record):
      return 'IR33'

    if MDCI_DRG.IR35_group(record):
      return 'IR35'

    return 'IR3'
  else:
    return ''


from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["81.0100x001","81.0101","81.0102","81.0103","81.0104","81.0105","81.0200x001","81.0200x002","81.0300x001","81.0300x002","81.0400x004","81.0400x005","81.0401","81.0402","81.0500x005","81.0500x006","81.0501","81.0502","81.0600x005","81.0600x006","81.0601","81.0602","81.0700x002","81.0701","81.0702","81.0800x016","81.0800x017","81.0800x018","81.0801","81.0802"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IB1入组条件，匹配规则：某一手术匹配')
    
    if MDCI_DRG.IB11_group(record):
      return 'IB11'

    if MDCI_DRG.IB13_group(record):
      return 'IB13'

    if MDCI_DRG.IB15_group(record):
      return 'IB15'

    return 'IB1'
  else:
    return ''


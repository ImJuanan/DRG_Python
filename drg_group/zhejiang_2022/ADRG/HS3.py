from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=["B15.900","B15.901","B15.902","B15.903","B15.905","B16.100","B16.100x002","B16.100x003","B16.100x004","B16.101","B16.901","B16.902","B16.903","B16.904","B16.905","B17.100","B17.100x003","B17.100x006","B17.101","B17.200","B17.200x004","B17.202","B17.203","B17.805","B17.806","B17.900","B17.900x002","B17.900x004","B17.901","B17.902","B17.903","B17.904","B18.002","B18.003","B18.100","B18.100x007","B18.101","B18.102","B18.104","B18.105","B18.107","B18.200","B18.200x009","B18.200x011","B18.200x012","B18.201","B18.202","B18.203","B18.800x001","B18.800x002","B18.800x005","B18.801","B18.802","B18.818","B18.900","B18.900x006","B18.900x021","B18.900x022","B18.901","B18.902","B19.900","B19.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合HS3入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HS31_group(record):
      return 'HS31'

    if MDCH_DRG.HS33_group(record):
      return 'HS33'

    if MDCH_DRG.HS35_group(record):
      return 'HS35'

    return 'HS3'
  else:
    return ''


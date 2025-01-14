from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=["E03.500","G93.500x001","G93.500x002","G93.500x005","G93.500x006","G93.500x007","G93.500x008","G93.500x009","G93.500x010","G93.501","G93.600","G93.600x002","G93.600x003","G93.600x004","G93.600x005","G93.600x006","G93.600x007","G93.600x008","G93.600x009","G97.100x003","R40.000","R40.100","R40.100x002","R40.100x003","R40.100x005","R40.200","R40.200x002","R40.200x004","R40.200x005","R40.201"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合BS1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BS19_group(record):
      return 'BS19'

    return 'BS1'
  else:
    return ''


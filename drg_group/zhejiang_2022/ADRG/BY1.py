from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=["S01.800x011","S01.800x021","S01.800x081","S01.800x083","S01.800x086","S01.800x087","S02.000","S02.000x003","S02.000x004","S02.000x005","S02.001","S02.002","S02.011","S02.012","S02.100","S02.100x002","S02.100x003","S02.100x004","S02.100x006","S02.100x008","S02.100x009","S02.101","S02.102","S02.103","S02.111","S02.112","S02.113","S02.114","S02.300","S02.300x002","S02.700x001","S02.700x002","S02.701","S02.712","S02.900x002","S02.902","S02.911","S06.211","S06.310","S06.700x005","S06.700x006","S06.700x007","S06.700x008","S06.710","S06.814","S06.910","S06.911","T02.000x001","T02.010"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合BY1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BY19_group(record):
      return 'BY19'

    return 'BY1'
  else:
    return ''


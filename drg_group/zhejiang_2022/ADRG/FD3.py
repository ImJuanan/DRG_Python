from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["35.4200x003","35.4200x009","35.5200x001","35.5200x002","35.5201","35.5202","35.5500x001","35.5501","35.9800x001","35.9800x002","36.9900x005","36.9901","39.7900x008","39.7900x014","39.9000x026"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FD3入组条件，匹配规则：某一手术匹配')
    
    if MDCF_DRG.FD39_group(record):
      return 'FD39'

    return 'FD3'
  else:
    return ''


from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCD_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["27.5301","27.5302","27.5401","27.5911","27.5915","27.6100","27.6200x002","27.6200x003","27.6201","27.6300x002","27.6301","27.6302","27.6400","27.6900x003","27.6900x004","27.6900x007","27.6900x008","27.6901","27.6902","27.6903","27.6904","27.6905","27.6906","27.6907","27.6908","27.6909","27.7100","27.7202","27.7300","27.9100x001","27.9101","27.9900x006"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DG3入组条件，匹配规则：某一手术匹配')
    
    if MDCD_DRG.DG30_group(record):
      return 'DG30'

    if MDCD_DRG.DG39_group(record):
      return 'DG39'

    return 'DG3'
  else:
    return ''


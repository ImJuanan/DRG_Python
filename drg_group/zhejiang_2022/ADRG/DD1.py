from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCD_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["21.3200x011","21.8300x001","21.8301","21.8302","21.8400x002","21.8400x003","21.8400x006","21.8401","21.8402","21.8500x002","21.8500x004","21.8500x005","21.8500x007","21.8500x008","21.8500x010","21.8500x011","21.8501","21.8502","21.8503","21.8504","21.8505","21.8600x004","21.8601","21.8602","21.8603","21.8700x003","21.8700x004","21.8700x005","21.8700x008","21.8700x009","21.8701","21.8702","21.8801","21.8802","21.8900x002","21.8900x003","21.8900x004","21.8901","21.9901"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DD1入组条件，匹配规则：某一手术匹配')
    
    if MDCD_DRG.DD19_group(record):
      return 'DD19'

    return 'DD1'
  else:
    return ''


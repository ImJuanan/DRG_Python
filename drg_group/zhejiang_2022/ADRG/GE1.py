from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["17.1100x001","17.1200x001","17.1300x001","17.1300x002","17.2100x001","17.2200x001","17.2300x001","17.2400x001","53.0001","53.0002","53.0100x001","53.0101","53.0102","53.0201","53.0202","53.0203","53.0204","53.0301","53.0302","53.0401","53.0501","53.1000","53.1101","53.1201","53.1202","53.1203","53.1301","53.1401","53.1501","53.1601","53.1701","53.2101","53.2901","53.3101","53.3901","53.6200","53.6301","53.6302","53.6901"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GE1入组条件，匹配规则：某一手术匹配')
    
    if MDCG_DRG.GE10_group(record):
      return 'GE10'

    if MDCG_DRG.GE11_group(record):
      return 'GE11'

    if MDCG_DRG.GE13_group(record):
      return 'GE13'

    if MDCG_DRG.GE15_group(record):
      return 'GE15'

    if MDCG_DRG.GE19_group(record):
      return 'GE19'

    return 'GE1'
  else:
    return ''


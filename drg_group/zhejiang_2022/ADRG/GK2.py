from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["42.3300x006","42.3300x007","42.3301","42.3310","42.8100","42.8101","42.9200x006","42.9202","42.9900x001","42.9901","43.1100x001","43.4100x011","43.4100x013","43.4100x014","43.4100x015","43.4100x016","43.4100x020","43.4101","43.4102","43.4103","43.4104","43.4105","43.4109","43.4110","44.2200x001","44.2201","44.2202","44.4300x001","44.4300x002","44.4301","44.4302","44.4303","44.9300","44.9400","44.9800x003","44.9800x004","45.3001","46.8500x005","46.8501","46.8503","46.8510","98.0301","98.0302"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GK2入组条件，匹配规则：某一手术匹配')
    
    if MDCG_DRG.GK21_group(record):
      return 'GK21'

    if MDCG_DRG.GK23_group(record):
      return 'GK23'

    if MDCG_DRG.GK25_group(record):
      return 'GK25'

    return 'GK2'
  else:
    return ''


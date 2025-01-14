from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCD_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["21.0100","22.1100x002","22.1200","22.1901","23.5x01","23.7000x001","23.7001","23.7002","24.7x01","24.7x02","24.7x03","24.7x04","24.8x02","26.1100x001","26.1100x003","26.1200x001","26.1200x002","26.1900x001","27.2101","27.2901","27.9201","29.1204","31.4301","31.4502","31.9400","31.9804","31.9805","31.9806","31.9902","42.3200x003","96.0600","98.0101","98.1100x001","98.1200x001","98.1201","98.1300x001","98.1400x001","98.1400x002","98.1501"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DK1入组条件，匹配规则：某一手术匹配')
    
    if MDCD_DRG.DK11_group(record):
      return 'DK11'

    if MDCD_DRG.DK13_group(record):
      return 'DK13'

    if MDCD_DRG.DK15_group(record):
      return 'DK15'

    return 'DK1'
  else:
    return ''


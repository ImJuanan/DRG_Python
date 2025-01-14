from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCD_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["26.0x00x002","26.0x00x004","26.0x01","26.2100x001","26.2101","26.2901","26.2902","26.2903","26.2904","26.2905","26.2906","26.3000","26.3100x008","26.3100x009","26.3101","26.3102","26.3103","26.3104","26.3105","26.3201","26.3202","26.3203","26.4100x001","26.4200x001","26.4200x002","26.4900x001","26.4900x005","26.4900x006","26.4900x007","26.4900x008","26.4900x009","26.4900x010","26.4901","26.4902","26.4903","26.4904","26.4905","26.4906","26.9101","26.9900x001","26.9901","27.0x07"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DG1入组条件，匹配规则：某一手术匹配')
    
    if MDCD_DRG.DG11_group(record):
      return 'DG11'

    if MDCD_DRG.DG13_group(record):
      return 'DG13'

    if MDCD_DRG.DG15_group(record):
      return 'DG15'

    return 'DG1'
  else:
    return ''


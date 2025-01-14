from drg_group.yancheng_2022.Base import message,intersect,SS_VALID
from drg_group.yancheng_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["35.3100x001","36.3100x001","37.0x00x003","37.1000x004","37.1000x007","37.1000x008","37.1100x004","37.1100x006","37.1100x008","37.1100x009","37.1101","37.1102","37.1103","37.1104","37.1200x005","37.1200x008","37.1200x009","37.1200x010","37.1200x011","37.1201","37.1202","37.1203","37.1204","37.3100x006","37.3101","37.3102","37.3103","37.3104","37.3201","37.3202","37.3300x006","37.3300x008","37.3300x012","37.3300x013","37.3300x014","37.3300x015","37.3300x016","37.3300x018","37.3300x019","37.3300x022","37.3300x023","37.3300x024","37.3300x025","37.3300x027","37.3300x028","37.3301","37.3302","37.3303","37.3304","37.3305","37.3306","37.3307","37.3308","37.3500x005","37.3502","37.3600x001","37.3600x005","37.3600x006","37.3600x007","37.3600x008","37.3701","37.3702","37.3703","37.3704","37.4100","37.4900x001","37.4900x002","37.4900x005","37.4900x007","37.4900x014","37.4900x015","37.4900x016","37.4901","37.4902","37.4903","37.9000x001","37.9100"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FD2入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FD23_group(record):
      return 'FD23'

    if MDCF_DRG.FD25_group(record):
      return 'FD25'

    return 'FD2'
  else:
    return ''


from drg_group.yancheng_2022.Base import message,intersect,SS_VALID
from drg_group.yancheng_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.5500x008","38.9300x202","39.4900x011","39.4901","39.4902","39.5000x015","39.5000x027","39.5000x034","39.5000x035","39.5000x036","39.5000x037","39.5000x038","39.5000x039","39.5000x040","39.5000x041","39.5003","39.5010","39.7100x004","39.7101","39.7102","39.7103","39.7300x003","39.7301","39.7302","39.7303","39.7701","39.7800x001","39.7800x002","39.7800x006","39.7800x010","39.7900x011","39.7900x030","39.7900x031","39.7900x517","39.9000x022","39.9000x027","39.9000x037","39.9000x038","39.9002"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FM4入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FM43_group(record):
      return 'FM43'

    if MDCF_DRG.FM45_group(record):
      return 'FM45'

    return 'FM4'
  else:
    return ''


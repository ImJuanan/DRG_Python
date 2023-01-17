from drg_group.suzhou_2022.Base import message,intersect,SS_VALID
from drg_group.suzhou_2022.DRG import MDCM_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.8607","39.7900x022","39.7900x024","39.9800x001","39.9801","40.2400","40.2900x002","40.2900x017","40.2900x018","40.2908","40.3x00x001","40.3x00x002","40.5400x001","40.5400x002","40.5400x003","40.5909","40.5910","40.5912","54.0x00x002","54.0x00x004","54.0x00x006","54.0x00x010","54.0x00x013","54.0x00x018","54.0x00x021","54.0x00x022","54.0x00x023","54.0x00x024","54.0x00x025","54.0x01","54.0x02","54.0x03","54.1100","54.1101","54.1201","54.1202","54.1900x001","54.1900x005","54.1900x006","54.1900x010","54.1900x011","54.1900x020","54.1900x023","54.1901","54.1902","54.1903","54.1904","54.1905","54.1907","54.1909","54.2100","54.4x00x012","54.4x00x021","54.4x00x035","54.4x00x039","54.4x00x042","54.4x00x048","54.4x00x050","54.4x01","54.4x02","54.4x03","54.4x04","54.4x05","54.4x07","54.4x08","54.4x09","54.4x10","54.4x11","54.4x12","54.4x13","54.4x14","54.4x15","54.5100","54.5100x005","54.5100x009","54.5101","54.5102","54.5103","54.5900x007","54.5901","54.5902","54.5903","54.5904","54.5905","54.5906","54.6101","54.6301","54.6400","54.6401","54.7100","54.7200x001","54.7300x001","54.7400x001","54.7400x002","54.7400x003","54.7400x004","54.7400x005","54.7400x006","54.7404","54.7500x002","54.7501","54.9100x002","54.9100x009","54.9900x010","54.9900x011","54.9900x017","54.9901","54.9903","54.9904","57.7102","58.3102","60.1200","60.1400","60.1901","60.7100","60.7200","60.7200x002","60.7300","60.7300x003","60.7300x004","60.7301","60.7900x002","60.7900x003","60.7900x004","60.7901","60.8100x001","60.8101","60.9100","61.0x00x003","61.0x01","61.0x02","61.0x03","61.0x04","61.3x00x005","61.3x00x006","61.3x00x007","61.3x01","61.3x02","61.3x03","61.3x04","61.4900x002","61.4901","61.4902","61.4903","61.4904","61.4905","62.9100","63.0103","63.1x00x004","63.1x00x005","63.3x00x001","63.3x01","63.3x02","63.3x03","63.5100","63.5101","63.6x00x003","63.6x00x004","63.7000x001","63.7100","63.7101","63.7200","63.7300","63.7300x003","63.7301","63.8100","63.8101","63.8102","63.8200x001","63.8200x002","63.8300x001","63.8400","63.8500","63.8900","63.9100","63.9200x002","63.9500","63.9900x001","63.9900x002","63.9901","64.0x00","64.9900","86.0402","86.2200x011","86.2800x012","86.3x04","86.5903","98.1900x001","98.2402"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合MJ1入组条件，匹配规则：主手术匹配')
    
    if MDCM_DRG.MJ1A_group(record):
      return 'MJ1A'

    if MDCM_DRG.MJ15_group(record):
      return 'MJ15'

  return ''


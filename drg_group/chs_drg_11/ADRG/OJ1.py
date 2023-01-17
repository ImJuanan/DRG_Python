from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.DRG import MDCO_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.7x01","38.7x02","38.7x03","38.7x04","54.1202","54.4x10","54.6101","65.0100x002","65.0103","65.0105","65.0900x003","65.0900x003","65.0900x004","65.0903","65.0905","65.1200x001","65.1201","65.1300","65.2100","65.2200","65.2300","65.2400","65.2500x003","65.2500x005","65.2500x011","65.2501","65.2502","65.2503","65.2504","65.2505","65.5300","65.6100","65.6101","65.6300","65.6301","65.7100x001","65.7300x001","65.7400","65.7600","65.7900x008","65.7900x009","65.7901","65.7902","65.7903","65.7904","65.7905","65.8100","65.8101","65.8102","65.8900x001","65.8901","65.8902","65.9100","65.9101","65.9300","65.9500","65.9900x006","65.9901","65.9902","66.0100x003","66.0100x005","66.0100x006","66.0100x008","66.0101","66.0102","66.0103","66.0200","66.0201","66.0202","66.0203","66.1100","66.2101","66.2102","66.2200x001","66.2201","66.2900x001","66.2901","66.2902","66.2903","66.3100","66.4x00","66.4x01","66.4x02","66.5100","66.5101","66.5102","66.5200","66.6100x001","66.6100x002","66.6100x003","66.6100x006","66.6100x007","66.6100x008","66.6100x011","66.6100x012","66.6100x014","66.6101","66.6102","66.6103","66.6104","66.6200","66.6200x004","66.6201","66.6300","66.6301","66.6901","66.7100","66.7300","66.7301","66.7900x004","66.7901","66.7902","66.7903","66.7904","66.7905","66.8x00x007","66.8x01","66.8x02","66.9100x003","66.9101","66.9200x001","66.9201","66.9202","66.9203","66.9204","66.9500x001","66.9500x004","66.9501","66.9502","66.9600","66.9700","66.9900","67.1901","67.2x00","67.2x01","67.4x00x005","67.4x01","67.4x02","67.4x04","67.4x05","67.4x07","67.5100","67.5101","67.6100","67.6901","67.6902","68.0x00x004","68.0x00x005","68.0x00x006","68.0x00x007","68.1300","68.1400","68.1501","68.1601","68.2100x002","68.2101","68.2201","68.2202","68.2204","68.2206","68.2206","68.2300","68.2300x005","68.2301","68.2302","68.3100","68.3100x002","68.3101","68.3102","68.3103","68.3104","68.3106","68.4100","68.4101","68.4102","68.5100","68.5100x004","68.5101","68.5102","68.5103","68.5901","68.6100x001","68.6100x002","68.6101","68.6900x001","68.6900x001","68.6901","68.8x01","68.9x00","69.0100x002","69.0101","69.0200x003","69.0201","69.0202","69.1900x022","69.1901","69.1902","69.1903","69.1904","69.1905","69.1906","69.1907","69.1908","69.1909","69.2101","69.2200x006","69.2200x008","69.2200x013","69.2200x015","69.2200x017","69.2200x025","69.2200x030","69.2201","69.2202","69.2205","69.2208","69.2212","69.2300","69.2901","69.4100","69.4901","69.5101","69.5102","69.5103","69.5201","69.5202","69.5901","69.7x00","69.9202","69.9400","69.9500","69.9500x001","69.9600","69.9900","70.0x00x002","70.1100","70.1200x001","70.1201","70.2300","70.2901","70.3100","70.3300x003","70.3301","70.3302","70.3303","70.4x04","70.5001","70.5100","70.5101","70.5201","70.5202","70.6200x002","70.6400x001","70.7300","70.7400x001","70.7501","70.7600","70.7700x004","70.7800x002","70.7802","70.7900x005","70.7900x006","70.7901","70.7902","70.7903","70.7905","70.7906","70.7907","70.7908","70.7909","71.0100x002","71.0900x001","71.0900x004","71.0900x006","71.0901","71.0902","71.0903","71.0904","71.0905","71.2100x001","71.2300x001","71.4x01","71.6100","71.7202","71.7900x001","71.7900x008","71.7900x011","71.7900x013","71.7901","71.7902","71.7903","71.7904","72.1x00","72.9x00","73.0100","73.0900x001","73.1x00x001","73.1x00x002","73.1x01","73.1x02","73.4x00x004","73.4x00x008","73.4x01","73.4x02","73.4x03","74.3x00x012","75.1x00x002","75.2x00x001","75.3100","75.3101","75.3300x001","75.3300x002","75.3301","75.3302","75.3303","75.3600x002","75.3700","75.6101","75.6102","75.6201","75.6202","75.7x00","75.9900x001","75.9900x002","75.9900x004","75.9900x005","75.9901","75.9902","97.1600x002","97.2601"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合OJ1入组条件，匹配规则：主手术匹配')
    
    if MDCO_DRG.OJ19_group(record):
      return 'OJ19'

    return 'OJ1'
  else:
    return ''


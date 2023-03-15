from drg_group.changsha_2023.Base import message,intersect,SS_VALID
from drg_group.changsha_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["01.2600","01.2700","01.2800","21.0600","38.0100x001","38.0200x002","38.0200x003","38.0201","38.0202","38.1100","38.1200x003","38.1201","38.1202","38.3000","38.3000x001","38.3100","38.3100x001","38.3101","38.3200x002","38.3201","38.3202","38.4000","38.4100","38.4200x001","38.4200x002","38.4200x003","38.4201","38.4202","38.4203","38.6100x002","38.6101","38.6102","38.6200x002","38.6200x003","38.6200x005","38.6200x006","38.6200x007","38.6201","38.8000","38.8100x004","38.8101","38.8200x003","38.8200x007","38.8200x008","38.8201","39.0x02","39.2200x001","39.2200x002","39.2200x003","39.2200x004","39.2200x005","39.2200x006","39.2200x008","39.2200x009","39.2200x010","39.2200x011","39.2200x012","39.2200x014","39.2200x015","39.2200x016","39.2200x018","39.2200x019","39.2200x021","39.2203","39.2205","39.2206","39.2207","39.2208","39.2209","39.2211","39.2800x002","39.2800x003","39.2800x005","39.2800x008","39.2800x009","39.2800x010","39.2801","39.2802","39.2900x057","39.3100x005","39.3109","39.3204","39.5001","39.5100x004","39.5100x007","39.5101","39.5102","39.5103","39.5104","39.5105","39.5106","39.5107","39.5108","39.5200x002","39.5200x003","39.5200x007","39.5200x008","39.5202","39.5203","39.5300x013","39.5300x019","39.5300x020","39.5300x021","39.5302","39.5303","39.5304","39.5900x006","39.5900x013","39.7200x018","39.8901","39.9800x003"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合BE1入组条件，匹配规则：主手术匹配')
    
    if MDCB_DRG.BE13_group(record):
      return 'BE13'

    if MDCB_DRG.BE15_group(record):
      return 'BE15'

    return 'BE1'
  else:
    return ''


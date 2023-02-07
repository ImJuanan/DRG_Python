from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.DRG import MDCP_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.6700x005","40.2900x023","40.2905","40.2907","40.2909","40.3x00x001","42.9200x008","43.0x00x003","43.0x02","43.0x03","43.1900x003","43.1900x005","43.3x00x003","43.3x00x004","43.3x01","43.5x00x003","43.5x00x007","43.5x01","43.5x02","43.5x03","43.6x00x005","43.6x00x006","43.6x01","43.6x02","43.7x00x001","43.7x01","43.7x02","43.7x03","43.8100","43.8201","43.8202","43.8901","43.8902","43.8903","43.9101","43.9102","43.9900x002","43.9900x003","43.9900x004","43.9901","43.9902","43.9903","43.9904","43.9905","44.0100","44.0200x002","44.0300x001","44.1500","44.2100x001","44.2100x002","44.2200x001","44.2200x001","44.2200x003","44.2200x004","44.2900x001","44.2901","44.3801","44.3802","44.3803","44.3804","44.3900x003","44.3901","44.3902","44.3903","44.3904","44.4100x008","44.4102","44.4901","44.4902","44.5x00x002","44.5x00x004","44.5x00x005","44.5x01","44.5x02","44.6200","44.6300x001","44.6301","44.6302","44.6400","44.6401","44.6500","44.6500x001","44.6500x002","44.6501","44.6600x002","44.6601","44.6701","44.6800x002","44.6801","44.6902","44.9100x001","44.9100x002","44.9100x005","44.9101","44.9201","44.9501","44.9502","44.9601","44.9602","44.9701","44.9801","44.9802","45.0100x005","45.0101","45.0102","45.0200x001","45.0201","45.0202","45.0203","45.0204","45.0300x002","45.0300x003","45.0301","45.0302","45.0303","45.1500","45.2600","45.3101","45.3102","45.3200x001","45.3300x006","45.3301","45.3303","45.4100x001","45.4101","45.4102","45.4103","45.4104","45.4105","45.4107","45.4108","45.4900x001","45.4900x003","45.4900x005","45.4901","45.5100x001","45.5101","45.5201","45.6200x001","45.6200x002","45.6201","45.6202","45.6203","45.6204","45.6205","45.6206","45.6207","45.6208","45.6300","45.7200x002","45.7200x004","45.7201","45.7202","45.7300x003","45.7300x006","45.7300x007","45.7301","45.7302","45.7304","45.7400x003","45.7401","45.7500","45.7500","45.7500x001","45.7501","45.7600x008","45.7601","45.7901","45.8100","45.8100x001","45.8200","45.9100x006","45.9100x008","45.9101","45.9102","45.9103","45.9104","45.9200","45.9300x012","45.9300x013","45.9300x014","45.9300x015","45.9302","45.9304","45.9305","45.9307","45.9310","45.9400x004","45.9400x009","45.9400x012","45.9400x016","45.9401","45.9402","45.9403","45.9404","45.9405","45.9406","45.9407","45.9408","45.9501","45.9502","45.9503","45.9504","46.0100x001","46.0101","46.0102","46.0300x001","46.0300x003","46.0300x004","46.0301","46.0302","46.0400x002","46.0401","46.0402","46.1000","46.1000x007","46.1100","46.1100x002","46.1300","46.1301","46.1400","46.2100","46.2300x001","46.2301","46.2400","46.3900x002","46.3900x006","46.3900x007","46.3901","46.3902","46.3904","46.3905","46.4101","46.4102","46.4103","46.4200","46.4201","46.4202","46.4300x004","46.4300x005","46.4301","46.4302","46.4303","46.5100x002","46.5100x004","46.5100x006","46.5101","46.5102","46.5200x006","46.5200x010","46.5200x011","46.5201","46.5202","46.5203","46.5204","46.6200x003","46.6200x004","46.6201","46.6301","46.6302","46.6401","46.6402","46.6403","46.7100","46.7200","46.7300x005","46.7301","46.7302","46.7303","46.7400x004","46.7401","46.7402","46.7403","46.7404","46.7405","46.7500x004","46.7501","46.7502","46.7503","46.7504","46.7505","46.7506","46.7601","46.7602","46.7603","46.7604","46.7900x009","46.7902","46.7903","46.7904","46.8101","46.8102","46.8201","46.8202","46.9100","46.9200x001","46.9201","46.9300x001","46.9301","46.9401","47.0100","47.0901","47.0902","47.0903","47.1100","47.2x00","47.2x01","47.9100","47.9200","47.9901","48.0x00x002","48.0x00x003","48.0x01","48.0x02","48.0x03","48.0x04","48.1x00","48.2500","48.3101","48.3200x003","48.3201","48.3301","48.3501","48.3502","48.3504","48.3505","48.3506","48.3507","48.3600x007","48.3601","48.3603","48.4101","48.4102","48.4103","48.4104","48.4105","48.4106","48.4900x002","48.4900x003","48.4901","48.4902","48.4903","48.4904","48.4905","48.5100","48.5100x002","48.5200","48.5201","48.5900x001","48.6100","48.6100x001","48.6100x002","48.6200","48.6201","48.6301","48.6302","48.6303","48.6400x001","48.6500x001","48.6900x002","48.6900x004","48.6900x007","48.6901","48.6902","48.6903","48.6904","48.6905","48.6906","48.6907","48.6908","48.6909","48.6910","48.6911","48.6912","48.6913","48.7100","48.7101","48.7200","48.7300x001","48.7301","48.7302","48.7303","48.7400","48.7401","48.7501","48.7600x001","48.7600x002","48.7600x008","48.7601","48.7602","48.7603","48.7604","48.7605","48.7900x003","48.7901","48.8100x001","48.8101","48.8102","48.8201","48.8202","48.8203","48.8204","48.8205","48.8206","48.9100","48.9200","48.9201","48.9300","49.0100x004","49.0101","49.0200x001","49.0201","49.0300","49.0400x008","49.0400x009","49.0401","49.0402","49.1100","49.1200","49.3900x015","49.3901","49.3902","49.3903","49.3904","49.3905","49.3906","49.3907","49.4902","49.5200x002","49.5900x001","49.5901","49.5902","49.5903","49.6x00","49.6x01","49.7100","49.7200","49.7302","49.7400x001","49.7501","49.7502","49.7600","49.7900x005","49.7901","49.7902","49.7903","49.7904","49.9300x001","49.9300x002","49.9300x003","49.9300x004","49.9302","49.9400","49.9500x002","49.9900x007","49.9901","50.0x00x004","50.0x00x008","50.0x00x016","50.0x01","50.0x02","50.0x03","50.0x04","50.0x05","50.1200","50.1400","50.2200x003","50.2200x004","50.2200x005","50.2200x006","50.2200x007","50.2200x008","50.2200x009","50.2205","50.2301","50.2302","50.2303","50.2501","50.2502","50.2503","50.2900x021","50.2901","50.2902","50.2903","50.2904","50.2905","50.2906","50.2907","50.2908","50.2909","50.2910","50.3x01","50.3x02","50.3x03","50.3x04","50.3x05","50.3x06","50.4x00","50.6101","50.6900x002","50.9900x003","51.0300x002","51.0301","51.0400x004","51.0400x006","51.0400x008","51.0402","51.0405","51.1104","51.1105","51.1301","51.1302","51.2200","51.2200x004","51.2201","51.2300","51.2301","51.2400","51.3100","51.3201","51.3202","51.3203","51.3204","51.3400","51.3601","51.3602","51.3700x001","51.3700x002","51.3700x003","51.3700x007","51.3701","51.3702","51.3703","51.3704","51.3900x005","51.3900x008","51.3901","51.3902","51.3904","51.3905","51.3906","51.4100x001","51.4201","51.4202","51.4301","51.4302","51.4303","51.4304","51.4900x002","51.4900x003","51.4901","51.4902","51.4903","51.4904","51.4905","51.5100","51.5101","51.5102","51.5900x005","51.5900x006","51.5900x008","51.5901","51.5902","51.5903","51.5904","51.6100x001","51.6200x002","51.6201","51.6301","51.6302","51.6303","51.6900x007","51.6900x008","51.6900x012","51.6900x013","51.6901","51.6902","51.6903","51.6904","51.6905","51.7101","51.7200x001","51.7201","51.7202","51.7203","51.7204","51.7900x002","51.7900x005","51.7900x006","51.7900x007","51.7901","51.7902","51.7903","51.7904","51.7905","51.7906","51.7907","51.7908","51.7909","51.7910","51.8100","51.8101","51.8200x001","51.8200x002","51.8200x003","51.8201","51.8300x003","51.8301","51.8800x006","51.8803","51.9100","51.9101","51.9200","51.9300x001","51.9301","51.9302","51.9303","51.9304","51.9305","51.9401","51.9800x010","51.9901","52.0100","52.0101","52.0102","52.0900x001","52.0901","52.0902","52.0903","52.0904","52.1200","52.1302","52.2101","52.2102","52.2201","52.3x00","52.4x00x004","52.4x02","52.5101","52.5102","52.5103","52.5104","52.5202","52.5203","52.5300","52.5301","52.5901","52.5902","52.5903","52.5904","52.5905","52.5906","52.6x00","52.6x00x003","52.6x01","52.6x02","52.6x03","52.7x00","52.7x00x003","52.7x01","52.8100","52.9201","52.9500x001","52.9500x002","52.9501","52.9502","52.9503","52.9504","52.9601","52.9602","52.9603","52.9604","52.9605","53.0001","53.0002","53.0100x001","53.0101","53.0102","53.0201","53.0202","53.0203","53.0204","53.0301","53.0302","53.0401","53.0501","53.1000","53.1101","53.1201","53.1202","53.1203","53.1301","53.1401","53.1501","53.1601","53.1701","53.2101","53.2901","53.3101","53.3901","53.4101","53.4201","53.4301","53.4901","53.4902","53.5100","53.5101","53.5900x001","53.5901","53.5902","53.6101","53.6900x002","53.6901","53.9x00x015","53.9x00x016","53.9x01","53.9x02","53.9x03","53.9x04","53.9x06","54.0x00x002","54.0x00x004","54.0x00x006","54.0x00x010","54.0x00x013","54.0x00x018","54.0x00x021","54.0x00x022","54.0x00x023","54.0x00x024","54.0x00x025","54.0x01","54.0x02","54.0x03","54.0x04","54.0x05","54.0x06","54.0x07","54.0x08","54.1100","54.1202","54.1900x005","54.1900x006","54.1900x010","54.1900x011","54.1900x023","54.1901","54.1902","54.1903","54.1904","54.1905","54.1906","54.1907","54.1909","54.2100","54.2200x003","54.2300x003","54.2301","54.2302","54.2303","54.3x00x004","54.3x00x010","54.3x00x011","54.3x00x027","54.3x01","54.3x02","54.3x03","54.3x05","54.3x06","54.3x07","54.4x00x005","54.4x00x006","54.4x00x007","54.4x00x012","54.4x00x021","54.4x00x035","54.4x00x039","54.4x00x042","54.4x00x048","54.4x00x050","54.4x01","54.4x03","54.4x04","54.4x05","54.4x08","54.4x09","54.4x10","54.4x11","54.4x12","54.4x13","54.4x14","54.4x15","54.4x16","54.5100","54.5100x005","54.5100x009","54.5101","54.5103","54.5900x007","54.5901","54.5902","54.5904","54.5906","54.6101","54.6301","54.6401","54.7200x001","54.7300x001","54.7301","54.7302","54.7400x001","54.7400x002","54.7400x003","54.7400x004","54.7400x005","54.7400x006","54.7401","54.7402","54.7403","54.7404","54.7405","54.7500x002","54.7501","54.7502","54.9201","54.9202","54.9300x001","54.9300x003","54.9300x004","54.9300x005","54.9300x006","54.9300x009","54.9400x002","54.9401","54.9402","54.9500x004","54.9502","54.9900x010","54.9900x011","54.9900x017","54.9904","55.5101","57.8600","70.5200","70.5202","70.7200","70.7400x001","70.7401"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ageDay!=None and record.ageDay<=28:
    message('符合PC1入组条件，匹配规则：主手术匹配、新生儿')
    
    if MDCP_DRG.PC11_group(record):
      return 'PC11'

    if MDCP_DRG.PC13_group(record):
      return 'PC13'

    if MDCP_DRG.PC15_group(record):
      return 'PC15'

    return 'PC1'
  else:
    return ''


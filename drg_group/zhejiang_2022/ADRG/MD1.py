from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCM_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["61.0x01","61.2x01","61.2x02","61.4101","61.4102","61.4201","61.4900x002","61.4901","61.4904","61.4905","61.9101","61.9200x001","61.9900","62.0x00x001","62.0x01","62.0x02","62.0x03","62.2x00x002","62.2x01","62.3x00","62.3x01","62.3x02","62.3x03","62.3x04","62.4100x004","62.4101","62.4104","62.4105","62.4200","62.5x00","62.5x01","62.5x02","62.6100","62.6900x001","62.6901","62.7x00","62.9900x001","63.1x00x003","63.1x01","63.1x02","63.1x03","63.2x00","63.2x01","63.3x01","63.3x03","63.4x00","63.5200x001","63.5201","63.5202","63.5203","63.5300","63.5900","63.6x00x001","63.6x01","63.8102","63.8300","63.8900","63.9200x001","63.9300","63.9400","63.9901","69.1906"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合MD1入组条件，匹配规则：某一手术匹配')
    
    if MDCM_DRG.MD10_group(record):
      return 'MD10'

    if MDCM_DRG.MD11_group(record):
      return 'MD11'

    if MDCM_DRG.MD13_group(record):
      return 'MD13'

    if MDCM_DRG.MD15_group(record):
      return 'MD15'

    return 'MD1'
  else:
    return ''


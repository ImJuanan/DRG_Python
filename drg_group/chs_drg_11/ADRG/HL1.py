from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.9900x501","38.9900x901","39.7900x033","39.7903","42.3200x003","42.3300x006","42.3307","42.3308","42.3309","42.3310","42.9200x006","44.4400x001","45.3001","50.2400x003","50.2401","50.2402","50.2403","50.2404","50.9101","50.9102","50.9103","50.9300","50.9400x005","50.9401","50.9402","51.0101","51.0102","51.0103","51.6400x002","51.6400x003","51.8400x001","51.8401","51.8402","51.8403","51.8404","51.8500x002","51.8501","51.8502","51.8503","51.8600x002","51.8700x001","51.8700x003","51.8700x004","51.8700x005","51.8702","51.9501","51.9600x001","51.9601","51.9800x001","51.9800x005","51.9800x008","51.9800x009","51.9800x010","51.9800x012","51.9800x013","51.9800x015","51.9800x016","51.9801","51.9803","51.9804","51.9805","51.9806","51.9807","51.9808","52.2200x001","52.4x00x011","52.4x00x012","52.9200x001","52.9201","52.9300","52.9300x002","52.9301","52.9400","52.9400x002","52.9700","52.9800x001","97.0502","97.5501","97.5506","97.5601","98.5201","98.5202","98.5900x003"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合HL1入组条件，匹配规则：主手术匹配')
    
    if MDCH_DRG.HL11_group(record):
      return 'HL11'

    if MDCH_DRG.HL15_group(record):
      return 'HL15'

    return 'HL1'
  else:
    return ''


from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.DRG import MDCC_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["08.0100","08.0200","08.0901","08.0902","08.0903","08.0904","08.2000x003","08.2000x005","08.2000x006","08.2000x009","08.2000x010","08.2001","08.2002","08.2003","08.2100","08.2100x001","08.2100x004","08.2200x003","08.2201","08.2300x001","08.2400x001","08.2500","08.3101","08.3102","08.3200x001","08.3200x002","08.3200x003","08.3201","08.3202","08.3300x001","08.3400x001","08.3500","08.3600x002","08.3700","08.3800","08.4101","08.4102","08.4201","08.4202","08.4203","08.4204","08.4301","08.4302","08.4401","08.4402","08.4403","08.4901","08.4902","08.5100","08.5101","08.5200x002","08.5200x003","08.5200x004","08.5900x001","08.5900x004","08.5900x005","08.5900x006","08.5900x007","08.5901","08.5902","08.5903","08.5904","08.6100x002","08.6100x003","08.6100x004","08.6100x005","08.6101","08.6102","08.6103","08.6201","08.6300x005","08.6300x006","08.6301","08.6400","08.6900","08.7001","08.7100x001","08.7200x001","08.7300x001","08.7400x001","08.8101","08.8102","08.8200x001","08.8300x001","08.8400x001","08.8500x001","08.8600x002","08.8700","08.8900x002","08.8900x005","08.8900x006","08.8900x007","08.8900x008","08.8901","08.8902","08.8903","08.9100x001","08.9100x002","08.9200","08.9300x001","08.9900x003","08.9901","09.0x00x001","09.4100","09.4100x001","09.4200","09.4300","09.4401","09.4402","09.4403","09.4404","09.4405","09.4900x002","09.4900x003","09.4901","09.5100","09.5200","09.5300","09.5900x001","09.6x00x001","09.6x00x006","09.6x01","09.6x02","09.6x03","09.6x04","09.7100","09.7200x001","09.7201","09.7300x001","09.7300x003","09.7300x004","09.7301","09.8100x004","09.8101","09.8200","09.8301","09.9100","09.9900x002","15.1100","15.1200","15.1300","15.1900x001","15.2100","15.2200","15.2901","15.3x01","15.3x02","15.4x01","15.4x02","15.5x00","15.6x00","15.7x01","15.9x00x001","15.9x00x007","15.9x00x008","15.9x00x009","15.9x00x010","15.9x01","38.6000x012","86.2200x011","86.2201","86.2800x012","86.4x01","98.2200x004","98.2202"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合CD1入组条件，匹配规则：主手术匹配')
    
    if MDCC_DRG.CD19_group(record):
      return 'CD19'

    return 'CD1'
  else:
    return ''


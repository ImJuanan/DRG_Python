from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["21.0400","21.0500","21.0501","21.0600","21.0903","38.0000","38.0200x002","38.0201","38.0300x003","38.0300x005","38.0302","38.0501","38.0503","38.0600x001","38.0601","38.0602","38.0800x002","38.0800x003","38.0801","38.0802","38.1000x002","38.1200x003","38.1201","38.1202","38.1300","38.1600x002","38.1600x005","38.1601","38.1602","38.1603","38.1800x001","38.1800x002","38.1800x003","38.1800x004","38.1800x005","38.1800x006","38.1800x007","38.1801","38.1802","38.1803","38.1804","38.3000","38.3000x001","38.3200x002","38.3201","38.3202","38.3300","38.3301","38.3500x002","38.3600","38.3800","38.4508","38.4509","38.6000x011","38.6000x012","38.6000x013","38.6200x005","38.6200x006","38.6201","38.6300x001","38.6301","38.6302","38.6500x001","38.6600x002","38.6601","38.6602","38.6800x002","38.6801","38.6802","38.8000","38.8200x003","38.8200x007","38.8200x008","38.8201","38.8203","38.8300x004","38.8301","38.8302","38.8303","38.8500x010","38.8500x017","38.8503","38.8504","38.8600x004","38.8600x005","38.8601","38.8602","38.8603","38.8604","38.8605","38.8606","38.8607","38.8608","38.8609","38.8800x002","38.8801","38.9100x601","38.9100x602","39.3100x002","39.3100x004","39.3100x005","39.3100x006","39.3100x007","39.3100x009","39.3100x010","39.3101","39.3102","39.3103","39.3104","39.3105","39.3106","39.3108","39.3109","39.3110","39.3111","39.3112","39.3113","39.4100x001","39.4100x002","39.4301","39.4900x001","39.4900x004","39.4900x005","39.4900x006","39.4900x008","39.4903","39.5001","39.5014","39.5101","39.5200x002","39.5200x003","39.5201","39.5202","39.5203","39.5300x005","39.5300x007","39.5300x008","39.5300x009","39.5300x010","39.5300x011","39.5300x013","39.5300x015","39.5300x016","39.5300x017","39.5300x018","39.5302","39.5303","39.5304","39.5500","39.5601","39.5702","39.5800","39.5900x001","39.5900x004","39.5900x006","39.5900x008","39.5900x010","39.5900x011","39.5900x013","39.5900x022","39.5900x024","39.5900x025","39.8101","39.8102","39.8201","39.8202","39.8301","39.8302","39.8400","39.8500","39.8600","39.8700","39.8800","39.8900x001","39.8901","39.9300","39.9401","39.9500x006","39.9800x003","39.9900","99.6400"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FF2入组条件，匹配规则：某一手术匹配')
    
    if MDCF_DRG.FF21_group(record):
      return 'FF21'

    if MDCF_DRG.FF23_group(record):
      return 'FF23'

    if MDCF_DRG.FF25_group(record):
      return 'FF25'

    return 'FF2'
  else:
    return ''

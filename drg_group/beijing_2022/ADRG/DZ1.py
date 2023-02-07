from drg_group.beijing_2022.Base import message,intersect,SS_VALID
from drg_group.beijing_2022.DRG import MDCD_DRG

def group(record):
  adrg_zd=["A18.200x002","A18.200x005","A18.201","A18.205","A18.400x018","A18.400x019","A36.000","A36.000x002","A36.000x004","A36.100","A52.700x003+J99.8*","A52.700x004+J99.8*","A66.501+J99.8*","B02.800","B02.801+H62.1*","B36.902+H62.2*","B36.903+H62.2*","B37.200x005+H62.2*","B44.200x001+J99.8*","B44.800x001","B44.800x004+H62.2*","B44.800x006","B44.800x007","B44.804","B48.100","B49.x05","B49.x06","B49.x07","B49.x08","B49.x09","B49.x10","D37.002","D37.004","D37.006","D37.008","D37.010","D37.012","D37.014","D37.016","D37.018","D38.002","D38.501","D38.503","D38.505","D38.507","D48.518","D48.519","D48.701","D86.802","E85.410","G47.300","G47.300x001","G47.300x031","G47.300x033","G47.300x035","G47.300x036","G47.300x037","G47.301","G47.302","G47.303","G47.304","H60.000","H60.000x002","H60.000x004","H60.000x005","H60.001","H60.002","H60.100","H60.100x001","H60.100x002","H60.200","H60.300","H60.300x002","H60.300x003","H60.300x005","H60.300x006","H60.301","H60.302","H60.303","H60.400","H60.400x004","H60.401","H60.500x006","H60.500x007","H60.501","H60.502","H60.503","H60.801","H60.900","H60.901","H61.000","H61.001","H61.103","H61.105","H61.200","H61.805","H68.100","H68.100x003","H68.101","H69.000","H69.800","H69.900","H74.201","H74.300","H74.300x003","H74.300x004","H74.400","H74.900","H80.000x001","H80.000x002","H80.100x001","H80.100x002","H80.200","H80.800x001","H80.900","H92.000","H92.100","H92.100x001","H92.200","H93.300","H93.301","H93.800x001","H95.000x001","H95.101","H95.102","H95.800","H95.900","H95.900x001","H95.900x002","I77.001","I77.003","I86.000","I88.101","I88.102","I88.103","I88.104","I88.900x004","I88.900x007","I89.000x014","J04.200","J06.000x002","J06.800x001","J30.200","J32.006","J33.100","J34.000x004","J34.001","J34.002","J34.003","J34.004","J34.005","J34.006","J34.007","J34.008","J34.300","J34.800x001","J34.800x002","J34.800x004","J34.800x006","J34.800x019","J34.800x020","J34.801","J34.803","J34.804","J34.806","J34.807","J34.809","J34.812","J34.813","J35.801","J35.804","J35.806","J35.808","J38.000x001","J38.000x002","J38.000x005","J38.000x006","J38.000x011","J38.000x012","J38.000x021","J38.000x022","J38.000x031","J38.000x032","J38.001","J38.002","J38.300x008","J38.300x016","J38.300x018","J38.301","J38.302","J38.303","J38.304","J38.307","J38.309","J38.400","J38.400x002","J38.400x003","J38.400x004","J38.401","J38.402","J38.500","J38.600","J38.601","J38.700x003","J38.700x013","J38.700x017","J38.719","J38.720","J39.200x008","J39.200x009","J39.200x015","J39.201","J39.202","J39.205","J39.208","J39.209","J39.210","J39.212","J39.214","J39.215","J39.218","J39.221","J39.222","J39.223","J39.224","J39.300","J39.900","J95.000","J95.000x001","J95.000x002","J95.000x007","J95.001","J95.002","J95.003","J95.004","J95.005","J95.400","J95.500","J95.501","J95.800x001","J95.800x013","J95.803","J95.805","J95.806","J95.807","J95.809","K10.000","K10.002","K10.202","K10.203","K10.207","K10.209","K10.210","K11.000","K11.200","K11.200x009","K11.200x011","K11.200x012","K11.200x014","K11.201","K11.202","K11.203","K11.204","K11.205","K11.206","K11.209","K11.210","K11.211","K11.300","K11.301","K11.302","K11.303","K11.400","K11.400x003","K11.401","K11.402","K11.404","K11.500x003","K11.500x005","K11.501","K11.503","K11.700x001","K11.700x002","K11.700x003","K11.701","K11.800x002","K11.800x006","K11.800x007","K11.800x010","K11.801","K11.802","K11.803","K11.805","K11.806","K11.807","K11.900x004","L02.000","L04.001","L04.002","M35.900x011","Q16.000","Q16.101","Q16.102","Q16.103","Q16.200","Q16.300","Q16.301","Q16.400","Q16.401","Q16.500","Q16.501","Q16.900","Q16.901","Q17.000","Q17.000x003","Q17.000x005","Q17.001","Q17.002","Q17.003","Q17.100","Q17.200","Q17.300x002","Q17.300x004","Q17.300x005","Q17.300x006","Q17.301","Q17.302","Q17.303","Q17.400","Q17.400x002","Q17.500","Q17.501","Q17.800x004","Q17.801","Q17.802","Q17.803","Q17.900","Q18.001","Q18.002","Q18.003","Q18.100x003","Q18.100x006","Q18.100x008","Q18.100x009","Q18.101","Q18.102","Q18.103","Q18.104","Q18.200","Q18.200x003","Q18.200x004","Q18.300","Q18.400x004","Q18.800x001","Q18.800x002","Q18.800x003","Q18.800x004","Q18.801","Q18.802","Q18.804","Q18.805","Q18.806","Q18.807","Q18.900x002","Q18.903","Q27.300x007","Q27.300x010","Q27.302","Q27.800x021","Q27.800x024","Q27.800x026","Q27.800x027","Q27.800x028","Q27.800x030","Q27.800x036","Q27.800x040","Q27.802","Q30.000","Q30.001","Q30.100x001","Q30.101","Q30.200x001","Q30.201","Q30.300","Q30.800x003","Q30.800x004","Q30.800x005","Q30.800x006","Q30.800x007","Q30.801","Q30.802","Q30.804","Q30.805","Q30.900","Q31.000","Q31.100","Q31.200","Q31.301","Q31.500","Q31.800x003","Q31.800x004","Q31.800x005","Q31.801","Q31.802","Q31.803","Q31.804","Q31.805","Q31.806","Q31.900","Q32.000","Q32.100","Q32.101","Q34.801","Q35.900","Q35.903","Q36.902","Q37.000","Q37.100","Q37.400","Q37.500","Q37.800","Q38.001","Q38.304","Q38.600x004","Q38.700","Q38.701","Q38.801","Q38.802","Q67.200","Q67.300","Q67.400x202","Q67.400x906","Q67.401","Q67.402","Q67.403","Q67.404","Q67.405","Q67.406","Q67.407","Q75.200x001","Q75.400","Q75.801","Q75.804","Q75.805","Q75.900x005","Q85.900x012","Q85.900x031","Q85.900x035","Q85.900x037","Q85.900x038","Q87.000x301","Q89.202","Q89.800x904","Q89.800x906","Q89.800x908","Q89.800x909","R04.000","R04.100","R04.801","R06.501","R06.700","R07.000","R43.800x002","R44.201","R49.000","R49.001","R49.100","R49.201","R49.202","R59.000x004","T16.x00","T16.x00x001","T16.x00x002","T17.101","T17.200","T17.200x001","T17.300","T27.000x002","T27.000x003","T27.100x001","T27.401","T27.402","T27.500x001","T28.000x002","T28.000x003","T28.501","T28.502","T81.804","T85.606","T85.607","T85.800x804","T85.800x810","T85.800x811","T86.802","T90.800","Z41.102","Z41.103","Z42.000x002","Z42.000x015","Z42.000x019","Z42.002","Z42.005","Z42.006","Z42.007","Z42.008","Z42.009","Z42.010","Z43.000","Z43.000x002","Z43.001","Z45.301","Z45.302","Z45.303","Z45.304","Z45.801","Z46.100","Z46.300x001","Z46.400"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合DZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCD_DRG.DZ19_group(record):
      return 'DZ19'

    return 'DZ1'
  else:
    return ''


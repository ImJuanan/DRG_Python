from drg_group.beijing_2022.Base import message,intersect,SS_VALID
from drg_group.beijing_2022.ADRG import TB1,TR1,TR2,TS1,TS2,TT1,TT2,TU1,TV1,TW1

def group(record):
  mdc_zd=["F51.400","F04.x00x001","F07.900","F90.000","F23.900","F44.902","F23.901","F79.900","F42.900","F79.800","F25.200","F06.300x021","F44.903","F40.200x002","F44.301","F44.406","F60.000","F70.900","F72.000x001","F91.100","F23.100","F43.900","F44.401","F05.000x001","F07.800x003","F06.800x006","F91.000","F06.100","F32.801","F64.000x002","F06.800x018","F06.800x016","F44.804","F84.900x001","F43.200x031","F54.x00","F23.200x003","F84.000","F06.800x050","F45.300x022","F44.300","F95.900","R45.300x002","F44.000","F23.301","F30.200","F62.100","F59.x00","R48.000x002","F41.201","F06.800x015","F42.200","F65.500x001","F07.100","F64.800","F50.401","F44.404","F06.000","F84.500","F30.000","F28.x01","F45.900","F60.301","F32.100x011","F50.502","F31.301","F44.405","F32.800x002","F44.600","F65.800","F68.100x001","F71.000","R45.200x001","F51.200","F31.802","F48.000","F60.900","F38.001","F45.305","R48.801","F32.000x002","F34.800","F81.000","F98.800x001","F44.407","F45.801","F44.805","F94.900","F33.400","F44.800x002","F20.803","F44.800x011","F84.301","F22.000","F28.x00x002","F45.806","F45.308","F98.803","F06.800x044","F20.000","F06.802","F42.800x001","F50.300","F64.100","G47.000","F65.100","F42.001","F80.203","F43.200x041","F72.800","R45.600","F43.100","F34.102","F45.400","F31.700","F44.500","R41.801","F95.101","F33.000x002","F92.900","F53.800","F33.100","F06.800x046","F79.901","F23.300x003","F81.900","F44.800x021","F59.x00x001","F06.800x045","F64.200","F63.800","F06.800x043","F93.000","F06.800x013","F32.902","F23.200x011","F06.800x025","F20.200","F23.002","R45.200","F06.811","F81.201","F44.200","F06.700","R45.400x002","F65.500x002","R68.803","F60.800x002","R48.800x005","F98.100","F06.800x009","F64.000x001","R46.200x002","F99.x00","R44.000","F24.x00","F06.800x020","F44.900","F51.000","F91.900","F42.800","F48.801","F88.x00","F04.x00x901","F79.000","F60.800x001","F91.800","F45.200","F80.100","F41.200x002","F33.800","F60.100","F44.901","F63.000","F06.300x010","F52.001","R44.300","F79.100","F50.900","F06.800x037","F73.900","F32.900","F50.200","F84.900","F06.200","F28.x02","F52.200x002","F69.x00","R45.500","F33.000","F44.400","F98.001","R46.400","F45.807","F84.400","F44.601","F72.100","F94.000","F32.100x002","F44.801","F62.000","F06.809","F50.100","F25.100x001","G47.000x002","F43.801","F31.300x012","F98.300","F40.900","F65.300","Q93.900","F81.800","F31.000","F60.201","F52.100x011","F32.000x011","F06.800x039","F32.300","F20.800x001","F34.100","F70.000x001","F90.100","F71.900","G47.800x001","F41.102","F41.900","F45.803","F41.800","F80.900","F31.100","R45.700x001","F50.800x002","F60.801","F30.800x002","F92.800","R45.200x003","F06.800x017","F42.003","F06.301","R45.801","F95.800","F41.200","F84.800","F66.800","F05.802","F09.x02","F43.002","F06.800x012","F20.200x002","F63.200","F71.000x001","F48.001","F30.201","F48.100","F06.800x032","G47.100","F66.900","F20.801","F52.700","F06.805","F93.800","F40.000","F80.202","F23.001","F20.800x002","F25.200x001","F34.001","F23.300x002","F05.900","F06.500","G47.801","F05.801","F90.900","F43.804","F20.800x003","F38.100x002","F33.100x002","F61.x00","F42.901","F25.800","F07.900x001","R48.800x001","F06.800x011","F38.000x001","F06.808","F33.900","F45.805","F07.901","F70.800","F06.800x021","F29.x00","F06.810","F20.802","F06.302","F31.801","F20.100","Q91.300","F43.200x081","F80.205","F51.300","F20.600","F98.200","F81.300","F06.803","F65.400","F51.900","F95.201","F52.201","R48.800x004","F89.x00","F53.002","F63.900","R48.001","F20.500","F45.000","F32.802","F06.800","F45.302","F06.801","F70.000","F34.000","F23.800","F63.801","F84.000x001","R48.200","F94.200","F53.100x001","F06.800x041","F05.101","F80.204","F44.802","F44.600x002","F42.100","F31.902","F91.100x002","F09.x00x004","F78.000","F06.300","F06.804","F51.200x003","F45.303","F95.801","F60.302","F31.400","F09.x00x003","F45.401","F40.800","F78.100","F80.300","F45.802","F33.100x011","F20.301","F98.802","F60.200","F60.400","F42.101","F73.000x001","F06.300x020","F25.000x001","F28.x00x011","F50.000","F45.301","F05.001","F31.803","F79.000x001","F60.700","F88.x01","F80.201","F30.200x002","F66.200","Q93.400","F98.801","F06.800x005","F20.300","F50.501","F50.801","F06.800x049","F07.800x002","F63.800x001","F52.500","F45.304","F38.100x001","F06.800x002","F53.001","F51.800","F31.300x002","F45.300x051","F06.800x040","F60.600","F09.x03","F84.100","F98.500","F34.900","F31.300x011","F44.402","F22.002","F06.800x010","F94.800","F06.807","F32.301","F65.000","F68.000","F42.000","F66.000","F66.100","F92.000","F41.101","F45.402","F98.000","F06.800x008","F80.800","F43.803","F98.101","F93.100","F06.800x042","F52.400","F98.900","F43.000","F07.200","F65.500","F84.200","F91.200","F06.800x004","F41.001","F31.500","F98.600","F62.900","F31.800x002","F06.900","F45.310","F93.900","F06.300x002","F45.202","F05.901","F06.800x047","F06.400","F65.600","F72.000","F20.400","F60.802","F28.x00x012","F06.400x003","F52.200","F40.200x004","F98.800","F95.100","F95.200","F23.000","F30.901","F09.x01","F06.800x003","F32.800x001","F31.901","F45.307","G47.900","F45.100","F98.400","F43.200","F20.201","F40.200x001","F31.300x003","F22.003","F30.100x001","R45.800x091","F39.x00","F45.800x002","F22.800x001","F06.800x038","F84.002","F06.806","F48.901","F45.300x041","F22.800","R45.700x002","F06.300x030","R45.300x001","F45.403","F05.902","R48.100","F30.200x001","F45.201","F90.800","Q90.900","F31.300x005","F64.900","R45.100x001","F44.603","F80.000","F65.900","F52.600","F06.800x007","F78.800","F32.901","F06.800x014","F83.x00","F33.200","F34.002","F60.800x003","F70.100","R48.800x002","F48.900","F23.300x001","F20.900","F23.903","F51.100","F71.100","F41.100","F52.800","F91.300","F06.800x026","F07.000","F44.100","F44.501","F53.900","F07.001","F65.200","F06.800x034","F53.101","F45.901","F62.800","Q93.500x001","F60.500","Q93.500","F82.x00","F20.501","F25.100","F43.200x051","F25.200x002","F41.000","F06.800x019","F06.800x027","F33.300","F22.900","F34.101","F68.800","F06.800x048","F06.800x023","F52.202","F44.700","G47.800x002","F93.300","F43.802","F31.800x003","F63.300","F78.900","F84.001","F73.000","F23.902","F22.001","F45.300x091","F68.000x001","F80.200","F44.403","G47.000x001","F44.800x012","F72.900","F68.100","F32.200","F52.100","F63.100","F25.900","F45.300x031","F23.200","F81.100","F52.300","F40.901","F07.201","F25.000","F94.100","F73.100","F45.306","F05.000","F33.000x011","F40.100","F51.500","F93.200","Q93.501","F71.800","F07.800x001","F52.000","F45.804","F06.600","F43.101","F51.200x002","F95.000","F43.001","R45.000","R45.100x002","F31.200","R45.400x001","F31.600","Z03.200","F21.x00","F43.800x002","F45.300","F48.802","F48.100x002","F45.309","F44.602","F41.300x001","F05.100","F31.800x001","F06.800x024","F06.800x033","F60.300","F30.100","F31.900","F81.200","F84.300x001","F45.300x021","F30.900","F52.100x002","F61.x00x011","F73.800","F38.800","F90.000x001","F52.900","F40.200x003","F53.000x001"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCT入组条件，匹配规则：主诊断匹配')

  result=TB1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合TQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'TQY'

  result=TR1.group(record)
  if result:
    return result

  result=TR2.group(record)
  if result:
    return result

  result=TS1.group(record)
  if result:
    return result

  result=TS2.group(record)
  if result:
    return result

  result=TT1.group(record)
  if result:
    return result

  result=TT2.group(record)
  if result:
    return result

  result=TU1.group(record)
  if result:
    return result

  result=TV1.group(record)
  if result:
    return result

  result=TW1.group(record)
  if result:
    return result

  message('不符合MDCT的ADRG入组条件')


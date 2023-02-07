from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.ADRG import HB1,HC1,HC2,HC3,HJ1,HK1,HL1,HL2,HR1,HS1,HS2,HS3,HT1,HT2,HU1,HZ1,HZ2,HZ3

def group(record):
  mdc_zd=["K85.002","K82.800x009","R17.900","K76.000","B15.900","Q44.705","K80.402","B16.203","B18.200","K74.617+I98.3*","K76.800x027","K80.505","K82.302","K70.304+I98.2*","C78.807","K70.401","I77.100x011","K81.003","B17.900x006","K83.104","Q44.001","Q45.300x904","B17.900","K83.401","K86.105","K85.001","K71.903+I98.3*","K83.019","K83.108","K86.800x013","K72.004","K83.015","K86.300","K83.303","K86.800x002","T86.400x011","S36.100x001","K71.900","K72.003","K75.800x001","K85.902","K75.801","D13.501","B17.800x002","K83.009","D01.502","T86.400x018","K80.302","Q44.301","B16.100x002","K71.500x001","K83.109","B17.900x002","Q44.003","K70.402","K82.800x002","K92.800x012","Q44.300","R93.205","S36.111","C25.200","I87.121","E80.601","K71.900x003","K80.200x003","Q45.300x902","K80.304","S36.103","T86.400x010","K70.306+I98.3*","K80.801","Q45.002","I82.000x001","K81.008","B16.101","B17.203","K74.613","C24.000","Q45.100","E80.600x005","B19.900","S36.101","B67.800x001+K77.0*","K85.900","I87.803","A01.001+K77.0*","I86.808","K82.802","K85.202","B18.800x003","K74.400","B17.800x003","B65.906+I98.3*","K83.811","Q44.700x004","B65.900x004+K77.0*","B15.001","A18.816+K87.0*","B16.901","Q44.100x003","K83.100","B66.301","K75.100","K71.100","K74.616+I98.2*","B67.000x001+K77.0*","K86.807","K85.201","S36.112","A18.817+K87.1*","K82.000x003","I87.109","K85.821","K83.800x012","Q85.900x019","D37.601","Q27.804","A50.000x002+K77.0*","B18.900","B18.804","K85.900x003","K74.500","K81.007","K74.615+I98.3*","K71.601","K91.800x403","T86.400x013","K82.306","K73.800x001","K81.801","B18.107","K73.200x002","K85.302","C22.100","Q85.911","C24.000x007","Q45.300x901","R93.203","S36.102","K75.300x001","K80.002","K70.001","K70.201","K75.901","K76.600x002","K82.001","Q44.703","B16.000x001","K75.401","D37.603","C24.001","Q45.200","B16.905","K76.800x023","K83.307","C22.101","K71.102","D37.706","K81.900","B15.901","E84.901","K83.018","B17.100","B18.003","K76.804","K81.001","Q44.601","B67.500x001+K77.0*","B16.902","K72.000x005","K82.801","C25.900","K80.502","K83.501","K83.304","C24.100","I72.809","I74.803","K74.100","B17.900x004","D01.501","K73.000x001","K80.101","K85.800x003","Q45.802","A52.705+K77.0*","Q44.004","B17.903","K83.010","K83.101","K83.802","K83.011","S36.210","K74.601","T86.400x006","E80.603","K74.620+I98.2*","K85.814","S36.202","K81.100","K83.502","K86.812","Q44.700x003","Q45.003","B65.202+K77.0*","K76.813","B17.100x003","T86.400x009","K86.818","K71.300x001","K75.810","T86.400x003","B66.100x001+K77.0*","B18.902","K75.000x002","I74.804","D37.600x001","S36.110","B45.800x001","K71.100x006","K73.801","Q45.001","K80.303","B19.001","K86.802","K70.100","B65.900x010+K77.0*","C22.300","B26.802+K77.0*","K80.305","K82.100x002","K85.815","K86.100x004","T86.400x014","I86.809","K86.801","K86.817","K75.000x003","Q44.002","D13.500x001","K76.809","K85.101","E80.600x006","A18.815+K87.0*","B58.100+K77.0*","E80.600x007","B25.101+K77.0*","K74.301+I98.2*","K74.600x003","K74.600x030","K76.401","K85.200","R16.200x001","D37.600x003","Q44.504","K74.300x006+I98.3*","K76.814","K83.000x012","M32.108+K77.8*","K76.500x002","K83.200x001","D37.604","D13.400","K76.601","K82.303","D37.602","K72.005","D37.600x002","B18.900x006","K71.104","B18.100","D13.600","K74.300x008+I98.3*","K83.017","K74.600x034","K83.302","B18.200x009","K71.901","K72.100","M35.003+K77.8*","K85.901","K75.806","B18.000","B18.104","K83.016","B26.300+K87.1*","K83.106","C25.300","K76.808","I81.x00","K75.805","K82.804","K76.800x021","K83.001","B16.200","K83.809","K74.602","C24.003","K74.600x010","K75.803","K70.901","K76.901","B00.803+K77.0*","K86.815","K82.803","K71.002","T86.400x017","Q44.700x002","S36.100x011","K71.500x002","K86.100x001","K86.806","K91.800x407","K92.800x009","D01.500x001","Q44.102","C24.800x001","K85.100","B17.200x004","K86.106","K76.819","K85.816","K74.614","K80.200x001","K71.902+I98.2*","K80.500x002","B18.803","C78.808","B15.003","K82.808","A52.700x007+K77.0*","C24.900","K86.814","B18.203","C25.400","K86.107","S36.100x041","K80.404","K82.806","K74.600x025","K86.000","K85.809","K83.000","K75.400","E80.400","K85.301","I81.x00x003","K83.816","K82.900x001","B18.800x004","K83.005","B19.000","K70.403","K83.901","K86.805","B17.101","K71.103","K86.800x015","K76.810","R93.302","B18.106","K76.807","B16.001","T86.400x004","K85.801","B17.202","B18.901","A18.301","K76.801","T81.800x006","K74.604","C24.800","K83.807","B18.004","S36.100x021","B17.200","K80.400","B15.903","B17.200x005","C25.800x001","K86.816","B00.802+K77.0*","K76.101","C78.800x009","K80.506","K85.300","S36.100x031","B18.805","T86.401","Q44.500x005","Q27.800x004","B18.002","K85.000","B17.902","K80.401","K70.900","K83.301","K71.200x001","K74.600x029","B18.800x005","K74.605","C24.004","K70.303+I98.2*","K74.608","K83.100x008","Q44.101","E85.415+K77.8*","K71.101","K83.014","K86.200","B17.904","K86.811","C22.200","B17.801","K76.102","K83.810","K80.306","K86.804","K85.818","C78.700","B18.100x007","K76.600x006","K86.800x001","K76.818","K86.101","T86.804","B16.903","Q44.502","C24.101","D37.700x003","K72.900x003+G94.3*","R16.000x001","K76.800x003","K91.807","K83.808","B18.105","I87.108","K74.612","K80.000x002","Q44.400","T86.400x012","K83.400x001","S36.113","K82.807","K86.100x002","C25.801","K71.600x002","B16.100","K85.822","B16.202","K80.000x004","K81.004","K71.100x008","S36.200x092","C22.400","K83.012","K83.800x009","K70.400x002","K83.803","K75.300","K76.800x007","K76.001","K74.619+I98.2*","K83.013","R93.200x001","A18.814+K77.0*","K83.305","K91.840","A06.400+K77.0*","D18.013","K74.618+I98.3*","K85.800x002","E80.500","C25.401","K70.305+I98.3*","C22.000","K86.103","K75.000","K76.700x003","R17.900x001","S36.100x013","K74.300","K76.300","B25.100+K77.0*","K71.701","D01.700","K80.202","K71.400x001","D37.605","K91.822","D13.500x003","K80.405","S36.100x051","K72.900x001","B44.803","K81.006","D13.701","K80.301","B18.801","K82.305","K71.600","Q85.912","K72.000x013","K80.507","K76.800x009","K70.000","K91.827","K82.200x002","Q44.702","S36.200x011","R94.500","K86.102","T85.800x802","K74.600x002","B18.800x002","K72.902","S36.200x021","T86.400x007","Q44.500x006","K82.301","K82.400","K83.105","K83.817","K71.800","Q44.200x003","S36.200x001","D13.401","K80.001","K71.700","B17.102","K75.002","B17.800x001","D13.700x001","B17.803","K91.826","Q44.600","K76.811","K83.818","E83.102","K75.800x006","K71.100x003","K76.803","K86.809","K74.600x027","T82.813","K91.500","K85.800x001","Q44.200","C25.701","K83.103","S36.201","K71.001","K65.007","K83.804","K74.607","K91.800x401","K91.823","Z52.600x001","K83.300","K74.000","K75.804","K80.203","K82.805","K81.101","T86.400x005","D37.705","A51.400x008+K77.0*","K75.001","K74.600x042","K74.300x005+I98.2*","B15.000","Q44.100x002","C23.x00","K82.101","K74.200","C22.301","B17.103","K92.801","K71.702","K83.100x001","Q27.805","K91.841","K82.304","K72.000x004","K74.300x007+I98.2*","K74.610","K82.000","K76.800x026","K70.300","K80.300x002","R93.201","K83.805","N82.302","D18.000x031","K83.107","C24.002","K91.800x301","K86.803","B18.204","K82.800x004","K73.100","B18.202","K86.901","I82.001","D13.500","C45.704","K76.500","K74.600x041","B15.002","K83.820","B18.001","K75.003","C22.001","K76.817","B16.904","E80.602","K74.600x036","Q44.701","R17.901","C78.806","K83.800x023","K82.300","Q27.304","B18.903","K81.900x001","K85.102","K92.800x006","K83.813","B18.802","K83.102","K71.000x002","K86.810","K83.306","Q85.900x044","Q44.501","K70.302+I98.3*","K71.100x005","K76.400","K76.200","R93.204","Q45.301","K91.800x304","B19.002","E80.501","Q44.201","K85.802","K83.815","K82.200","B17.100x006","K73.901","K76.815","K72.904","K91.800x402","K80.500x001","T86.400x016","K81.000x008","Q44.503","B17.900x005","I74.800x016","B19.901","K74.603","K83.000x007","K76.600x007","K86.104","T86.400x015","K76.805","K83.814","K80.800x001","S36.100x081","K80.501","K76.800x022","R93.200x002","C25.000","C25.802","K80.300x005","K80.403","I77.000x017","K76.816","K83.902","I72.800x072","K83.819","B16.100x004","K76.700x001","K80.406","K83.008","B16.000","K76.500x001","Q44.505","B15.902","B25.200+K87.1*","K81.002","K83.006","K70.301+I98.2*","K74.600","B17.205","E80.600x008","K80.504","K86.808","K72.002","K80.503","C22.700","B65.903+K77.0*","K76.800x015","K83.800x022","K81.005","K85.813","B65.904+I98.2*","S36.200x031","K74.600x021","K76.602","B18.201","K91.800x411","B18.800x001","C77.204","K76.603","K91.825","K76.806","K80.400x004","B17.000","K80.201","K71.100x007","B17.204","K73.900","K80.100x001","C77.203","B05.800x003+K77.0*","N82.201","D01.701","K85.807","K86.813","K83.004","Q44.704","K85.900x002","K76.900x002","K74.606","K76.700","B54.x00x003+K77.0*","B16.204","K85.817","K85.803","B15.905","K75.200","S36.200","K72.001","K74.302+I98.3*","B16.100x003","K76.800x006","B54.x00","B16.201","D17.700x015","K82.900x002","K91.806","D01.503","C25.803","K74.611","K92.800x010","C25.100","D37.600x004","Q44.500x007","K74.600x031","K83.007","C22.900","T86.400x001","T86.800x021","K81.000","S36.200x091","K85.808"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCH入组条件，匹配规则：主诊断匹配')

  result=HB1.group(record)
  if result:
    return result
  result=HC1.group(record)
  if result:
    return result
  result=HC2.group(record)
  if result:
    return result
  result=HC3.group(record)
  if result:
    return result
  result=HJ1.group(record)
  if result:
    return result
  result=HK1.group(record)
  if result:
    return result
  result=HL1.group(record)
  if result:
    return result
  result=HL2.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合HQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'HQY'

  result=HR1.group(record)
  if result:
    return result

  result=HS1.group(record)
  if result:
    return result

  result=HS2.group(record)
  if result:
    return result

  result=HS3.group(record)
  if result:
    return result

  result=HT1.group(record)
  if result:
    return result

  result=HT2.group(record)
  if result:
    return result

  result=HU1.group(record)
  if result:
    return result

  result=HZ1.group(record)
  if result:
    return result

  result=HZ2.group(record)
  if result:
    return result

  result=HZ3.group(record)
  if result:
    return result

  message('不符合MDCH的ADRG入组条件')


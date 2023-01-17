from drg_group.suzhou_2022.Base import message,intersect,SS_VALID
from drg_group.suzhou_2022.ADRG import RA1,RA2,RA3,RA4,RB1,RB2,RC1,RD1,RE1,RG1,RR1,RS1,RS2,RT1,RT2,RU1,RV1,RW1,RW2

def group(record):
  mdc_zd=["C96.400","C93.100x011","D47.100","C76.700","C91.000x009","D18.105","C92.901","C93.900","C85.900x014","C96.900","Z51.809","C92.400x011","D47.701","C85.900x037","C94.400","C90.000x038","C90.200","C95.000x018","C85.900x025","C45.706","Z51.800x092","C95.100x012","C85.100x017","C85.900x011","C91.000x015","C97.x00","D47.402","C91.000x012","C84.901","D19.700","C92.501","Z08.800x003","C85.709","C88.203","C85.900x038","C88.403","C90.302","C95.003","C94.004","C95.000x003","Z51.000x013","Z51.800x094","C85.900x039","C84.500x012","C80.001","C85.900x019","Z51.000x012","C84.700","C95.000x017","Z51.800x925","C81.100","D46.001","C77.900","C84.406","Z51.200x008","C91.000x016","C94.700x014","C92.700","C85.900x036","C95.000x116","C85.900x040","D45.x00","D47.200","C84.400","C80.904","D36.700x011","C88.000x012","C83.003","C95.901","C91.101","D46.901","C79.800x862","C88.200x012","C95.900x013+M36.1*","D36.700x023","C96.400x003","C92.005","D48.716","C91.901","C96.604","C79.800x804","D47.500","C84.401","C85.900x041","C83.306","C85.900x017","D48.700x015","D47.100x004","C92.700x006","C92.100x002","Z51.801","C97.x01","C79.811","D89.801","C96.501","C83.001","C88.700x002","Z51.811","D46.500","D47.000","D46.700x006","Z51.000x003","C90.000x039","D36.700x025","C88.000x002","C90.000","C85.900x005","C96.000","C93.100x013","C86.603","C93.100","C45.900","C90.300x004","C90.000x037","C92.100x019","D47.100x009","Z51.500x001","C82.703","C92.001","C83.300","C95.000x115","D46.700","C91.900","C88.200x011","C95.700x002","C96.704","C85.900x013","D36.700x016","C90.000x032","Z08.100","C45.100x005","C92.800","C85.200","D46.600","C80.903","C93.901","C91.600","C92.300x011","C83.503","C92.000x014","D47.404","C92.006","D46.100","C46.900x002","C82.901","C77.206","C94.000x001","C85.100x021","C88.000x011","C88.000","C85.900x001","C92.401","D47.200x004+G63.1*","C93.000x011","C95.000x101","C88.900","D36.710","C83.307","Z08.200","C90.000x022","C77.302","C85.900x004","C84.000","C96.002","C94.200x011","Z51.003","C95.000x102","D46.900x004","D48.700x001","C92.102","D47.400","Z51.000x008","C45.103","D46.900x002","C86.602","C93.300","D47.401","C85.900x002","C95.000x117","Z51.104","C92.003","C94.702","C91.007","C94.200","C92.002","D47.100x018","C92.300x003","C92.000x017","C93.100x012","C81.000","C79.900x001","C83.002","C90.300x003","C76.800","Z09.200","C88.402","C91.300","D48.723","D47.900x002","D18.109","C77.300x003","Z51.800x097","C94.001","C84.500","C85.900x008","C96.500","D18.106","C90.000x012","C77.303","C86.100","C92.600","C83.504","C91.102","C84.600","C91.100x011","D47.002","C95.100x011","C91.100x012","C46.700","C84.405","Z08.800x001","C95.000x015","C86.000","C88.301","C88.201","C95.002","C85.705","C90.000x026","C94.600","C96.004","C85.900x022","C91.000x007","Q85.802","Z51.800x952","Z51.810","Z51.002","C96.403","C91.008","D47.900x001","C90.300","C82.701","Z08.000","C92.200x011","C86.500","C90.000x035","Z51.804","D47.700x006","D48.725","C96.603","C84.601","C81.700","C85.900x016","C96.200","C85.900","C95.004","D47.700x005","C92.000x015","C92.300x013","C83.004","C85.100","C85.704","Z51.101","C82.000","C92.100x001","C84.900","C82.900","C83.302","C84.404","C83.100","C85.900x010","C84.500x004","C95.006","Z51.800x924","C85.700x016","Z51.500x002","Z09.100","D48.900","C82.300","D48.715","Z08.900","C90.000x040","C91.006","C92.000x018","D47.702","C83.800x009","Z51.800x927","Z51.800x921","C83.700","C93.003","C83.800x008","C96.402","C92.000x003","C46.800","C82.200","C92.706","Z51.800x096","C92.500x011","D46.700x007","C92.201","C95.700x011","C91.400","C83.101","C88.900x001","C81.900x005","Z08.800x004","C96.400x001","C90.000x027","D47.200x005+G63.1*","Z08.700","C92.900x011","C93.104","C93.102","D47.001","C91.704","C91.400x013","C95.000x002","C95.900","C82.704","C90.000x004","C90.000x021","C93.001","C91.500","C92.402","C90.200x013","C94.201","C92.703","C82.700","C90.000x029","D36.700x028","C79.826","C96.602","C93.002","C78.605","C91.701","C83.300x009","C95.100","Z51.800x953","C77.503","D47.003","C90.000x028","C83.502","C95.000x118","Z54.001","C81.703","C96.202","C79.800x811","C85.900x028","C91.001","C88.200","C91.000x014","C83.305","Z51.800x922","C82.600","C80.905","C77.502","C79.800x816","C85.900x030","D46.700x003","C76.101","C83.803","C95.000","C80.000x001","D48.902","C91.100","C76.306","C77.205","D19.900x001","C85.900x031","C85.901","D36.700x021","C92.700x013","C82.903","C92.300","D36.700x012","D48.722","C82.500","C83.303","C85.900x012","C88.700x013","C91.700","C85.701","C85.900x015","C90.000x041","C77.800","C96.800","C77.401","C90.200x009","D46.900","C77.202","C92.000x013","C85.900x006","C88.300","C93.701","D46.700x002","Z51.800x095","D46.700x008","C77.500","D09.700","C83.501","C83.801","Z51.806","C81.400","C92.007","C91.400x004","C92.700x012","C84.000x002","C90.300x002","C79.829","C85.700","D47.100x017","C85.900x023","C85.900x027","C93.101","C48.102","C49.901","C90.000x030","C80.000","C93.103","D09.700x001","C86.600","C94.300","C94.703","D46.100x012","D47.700","C92.701","Z51.100x004","Z08.800x002","Z51.500x003","C91.000x017","C90.000x024","Z51.103","C90.200x008","C92.100","D46.100x002","C80.901","D47.100x019","C96.705","C81.200","C92.200x001","C85.900x029","C81.900","C85.900x026","C84.403","C96.601","C77.200","C86.601","C90.000x033","C91.401","C85.900x034","C88.701","C90.100","C94.202","C92.601","C83.301","C79.800x818","D47.403","C85.900x003","Z51.102","C91.003","C84.100","C91.800","C88.202","C82.702","D47.700x007","C96.400x002","C90.000x009","C92.103","C76.300","C92.100x018","C90.000x014","C83.000","D48.700x023","D48.708","C90.303","D46.400","Z51.800x981","C76.305","Z51.808","D47.300","C84.000x003","C85.700x004","C88.700x012","C96.200x013","D47.703","C85.715","C76.302","C81.702","C94.700x004","C95.000x016","Z51.800x951","C93.300x001","C83.802","C77.900x001","C86.300","C76.700x002","C95.900x003+M36.1*","D36.705","C83.900","C91.000x006","C92.100x004","C95.700x003","D36.709","C95.700x001","C77.501","C88.302","C76.200x002","C76.801","C46.300","C83.800","C85.900x009","C77.301","C93.700","C88.700","C85.707","C92.000x016","C77.300","C92.100x016","C82.100","C86.400","C92.100x014","C92.100x012","C92.000","C90.000x008+M90.6*","C90.000x036","D47.100x007","C96.201","C90.000x011","D47.900","C90.000x034","C83.300x007","C96.502","C93.000x016","C95.900x015","C91.004","C84.800","C92.000x006","C88.401","C84.402","Z51.800x983","C92.900","C77.300x001","C90.000x005","C85.900x020","D47.100x008","C86.200","C90.000x025","C94.400x001","C96.400x004","Z51.807","C96.700","C96.200x005","C94.300x011","D36.711","C85.100x010","C92.200","C92.502","C88.700x003","C90.001","C77.107","C92.004","C84.400x001","C91.002","C96.600","C80.902","C79.900","C90.301","C95.900x005","C83.500","C85.900x042","C88.400","Z51.802","Z51.805","C85.900x024","C90.100x002","C94.000x011","C84.500x016","C84.502","C46.900","C83.800x006","D47.101","C85.900x043","D46.201x001","C92.300x001","C92.100x017","Z51.001","C83.505","C46.900x004","C90.000x023","C90.000x031","C83.703","C46.900x003","D46.700x001","C78.604","C83.102","C48.101","C83.300x006","C80.900","C83.300x008","C91.000x013","C83.304","C84.407","C94.700","D09.900","C95.005","Q85.909","C82.400","C92.000x012","C92.403","D46.200","D47.004","D46.203","C83.702","C91.000","D48.901","C96.801","C91.500x011","C92.100x011","D48.707","D46.900x006","C81.300","C90.300x001","C96.401","C81.701","D36.704","C79.800x837","C90.002","D47.200x003","C92.900x001","C92.101","C90.100x011","C92.009","C92.000x011","C92.008","C77.400x001","C95.900x012"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCR入组条件，匹配规则：主诊断匹配')

  result=RA1.group(record)
  if result:
    return result
  result=RA2.group(record)
  if result:
    return result
  result=RA3.group(record)
  if result:
    return result
  result=RA4.group(record)
  if result:
    return result
  result=RB1.group(record)
  if result:
    return result
  result=RB2.group(record)
  if result:
    return result
  result=RC1.group(record)
  if result:
    return result
  result=RD1.group(record)
  if result:
    return result
  result=RE1.group(record)
  if result:
    return result
  result=RG1.group(record)
  if result:
    return result

  if record.ssList and record.ssList[0] in SS_VALID:
    message('符合RQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'RQY'

  result=RR1.group(record)
  if result:
    return result

  result=RS1.group(record)
  if result:
    return result

  result=RS2.group(record)
  if result:
    return result

  result=RT1.group(record)
  if result:
    return result

  result=RT2.group(record)
  if result:
    return result

  result=RU1.group(record)
  if result:
    return result

  result=RV1.group(record)
  if result:
    return result

  result=RW1.group(record)
  if result:
    return result

  result=RW2.group(record)
  if result:
    return result

  message('不符合MDCR的ADRG入组条件')


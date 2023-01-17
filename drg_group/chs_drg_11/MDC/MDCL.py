from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.ADRG import LA1,LA2,LB1,LB2,LC1,LD1,LE1,LF1,LJ1,LL1,LR1,LS1,LT1,LU1,LV1,LW1,LX1,LZ1

def group(record):
  mdc_zd=["D30.200","N32.900x002","E10.200x014+N08.3*","C64.x00x003","C90.005+N08.1*","R82.500x007","Q62.104","R82.800","N32.202","Z49.000","Q85.900x013","Z46.800x001","N00.100x001","N28.805","R80.x00x003","M31.100","Q64.600","N32.811","N39.800","N13.600x002","C67.300","D09.103","N04.502","N26.x01","T83.800","N30.400","S37.111","R35.x00","N05.000x004","N28.818","N17.002","Q63.102","Z45.800x007","E10.200x031+N29.8*","N18.200","N06.001","E10.200x015+N08.3*","E10.200x212+N08.3*","N31.200x006","E11.400x381+N33.8*","N05.000x003","M31.002+N08.5*","N07.200","N13.000","N13.203","N32.800x003","Q64.401","Z52.400","Q64.706","R82.200","T83.804","N15.900x003","N99.100","N28.834","S37.000x031","N30.808","R82.000","I12.900x009","I12.900x008","M35.006+N16.4*","N05.101","R82.300","N13.504","N25.800x006","Q62.100","N32.800x019","R82.600x001","N02.900x001","C67.500","N36.901","S37.200","N01.800","E10.200x025+N08.3*","S37.200x081","N32.808","T86.100x003","N00.902","N14.201","N30.806","N32.802","N05.900","N11.901","D41.300x001","N39.001","Q63.301","N28.804","N28.833","N14.102","N34.000x005","N99.800x011","N02.502","N05.801","S37.000x013","N03.900","N13.400","S37.200x023","E10.200x213+N08.3*","D41.900x001","Q64.707","C76.303","D69.005+N08.2*","Q62.100x802","Q63.302","N13.801","C66.x00x003","N03.200x001","N20.002","N34.200x003","R80.x02","N07.900x001","N30.900","T28.800x001","T86.106","E14.200x021+N08.3*","N03.100","N21.100","S37.000x022","N30.802","N36.200","N28.901","T86.105","E11.200x017+N08.3*","E10.200x215+N08.3*","E11.200x016+N08.3*","E85.411+N29.8*","Q62.103","T86.107","N00.900x009","N31.901","N11.802","N28.821","N31.200x007","N20.001","Q64.100x091","C65.x01","N03.300x001","E11.200x092+N08.3*","N10.x01","N07.500","N25.900","N39.300","N25.001","S37.302","S37.300x004","E10.200x030+N08.3*","A41.902+N08.0*","N03.900x007","T83.102","R80.x00","C67.900x002","Q64.200x021","Q64.701","N32.000","N04.300x003","N36.001","N30.300","N30.804","C67.400","N17.901","E14.200x026+N08.3*","N02.801","Q60.500","D30.400","N32.102","D41.000x001","N32.400","N28.801","N12.x02","N28.816","N28.900x004","N28.002","N30.201","Q64.708","T83.100x001","D30.000","N18.400","N39.200","N36.808","T83.801","N28.814","Q62.400x002","D18.000x811","N28.810","Q61.401","C66.x00x002","Q64.700x601","T79.500x002","N32.803","A02.205+N16.0*","R39.801","E10.200x026+N08.3*","Q64.700x201","N01.200x001","R30.000x002","N04.200x001","N28.809","N32.200","E11.201+N08.3*","N06.900","N36.301","N32.801","N39.403","N20.000x002","R93.400x001","E66.902+N08.4*","N34.204","Z46.603","N04.902","Q60.400","Q61.400","R93.401","E10.200x214+N08.3*","E72.006+N29.8*","R93.405","N07.400","N28.003","N32.812","T83.500x003","Q62.202","N15.801","N28.820","R82.901","N02.600","D09.000","N32.800x009","N00.900x002","N36.804","Q63.001","T83.802","N31.201","Q61.500","R94.402","S37.000x023","T86.100x005","N00.600","Q62.500","R93.400x002","Q64.501","S37.300x011","S37.814","N36.802","N39.404","A40.901+N08.0*","R94.803","D41.401","R82.700","T86.103","C68.000","T83.101","R82.500x005","T86.102","N04.700","N06.500","Z49.101","N01.400x001","N35.000x001","C67.200","C67.800","E11.200x015+N08.3*","N36.806","N34.203","N14.400","D41.001","N05.501","C68.800x003","Q62.101","N01.000","N28.828","D41.901","N19.x01","N06.100","E14.400x381+N33.8*","N00.900x006","R30.100x001","D09.104","N13.503","Q87.800x903","T83.200","N28.900x026","R82.900x002","C64.x00x004","C65.x02","N32.103","Q51.701","Q61.403","N28.900x017","Q61.000","N02.002","R30.000","N18.300","N34.002","Q62.300x901","Q64.402","N36.300","E11.200x212+N08.3*","Q27.305","N28.101","Q62.301","N36.201","Q62.600","D18.000x806","E10.200x028+N08.3*","N02.800x003","N02.102","S37.300x005","S37.300x021","N28.902","N36.000x007","N28.900x010","N34.001","N32.815","N36.004","N01.300x001","N13.100x001","E10.200x091+N08.3*","N31.000x001","N07.800","N36.100","N07.700","N39.401","E14.200x028+N08.3*","N02.401","N28.838","S37.001","N39.000","N03.900x005","N05.000x001","N34.300","R93.404","Q62.300x905","N00.000","N21.800","C67.700","N00.801","N35.100x001","N00.802","I12.000x001","E11.200x013+N08.3*","I12.900x002","S37.010","T86.100x007","E11.200x214+N08.3*","N03.900x002","N06.200","M31.102+N08.5*","N03.900x003","E14.400x380+G99.0*","R94.400","E10.200x029+N08.3*","C90.004+N16.1*","N17.900x004","N04.900","C48.001","Q63.103","N03.900x004","N28.808","S37.300x081","N05.802","R31.x00","M10.005+N22.8*","N03.800x004","Q64.000","N25.806","N17.101","T83.500x002","N32.100","N34.201","E14.200x215+N08.3*","I12.900x003","N30.809","N28.835","N99.805","R30.900x001","N05.201","N20.000","N28.806","N32.201","Q62.201","T19.801","Q61.900","D09.100x001","N32.800x014","E14.200x029+N08.3*","N30.801","D18.000x819","N14.301","E14.200x213+N08.3*","N03.900x006","N99.800x006","I13.100x001","T19.000","N28.829","N04.903","Q64.700x901","Q64.702","Q64.303","C67.100","N28.813","N32.204","N28.819","N30.100","E14.200x016+N08.3*","Q60.200","N31.200x003","N34.200x006","N04.800x002","T83.800x001","Q60.600","M31.305+N08.5*","E10.200x016+N08.3*","D89.101+N08.2*","N11.900x001","Q61.800","D17.700x016","N31.100x001","N36.002","Z49.201","N34.102","N28.812","T28.800","N28.004","N27.000","E10.201+N08.3*","N05.900x002","N30.805","N30.803","N99.001","N12.x01","T83.103","S37.310","N17.900x003","T83.100x002","N28.815","E11.200x029+N08.3*","E11.200x025+N08.3*","M10.001+N16.8*","N34.202","Z49.000x004","N11.801","N21.000","N07.600","N25.802","N10.x00","N18.100","Q64.403","Q85.900x029","N02.900x002","E11.200x091+N08.3*","N03.800x003","R30.100","R34.x02","N28.839","Q64.400x301","E14.200x212+N08.3*","N99.808","N23.x00","S37.211","N03.503","R82.902","E11.200x012+N08.3*","R80.x01","N03.700","N11.900","N26.x02","Q62.700x001","S37.201","T83.000x001","S37.000x015","R82.500x004","N18.902","S37.004","N18.904","N04.300x001","N17.900","Q85.903","N30.000","E10.200x027+N08.3*","N31.200x002","N21.001","Q62.700","N06.800","I86.201","N05.900x003","N15.101","N04.102","R35.x00x003","D41.101","M31.703+N08.5*","Q64.705","N02.201","R39.200","N21.900","Z46.800x002","N18.901","Z49.000x002","N18.501","Q62.300x904","S37.000x012","Q62.601","D21.506","N05.600","N03.601","N17.200x002","D30.900","N17.200","N01.900x002","N17.001","R82.500x003","N03.800x001","Q64.700x904","R32.x01","R39.101","N02.203","E11.200x211+N08.3*","R93.403","Q60.400x001","N28.900x013","R39.100x002","T81.800x011","D09.101","Q63.002","E11.200x014+N08.3*","R35.x00x001","N28.800x001","Q62.400","N35.000","E11.200x011+N08.3*","N36.803","T86.104","Q61.404","C68.804","N28.100","C67.501","E13.201+N08.3*","S37.011","N06.700","I12.900x001","N28.001","N28.822","N99.101","N13.501","Q63.000","E11.200x031+N29.8*","N28.803","E14.200x014+N08.3*","D41.700","N01.600x001","Q64.301","N32.101","E72.007","C79.103","N04.501","T86.100x008","E14.200x091+N08.3*","N11.800x002","Q64.700x902","N17.100","C68.801","N07.000","Q64.704","T19.100","N32.806","E14.200x012+N08.3*","Q64.700x701","D41.301","T86.100x006","C65.x00","N17.200x003","E10.200x012+N08.3*","E14.200x013+N08.3*","N39.402","R34.x01","C68.802","C95.900x007+N16.1*","E11.200x024+N08.3*","N01.700x001","E14.200x015+N08.3*","N02.101","N04.901","N14.101","N25.805","N39.300x002","N03.901","N99.100x005","S37.303","T83.500","N17.900x002","N11.900x003","N39.405","N31.203","Q63.900","Q61.100","N13.601","B65.002+N22.0*","N15.901","N19.x00","R94.802","Q62.000","N30.800x004","E14.200x214+N08.3*","N30.902","Q63.801","Z46.600x001","R39.000","N02.702","N13.302","E14.200x025+N08.3*","N32.203","N20.000x003","C68.805","D30.300","E14.200x092+N08.3*","N36.805","E10.200x092+N08.3*","N13.202","N13.901","N03.501","E85.403","N15.900x004","Q62.300x101","C95.900x017+N16.1*","N32.800x008","S37.300x082","C68.803","E10.200x024+N08.3*","N36.000","E14.200x024+N08.3*","N18.500","E10.200x023+N08.3*","Q64.200","N14.000","C68.900","C67.600","N32.807","Q64.700x801","N04.101","Q63.200","N18.900x011","N05.900x006","E13.200x521+N08.3*","T19.800x001","E11.200x027+N08.3*","N28.837","N30.901","N20.000x001","N10.x02","S37.000x016","N36.005","S37.000","N28.830","T28.300","D30.302","N00.900","E11.400x380+G99.0*","C79.100x002","N07.100","N05.400","T81.800x014","C76.301","N32.813","N28.102","N13.500x010","N00.901","N15.102","N99.500","N00.500","E83.100x008+N16.3*","N13.604","Q62.300x903","N99.000","R32.x00","N07.300","D41.200x001","E14.200x031+N29.8*","N32.810","R39.200x001","N13.603","N99.100x003","N06.400","E14.200x011+N08.3*","N02.900","N34.200x004","N05.900x007","T83.501","N36.809","C66.x00","M31.003+N08.5*","S37.301","Q64.703","Q60.100","E10.200x017+N08.3*","N28.807","N27.900","N34.100","Q64.900","N32.104","N13.201","N13.600","N15.900x002","N06.300","N19.x02","R93.402","N01.100x002","N05.301","N32.301","Q62.700x201","N02.302","N36.807","Q64.100","R33.x00","N28.836","E10.200x013+N08.3*","N12.x03","N13.506","N13.602","C79.101","N03.801","Q62.300x301","N01.900x003","Q60.300","E12.200","S37.300x083","T83.002","N05.803","N39.100","Q60.000","N32.901","N03.400","E11.200x030+N08.3*","E10.200x011+N08.3*","N13.600x001","N32.809","T83.100","C79.102","N05.701","N02.301","R79.802","N32.805","R39.100x001","S37.300","N28.832","S37.002","M31.701+N08.5*","D30.100","S37.200x022","E14.200x027+N08.3*","D41.400x004","C68.100","N27.100","N15.000","Q42.200x201","Q62.300x902","E10.200x211+N08.3*","S37.000x032","T83.003","S37.200x024","E85.002","S37.200x011","N00.200","N02.701","M32.102+N16.4*","Q87.808","D41.400x001","T86.100x002","N28.831","N31.202","S37.813","N28.817","N03.000","N13.204","E11.200x213+N08.3*","N20.901","N11.800x003","Q61.402","Q63.201","Q60.501","N20.900x001","N28.802","T86.100x001","N28.824","Q63.800x101","Q63.800x902","S37.101","N36.003","T83.004","T79.500","N00.700","Q64.200x001","T83.100x004","D30.301","M32.101+N08.5*","N13.300x005","N04.601","I12.900x005","N35.901","N32.800x012","D41.201","N13.301","N32.804","S37.003","N32.300","N99.806","Q62.400x001","E11.200x028+N08.3*","N34.000","T83.100x003","E14.200x030+N08.3*","N03.500x003","C64.x00x001","D09.102","N34.205","C67.000","N25.004","T19.900","N01.500x001","N36.302","Q64.302","N11.100","N11.000x001","N04.801","N00.800x001","C79.001","N13.502","N05.900x009","Q64.304","N13.701","C79.000x001","I12.900x006","N28.005","Q64.800x001","Q61.200","N25.803","N02.802","Q61.901","N28.826","S37.300x031","N03.502","N17.000","N26.x00","R82.900x003","E14.200x017+N08.3*","N39.900","Q62.100x902","Q62.800","M35.007+N16.4*","N00.400","N25.100","N30.810","N35.800","Q62.602","N12.x00","E14.200x023+N08.3*","N25.804","Q64.400x902","C68.800","R94.401","S37.100","Q63.101","N32.001","Q61.300","N20.200x001","N13.600x004","D30.701","N20.900","N35.900","N17.800","Q62.700x101","N01.900","N20.100","N32.814","N99.803","R93.400x003","T86.811","N04.400x001","N01.900x001","N34.101","Q64.502","Z46.601","E11.200x026+N08.3*","N06.600","N31.800","Q63.203","E11.200x023+N08.3*","N28.823","N04.001","N30.807","N32.002","Q61.801","C67.900","N39.800x001","R36.x01","R82.500x006","N28.825","N28.811","N00.301","E11.200x215+N08.3*","I12.904","T83.001","N39.400","N28.827","N00.900x008","E14.200x211+N08.3*","D41.100x001","Q62.200","Z46.602","N02.001","N31.200x001","N13.605","N19.x03"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCL入组条件，匹配规则：主诊断匹配')

  result=LA1.group(record)
  if result:
    return result
  result=LA2.group(record)
  if result:
    return result
  result=LB1.group(record)
  if result:
    return result
  result=LB2.group(record)
  if result:
    return result
  result=LC1.group(record)
  if result:
    return result
  result=LD1.group(record)
  if result:
    return result
  result=LE1.group(record)
  if result:
    return result
  result=LF1.group(record)
  if result:
    return result
  result=LJ1.group(record)
  if result:
    return result
  result=LL1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合LQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'LQY'

  result=LR1.group(record)
  if result:
    return result

  result=LS1.group(record)
  if result:
    return result

  result=LT1.group(record)
  if result:
    return result

  result=LU1.group(record)
  if result:
    return result

  result=LV1.group(record)
  if result:
    return result

  result=LW1.group(record)
  if result:
    return result

  result=LX1.group(record)
  if result:
    return result

  result=LZ1.group(record)
  if result:
    return result

  message('不符合MDCL的ADRG入组条件')


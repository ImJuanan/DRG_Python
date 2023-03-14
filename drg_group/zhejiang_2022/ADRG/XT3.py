from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCX_DRG

def group(record):
  adrg_zd=["B90.000","B90.001","B90.002","B90.100","B90.101","B90.200","B90.200x002","B90.200x003","B90.201","B90.202","B90.800x004","B90.800x005","B90.800x006","B90.801","B90.802","B90.803","B90.804","B90.901","B90.902","B90.903","B90.904","B91.x00","B92.x00","B94.000","B94.100","B94.101","B94.200","B94.201","B94.800x001","B94.800x003","B94.801","B94.802","B94.900","E89.900","J95.900","Q85.914","Q90.200","R46.300","R46.500","R46.800x001","R46.801","R58.x00x002","R58.x00x006","R96.100x001","R98.x00x002","R99.x00x002","R99.x01","T73.200","T73.300","T75.200","T80.202","T80.203","T80.800","T80.801","T81.601","T82.812","T84.400","T84.700","T84.700x001","T84.900","T84.901","T85.800","T85.801","T85.802","T85.806","T85.902","T86.900","T87.200","T88.901","T96.x00x001","T96.x00x002","T96.x00x003","T98.000","T98.200","T98.200x031","T98.200x032","T98.300x007","T98.301","Z00.001","Z00.100","Z00.200","Z00.300","Z00.300x001","Z01.600x002","Z01.800x002","Z03.100","Z03.101","Z03.102","Z03.103","Z03.300","Z03.600x001","Z03.800","Z03.800x701","Z03.800x711","Z03.800x721","Z03.800x731","Z03.802","Z03.803","Z03.900","Z03.900x001","Z09.001","Z10.000","Z11.000","Z11.100","Z11.200","Z11.300","Z11.400","Z11.500","Z11.600","Z11.800x001","Z11.801","Z11.802","Z11.803","Z11.901","Z11.902","Z12.000","Z12.100","Z12.200","Z12.300","Z12.400","Z12.500","Z12.600","Z12.800","Z12.900x001","Z12.901","Z13.000x001","Z13.001","Z13.100","Z13.200","Z13.300","Z13.300x002","Z13.300x003","Z13.400x001","Z13.500","Z13.500x001","Z13.501","Z13.600","Z13.700","Z13.800x011","Z13.800x021","Z13.800x022","Z13.800x031","Z13.800x032","Z13.800x041","Z13.800x051","Z13.800x061","Z13.801","Z13.900","Z20.000","Z20.001","Z20.100","Z20.200","Z20.300","Z20.400","Z20.500","Z20.701","Z20.702","Z20.801","Z20.802","Z20.900","Z22.000","Z22.100","Z22.101","Z22.102","Z22.103","Z22.200","Z22.300","Z22.301","Z22.302","Z22.303","Z22.400","Z22.401","Z22.402","Z22.600","Z22.700","Z22.801","Z22.900x001","Z23.000","Z23.100","Z23.200","Z23.300","Z23.400","Z23.500","Z23.600","Z23.700","Z23.800x001","Z24.001","Z24.100","Z24.200","Z24.300","Z24.400","Z24.500","Z24.600","Z24.601","Z25.000","Z25.100","Z25.800x001","Z26.000","Z26.800","Z26.900","Z27.000","Z27.100","Z27.200","Z27.300","Z27.400x001","Z27.800","Z27.900","Z28.000","Z28.100","Z28.101","Z28.201","Z28.800","Z28.900","Z29.000","Z29.100","Z30.000x001","Z30.000x002","Z30.000x003","Z30.101","Z30.102","Z30.103","Z30.201","Z30.202","Z30.203","Z30.301","Z30.302","Z30.400x001","Z30.400x003","Z30.400x004","Z30.500x011","Z30.501","Z30.503","Z30.504","Z30.505","Z30.800x001","Z30.800x002","Z30.800x003","Z30.800x004","Z30.800x005","Z30.900","Z31.202","Z31.203","Z31.400x003","Z31.400x004","Z31.401","Z31.402","Z31.500","Z31.600x001","Z31.800","Z31.900","Z32.000x001","Z32.100","Z39.100x001","Z39.100x002","Z39.100x003","Z39.200x001","Z40.000x001","Z40.800","Z40.900x001","Z41.300","Z41.800x002","Z41.801","Z41.900","Z51.300","Z51.400x002","Z51.400x003","Z51.800","Z52.000","Z52.001","Z52.300x002","Z52.900","Z53.000x001","Z53.100x001","Z53.200x001","Z53.800x001","Z53.800x002","Z53.800x003","Z53.900x001","Z54.000","Z54.000x002","Z54.000x003","Z54.000x004","Z54.000x005","Z54.000x006","Z54.000x007","Z54.000x008","Z54.000x009","Z54.000x010","Z54.000x012","Z54.000x013","Z54.000x014","Z54.000x015","Z54.000x016","Z54.000x017","Z54.000x018","Z54.000x019","Z54.000x020","Z54.000x021","Z54.000x022","Z54.100","Z54.200x001","Z54.300","Z54.400","Z54.700","Z54.800x001","Z54.800x002","Z54.800x003","Z54.800x004","Z54.800x005","Z54.800x006","Z54.800x007","Z54.800x008","Z54.800x009","Z54.800x010","Z55.000","Z55.100","Z55.200","Z55.300","Z55.400","Z55.800","Z55.900","Z56.000","Z56.100","Z56.200","Z56.300","Z56.400","Z56.500","Z56.600","Z56.700","Z57.000","Z57.100","Z57.201","Z57.300","Z57.400","Z57.501","Z57.502","Z57.503","Z57.504","Z57.505","Z57.506","Z57.507","Z57.508","Z57.600","Z57.700","Z57.800","Z57.900","Z58.000","Z58.100","Z58.200","Z58.300","Z58.400","Z58.500","Z58.600","Z58.700","Z58.800","Z58.900","Z59.000x001","Z59.100","Z59.200","Z59.300","Z59.400","Z59.500","Z59.600","Z59.700","Z59.800","Z59.900","Z60.000x001","Z60.100x001","Z60.200x001","Z60.300x002","Z60.400","Z60.500","Z60.800","Z60.900","Z61.000x001","Z61.100x001","Z61.200x001","Z61.300x001","Z61.400x001","Z61.500x001","Z61.600x001","Z61.700x001","Z61.800","Z61.900x001","Z62.000x001","Z62.100x001","Z62.200x001","Z62.300x001","Z62.400x001","Z62.500x001","Z62.600x001","Z62.800","Z62.900","Z63.000","Z63.100x001","Z63.200x001","Z63.300x001","Z63.400x001","Z63.400x002","Z63.400x003","Z63.500x001","Z63.500x002","Z63.500x003","Z63.600","Z63.700x001","Z63.700x011","Z63.700x021","Z63.700x091","Z63.700x092","Z63.700x093","Z63.800x001","Z63.800x002","Z63.800x003","Z63.800x004","Z63.900","Z64.100x001","Z64.200","Z64.300","Z64.400x001","Z64.400x002","Z64.400x003","Z65.000","Z65.100x001","Z65.200","Z65.300x001","Z65.300x002","Z65.300x003","Z65.300x004","Z65.300x005","Z65.400x001","Z65.400x002","Z65.400x003","Z65.500x001","Z65.500x002","Z65.500x003","Z65.800","Z65.900","Z70.000","Z70.100","Z70.200","Z70.300","Z70.800","Z70.900","Z71.000","Z71.100","Z71.200","Z71.300","Z71.400","Z71.500","Z71.600","Z71.700","Z71.800","Z71.900","Z72.000","Z72.100","Z72.200","Z72.300","Z72.400","Z72.500","Z72.600","Z72.800","Z72.900","Z73.000","Z73.100x001","Z73.200","Z73.300","Z73.400","Z73.500","Z73.600","Z73.800","Z73.900","Z74.000","Z74.100x001","Z74.200","Z74.300","Z74.800","Z74.900","Z75.000","Z75.100","Z75.200","Z75.300","Z75.400","Z75.500","Z75.800x001","Z75.900x001","Z76.000","Z76.100","Z76.201","Z76.300","Z76.400","Z76.500","Z76.800x001","Z76.900","Z80.000","Z80.001","Z80.002","Z80.100","Z80.200","Z80.300","Z80.400","Z80.401","Z80.500","Z80.600","Z80.700","Z80.801","Z80.900","Z81.000x001","Z81.100","Z81.200","Z81.300","Z81.400","Z81.800","Z82.000","Z82.000x001","Z82.100","Z82.200","Z82.300x001","Z82.400","Z82.500","Z82.600","Z82.700","Z82.701","Z82.800","Z83.000","Z83.100","Z83.200","Z83.201","Z83.300","Z83.400","Z83.500","Z83.600","Z83.700","Z84.000","Z84.100","Z84.200","Z84.201","Z84.300","Z84.800","Z86.100","Z86.100x021","Z86.100x031","Z86.100x801","Z86.101","Z86.102","Z86.103","Z86.104","Z86.200x001","Z86.200x002","Z86.300","Z86.300x001","Z86.301","Z86.400","Z86.501","Z86.600","Z86.600x001","Z86.600x002","Z86.600x003","Z86.600x004","Z86.600x005","Z86.700","Z86.701","Z86.702","Z86.703","Z87.000","Z87.100","Z87.100x011","Z87.100x021","Z87.200","Z87.300","Z87.400","Z87.500x001","Z87.500x003","Z87.500x004","Z87.500x005","Z87.600x001","Z87.701","Z87.800","Z88.000x001","Z88.101","Z88.102","Z88.200x001","Z88.300x001","Z88.301","Z88.302","Z88.400x001","Z88.500x001","Z88.600x001","Z88.700x001","Z88.801","Z88.802","Z88.803","Z88.804","Z88.805","Z88.806","Z88.807","Z88.808","Z88.811","Z88.812","Z88.813","Z88.814","Z88.815","Z88.817","Z88.818","Z88.819","Z88.820","Z88.821","Z88.822","Z88.823","Z88.824","Z88.825","Z88.900x001","Z89.000x001","Z89.000x002","Z89.000x003","Z89.100x001","Z89.200","Z89.200x002","Z89.300","Z89.300x002","Z89.400x001","Z89.401","Z89.500x002","Z89.600x001","Z89.600x002","Z89.700x001","Z89.800","Z89.800x001","Z89.800x002","Z89.800x003","Z89.900x001","Z90.000x001","Z90.000x002","Z90.000x003","Z90.000x004","Z90.000x005","Z90.000x006","Z90.000x007","Z90.000x008","Z90.000x009","Z90.000x010","Z90.000x011","Z90.000x012","Z90.000x013","Z90.000x014","Z90.000x015","Z90.000x016","Z90.000x017","Z90.000x018","Z90.000x019","Z90.000x021","Z90.000x022","Z90.000x023","Z90.000x024","Z90.001","Z90.002","Z90.100x001","Z90.200x001","Z90.300x001","Z90.400x001","Z90.400x002","Z90.400x003","Z90.401","Z90.402","Z90.403","Z90.404","Z90.405","Z90.406","Z90.407","Z90.500x001","Z90.600","Z90.600x002","Z90.600x003","Z90.700x002","Z90.700x003","Z90.700x005","Z90.700x006","Z90.701","Z90.702","Z90.703","Z90.704","Z90.705","Z90.706","Z90.707","Z90.708","Z90.709","Z90.800x002","Z91.000","Z91.100","Z91.200","Z91.300","Z91.400x001","Z91.500x001","Z91.500x003","Z91.501","Z91.601","Z91.700","Z91.800x001","Z91.800x002","Z92.000x001","Z92.001","Z92.100","Z92.200","Z92.200x021","Z92.201","Z92.300x001","Z92.401","Z92.402","Z92.500","Z92.800x001","Z92.800x002","Z92.900","Z93.000","Z93.100","Z93.200","Z93.201","Z93.300","Z93.400","Z93.500","Z93.601","Z93.602","Z93.603","Z93.800","Z93.900","Z94.001","Z94.002","Z94.100","Z94.200","Z94.300x001","Z94.400","Z94.500","Z94.500x001","Z94.500x003","Z94.500x004","Z94.500x005","Z94.500x006","Z94.500x007","Z94.600","Z94.700","Z94.800x004","Z94.800x006","Z94.800x007","Z94.800x010","Z94.800x011","Z94.800x012","Z94.801","Z94.802","Z94.803","Z94.804","Z94.900","Z95.001","Z95.002","Z95.003","Z95.004","Z95.101","Z95.200x002","Z95.200x003","Z95.200x004","Z95.300x002","Z95.300x003","Z95.300x004","Z95.400","Z95.500x002","Z95.501","Z95.800x001","Z95.800x003","Z95.800x004","Z95.800x005","Z95.800x006","Z95.800x007","Z95.801","Z95.900","Z96.001","Z96.101","Z96.102","Z96.200x001","Z96.200x005","Z96.201","Z96.300","Z96.401","Z96.500","Z96.600x001","Z96.600x011","Z96.600x021","Z96.600x031","Z96.600x061","Z96.601","Z96.602","Z96.603","Z96.700","Z96.701","Z96.800","Z96.900","Z97.000x001","Z97.000x002","Z97.100x001","Z97.200x001","Z97.300x002","Z97.301","Z97.400","Z97.500x001","Z97.800","Z98.000x001","Z98.000x002","Z98.100","Z98.200x001","Z98.800x001","Z98.800x002","Z98.800x003","Z98.800x004","Z98.800x005","Z98.800x006","Z98.800x007","Z98.800x101","Z98.800x102","Z98.800x103","Z98.800x104","Z98.800x105","Z98.800x107","Z98.800x108","Z98.800x109","Z98.800x110","Z98.800x111","Z98.800x112","Z98.800x114","Z98.800x115","Z98.800x116","Z98.800x117","Z98.800x118","Z98.800x119","Z98.800x120","Z98.800x121","Z98.800x122","Z98.800x123","Z98.800x124","Z98.800x201","Z98.800x202","Z98.800x203","Z98.800x205","Z98.800x208","Z98.800x209","Z98.800x210","Z98.800x301","Z98.800x302","Z98.800x303","Z98.800x305","Z98.800x306","Z98.800x307","Z98.800x308","Z98.800x309","Z98.800x310","Z98.800x311","Z98.800x312","Z98.800x313","Z98.800x315","Z98.800x316","Z98.800x317","Z98.800x318","Z98.800x319","Z98.800x401","Z98.800x402","Z98.800x403","Z98.800x404","Z98.800x405","Z98.800x406","Z98.800x407","Z98.800x408","Z98.800x409","Z98.800x410","Z98.800x411","Z98.800x412","Z98.800x413","Z98.800x414","Z98.800x416","Z98.800x417","Z98.800x418","Z98.800x420","Z98.800x421","Z98.800x422","Z98.800x423","Z98.800x501","Z98.800x502","Z98.800x503","Z98.800x507","Z98.800x602","Z98.800x605","Z98.800x606","Z98.800x609","Z98.800x610","Z98.800x611","Z98.800x612","Z98.800x614","Z98.800x615","Z98.800x616","Z98.800x701","Z98.800x704","Z98.800x901","Z98.800x902","Z98.800x903","Z98.800x904","Z98.800x905","Z98.800x906","Z98.800x907","Z98.800x908","Z98.801","Z99.000","Z99.100x001","Z99.300","Z99.400","Z99.800","Z99.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合XT3入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XT39_group(record):
      return 'XT39'

    return 'XT3'
  else:
    return ''

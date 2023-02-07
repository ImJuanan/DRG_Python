from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=["B57.201+I98.1*","C38.000","C38.000x004","C38.001","C38.002","C45.200","C49.300x006","C49.402","C49.900x001","C75.400","C75.500x001","C79.800x807","C79.800x819","C79.800x830","C79.800x863","C79.808","D15.100","D15.101","D15.102","D15.103","D15.104","D15.105","D15.106","D18.000x001","D18.000x003","D18.000x004","D18.000x005","D18.000x822","D18.000x835","D18.000x836","D18.000x837","D18.000x840","D18.000x841","D18.010","D18.109","D20.000x002","D21.300x005","D21.400","D21.400x004","D35.600x001","D44.601","D44.700","D44.700x002","D44.701","D44.702","D44.703","D48.100x008","D48.100x024","D48.711","D48.712","E03.900x004+I43.8*","E05.900x004+I43.8*","E05.903+I43.8*","I02.900x001","I02.900x003","I09.900","I09.900x002","I25.300x006","I25.300x007","I25.300x008","I25.300x009","I25.300x010","I25.300x011","I25.300x012","I25.300x013","I25.301","I25.302","I26.001","I27.100","I27.900","I27.900x002","I28.100","I28.800x005","I28.800x007","I28.900x001","I51.000x001","I51.001","I51.301","I51.302","I51.303","I51.304","I51.402","I51.700","I51.700x003","I51.700x004","I51.700x006","I51.700x007","I51.700x009","I51.700x014","I51.700x015","I51.701","I51.702","I51.703","I51.704","I51.705","I51.706","I51.707","I51.708","I51.709","I51.800x004","I51.800x005","I51.800x006","I51.801","I51.900","I51.900x001","I51.900x002","I51.900x003","I51.901","I51.903","I74.800x004","I78.000","I78.102","I78.801","I78.803","I78.900","I89.001","I95.000","I95.200","I95.800x001","I95.900","I97.000","I97.001","I97.800x004","I97.800x005","I97.800x006","I97.800x008","I97.800x009","I97.800x010","I97.800x011","I97.800x013","I97.800x014","I97.800x015","I97.801","I97.900","I99.x01","J94.000","M05.304+I52.8*","M05.307+I39.8*","M10.004+I43.8*","M32.109+I39.8*","M34.800x009+I52.8*","N18.505+I68.8*","Q27.300x009","Q27.800x020","Q27.800x033","Q27.800x034","Q27.800x035","Q27.800x037","Q27.803","Q27.806","Q27.809","Q27.811","Q27.815","Q28.801","Q28.900","Q85.900x048","R01.000","R01.100","R01.200x003","R03.001","R03.100","R07.101","R07.200","R07.301","R07.400","R09.800x081","R09.800x082","R93.100x002","R93.101","R93.102","R93.103","R94.300","R94.300x007","R94.301","R94.303","R94.304","R94.305","R94.306","R94.307","S09.000x001","S15.000x002","S15.700x001","S25.400","S25.500","S25.700","S25.900","S26.800x011","S26.800x021","S26.800x031","S26.800x082","S26.800x083","S26.810","S26.811","S26.812","S26.813","S26.900","S26.910","S35.700x001","S35.700x004","S35.701","S35.900x001","S35.901","S35.902","S35.903","S45.700x001","S45.701","S45.800","S45.900x001","S55.700x001","S55.800","S55.900x001","S65.400","S65.500","S65.700x001","S65.800","S65.900x001","S75.700x001","S75.700x002","S75.800","S75.900x001","S75.900x002","S85.700x001","S85.800x001","S85.900x001","S95.700x001","S95.800","S95.900x001","T11.400","T13.400","T79.100","T79.101","T80.000","T80.000x001","T81.700x002","T81.700x003","T81.700x005","T81.700x102","T81.700x103","T81.700x202","T81.700x203","T81.700x301","T81.700x302","T81.700x402","T81.700x403","T81.703","T82.000x002","T82.002","T82.100","T82.100x002","T82.100x003","T82.100x005","T82.100x006","T82.100x007","T82.100x008","T82.100x009","T82.100x010","T82.100x011","T82.100x012","T82.100x013","T82.100x014","T82.100x015","T82.101","T82.102","T82.103","T82.300","T82.301","T82.302","T82.303","T82.400","T82.500x001","T82.500x002","T82.500x003","T82.500x003","T82.502","T82.503","T82.504","T82.600","T82.600x001","T82.601","T82.700","T82.704","T82.800x006","T82.800x008","T82.800x009","T82.800x101","T82.800x102","T82.800x103","T82.800x104","T82.800x105","T82.800x106","T82.800x202","T82.800x203","T82.800x301","T82.800x409","T82.800x410","T82.800x411","T82.811","T82.814","T82.900x001","T82.900x002","T82.901","T82.903","T82.904","T86.200x001","T86.200x002","T86.300x001","T86.300x002","Z03.400","Z03.500x001","Z03.501"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合FZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FZ11_group(record):
      return 'FZ11'

    if MDCF_DRG.FZ13_group(record):
      return 'FZ13'

    if MDCF_DRG.FZ15_group(record):
      return 'FZ15'

    return 'FZ1'
  else:
    return ''


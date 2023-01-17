from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.DRG import MDCB_DRG

def group(record):
  adrg_zd=["D18.000x023","D18.000x024","D18.000x025","D18.000x026","D18.000x027","D18.000x028","D18.002","E03.902+G73.5*","E05.900x007+G73.0*","E05.904+G73.5*","E06.302+G94.8*","E10.400x360+G99.0*","E11.400x360+G99.0*","E12.400","E12.400x001+G99.0*","E12.400x002+N33.8*","E14.400x360+G99.0*","E16.108+G94.8*","E16.111+G94.3*","E51.200+G32.8*","E63.900x001","E71.300x006","E75.600x002+G32.8*","E85.400x012","E85.414+I68.0*","F01.101","G04.100","G04.800","G09.x00","G09.x00x001","G09.x00x004","G09.x01","G24.300","G31.901","G31.902","G45.002","G45.004","G45.300","G45.901","G47.200","G47.200x002","G47.200x003","G47.400x002","G47.400x003","G47.401","G83.500","G83.900","G91.000","G91.000x003","G91.100","G91.100x002","G91.100x003","G91.200","G91.300","G91.301","G91.800x001","G91.800x003","G91.800x004","G91.800x006","G91.801","G91.802","G91.900","G92.x00","G92.x00x002","G92.x00x003","G92.x01","G92.x02","G93.000","G93.000x002","G93.000x006","G93.000x007","G93.000x009","G93.000x010","G93.000x011","G93.000x012","G93.000x013","G93.000x014","G93.000x015","G93.001","G93.002","G93.003","G93.004","G93.005","G93.100","G93.100x002","G93.101","G93.102","G93.200","G93.200x003","G93.200x004","G93.201","G93.300","G93.300x002","G93.301","G93.400","G93.400x001","G93.400x002","G93.400x004","G93.400x005","G93.400x006","G93.400x007","G93.400x008","G93.401","G93.402","G93.403","G93.404","G93.405","G93.500","G93.503","G93.504","G93.600","G93.600x002","G93.600x003","G93.600x004","G93.600x005","G93.600x006","G93.600x007","G93.600x008","G93.600x009","G93.700","G93.800x007","G93.800x009","G93.800x010","G93.800x012","G93.800x013","G93.801","G93.802","G93.803","G93.804","G93.805","G93.806","G93.807","G93.808","G93.809","G93.810","G93.811","G93.812","G93.814","G93.815","G93.900","G93.900x001","G93.901","G93.902","G93.903","G93.904","G95.808","G96.000","G96.000x005","G96.000x006","G96.001","G96.002","G96.003","G96.100","G96.100x001","G96.100x002","G96.100x003","G96.100x004","G96.100x005","G96.100x007","G96.100x008","G96.100x009","G96.100x010","G96.100x013","G96.101","G96.103","G96.104","G96.800x002","G96.800x003","G96.800x005","G96.800x007","G96.900","G96.900x002","G96.900x003","G96.900x004","G96.901","G96.902","G97.000","G97.100","G97.100x002","G97.200","G97.800x001","G97.800x002","G97.800x003","G97.800x004","G97.800x005","G97.800x006","G97.800x008","G97.800x009","G97.801","G97.802","G97.803","G97.900","G98.x00","G98.x00x001","G98.x00x002","H47.401","H47.600","H47.601","H47.700","I61.904","I63.301","I63.802","I64.x01","I65.000x005","I65.800x001","I65.800x002","I66.203","I66.205+G46.2*","I66.901","I67.200","I67.200","I67.200","I67.200","I67.201","I67.202","I67.400x001","I67.600x003","I67.700x001","I67.700x002","I67.800x003","I67.800x004","I67.803","I67.804","I67.805","I67.900","I67.900x004+G46.3*","I69.000x001","I69.000x002","I69.000x003","I69.100x001","I69.100x002","I69.100x003","I69.200x001","I69.300","I69.300x002","I69.300x003","I69.800x003","I72.600x002","I77.302","I86.800x010","M05.301+G63.6*","M32.107+G99.2*","M32.114+G94.8*","M35.008+G94.8*","N18.503+G63.8*","N18.507+G99.8*","Q00.000x001","Q06.300","Q07.900","Q27.800x025","Q75.000","Q75.001","Q75.800x902","Q85.806","Q85.900x052","Q87.800x301","R20.000","R20.100","R20.200x002","R20.200x003","R20.200x006","R20.201","R20.202","R20.300","R20.801","R20.802","R20.803","R25.000","R25.001","R25.100","R25.100x001","R25.100x002","R25.100x003","R25.300","R25.300x002","R25.800x001","R25.801","R25.802","R25.803","R26.000","R26.000x001","R26.200x001","R26.300","R26.301","R26.800x001","R26.802","R27.800x001","R27.800x002","R27.801","R29.200","R29.300","R29.600","R29.800","R29.800x502","R29.800x503","R29.800x504","R29.800x505","R29.800x507","R29.800x508","R29.802","R29.803","R40.000","R40.200x005","R42.x00x001","R42.x00x002","R42.x00x004","R43.000","R43.100","R43.200","R43.800x001","R43.800x003","R43.800x004","R56.000","R83.000","R83.100","R83.200","R83.300","R83.400","R83.500","R83.600","R83.700","R83.800","R83.900","R83.900","R90.000x003","R90.800x003","R90.801","R90.803","R90.804","R90.805","R90.807","R93.000x001","R93.000x002","R94.000","R94.001","R94.102","R94.103","R94.104","T70.203","T79.100x002","T79.801","T80.600x007","T80.600x008","T80.600x009","T85.000","T85.001","T85.002","T85.003","T85.100","T85.100x001","T85.100x002","T85.100x004","T85.807","T90.500","T90.501","T90.502","Z42.000x011","Z42.001","Z46.200x001","Z46.200x002","Z46.201","Z46.202"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合BZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BZ11_group(record):
      return 'BZ11'

    if MDCB_DRG.BZ13_group(record):
      return 'BZ13'

    if MDCB_DRG.BZ15_group(record):
      return 'BZ15'

    return 'BZ1'
  else:
    return ''


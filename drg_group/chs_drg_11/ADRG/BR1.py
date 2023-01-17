from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.DRG import MDCB_DRG

def group(record):
  adrg_zd=["G91.000x002","I60.000","I60.000x001","I60.000x002","I60.000x003","I60.000x004","I60.000x006","I60.000x007","I60.000x008","I60.001","I60.100","I60.101","I60.200","I60.200x002","I60.200x003","I60.200x004","I60.200x005","I60.200x007","I60.201","I60.300","I60.301","I60.400","I60.400x002","I60.400x003","I60.400x004","I60.401","I60.500x003","I60.500x004","I60.600x001","I60.600x003","I60.600x004","I60.600x005","I60.600x006","I60.600x007","I60.600x008","I60.601","I60.602","I60.700x001","I60.701","I60.800x002","I60.800x003","I60.800x004","I60.800x005","I60.800x006","I60.800x008","I60.800x010","I60.800x013","I60.800x014","I60.800x015","I60.801","I60.802","I60.900x004","I60.900x005","I60.900x006","I60.902+H45.0*","I61.000x006","I61.000x007","I61.000x008","I61.000x009","I61.000x011","I61.001","I61.002","I61.003","I61.004","I61.005","I61.006","I61.100x001","I61.100x002","I61.100x003","I61.100x004","I61.100x005","I61.100x006","I61.100x007","I61.100x008","I61.100x009","I61.100x010","I61.100x011","I61.100x012","I61.100x013","I61.100x014","I61.101","I61.200x001","I61.300x002","I61.300x003","I61.300x004","I61.301","I61.400x001","I61.400x002","I61.400x003","I61.500x002","I61.500x003","I61.500x004","I61.500x005","I61.500x006","I61.500x007","I61.500x008","I61.600x001","I61.800x001","I61.801","I61.802","I61.803","I61.900x002","I61.900x004","I61.900x005","I61.900x006","I61.900x007","I61.900x008","I61.901","I61.902","I61.903","I61.905","I62.000","I62.000","I62.000x005","I62.001","I62.003","I62.003","I62.100","I62.100x001","I62.100x003","I62.100x004","I62.101","I62.900x001","I67.100x001","I67.100x005","I67.100x007","I67.100x008","I67.100x010","I67.100x011","I67.100x012","I67.100x013","I67.100x017","I67.100x018","I67.100x019","I67.100x020","I67.100x021","I67.100x023","I67.100x026","I67.100x029","I67.100x030","I67.100x032","I67.100x033","I67.101","I67.103","I67.106","I67.107","I67.108","I67.109","I67.110","I67.111","I72.000x034","I72.000x035","I72.000x036","I72.000x038","I72.500x001","I72.500x001","I72.500x002","I72.600x002","S06.811","S06.812","S06.813"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合BR1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BR11_group(record):
      return 'BR11'

    if MDCB_DRG.BR15_group(record):
      return 'BR15'

    return 'BR1'
  else:
    return ''


import urllib.request,urllib.parse,pathlib,json,hashlib,concurrent.futures,io,xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
root=pathlib.Path(__file__).parent
base='https://raw.githubusercontent.com/KalyssonRyan/Clone-Ifood/7f8c3b8781d8853f3f07f6ba52541ef95d65357b/fonts/'
files=[f'iFoodRC{family}-{weight}.woff2' for family in ['Textos','Titulos'] for weight in ['Regular','Medium','Bold','Light']]
def get(name):
 url=base+name
 try:
  r=urllib.request.urlopen(url,timeout=25);b=r.read();font=TTFont(io.BytesIO(b),checkChecksums=2);font.ensureDecompiled();names={}
  for i in [0,1,2,3,4,5,6,8,9,13,14,16,17]:
   vals=sorted(set(x.toUnicode() for x in font['name'].names if x.nameID==i));
   if vals:names[str(i)]=vals
  cmap=font.getBestCmap();rec={'file':name,'source_kind':'public GitHub mirror; not official CDN','url':url,'status':r.status,'size':len(b),'sha256':hashlib.sha256(b).hexdigest(),'flavor':font.flavor,'names':names,'glyph_count':font['maxp'].numGlyphs,'weight_class':font['OS/2'].usWeightClass,'embedding_fsType':font['OS/2'].fsType,'unitsPerEm':font['head'].unitsPerEm,'portuguese_chars':{c:ord(c) in cmap for c in 'áéíóúâêôãõçÁÉÍÓÚÂÊÔÃÕÇ'},'tables':font.keys(),'license_status':'No reuse license established by this download; internal copyright retained.'};(root/name).write_bytes(b);return rec
 except Exception as e:return {'file':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:rows=list(p.map(get,files))
(root/'font-validation.json').write_text(json.dumps(rows,indent=2));print(json.dumps([{k:v for k,v in r.items() if k in ['file','size','flavor','glyph_count','weight_class','error','names']} for r in rows],indent=2))
url='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','titles':'File:IFood logo.svg','prop':'imageinfo','iiprop':'url|extmetadata','format':'json'})
try:
 j=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ReferenceAssetResearch/1.0'}),timeout=25));(root/'logo-wikimedia-metadata.json').write_text(json.dumps(j,indent=2));p=next(iter(j['query']['pages'].values()));info=p['imageinfo'][0];u=info['url'];r=urllib.request.urlopen(u,timeout=25);b=r.read();xml=ET.fromstring(b);assert xml.tag.endswith('svg');assert not any(e.tag.split('}')[-1] in ['script','foreignObject'] for e in xml.iter());(root/'ifood-wordmark.svg').write_bytes(b);(root/'logo-provenance.json').write_text(json.dumps({'file':'ifood-wordmark.svg','url':u,'page':info['descriptionurl'],'sha256':hashlib.sha256(b).hexdigest(),'size':len(b),'viewBox':xml.get('viewBox'),'license_description':'Wikimedia page marks PD-textlogo, trademark restrictions separately noted; not an official-host download.'},indent=2));print('LOGO saved',len(b),xml.get('viewBox'))
except Exception as e:print('LOGO ERROR',e)

import urllib.request,pathlib,json,hashlib,concurrent.futures,io
from PIL import Image
root=pathlib.Path(__file__).parent
urls=[('restaurant.png','https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/restaurant.png'),('market.png','https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/market.png'),('drinks.png','https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/drinks.png'),('pharmacy.png','https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/pharmacy.png'),('petshop.png','https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/petshop.png'),('ifood-culture-2025.pdf','https://carreiras-cdn.ifood.com.br/assets/2025/12/DECK-DE-CULTURA-IFOOD_2025.pdf'),('designer-ifood-20.png','https://fabiohaagtype.com/wp-content/uploads/2023/05/iFood-20.png')]
def run(x):
 name,url=x
 try:
  r=urllib.request.urlopen(url,timeout=30);b=r.read();rec={'file':name,'url':url,'status':r.status,'size':len(b),'sha256':hashlib.sha256(b).hexdigest(),'content_type':r.headers.get('Content-Type')}
  if name.endswith('.pdf'):assert b.startswith(b'%PDF')
  else:
   im=Image.open(io.BytesIO(b));rec['dimensions']=im.size;rec['format']=im.format;im.verify()
  (root/name).write_bytes(b);return rec
 except Exception as e:return {'file':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:res=list(p.map(run,urls))
(root/'asset-provenance.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))

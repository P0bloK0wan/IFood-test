import urllib.request,pathlib,json,hashlib,concurrent.futures
root=pathlib.Path('/workspace/app-reconstruction/references/ifood');folder=root/'screenshots';folder.mkdir(exist_ok=True)
ids=['X0Tk4Rl8Vl895Na25SQBZCa6jEGqoecnulmShaDsSA0ScKjyPNTm2OIURScuIMQm34ivDfLGY_uvwaUNHogMcQ','v8sBtPpTmV-PHaTYM4jlQ6wRIVw5Bjro1L_g8Fqarew720J8i_g2TWh4Tv4Xl5C1WMifG70DjzYL9tc3l0QX8g','mGMAuY_KZt4QiXN9jrUgYHf5zEF0BcRizRDFWzW5Vs9qe_iON-fVXrqgfZ4_xPq-7sZ_lUsuFewKLc9C8Meb4vM','D1VPal_IItmOP7nj2oHlfZvIq_KZjfcECkKhiPJgnubo4WYN3o4-DwNYKTBa3ijeeKT3uIUzJ5jMyHCeClCJkaM']
def get(t):
 n,id=t;url='https://play-lh.googleusercontent.com/'+id+'=w1080';r=urllib.request.urlopen(url,timeout=30);b=r.read();path=folder/f'play-store-{n+1}.png';path.write_bytes(b);return {'file':str(path.relative_to(root)),'url':url,'parent':'https://play.google.com/store/apps/details?gl=BR&id=br.com.brainweb.ifood','sha256':hashlib.sha256(b).hexdigest(),'content_type':r.headers.get('Content-Type')}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:res=list(p.map(get,enumerate(ids)))
(root/'screenshot-sources.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))

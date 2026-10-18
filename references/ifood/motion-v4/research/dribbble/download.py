import re,pathlib,html,json,urllib.request,hashlib,subprocess,concurrent.futures,io
from PIL import Image
root=pathlib.Path(__file__).parent
source=root.parents[1]/'courier/ifood-design.html'
s=source.read_text()
items=[('7637059','restaurant-rating'),('6749537','home-main-covers'),('6666774','order-manager-concept'),('6631314','tab-bar'),('9894657','delivery-app'),('7863300','loop-onboarding')]
def get(pair):
 id,name=pair;e=re.search(r'<li\b[^>]*id="screenshot-'+id+r'"[\s\S]*?</li>',s).group(0);page='https://dribbble.com'+re.search(r'href="(/shots/[^\"]+)"',e).group(1)
 m=re.search('data-video-teaser-large="([^"]+)"',e);m=m or re.search('data-animated-url="([^"]+)"',e);m=m or re.search('<noscript>\s*<img src="([^"]+)"',e);url=html.unescape(m.group(1));ext=url.split('?')[0].rsplit('.',1)[1];file=name+'.'+ext;row={'id':id,'title':name,'source_profile':'https://dribbble.com/ifooddesign','source_page':page,'media_url':url,'discovered_in':str(source),'file':file,'classification':'official design-team portfolio rendition; not native source or evidence of current shipped UI','license':'No separate reuse license established'}
 try:
  r=urllib.request.urlopen(url,timeout=30);b=r.read();(root/file).write_bytes(b);row.update(size=len(b),sha256=hashlib.sha256(b).hexdigest(),status=r.status)
  if ext=='mp4':
   probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(root/file)]));row['probe']=probe;(root/(name+'-ffprobe.json')).write_text(json.dumps(probe,indent=2));duration=float(probe['format']['duration'])
   for n,t in enumerate([0,duration/3,2*duration/3]):subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(t),'-i',str(root/file),'-frames:v','1',str(root/f'{name}-frame-{n}.jpg')],check=True)
  else:
   im=Image.open(io.BytesIO(b));dur=[]
   for n in range(getattr(im,'n_frames',1)):im.seek(n);dur.append(im.info.get('duration',0))
   row['image']={'format':im.format,'size':im.size,'frames':getattr(im,'n_frames',1),'duration_ms':sum(dur),'frame_durations_ms':sorted(set(dur))}
   for n,k in enumerate([0,getattr(im,'n_frames',1)//3,2*getattr(im,'n_frames',1)//3]):im.seek(k);im.convert('RGB').save(root/f'{name}-frame-{n}.jpg')
 except Exception as ex:row['error']=str(ex)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(get,items))
(root/'manifest.json').write_text(json.dumps(rows,indent=2));print(json.dumps([{k:v for k,v in r.items() if k not in ['probe']} for r in rows],indent=2))

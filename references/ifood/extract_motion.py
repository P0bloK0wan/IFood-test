import zipfile,pathlib,json,io,hashlib,collections
root=pathlib.Path('/workspace/app-reconstruction/references/ifood');assets=root/'assets';z=zipfile.ZipFile('/workspace/app-reconstruction/recovered/ifood-partial-recovered.apk');records=[]
def walk(v,c):
 if isinstance(v,dict):
  if isinstance(v.get('ty'),str):c['shape_types'][v['ty']]+=1
  if v.get('a')==1 and isinstance(v.get('k'),list):
   for k in v['k']:
    if isinstance(k,dict) and 't' in k:c['keyframe_times'].add(k['t'])
  if 'ef' in v:c['effect_groups']+=1
  for x in v.values():walk(x,c)
 elif isinstance(v,list):
  for x in v:walk(x,c)
for name in z.namelist():
 if not (name.startswith('assets/') and name.endswith(('.lottie','.json'))) or 'FaceTec' in name:continue
 data=z.read(name);target=assets/pathlib.PurePosixPath(name).name;target.write_bytes(data)
 sub=[]
 if name.endswith('.lottie'):
  arc=zipfile.ZipFile(io.BytesIO(data));dest=assets/target.stem;dest.mkdir(exist_ok=True)
  for member in arc.namelist():
   p=pathlib.PurePosixPath(member)
   if p.is_absolute() or '..' in p.parts:raise ValueError('unsafe path')
   f=dest/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(arc.read(member))
   if member.startswith('animations/') and member.endswith('.json'):sub.append((str(f.relative_to(root)),json.loads(arc.read(member))))
 else:
  try:j=json.loads(data)
  except:continue
  if 'fr' in j:sub.append((str(target.relative_to(root)),j))
 for output,j in sub:
  c={'shape_types':collections.Counter(),'keyframe_times':set(),'effect_groups':0};walk(j,c)
  records.append({'original_apk_member':name,'source_member_sha256':hashlib.sha256(data).hexdigest(),'json_file':output,'lottie_version':j.get('v'),'name':j.get('nm'),'width':j.get('w'),'height':j.get('h'),'fps':j.get('fr'),'in_frame':j.get('ip'),'out_frame':j.get('op'),'duration_seconds':(j['op']-j['ip'])/j['fr'],'top_level_layers':[{'name':l.get('nm'),'type':l.get('ty'),'in':l.get('ip'),'out':l.get('op')} for l in j.get('layers',[])],'asset_count':len(j.get('assets',[])),'external_image_assets':[a for a in j.get('assets',[]) if 'p' in a],'shape_types':dict(c['shape_types']),'keyframe_count_unique_times':len(c['keyframe_times']),'effect_groups':c['effect_groups'],'markers':j.get('markers',[])})
(root/'motion-inventory.json').write_text(json.dumps(records,indent=2));print(json.dumps([{k:r[k] for k in ['json_file','fps','duration_seconds','width','height','shape_types']} for r in records],indent=2))

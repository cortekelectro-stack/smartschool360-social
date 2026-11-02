import os,json
exec(open('gen.py').read().split('P={}')[0])
P={}
P['post-5-brass-bell']=[cover_photo(1,1,'bell.jpg','Who rings your bell?','The old way','Still ringing it<br><span>by hand?</span>','A peon, a rope and a wristwatch. <b>Smart School 360 rings every bell on time</b>, plays prayers and announcements, and never takes a day off.',pos='center 30%')]
P['post-6-teacher-time']=[cover_photo(1,1,'teacher.jpg','For teachers','Class time is teaching time','<style>.ph:after{background:linear-gradient(180deg,rgba(11,9,7,.6) 0%,rgba(11,9,7,0) 22%,rgba(11,9,7,0) 72%,#0B0907 100%)!important}</style>Just teach.<br><span>The bell is sorted.</span>','No watching the clock, no sending a student to ring the bell. <b>Every period starts and ends on time</b>, automatically.',h=800,tagtop=790,copytop=860,size=124,pos='center 75%')]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

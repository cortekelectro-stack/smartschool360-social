import os,json
exec(open('gen3.py').read().split('P={}')[0])
P={}
W='smartschool360.co.in'
def ph1(img,pos,kick,title,sub):
    return pg(f'<div class=abs style="inset:0;background:url({img}) {pos}/cover"></div><div class=abs style="left:0;right:0;bottom:0;height:760px;background:linear-gradient(180deg,rgba(11,12,10,0),rgba(11,12,10,.92) 62%)"></div><div class=abs style="left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(11,12,10,.55),rgba(11,12,10,0))"></div>'
      +hd('Smart School 360','color:#F4F3EE')+f'<div class="abs m" style="left:80px;top:860px;color:var(--lime)">{kick}</div><div class=abs style="left:80px;right:80px;top:905px;font:900 100px/0.95 Inter Tight;letter-spacing:-4px;color:#fff">{title}</div><div class=abs style="left:80px;right:180px;top:1110px;font:500 30px/1.4 Inter Tight;color:#D6D7D0">{sub}</div>'
      +ft('Free online demo',W,'color:#BFC0B9'),'dark')
P['l5-brass-bell']=[pg('<div class=abs style="left:0;right:0;top:0;height:860px;background:url(bell-crop.jpg) center top/cover"></div><div class=abs style="left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(11,12,10,.6),rgba(11,12,10,0))"></div>'
 +hd('Smart School 360','color:#F4F3EE')+'<div class="abs m" style="left:80px;top:920px;color:var(--lime)">Who rings your bell?</div><div class=abs style="left:80px;right:80px;top:965px;font:900 100px/0.95 Inter Tight;letter-spacing:-4px;color:#fff">Still rung by hand?</div><div class=abs style="left:80px;right:180px;top:1100px;font:500 30px/1.4 Inter Tight;color:#D6D7D0">Smart School 360 rings every period on time, automatically.</div>'
 +ft('Free online demo',W,'color:#BFC0B9'),'dark',bg='background:#0B0C0A')]
P['l6-teacher-time']=[pg('<div class=abs style="left:0;right:0;top:0;height:800px;background:url(teacher.jpg) center 75%/cover"></div><div class=abs style="left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(11,12,10,.6),rgba(11,12,10,0))"></div>'
 +hd('Smart School 360','color:#F4F3EE')+'<div class="abs m" style="left:80px;top:870px;color:var(--lime)">Class time is teaching time</div><div class=abs style="left:80px;right:80px;top:915px;font:900 100px/0.95 Inter Tight;letter-spacing:-4px;color:#fff">Teach. The bell<br>is handled.</div><div class=abs style="left:80px;right:180px;top:1130px;font:500 30px/1.4 Inter Tight;color:#D6D7D0">No clock-watching. Every period starts and ends on time.</div>'
 +ft('Free online demo',W,'color:#BFC0B9'),'dark',bg='background:#0B0C0A')]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post'; open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

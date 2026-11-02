import json
H='<html><head><meta charset=utf-8><link rel=stylesheet href=base.css></head>'
def hd(r='Smart School 360',col=''): return f'<div class="hd m" style="top:240px;{col}"><span class=lg><img src=logo.png>Cortek Electro</span><span>{r}</span></div>'
def pg(b,cls='',bg=''): return H+f'<body class="{cls}" style="{bg}">{b}</body></html>'
S={}
S['story-1-every-bell']=pg(hd(col='color:#F4F3EE')+
 '<div class="abs m" style="left:80px;top:420px;color:var(--lime)">With Smart School 360</div>'
 '<div class=abs style="left:62px;top:470px;font:900 330px/0.9 Inter Tight;letter-spacing:-18px;color:var(--lime)">11:00</div>'
 '<div class=abs style="left:80px;top:800px;font:900 112px/0.95 Inter Tight;letter-spacing:-5px;color:#F4F3EE">Every bell.<br>Every day.</div>'
 '<div class=abs style="left:80px;right:80px;top:1040px;font:500 38px/1.35 Inter Tight;color:#A9AAA3">Set the timetable once. It rings every bell, prayer and announcement on its own.</div>'
 '<div class=abs style="left:0;right:0;top:1230px;bottom:0;background:#fff url(photo.png) center 40%/820px auto no-repeat"></div>','dark')
S['story-2-runs-the-day']=pg(hd()+
 '<div class=abs style="left:80px;right:80px;top:420px;text-align:center;font:900 130px/0.92 Inter Tight;letter-spacing:-6px">Runs the day.<br><span style="color:#B9BAB3">On its own.</span></div>'
 '<img src=photo.png class=abs style="left:60px;top:760px;width:960px;-webkit-mask-image:linear-gradient(180deg,transparent 0,#000 12%)">'
 '<div class="abs m" style="left:80px;right:80px;top:1430px;text-align:center;font-size:22px">Bells · Prayers · Announcements · Siren</div>'
 '<div class=abs style="left:80px;right:80px;top:1490px;text-align:center;font:500 34px Inter Tight;color:var(--mute)">With battery backup, so it keeps going in a power cut.</div>','',
 'background:#fff')
S['story-3-cares-daily']=pg('<div class=abs style="inset:0;background:url(knobs.png) center 30%/cover"></div>'
 '<div class=abs style="left:0;right:0;bottom:0;height:1200px;background:linear-gradient(180deg,rgba(11,12,10,0),rgba(11,12,10,.95) 50%)"></div>'+hd(col='color:#F4F3EE')+
 '<div class=abs style="left:80px;right:80px;top:1060px;font:900 128px/0.92 Inter Tight;letter-spacing:-6px;color:#F4F3EE">Set it once.<br><span style="color:var(--lime)">It cares daily.</span></div>'
 '<div class=abs style="left:80px;right:80px;top:1340px;font:500 36px/1.35 Inter Tight;color:#C9CAC3">Prayer, anthem, water bell and calm audio, each at its own time.</div>'
 '<div class=abs style="left:80px;top:1480px"><span class=btn>Book a free online demo</span></div>')
col=lambda m,a,z,on: f'<div style="text-align:center;padding:40px 16px 44px;border-radius:28px;{"background:var(--ink);color:#fff" if on else "background:#F4F3EE"}"><div style="font:900 104px Inter Tight;letter-spacing:-4px;{"color:var(--lime)" if on else ""}">{m}</div><div style="font:700 32px Inter Tight;margin-top:6px">{a}</div><div style="font:500 28px Inter Tight;margin-top:10px;color:{"#A9AAA3" if on else "var(--mute)"}">{z}</div>{"<div class=m style=\"margin-top:18px;font-size:15px;color:var(--lime)\">Most popular</div>" if on else ""}</div>'
S['story-4-models']=pg(hd()+
 '<div class=abs style="left:80px;right:80px;top:400px;text-align:center;font:900 124px/0.95 Inter Tight;letter-spacing:-6px">A model for<br>every campus.</div>'
 '<img src=photo.png class=abs style="left:110px;top:680px;width:860px;-webkit-mask-image:linear-gradient(180deg,transparent 0,#000 14%)">'
 '<div class=abs style="left:80px;right:80px;top:1200px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;align-items:end">'+col('Z2','Small schools','2 zones',0)+col('Z4','Most schools','4 zones',1)+col('Z5','Large campuses','5 zones',0)+'</div>'
 '<div class=abs style="left:80px;right:80px;top:1580px;text-align:center;font:500 30px Inter Tight;color:var(--mute)">Same touchscreen, siren and battery backup in every model.</div>','','background:#fff')
for k,v in S.items(): open(k+'.html','w').write(v)
json.dump(list(S),open('list.json','w'))

import os,json
exec(open('gen3.py').read().split('P={}')[0])
P={}
W='smartschool360.co.in'
# L1 Swiss typographic: exam modes
row=lambda k,t,d,on: f'<div style="display:flex;align-items:center;gap:40px;padding:22px 40px;border-top:3px solid var(--ink);{"background:var(--ink);color:#F4F3EE" if on else ""}"><div style="font:900 120px/0.85 Inter Tight;letter-spacing:-6px;width:260px;{"color:var(--lime)" if on else ""}">{k}</div><div><div style="font:800 46px Inter Tight;letter-spacing:-1px">{t}</div><div style="font:500 28px Inter Tight;margin-top:8px;color:{"#A9AAA3" if on else "var(--mute)"}">{d}</div></div></div>'
P['l1-exam-modes']=[pg(hd()+'<div class=abs style="left:80px;right:80px;top:200px;font:900 104px/0.95 Inter Tight;letter-spacing:-5px">Exam week.<br>One tap.</div>'
 +'<div class=abs style="left:80px;right:80px;top:470px">'+row('A0','Regular school','Your everyday timetable.',0)+row('A1','Examination','Adjusted bell times for exam days.',1)+row('A2','Vacation or special','Holidays, Saturday lessons, events.',0)+'<div style="border-top:3px solid var(--ink)"></div></div>'
 +'<div class=abs style="left:80px;right:80px;top:1110px;font:500 30px/1.4 Inter Tight;color:var(--mute)">Program all three at the start of term. Switch on exam morning.<br>No reprogramming.</div>'
 +ft('Free online demo',W,'color:var(--mute)'),bg='background:var(--paper)')]
# L2 Apple minimal: Silent mode
P['l2-silent-mode']=[pg(hd()+'<div class=abs style="left:0;right:0;top:230px;text-align:center;font:900 300px/0.9 Inter Tight;letter-spacing:-16px">Shh.</div>'
 +'<div class=abs style="left:140px;right:140px;top:560px;text-align:center;font:600 44px/1.25 Inter Tight;letter-spacing:-1px">Silent mode pauses every<br>scheduled bell. One tap.</div>'
 +'<img src=main-screen.png class=abs style="left:240px;top:760px;width:600px">'
 +'<div class=abs style="left:432px;top:793px;width:96px;height:96px;border-radius:50%;border:6px solid var(--lime)"></div>'
 +'<div class="abs m" style="left:80px;right:80px;top:1215px;text-align:center;color:var(--mute);font-size:17px">VIP visits · Assemblies · Prayer sessions</div>',bg='background:#fff')]
# L3 Day board: weekday prayers
days=[('MON','07:30','MORNING PRAYER'),('TUE','07:30','NATIONAL ANTHEM'),('WED','07:30','SCHOOL PRAYER'),('THU','07:30','PLEDGE'),('FRI','07:30','SCHOOL SONG'),('SAT','07:30','CALM AUDIO')]
cell=lambda t,w,c='#F4F3EE': f'<span style="display:inline-block;width:{w}px;font:700 34px Roboto Mono;color:{c};letter-spacing:2px">{t}</span>'
rows=''.join(f'<div style="padding:22px 34px;border-top:2px solid #23251F">{cell(d,130,"var(--lime)")}{cell(t,160)}{cell(a,520)}</div>' for d,t,a in days)
P['l3-weekday-prayers']=[pg(hd()+'<div class=abs style="left:80px;right:80px;top:190px;font:900 100px/0.95 Inter Tight;letter-spacing:-5px">Same time.<br>Different prayer.</div>'
 +f'<div class=abs style="left:80px;right:80px;top:470px;background:var(--ink);border-radius:28px;overflow:hidden"><div class=m style="padding:26px 34px;color:#8D8F87;font-size:16px">DAY &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TIME &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AUDIO</div>{rows}</div>'
 +'<div class=abs style="left:80px;right:80px;top:1150px;font:500 30px/1.4 Inter Tight;color:var(--ink)">Set each day once. It plays on its own, every week.</div>'
 +ft('Example timetable',W,'color:var(--ink)'),bg='background:var(--lime)')]
# L4 data editorial: zone volume
zs=[('Zone 1','Classrooms',60),('Zone 2','Office',35),('Zone 3','Playground',95),('Zone 4','Library',15),('Zone 5','Corridors',50)]
bars=''.join(f'<div style="display:flex;align-items:center;gap:24px;padding:20px 0;border-top:2px solid #E6E5DF"><div style="width:250px"><div class=m style="font-size:15px;color:var(--mute)">{z}</div><div style="font:800 38px Inter Tight;letter-spacing:-1px">{n}</div></div><div style="flex:1;height:22px;background:#EEEDE7;border-radius:11px"><div style="width:{v}%;height:22px;background:var(--ink);border-radius:11px"></div></div><div class=m style="width:70px;text-align:right;font-size:20px">{v}%</div></div>' for z,n,v in zs)
P['l4-zone-volume']=[pg(hd()+'<div class=abs style="left:80px;right:500px;top:200px;font:900 92px/0.95 Inter Tight;letter-spacing:-4px">Every zone.<br>Its own volume.</div>'
 +'<img src=zone-selection.png class=abs style="right:70px;top:190px;width:400px">'
 +f'<div class=abs style="left:80px;right:80px;top:520px">{bars}</div>'
 +'<div class=abs style="left:80px;right:80px;top:1150px;font:500 28px/1.4 Inter Tight;color:var(--mute)">Loud on the ground, soft near the library. Example levels; up to 5 zones depending on model.</div>'
 +ft('Free online demo',W,'color:var(--mute)'),bg='background:#fff')]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post'; open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

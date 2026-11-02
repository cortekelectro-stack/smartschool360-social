import os,json
exec(open('gen3.py').read().split('P={}')[0])
P={}
W='smartschool360.co.in'
# L1 Swiss typographic: exam modes
row=lambda k,t,d,on: f'<div style="display:flex;align-items:center;gap:40px;padding:22px 40px;border-top:3px solid var(--ink);{"background:var(--ink);color:#F4F3EE" if on else ""}"><div style="font:900 96px/0.85 Inter Tight;letter-spacing:-4px;width:200px;{"color:var(--lime)" if on else ""}">{k}</div><div><div style="font:800 46px Inter Tight;letter-spacing:-1px">{t}</div><div style="font:500 28px Inter Tight;margin-top:8px;color:{"#A9AAA3" if on else "var(--mute)"}">{d}</div></div></div>'
P['l7-naac']=[pg(hd()+'<div class=abs style="left:80px;right:80px;top:190px;font:900 100px/0.95 Inter Tight;letter-spacing:-5px">NAAC visit<br>coming up?</div>'
 +'<div class=abs style="left:80px;right:80px;top:420px;font:500 32px/1.35 Inter Tight;color:var(--mute)">Evidence assessors can see, from one installation.</div>'
 +'<div class=abs style="left:80px;right:80px;top:540px">'+row('C2','Teaching-learning','Every period on time. Prayer and anthem automated.',0)+row('C4','Infrastructure','Campus PA, zone audio, emergency siren.',1)+row('C6','Governance','ICT-based scheduling, internet time sync.',0)+row('C7','Best practices','Water bell, siren drills, punctuality.',0)+'<div style="border-top:3px solid var(--ink)"></div></div>'
 +ft('Free online demo',W,'color:var(--mute)'),bg='background:var(--paper)')]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post'; open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

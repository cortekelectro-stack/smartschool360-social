import os,json
exec(open('gen3.py').read().split('P={}')[0])
P={}
W='smartschool360.co.in'
# ---------- 9 Nov: A day in sound (Swiss timeline, no photos) ----------
rows=[('07:40','Morning prayer','Before assembly, every day.'),('08:00','Anthem and pledge','On time, without anyone pressing play.'),('10:15','Water bell','A reminder to drink water between periods.'),('14:00','Calm audio','Settles a class after lunch.')]
def tl(active=None):
    out=''
    for i,(t,a,b) in enumerate(rows):
        on = active is None or active==i
        out+=f'<div style="display:grid;grid-template-columns:230px 60px 1fr;align-items:start;padding:30px 0;opacity:{1 if on else .28}"><div style="font:900 64px/1 Inter Tight;letter-spacing:-2.5px">{t}</div><div style="padding-top:16px"><div style="width:26px;height:26px;border-radius:50%;background:{"var(--lime)" if on else "#C9C8C1"};box-shadow:0 0 0 8px {"rgba(163,207,68,.25)" if on else "transparent"}"></div></div><div><div style="font:800 46px/1.05 Inter Tight;letter-spacing:-1.5px">{a}</div><div style="font:500 28px/1.35 Inter Tight;color:var(--mute);margin-top:10px">{b}</div></div></div>'
    return f'<div class=abs style="left:80px;right:80px;top:560px"><div class=abs style="left:241px;top:60px;bottom:60px;width:3px;background:#D9D8D1"></div><div style="position:relative">{out}</div></div>'
P['p4-more-than-a-bell']=[
 pg(hd()+'<div class="abs m" style="left:80px;top:230px;color:var(--mute)">A day in sound</div><div class=abs style="left:80px;right:80px;top:280px;font:900 120px/0.92 Inter Tight;letter-spacing:-5.5px">A bell that<br>cares, <span style="color:var(--lime)">too.</span></div>'+tl()+ft(W,'Swipe →','color:var(--mute)'),bg='background:var(--paper)'),
 pg(hd()+'<div class=abs style="left:80px;top:250px;font:400 260px/0.7 Fraunces;color:var(--lime)">“</div><div class=abs style="left:80px;right:80px;top:400px;font:500 100px/1.05 Fraunces;letter-spacing:-1.5px">The water bell concept is very suitable for students.</div>'
   +'<div class="abs m" style="left:80px;top:880px;color:var(--mute)">Bhairavnath Vidyalaya, Donde, Khed</div>'
   +'<div class=abs style="left:80px;right:80px;top:1010px;font:500 30px/1.4 Inter Tight;color:var(--mute)">Schools can also add their own audio and Marathi voice-overs. Audio features vary by model.</div>'
   +ft(W,'02 / 03','color:var(--mute)'),bg='background:#fff'),
 pg(hd(col='color:#F4F3EE')+'<div class=abs style="left:80px;right:80px;top:250px;font:900 120px/0.92 Inter Tight;letter-spacing:-5px">Set it once.<br><span style="color:var(--lime)">It cares daily.</span></div>'
   +'<div class=abs style="left:-40px;top:400px;width:1160px;height:700px;background:radial-gradient(closest-side,rgba(244,243,238,.24),rgba(244,243,238,.07) 55%,rgba(244,243,238,0) 100%)"></div>'+'<img src=product-clean.png class=abs style="left:110px;top:560px;width:860px;filter:drop-shadow(0 40px 34px rgba(0,0,0,.6))">'
   +'<div class=abs style="left:80px;top:1020px"><span class=btn>Book a free online demo <span>→</span></span></div>'
   +ft('WhatsApp 98349 75938','03 / 03','color:#A9AAA3'),'dark')]
# ---------- 13 Nov: Swiss self-check ----------
items=['Sets its own clock','Manual override','Password lock','Live announcements','Separate speaker zones','Runs through power cuts']
box=lambda on:f'<div style="width:54px;height:54px;border:4px solid var(--ink);border-radius:10px;display:flex;align-items:center;justify-content:center;background:{"var(--lime)" if on else "transparent"};border-color:{"var(--lime)" if on else "var(--ink)"}">{"<svg width=30 height=30 viewBox=\"0 0 24 24\"><path d=\"M4 12l5 5L20 6\" stroke=\"#0B0C0A\" stroke-width=\"3.4\" fill=\"none\"/></svg>" if on else ""}</div>'
def checklist(on):
    return '<div class=abs style="left:80px;right:80px;top:560px;display:grid;grid-template-columns:1fr 1fr;column-gap:40px">'+''.join(f'<div style="display:flex;gap:26px;align-items:center;padding:50px 0;border-top:3px solid var(--ink)"><div>{box(on)}</div><div><div class=m style="color:var(--mute);font-size:16px">{i+1:02d}</div><div style="font:800 42px/1.1 Inter Tight;letter-spacing:-1px;margin-top:6px">{t}</div></div></div>' for i,t in enumerate(items))+'</div>'
P['p6-six-point-check']=[
 pg(hd('Self-check')+'<div class=abs style="left:56px;top:190px;font:900 460px/1 Inter Tight;letter-spacing:-26px">?<span style="color:#C9C8C1">/6</span></div>'
   +'<div class=abs style="left:80px;right:80px;top:720px;font:900 112px/0.95 Inter Tight;letter-spacing:-4.5px">Score your<br>bell system.</div>'
   +'<div class=abs style="left:80px;right:220px;top:980px;font:500 34px/1.4 Inter Tight;color:var(--mute)">Six things a modern school bell should do. Count how many yours can.</div>'
   +ft(W,'Swipe →','color:var(--mute)'),bg='background:#fff'),
 pg(hd('Self-check')+'<div class=abs style="left:80px;right:80px;top:230px;font:900 96px/0.95 Inter Tight;letter-spacing:-4px">Tick what your<br>system does today.</div>'+checklist(False)
   +'<div class=abs style="left:80px;right:80px;top:1170px;font:500 28px Inter Tight;color:var(--mute)">Keep count. Your score is on the next slide.</div>'+ft(W,'02 / 03','color:var(--mute)'),bg='background:#fff'),
 pg(hd('Self-check',col='color:#F4F3EE')+'<div class="abs m" style="left:80px;top:230px;color:#A9AAA3">Your score</div>'
   +'<div class=abs style="left:80px;right:80px;top:290px;display:grid;grid-template-columns:2fr 2fr 2fr;gap:12px">'
   +''.join(f'<div><div style="height:22px;border-radius:11px;background:{c}"></div><div style="font:900 64px Inter Tight;letter-spacing:-2px;margin-top:26px;color:{c}">{s}</div><div style="font:600 28px Inter Tight;color:#D6D7D0;margin-top:6px">{l}</div></div>' for s,l,c in [('0–2','Time to upgrade','#FF4D2E'),('3–4','Halfway there','#F5B83D'),('5–6','Well covered','#A3CF44')])+'</div>'
   +'<div class=abs style="left:80px;right:80px;top:640px;font:900 104px/0.95 Inter Tight;letter-spacing:-4.5px">Smart School 360:<br><span style="color:var(--lime)">six for six.</span></div>'
   +'<div class=abs style="left:80px;top:1000px"><span class=btn>Book a free online demo <span>→</span></span></div>'
   +ft('WhatsApp 98349 75938','03 / 03','color:#A9AAA3'),'dark')]
manifest={}
for post,slides in P.items():
    os.system(f'rm -rf out/{post}'); os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,h in enumerate(slides,1):
        name=f'slide-{k:02d}'; open(f'{name}__{post}.html','w').write(h); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

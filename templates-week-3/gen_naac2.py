import os,json
exec(open('gen.py').read().split('P={}')[0])
P={}
n=4
INK='#0B0907';LIME='#A3CF44';OFF='#F6F4F0'
def ab(css,html=''): return f'<div style="position:absolute;{css}">{html}</div>'
# 1 cover: paper, giant NAAC, product card, criteria stamp
s1=page('light', top(cnt(1,n))
 +ab('left:var(--m);top:200px;font:700 22px Barlow;letter-spacing:6px;color:var(--olive)','FOR COLLEGES &amp; UNIVERSITIES')
 +ab('left:70px;top:230px;font:800 300px/0.9 \'Barlow Condensed\';letter-spacing:-6px;color:'+INK,'NAAC')
 +ab('left:var(--m);top:510px;font:800 84px/0.95 \'Barlow Condensed\';color:'+INK,'visit coming up?')
 +ab('left:var(--m);right:var(--m);top:640px;height:470px;background:#fff;border-radius:36px;box-shadow:0 30px 80px rgba(11,9,7,.12);display:flex;align-items:center;justify-content:center','<img src=product.png style="height:440px;border-radius:30px">')
 +ab('right:60px;top:560px;width:230px;height:230px;border-radius:50%;background:'+LIME+';transform:rotate(-10deg);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;box-shadow:0 14px 40px rgba(11,9,7,.18)','<div style="font:700 18px Barlow;letter-spacing:4px">CRITERIA</div><div style="font:800 64px/1 \'Barlow Condensed\'">2·4·6·7</div>')
 +ab('left:var(--m);right:var(--m);top:1140px;font:500 30px/1.4 Barlow;color:#5f5a54','One installation. <b style="color:'+INK+'">Evidence assessors can see.</b>')
 +bottom(1,n,'var(--ink)',SW), grain=False)
# 2 dark: vertical big-number list
crit=[('2','Teaching-learning','Every period on time. Prayer and anthem automated.'),('4','Infrastructure','Campus PA, zone audio and an emergency siren.'),('6','Governance','ICT-based scheduling with internet time sync.'),('7','Best practices','Water bell, siren drills and a punctuality culture.')]
lst=''.join(f'<div style="display:flex;gap:40px;align-items:center;padding:30px 0;border-top:2px solid rgba(255,255,255,.14)"><div style="font:800 170px/0.8 \'Barlow Condensed\';color:{LIME};width:150px;text-align:center">{k}</div><div><div style="font:700 22px Barlow;letter-spacing:5px;color:#8C867F">CRITERION {k}</div><div style="font:800 56px/1 \'Barlow Condensed\';color:#fff;margin-top:6px">{t}</div><div style="font:500 28px/1.35 Barlow;color:#C9C3BB;margin-top:8px">{d}</div></div></div>' for k,t,d in crit)
s2=page('dark', top(cnt(2,n))+ab('left:var(--m);top:200px;font:800 104px/0.95 \'Barlow Condensed\';color:#fff','Where it <span style="color:'+LIME+'">counts</span>')+ab('left:var(--m);right:var(--m);top:350px',lst)+bottom(2,n,'#fff',nxt()))
# 3 paper evidence checklist on a clipboard card
ev=[('Installation certificate','PA infrastructure and zone setup','4.1'),('Timetable printout','Structured schedule, period discipline','2.7 · 6.2'),('Siren drill records','Safety infrastructure in use','4.1 · 7.1'),('Water bell schedule','Student health initiative','7.1'),('Staff training record','Done on installation day','6.3')]
chk=''.join(f'<div style="display:flex;gap:28px;align-items:center;padding:24px 0;border-bottom:2px dashed #DDD9D4"><div style="width:56px;height:56px;border-radius:12px;background:{LIME};display:flex;align-items:center;justify-content:center;font:800 40px Barlow;color:{INK}">✓</div><div style="flex:1"><div style="font:800 44px/1 \'Barlow Condensed\';color:{INK}">{t}</div><div style="font:500 24px Barlow;color:#7a746d;margin-top:6px">{d}</div></div><div style="font:700 20px Barlow;letter-spacing:2px;color:var(--olive)">{c}</div></div>' for t,d,c in ev)
s3=page('light', top(cnt(3,n))
 +ab('left:var(--m);top:190px;font:800 104px/0.95 \'Barlow Condensed\';color:'+INK,'Your evidence<br><span style="color:var(--olive)">file, ready</span>')
 +ab('left:var(--m);right:var(--m);top:440px;background:#fff;border-radius:32px;padding:36px 48px 20px;box-shadow:0 30px 80px rgba(11,9,7,.10)','<div style="position:absolute;top:-22px;left:50%;transform:translateX(-50%);width:200px;height:44px;border-radius:12px;background:'+INK+'"></div>'+chk)
 +bottom(3,n,'var(--ink)',nxt()), grain=False)
# 4 CTA
s4=cta(4,n,'Before your assessment','One day.<br>Fully documented.',['1-day install','Certificate','Staff training','Drill records'])
P['post-7-naac-v2']=[s1,s2,s3,s4]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name=f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

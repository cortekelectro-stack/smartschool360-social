import os,json
H='<html><head><meta charset=utf-8><link rel=stylesheet href=base.css></head>'
def hd(r='Smart School 360',col=''): return f'<div class="hd m" style="{col}"><span class=lg><img src=logo.png>Cortek Electro</span><span>{r}</span></div>'
def ft(l,r,col=''): return f'<div class="ft m" style="{col}"><span>{l}</span><span>{r}</span></div>'
def pg(body,cls='',bg=''): return H+f'<body class="{cls}" style="{bg}">{body}</body></html>'
P={};W='smartschool360.co.in'
# L1 Swiss: no accidental bells
grid='<div class=abs style="inset:0;background-image:linear-gradient(90deg,#0B0C0A10 1px,transparent 1px);background-size:180px 100%"></div>'
P['l1-no-accidental-bells']=[pg(grid+hd()+'<div class="abs m" style="left:80px;top:220px;color:var(--mute)">Before any manual bell plays</div>'
 +'<div class=abs style="left:70px;right:60px;top:260px;font:900 200px/0.86 Inter Tight;letter-spacing:-11px">Are you<br>sure?</div>'
 +'<div class=abs style="left:80px;right:80px;top:700px;border-top:3px solid var(--ink);display:grid;grid-template-columns:1fr 1fr">'
 +''.join(f'<div style="padding:34px {"30px 0 0" if i==0 else "0 0 36px"};{"border-right:2px solid #D9D8D1;" if i==0 else ""}"><img src={img} style="width:100%;border-radius:14px;box-shadow:0 14px 40px rgba(11,12,10,.14)"><div style="font:800 40px/1.1 Inter Tight;letter-spacing:-1px;margin-top:28px">{t}</div><div style="font:500 26px/1.35 Inter Tight;color:var(--mute);margin-top:10px">{d}</div></div>' for i,(img,t,d) in enumerate([('password.png','Password lock.','Programming and settings need a code.'),('are-you-sure.png','A second tap.','Every manual bell asks to confirm.')]))
 +'</div>'+ft('No accidental bells',W,'color:var(--mute)'),bg='background:var(--paper)')]
# L2 editorial timeline: mic + bell
ev=[('10:58:00','Announcement starts','The principal speaks on the mic.','var(--ink)'),('11:00:00','Scheduled bell','The bell takes priority, on the second.','var(--lime)'),('11:00:10','Mic resumes','The announcement carries on by itself.','var(--ink)')]
tl=''.join(f'<div style="display:grid;grid-template-columns:260px 40px 1fr;align-items:start;padding:34px 0;border-top:2px solid #E6E5DF"><div class=m style="font-size:26px;padding-top:8px">{t}</div><div style="width:22px;height:22px;border-radius:50%;background:{c};margin-top:12px"></div><div><div style="font:800 46px Inter Tight;letter-spacing:-1.5px">{h}</div><div style="font:500 28px/1.35 Inter Tight;color:var(--mute);margin-top:8px">{d}</div></div></div>' for t,h,d,c in ev)
P['l2-mic-and-bell']=[pg(hd()+'<div class=abs style="left:80px;right:80px;top:200px;font:900 100px/0.95 Inter Tight;letter-spacing:-4.5px">The bell<br>doesn’t wait.<br><span style="color:#B5B6AF">Neither does<br>the mic.</span></div>'
 +f'<div class=abs style="left:80px;right:80px;top:640px">{tl}<div style="border-top:2px solid #E6E5DF"></div></div>'
 +'<div class=abs style="left:80px;right:80px;top:1150px;font:500 28px/1.4 Inter Tight;color:var(--mute)">Illustrative timings. Live announcements and the bell schedule share the same speakers, without anyone stepping in.</div>'
 +ft('Live PA + bells',W,'color:var(--mute)'),bg='background:#fff')]
# L3 Apple minimal: play manually
P['l3-play-manually']=[pg(hd()+'<div class=abs style="left:0;right:0;top:210px;text-align:center;font:900 132px/0.92 Inter Tight;letter-spacing:-7px">Plan changed?</div>'
 +'<div class=abs style="left:140px;right:140px;top:400px;text-align:center;font:600 42px/1.25 Inter Tight;letter-spacing:-1px">Ring any bell or prayer by hand,<br>from the same screen.</div>'
 +'<img src=play-manually.png class=abs style="left:140px;top:570px;width:800px;border-radius:26px;box-shadow:0 24px 70px rgba(11,12,10,.16)">'
 +'<div class=abs style="left:160px;top:820px;width:648px;height:190px;border-radius:16px;border:6px solid var(--lime)"></div>'
 +'<div class="abs m" style="left:80px;right:80px;top:1140px;text-align:center;color:var(--mute);font-size:17px">Morning prayer · Evening prayer · Short bell · Long bell · Manual 1–8</div>'
 +ft('Free online demo',W,'color:var(--mute)'),bg='background:#fff')]
# L4 Day board on lime: to the second
board=lambda t,c='#F4F3EE': ''.join(f'<span style="display:inline-block;width:{70 if ch==":" else 100}px;height:190px;margin:0 5px;border-radius:12px;background:{"transparent" if ch==":" else "#1A1C17"};text-align:center;font:700 130px/190px Roboto Mono;color:{c}">{ch}</span>' for ch in t)
P['l4-to-the-second']=[pg(hd()+'<div class=abs style="left:80px;right:80px;top:190px;font:900 112px/0.95 Inter Tight;letter-spacing:-5px">Not roughly.<br>To the second.</div>'
 +'<div class=abs style="left:80px;right:80px;top:500px;background:var(--ink);border-radius:28px;padding:40px 30px 46px;text-align:center"><div class=m style="color:#8D8F87;font-size:16px;text-align:left;padding:0 14px 26px">Next bell · Period 1</div>'+board('07:30:')+board('00','var(--lime)').replace(';margin:0 5px',';margin:0 5px')+'</div>'
 +'<div class=abs style="left:80px;right:80px;top:900px;display:grid;grid-template-columns:1fr 1fr;gap:40px;border-top:3px solid var(--ink);padding-top:34px">'
 +''.join(f'<div><div style="font:800 40px Inter Tight;letter-spacing:-1px">{a}</div><div style="font:500 27px/1.38 Inter Tight;margin-top:10px">{b}</div></div>' for a,b in [('Programmed to the second.','Every bell, prayer and announcement.'),('Set from the internet.','Over Wi-Fi, so the clock doesn’t drift.')])
 +'</div>'+ft('Internet time',W,'color:var(--ink)'),bg='background:var(--lime)')]
# L5 report list: installation
st=[('01','Site survey','We visit and plan speaker zones.'),('02','Install','Controller, speakers, wiring.'),('03','Program','Timetable, prayers, announcements.'),('04','Test','Every bell, every zone.'),('05','Train','Principal, office and support staff.'),('06','Go live','The day runs on its own.')]
cells=''.join(f'<div style="padding:30px 30px 34px 0;border-top:2px solid #D9D8D1;{"border-right:2px solid #D9D8D1;" if i%2==0 else "padding-left:36px;"}"><div class=m style="color:var(--mute)">Step {n}</div><div style="font:800 44px Inter Tight;letter-spacing:-1.5px;margin-top:10px">{t}</div><div style="font:500 26px/1.35 Inter Tight;color:var(--mute);margin-top:6px">{d}</div></div>' for i,(n,t,d) in enumerate(st))
P['l5-first-call-to-first-bell']=[pg(hd()+'<div class=abs style="left:80px;right:80px;top:190px;font:900 104px/0.95 Inter Tight;letter-spacing:-5px">From first call<br>to first bell.</div>'
 +'<div class="abs m" style="left:80px;top:430px;color:var(--mute)">What happens after you say yes</div>'
 +f'<div class=abs style="left:80px;right:80px;top:480px;display:grid;grid-template-columns:1fr 1fr;border-bottom:3px solid var(--ink)">{cells}</div>'
 +'<div class=abs style="left:0;right:0;bottom:0;height:250px;background:var(--ink);color:#F4F3EE"><div class=abs style="left:80px;top:52px;font:800 46px Inter Tight;letter-spacing:-1.5px">No IT team needed.</div><div class=abs style="left:80px;top:118px;font:500 28px Inter Tight;color:#A9AAA3">In Marathi, Hindi or English.</div><div class=abs style="right:80px;top:66px"><span class=btn style="padding:24px 34px;font-size:30px">Free online demo →</span></div></div>',bg='background:var(--paper)')]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=['post']
    open(f'post__{post}.html','w').write(slides[0])
json.dump(manifest,open('manifest.json','w'))

import os,json
H='<html><head><meta charset=utf-8><link rel=stylesheet href=base.css></head>'
def hd(r='Smart School 360',col=''): return f'<div class="hd m" style="{col}"><span class=lg><img src=logo.png>Cortek Electro</span><span>{r}</span></div>'
def ft(l,r,col=''): return f'<div class="ft m" style="{col}"><span>{l}</span><span>{r}</span></div>'
def pg(body,cls='',bg=''): return H+f'<body class="{cls}" style="{bg}">{body}</body></html>'
P={}
W='smartschool360.co.in'
# ---------- 1 Apple-style reveal (cover = poster A) ----------
P['p1-company-update']=['A.png',
 pg(hd()+'<div class="abs m" style="left:80px;top:250px;color:var(--mute)">Since our last update</div>'
   +''.join(f'<div class=abs style="left:80px;right:80px;top:{t}px;border-top:2px solid #E4E3DD;padding-top:34px"><div style="font:800 76px/1 Inter Tight;letter-spacing:-3px">{a}</div><div style="font:500 32px/1.35 Inter Tight;color:var(--mute);margin-top:16px">{b}</div></div>' for t,a,b in [(320,'Smart School 360.','Our complete school bell and PA system.'),(610,'Three models.','Z1, Z2 and Z3, from small schools to large campuses.'),(900,'A government pilot.','Z.P. Primary School, Nighoje (Khed), with DEO (Primary), Pune permission.')])
   +ft(W,'02 / 04','color:var(--mute)'),bg='background:#fff'),
 pg(hd()+'<div class=abs style="left:80px;right:80px;top:230px;text-align:center;font:900 104px/0.95 Inter Tight;letter-spacing:-4.5px">Runs the day.<br><span style="color:#B5B6AF">On its own.</span></div>'
   +'<img src=product-clean.png class=abs style="left:110px;top:560px;width:860px;filter:drop-shadow(0 40px 34px rgba(0,0,0,.28))">'
   +'<div class="abs m" style="left:80px;right:80px;top:1060px;display:flex;justify-content:center;gap:34px;color:var(--ink)"><span>Bells</span><span style="color:var(--lime)">●</span><span>Prayers</span><span style="color:var(--lime)">●</span><span>Announcements</span><span style="color:var(--lime)">●</span><span>Siren</span></div>'
   +'<div class=abs style="left:80px;right:80px;top:1120px;text-align:center;font:500 30px Inter Tight;color:var(--mute)">With battery backup, so it keeps going in a power cut.</div>'
   +ft(W,'03 / 04','color:var(--mute)'),bg='background:var(--paper)'),
 pg(hd(col='color:#F4F3EE')+'<div class=abs style="left:80px;right:80px;top:300px;font:900 128px/0.92 Inter Tight;letter-spacing:-5px">See it run<br>on <span style="color:var(--lime)">your</span><br>timetable.</div>'
   +'<div class=abs style="left:80px;right:120px;top:740px;font:500 34px/1.4 Inter Tight;color:#A9AAA3">We survey your campus, install, program and train your staff in Marathi, Hindi or English.</div>'
   +'<div class=abs style="left:80px;top:950px"><span class=btn>Book a free online demo <span>→</span></span></div>'
   +ft('WhatsApp 98349 75938','04 / 04','color:#A9AAA3'),'dark')]
# ---------- 2 Swiss shock ----------
grid='<div class=abs style="inset:0;background-image:linear-gradient(90deg,#0B0C0A10 1px,transparent 1px);background-size:180px 100%"></div>'
P['p2-who-rings-the-bell']=[
 pg(grid+hd()+'<div class="abs m" style="left:80px;top:250px;color:var(--mute)">Recess was at 11:00</div>'
   +'<div class=abs style="left:62px;top:300px;font:900 380px/0.85 Inter Tight;letter-spacing:-22px;color:var(--red)">11:09</div>'
   +'<div class=abs style="left:80px;right:80px;top:720px;font:900 104px/0.95 Inter Tight;letter-spacing:-4px">Who rings<br>your school bell?</div>'
   +'<div class=abs style="left:80px;right:300px;top:1000px;font:500 32px/1.4 Inter Tight;color:var(--mute)">If the answer is a person, your timetable is only as reliable as their memory.</div>'
   +ft(W,'Swipe →','color:var(--mute)'),bg='background:var(--paper)'),
 pg(grid+hd()+'<div class=abs style="left:80px;right:80px;top:230px;font:900 96px/0.95 Inter Tight;letter-spacing:-4px">Where a manual<br>bell slips.</div>'
   +'<div class=abs style="left:80px;right:80px;top:500px;display:grid;grid-template-columns:1fr 1fr;border-top:3px solid var(--ink)">'
   +''.join(f'<div style="padding:40px 30px 50px 0;border-bottom:2px solid #D9D8D1;{"border-right:2px solid #D9D8D1;" if i%2==0 else "padding-left:36px;"}"><div style="font:900 84px Inter Tight;color:var(--red);letter-spacing:-3px">{n}</div><div style="font:800 40px/1.1 Inter Tight;letter-spacing:-1px;margin-top:18px">{t}</div><div style="font:500 26px/1.35 Inter Tight;color:var(--mute);margin-top:10px">{d}</div></div>' for i,(n,t,d) in enumerate([('01','Bell duty is on leave.','Nobody else knows the timings.'),('02','A meeting runs late.','One long period shifts the day.'),('03','Two mediums, one campus.','Their bells clash.'),('04','The far block can’t hear.','Half the school misses it.')]))
   +'</div>'+ft(W,'02 / 03','color:var(--mute)'),bg='background:var(--paper)'),
 pg(hd(col='color:#F4F3EE')+'<div class="abs m" style="left:80px;top:250px;color:var(--lime)">With Smart School 360</div>'
   +'<div class=abs style="left:62px;top:300px;font:900 380px/0.85 Inter Tight;letter-spacing:-22px;color:var(--lime)">11:00</div>'
   +'<div class=abs style="left:80px;right:80px;top:640px;font:900 92px/0.95 Inter Tight;letter-spacing:-3.5px">Every bell.<br>Every day.</div>'
   +'<div class=abs style="left:380px;top:780px;width:700px;height:500px;background:radial-gradient(closest-side,rgba(244,243,238,.24),rgba(244,243,238,.07) 55%,rgba(244,243,238,0) 100%)"></div>'+'<img src=product-clean.png class=abs style="left:470px;top:900px;width:520px;filter:drop-shadow(0 30px 30px rgba(0,0,0,.6))">'
   +'<div class=abs style="left:80px;width:340px;top:900px;font:500 28px/1.4 Inter Tight;color:#A9AAA3">Set the timetable once. It rings every bell, prayer and announcement on its own.</div>'
   +ft('Free online demo · '+W,'03 / 03','color:#A9AAA3'),'dark')]
# ---------- 3 data-led report ----------
def rep(i,n,label,big,bigsize,line,sub,extra=''):
    return pg(hd('Pilot report · Nov 2025')+f'<div class="abs m" style="left:80px;top:230px;color:var(--mute)">{label}</div>'
      +f'<div class=abs style="left:56px;top:250px;font:900 {bigsize}px/1 Inter Tight;letter-spacing:-{bigsize*0.05:.0f}px">{big}</div>'
      +f'<div class=abs style="left:80px;right:80px;top:820px;border-top:3px solid var(--ink);padding-top:36px;font:800 64px/1.02 Inter Tight;letter-spacing:-2.5px">{line}</div>'
      +f'<div class=abs style="left:80px;right:200px;top:1050px;font:500 30px/1.4 Inter Tight;color:var(--mute)">{sub}</div>'+extra
      +ft(W,('Swipe →' if i==1 else f'{i:02d} / {n:02d}'),'color:var(--mute)'),bg='background:#fff')
P['p3-nighoje-zp-pilot']=[
 rep(1,4,'Z.P. Primary School, Nighoje · Khed, Pune','0',560,'missed bells.<br><span style="color:var(--mute)">In a government school pilot.</span>','Run with permission from the DEO (Primary), Pune. Bells, Marathi announcements, prayers, PA and siren.'),
 rep(2,4,'Uptime','100<span style="font-size:240px;letter-spacing:-8px">%</span>',400,'uptime, including<br>through power cuts.','Clear sound recorded in every classroom, corridor and outdoor area, with battery backup and auto-charging.'),
 pg(hd('Pilot report · Nov 2025')+'<div class="abs m" style="left:80px;top:230px;color:var(--mute)">What officials recommended</div>'
   +'<div class=abs style="left:80px;right:80px;top:290px;font:900 100px/0.95 Inter Tight;letter-spacing:-4px">More schools.<br><span style="color:#B5B6AF">More districts.</span></div>'
   +''.join(f'<div class=abs style="left:80px;right:80px;top:{t}px;border-top:3px solid var(--ink);padding-top:30px;display:grid;grid-template-columns:200px 1fr"><div class=m style="color:var(--mute);padding-top:10px">{a}</div><div><div style="font:800 40px Inter Tight;letter-spacing:-1px">{b}</div><div style="font:500 30px/1.4 Inter Tight;color:var(--mute);margin-top:10px">{c}</div></div></div>' for t,a,b,c in [(620,'BEO','Block Education Officer, Khed','Recommended expanding the system to more schools.'),(880,'DEO','DEO (Primary), Pune','Recommended expansion across the district and state, and CSR sponsorship for rural schools.')])
   +ft(W,'03 / 04','color:var(--mute)'),bg='background:#fff'),
 pg(hd(col='color:#F4F3EE')+'<div class="abs m" style="left:80px;top:250px;color:var(--lime)">For ZP schools and CSR teams</div><div class=abs style="left:80px;right:80px;top:300px;font:900 124px/0.92 Inter Tight;letter-spacing:-5px">Bring the<br>pilot to your<br><span style="color:var(--lime)">schools.</span></div>'
   +'<div class=abs style="left:80px;right:140px;top:760px;font:500 34px/1.4 Inter Tight;color:#A9AAA3">We’ll share the full pilot summary and plan a rollout for your schools.</div>'
   +'<div class=abs style="left:80px;top:950px"><span class=btn>Book a free online demo <span>→</span></span></div>'+ft('WhatsApp 98349 75938','04 / 04','color:#A9AAA3'),'dark')]
# ---------- 4 real school environment ----------
def photo(i,n,img,pos,kick,title,sub):
    return pg(f'<div class=abs style="inset:0;background:url({img}) {pos}/cover"></div><div class=abs style="left:0;right:0;bottom:0;height:760px;background:linear-gradient(180deg,rgba(11,12,10,0),rgba(11,12,10,.92) 62%)"></div><div class=abs style="left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(11,12,10,.55),rgba(11,12,10,0))"></div>'
      +hd('Illustrative image','color:#F4F3EE')+f'<div class="abs m" style="left:80px;top:860px;color:var(--lime)">{kick}</div><div class=abs style="left:80px;right:80px;top:905px;font:900 100px/0.95 Inter Tight;letter-spacing:-4px;color:#fff">{title}</div><div class=abs style="left:80px;right:180px;top:{1110 if "<br>" in title else 1030}px;font:500 30px/1.4 Inter Tight;color:#D6D7D0">{sub}</div>'
      +ft(W,('Swipe →' if i==1 else f'{i:02d} / {n:02d}'),'color:#BFC0B9'),'dark')
P['p4-more-than-a-bell']=[
 photo(1,4,'09-assembly-stage-prayer.png','center 35%','07:40 · Morning prayer','A bell that<br>cares, too.','The schedule that runs your periods can run the routines that shape a school day.'),
 photo(2,4,'07-corridor-students-walking.png','center 40%','10:15 · Water bell','Drink water.','A gentle reminder between periods, at the times you choose.'),
 photo(3,4,'13-classroom-teacher-blackboard.png','center 45%','14:00 · Calm audio','Settle the class.','Meditation audio after lunch. Upload your own audio and Marathi voice-overs too.'),
 pg(hd()+'<div class=abs style="left:80px;top:250px;font:400 260px/0.7 Fraunces;color:var(--lime)">“</div><div class=abs style="left:80px;right:80px;top:420px;font:500 100px/1.05 Fraunces;letter-spacing:-1.5px">The water bell concept is very suitable for students.</div>'
   +'<div class="abs m" style="left:80px;top:880px;color:var(--mute)">Bhairavnath Vidyalaya, Donde, Khed</div>'
   +'<div class=abs style="left:80px;top:1040px"><span class=btn style="background:var(--ink);color:#fff">Book a free online demo <span style="color:var(--lime)">→</span></span></div>'
   +ft(W,'04 / 04','color:var(--mute)'),bg='background:var(--paper)')]
# ---------- 5 editorial quotes ----------
qs=[('The bell rings on time and accurately.','Mahatma Phule Vidyalaya, Bhosari, Pune'),('All activities happen sharply at bell time.','N.M. Joshi Vidyabhavan, Goregaon, Raigad'),('The earlier problem of not being able to hear announcements has been completely solved.','Nrusinha High School, Sangvi, Pune')]
P['p5-what-schools-wrote']=[pg(hd('Feedback letters · 2024–25')+'<div class=abs style="left:80px;top:220px;font:900 96px/0.95 Inter Tight;letter-spacing:-4px">In their words.</div>'
   +'<div class=abs style="left:80px;right:80px;top:400px">'+''.join(f'<div style="border-top:2px solid var(--ink);padding:46px 0 56px;display:grid;grid-template-columns:100px 1fr"><div style="font:400 140px/0.8 Fraunces;color:var(--lime)">“</div><div><div style="font:500 {60 if len(q)<60 else 52}px/1.12 Fraunces;letter-spacing:-.8px">{q}</div><div class=m style="color:var(--mute);margin-top:20px;font-size:16px">{w}</div></div></div>' for q,w in qs)+'</div>'
   +ft(W,'Smart School 360','color:var(--mute)'),bg='background:#F4EFE6')]
# ---------- 7 editorial Q&A ----------
def qa(i,n,items):
    out=''
    for k,(num,q,a) in enumerate(items):
        out+=f'<div style="border-top:3px solid var(--ink);padding:56px 0 90px"><div style="font:900 120px/1 Inter Tight;color:var(--lime);letter-spacing:-5px">{num}</div><div style="font:800 76px/1.02 Inter Tight;letter-spacing:-3px;margin-top:24px">{q}</div><div style="font:500 38px/1.4 Inter Tight;color:var(--mute);margin-top:22px">{a}</div></div>'
    return pg(hd('Principals ask')+f'<div class=abs style="left:80px;right:80px;top:200px">{out}</div>'+ft(W,f'{i:02d} / {n:02d}','color:var(--mute)'),bg='background:#fff')
P['p7-principals-faq']=[
 pg(hd()+'<div class=abs style="left:80px;right:80px;top:260px;font:900 150px/0.9 Inter Tight;letter-spacing:-7px">Five<br>questions<br>every<br>principal<br><span style="color:var(--lime)">asks us.</span></div>'
   +'<div class=abs style="left:80px;right:80px;top:1060px;font:500 32px/1.4 Inter Tight;color:var(--mute)">Answered plainly, before your first call.</div>'+ft(W,'Swipe →','color:var(--mute)'),bg='background:#fff'),
 qa(2,4,[('01','What happens in a power cut?','The bells keep ringing. Battery backup with auto-charging is built in.'),('02','Is there a yearly fee?','No. It’s a one-time purchase with a 1-year warranty.')]),
 qa(3,4,[('03','Are speakers included?','They’re quoted separately, based on your campus.'),('04','Can it announce in Marathi?','Yes. Our team records the voice announcements.')]),
 pg(hd(col='color:#F4F3EE')+'<div class=abs style="left:80px;right:80px;top:250px;border-top:3px solid #F4F3EE;padding-top:40px;display:grid;grid-template-columns:150px 1fr"><div style="font:900 64px Inter Tight;color:var(--lime)">05</div><div><div style="font:800 58px/1.05 Inter Tight;letter-spacing:-2px">Who sets it all up?</div><div style="font:500 32px/1.4 Inter Tight;color:#A9AAA3;margin-top:18px">We do. Site survey, installation, programming your timetable and training your staff.</div></div></div>'
   +'<div class=abs style="left:80px;right:80px;top:700px;font:900 100px/0.95 Inter Tight;letter-spacing:-4px">Another<br>question? <span style="color:var(--lime)">Ask us.</span></div>'
   +'<div class=abs style="left:80px;top:1000px"><span class=btn>Book a free online demo <span>→</span></span></div>'+ft('WhatsApp 98349 75938','04 / 04','color:#A9AAA3'),'dark')]
# ---------- 8 cinematic siren ----------
tri='<svg viewBox="0 0 200 180" width="420" height="378"><defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter></defs><path d="M100 12 L190 168 H10 Z" fill="#FF3B30" filter="url(#g)" opacity=".75"/><path d="M100 12 L190 168 H10 Z" fill="#FF3B30" stroke="#FF6A5C" stroke-width="3" stroke-linejoin="round"/><rect x="92" y="62" width="16" height="60" rx="8" fill="#0B0C0A"/><circle cx="100" cy="142" r="10" fill="#0B0C0A"/></svg>'
P['p8-emergency-siren']=[pg('<div class=abs style="left:50%;top:330px;width:900px;height:900px;margin-left:-450px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,59,48,.22),rgba(255,59,48,0))"></div>'
   +hd('School safety','color:#8E8F88')+f'<div class=abs style="left:330px;top:250px">{tri}</div>'
   +'<div class=abs style="left:80px;right:80px;top:720px;text-align:center;font:900 132px/0.92 Inter Tight;letter-spacing:-6px;color:#fff">One tap.<br><span style="color:#FF3B30">Every zone.</span></div>'
   +'<div class=abs style="left:80px;right:80px;top:1040px;display:grid;grid-template-columns:repeat(3,1fr);gap:30px;text-align:center">'+''.join(f'<div><div class=m style="color:#FF3B30;font-size:16px">{a}</div><div style="font:600 28px/1.3 Inter Tight;color:#D6D7D0;margin-top:12px">{b}</div></div>' for a,b in [('Tap','The red triangle'),('Confirm','No accidental alarms'),('Alert','Siren in every zone')])+'</div>'
   +ft('Build it into your next drill',W,'color:#8E8F88'),'dark')]
# ---------- 9 Apple lineup ----------
col=lambda m,a,z,on: f'<div style="text-align:center;padding:36px 20px 40px;border-radius:28px;{"background:var(--ink);color:#fff" if on else "background:#F4F3EE"}"><div style="font:900 96px Inter Tight;letter-spacing:-4px;{"color:var(--lime)" if on else ""}">{m}</div><div style="font:700 32px Inter Tight;margin-top:6px">{a}</div><div style="font:500 26px Inter Tight;margin-top:10px;color:{"#A9AAA3" if on else "var(--mute)"}">{z}</div>{"<div class=m style=\"margin-top:18px;font-size:14px;color:var(--lime)\">Most popular</div>" if on else ""}</div>'
P['p9-which-model-fits']=[pg(hd()+'<div class=abs style="left:80px;right:80px;top:210px;text-align:center;font:900 110px/0.95 Inter Tight;letter-spacing:-5px">A model for<br>every campus.</div>'
   +'<img src=product-clean.png class=abs style="left:190px;top:480px;width:700px;filter:drop-shadow(0 34px 30px rgba(0,0,0,.25))">'
   +'<div class=abs style="left:80px;right:80px;top:830px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;align-items:end">'+col('Z1','Small schools','Up to 2 zones',0)+col('Z2','Most schools','4 zones',1)+col('Z3','Large campuses','Full campus',0)+'</div>'
   +'<div class=abs style="left:80px;right:80px;top:1170px;text-align:center;font:500 26px Inter Tight;color:var(--mute)">Same touchscreen, siren and battery backup in every model.</div>'
   +ft('Free online demo',W,'color:var(--mute)'),bg='background:#fff')]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,h in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        if h.endswith('.png'): os.system(f'cp {h} out/{post}/{name}.png'); continue
        open(f'{name}__{post}.html','w').write(h); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

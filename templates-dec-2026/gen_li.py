import os,json
exec(open('gen3.py').read().split('P={}')[0])
H=H.replace('</head>','<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=Mukta:wght@500;600;700&display=block"></head>')
def pg(body,cls='',bg=''): return H+f'<body class="{cls}" style="{bg}">{body}</body></html>'
P={}
W='smartschool360.co.in'
T=lambda top,txt,size=100,col='': f'<div class=abs style="left:80px;right:80px;top:{top}px;font:900 {size}px/0.95 Inter Tight;letter-spacing:-{size//25}px;{col}">{txt}</div>'
S=lambda top,txt,col='var(--mute)',right=80: f'<div class=abs style="left:80px;right:{right}px;top:{top}px;font:500 30px/1.4 Inter Tight;color:{col}">{txt}</div>'

# L1 cinematic photo: annual day
P['l1-annual-day']=[pg('<div class=abs style="left:0;right:0;top:0;height:820px;background:url(assembly.png) center 40%/cover"></div><div class=abs style="left:0;right:0;top:420px;height:400px;background:linear-gradient(180deg,rgba(11,12,10,0),#0B0C0A)"></div><div class=abs style="left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(11,12,10,.6),rgba(11,12,10,0))"></div>'
 +hd('Illustrative image','color:#F4F3EE')+'<div class="abs m" style="left:80px;top:800px;color:var(--lime)">Annual day · Sports day</div>'
 +T(845,'One system.<br>Whole programme.',92,'color:#fff')
 +S(1050,'Event timetable in one tap. Live mic, music and zone-by-zone sound, from the same touchscreen that runs your bells.','#D6D7D0',120)
 +ft('Free online demo',W,'color:#BFC0B9'),'dark',bg='background:#0B0C0A')]

# L2 Swiss minimal: power cut
P['l2-power-cut']=[pg(hd('Smart School 360','color:#F4F3EE')
 +'<div class="abs m" style="left:80px;top:220px;color:#8D8F87">Mains power</div><div class=abs style="left:80px;top:255px;font:700 150px Roboto Mono;color:#3A3C36;letter-spacing:-4px">10:59</div><div class="abs m" style="left:560px;top:320px;color:#FF4D2E">● Off</div>'
 +'<div class=abs style="left:80px;right:80px;top:470px;border-top:3px solid #2A2C26"></div>'
 +'<div class="abs m" style="left:80px;top:510px;color:var(--lime)">Bell</div><div class=abs style="left:80px;top:545px;font:700 150px Roboto Mono;color:var(--lime);letter-spacing:-4px">11:00</div><div class="abs m" style="left:560px;top:610px;color:var(--lime)">● Rang on battery</div>'
 +T(820,'Power cut.<br>Bell still rings.',100,'color:#F4F3EE')
 +S(1050,'Inbuilt battery backup with auto charging, and a low-battery warning on the screen.','#A9AAA3',140)
 +ft('Free online demo',W,'color:#8D8F87'),'dark',bg='background:#0B0C0A')]

# L3 Day board (lime): Marathi announcements
ann=[('07:25','प्रार्थनेची वेळ झाली','Prayer time'),('10:30','मधली सुट्टी','Recess'),('12:00','पाणी पिण्याची वेळ','Water break'),('16:30','शाळा सुटली','School over')]
rows=''.join(f'<div style="display:flex;align-items:center;padding:24px 34px;border-top:2px solid #23251F"><span style="width:170px;font:700 34px Roboto Mono;color:var(--lime)">{t}</span><span style="flex:1;font:600 46px/1.1 Mukta;color:#F4F3EE">{m}</span><span class=m style="font-size:15px;color:#8D8F87">{e}</span></div>' for t,m,e in ann)
P['l3-marathi-announcements']=[pg(hd()+T(190,'Announcements<br>in Marathi.',100)
 +f'<div class=abs style="left:80px;right:80px;top:470px;background:var(--ink);border-radius:28px;overflow:hidden"><div class=m style="padding:26px 34px;color:#8D8F87;font-size:16px">Time &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Announcement</div>{rows}</div>'
 +S(1050,'Clear Marathi voice-overs, played automatically at the time you set. Staff and students hear the day in their own language.','var(--ink)')
 +ft('Example announcements',W,'color:var(--ink)'),bg='background:var(--lime)')]

# L4 editorial roles: no IT team
roles=[('Principal','Approves the timetable. Uses Silent mode and the siren.'),('Office admin','Edits bells, switches A0 / A1 / A2, makes announcements.'),('Support staff','Plays a bell or prayer by hand when plans change.')]
rr=''.join(f'<div style="display:flex;gap:40px;padding:34px 0;border-top:3px solid var(--ink)"><div class=m style="width:60px;padding-top:12px;font-size:20px">0{k+1}</div><div><div style="font:800 52px Inter Tight;letter-spacing:-1.5px">{r}</div><div style="font:500 28px/1.4 Inter Tight;margin-top:8px;color:var(--mute)">{d}</div></div></div>' for k,(r,d) in enumerate(roles))
P['l4-no-it-team']=[pg(hd()+T(190,'No IT team<br>required.',104)
 +S(420,'Training is part of every installation. We train the people who run your school day.','var(--mute)',200)
 +f'<div class=abs style="left:80px;right:80px;top:600px">{rr}<div style="border-top:3px solid var(--ink)"></div></div>'
 +ft('Free online demo',W,'color:var(--mute)'),bg='background:var(--paper)')]

# L5 data poster: 3+ schools
terms=[('Custom proposal','One plan across all your campuses.'),('Dedicated install team','Surveys and installs, campus by campus.'),('Staggered payment','Available on request.'),('Govt and NGO quotes','Tailored to your programme.')]
tg=''.join(f'<div style="padding:30px 32px;border-radius:24px;background:{"#0B0C0A;color:#F4F3EE" if k in (1,2) else "#fff"}"><div style="font:800 36px/1.05 Inter Tight;letter-spacing:-1px">{a}</div><div style="font:500 24px/1.35 Inter Tight;margin-top:10px;color:{"#A9AAA3" if k in (1,2) else "var(--mute)"}">{b}</div></div>' for k,(a,b) in enumerate(terms))
P['l5-three-plus-schools']=[pg(hd()+'<div class=abs style="left:56px;top:150px;font:900 400px/1 Inter Tight;letter-spacing:-24px">3+</div>'
 +'<div class=abs style="left:560px;right:80px;top:250px;font:800 60px/1 Inter Tight;letter-spacing:-2px">schools in your trust or group?</div>'
 +'<div class="abs m" style="left:560px;top:420px;color:var(--mute)">One proposal for all</div>'
 +f'<div class=abs style="left:80px;right:80px;top:600px;display:grid;grid-template-columns:1fr 1fr;gap:22px">{tg}</div>'
 +S(1090,'Tell us how many campuses you run, and we will send one proposal that covers all of them.')+ft('Talk to us',W,'color:var(--mute)'),bg='background:var(--paper)')]

# L6 checklist on white: new term
chk=[('A0','New term timings updated'),('A1','Exam timetable ready for prelims and boards'),('⚡','Battery tested with the power off'),('◐','Zone volumes right for each block'),('🔒','Password with admins only')]
cr=''.join(f'<div style="display:flex;align-items:center;gap:30px;padding:24px 0;border-top:2px solid #E6E5DF"><div style="width:56px;height:56px;border-radius:14px;border:3px solid var(--ink);display:flex;align-items:center;justify-content:center"><svg width=28 height=22 viewBox="0 0 28 22"><path d="M2 11l8 8L26 3" stroke="#0B0C0A" stroke-width="4" fill="none"/></svg></div><div style="font:700 38px Inter Tight;letter-spacing:-1px">{t}</div></div>' for _,t in chk)
P['l6-new-term-checklist']=[pg(hd()+'<div class="abs m" style="left:80px;top:200px;color:var(--mute)">Before term starts in January</div>'+T(240,'The 2027<br>bell checklist.',100)
 +f'<div class=abs style="left:80px;right:80px;top:540px">{cr}<div style="border-top:2px solid #E6E5DF"></div></div>'
 +S(1110,'Five checks now. A calmer first week in January.','var(--mute)')
 +ft('Free online demo',W,'color:var(--mute)'),bg='background:#fff')]

manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post'; open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

import os, json
HEAD='<html><head><meta charset=utf-8><link rel=stylesheet href=dayboard.css><script src=layout.js></script></head>'
def page(i,n,body,dark=False,left='smartschool360.co.in'):
    r=f'{i:02d} / {n:02d}' if n>1 else 'Smart School 360'
    if n>1 and i==1: r='Swipe →'
    return HEAD+f'<body class="{"dark" if dark else ""}"><div class=hd><span>Cortek Electro</span><span>Smart School 360</span></div>{body}<div class=ft><span>{left}</span><span>{r}</span></div></body></html>'
def h1(t,size=112,top=120,color=''): return f'<h1 style="font-size:{size}px;top:{top}px;{color}">{t}</h1>'
def flap(t): return '<div class=f>'+''.join(f'<i>{c}</i>' for c in t)+'</div>'
def frow(code,name,st='',cls='',nsize=None):
    return f'<div class=r><div>{flap(code)}</div><div class=n{f" style=font-size:{nsize}px" if nsize else ""}>{name}</div><div class="s {cls}">{st}</div></div>'
def trow(tag,title,desc='',cls=''): return f'<div class=r3><div><span class="tg {cls}">{tag}</span></div><div><h3>{title}</h3>{f"<p>{desc}</p>" if desc else ""}</div></div>'
def board(l,r,rows,top=500,extra=''): return f'<div class=board style="top:{top}px;{extra}"><div class=bh><span>{l}</span><span>{r}</span></div>{rows}</div>'
def tiles(items):
    out=''
    for t,sub,col in items:
        led=f' style="background:{col};box-shadow:0 0 14px {col}"' if col else ''
        out+=f'<div class=tl><div class=led{led}></div><h3>{t}</h3><p>{sub}</p></div>'
    return f'<div class=tiles>{out}</div>'
def note(t,top): return f'<div class=note style="top:{top}px">{t}</div>'
def cta(i,n,title,sub,rows=None,btn='Book a free online demo',hl='NEXT',hr='BOOKING OPEN'):
    rows=rows or frow('FREE','Online demo','BOOK NOW')+frow('CHAT','98349 75938','WHATSAPP')+frow('SITE','smartschool360.co.in','')
    return page(i,n,h1(title,112,120,'color:#F2F2EC')+board(hl,hr,rows,430)+note(sub,840)+f'<div class=cta style="top:1000px">{btn}<span>→</span></div>',dark=True)
LIME='<span style="color:#A3CF44">'
P={}
# 2 who rings
n=4
P['lc-02-who-rings-the-bell']=[
 page(1,n,h1('Who rang the<br>bell today?')+board('TODAY · MANUAL','BELL DUTY: 1 PERSON',
   frow('0745','Morning prayer','ON TIME')+frow('0800','Period 1','+4 MIN','amb')+frow('0920','Period 3','+9 MIN','amb')+frow('1100','Recess','MISSED','red')+frow('1330','Dismissal','?','red'),420)
   +note('If the answer is <b>“a person”</b>, your timetable is only as reliable as their memory.',1060)),
 page(2,n,h1('Where a manual<br>bell goes wrong.',104)+board('INCIDENT LOG','4 OPEN',
   trow('LEAVE','Bell duty is on leave','Nobody else knows the timings.','red')+trow('MEETING','A meeting runs late','One long period shifts the whole day.','amb')+trow('CLASH','Two mediums, one campus','Their bells clash all day.','amb')+trow('RANGE','The far block can’t hear it','Half the school misses the bell.','red'),400)),
 page(3,n,h1('Enter it once.<br>It runs itself.',104)+board('AFTER SMART SCHOOL 360','ALL RESOLVED',
   trow('SET ONCE','Your timetable, programmed','We set every bell, prayer and announcement with you.')+trow('ONE SCREEN','Change anything from the office','Shift a period or make an announcement in seconds.')+trow('TIME BACK','Nobody watches the clock','Staff stay on their real work.'),400)),
 cta(4,n,f'Every bell,<br>{LIME}on time.</span>','Smart School 360 runs the bells, prayers and announcements from one touchscreen.')]
# 3 Nighoje
n=5
P['lc-03-nighoje-zp-pilot']=[
 page(1,n,h1('A ZP school.<br>Zero missed<br>bells.')+board('PILOT · Z.P. PRIMARY SCHOOL, NIGHOJE','KHED, PUNE',
   frow('0000','Missed bells','REPORTED',nsize=44)+frow('100%','Uptime, incl. power cuts','REPORTED',nsize=40),560)
   +note('A government pilot, run with permission from the <b>DEO (Primary), Pune</b>. Report dated November 2025.',930)),
 page(2,n,h1('What went in.',112)+board('INSTALLED','ONE SYSTEM',tiles([('Programmed bells','EVERY PERIOD',None),('Marathi announcements','CLEAR VOICE-OVERS',None),('Automatic prayers','MORNING · EVENING',None),('PA + wireless mic','ALL AREAS',None)])
   +'<div style="margin-top:16px;background:#1d1f1b;border-radius:14px;padding:22px 28px;display:flex;justify-content:space-between;align-items:center"><span style="font:700 34px Inter Tight;color:#F2F2EC">Siren + battery backup</span><span style="font:700 16px Roboto Mono;letter-spacing:2px;color:#A3CF44">AUTO-CHARGING</span></div>',300)),
 page(3,n,h1('What the pilot<br>recorded.',104)+board('PILOT REPORT','NOV 2025',
   trow('BELLS','Zero missed bells','Every scheduled bell rang on time.')+trow('POWER','100% uptime','Including through power cuts.')+trow('SOUND','Clear in every area','Every classroom, corridor and outdoor area.'),400)),
 page(4,n,h1('Recommended<br>for more schools.',104)+board('OFFICIAL FEEDBACK','2 RECOMMENDATIONS',
   trow('BEO','Block Education Officer, Khed','Recommended expanding the system to more schools.')+trow('DEO','DEO (Primary), Pune','Recommended expansion across the district and state, and CSR sponsorship for rural schools.'),400)),
 cta(5,n,f'Bring it to<br>{LIME}your schools.</span>','For ZP schools, school groups and <b>CSR education programmes</b>.')]
# 4 more than a bell
n=4
P['lc-04-more-than-a-bell']=[
 page(1,n,h1('Your bell can<br>do more than<br>ring.')+board('TODAY · ROUTINES','AUTO',
   frow('0740','Morning prayer','PLAYED')+frow('0755','Anthem + pledge','PLAYED')+frow('1015','Water bell','PLAYED')+frow('1230','Water bell','NEXT ●')+frow('1400','Meditation audio','QUEUED','w'),560)),
 page(2,n,h1('Four routines.<br>Zero effort.',104)+board('SOUND SCHEDULE','SET ONCE',tiles([('Water bell','DRINK-WATER REMINDER',None),('Morning prayer','BEFORE ASSEMBLY',None),('Anthem + pledge','ON TIME · DAILY',None),('Meditation audio','SETTLE A CLASS',None)]),400)
   +note('Schools can also upload their own audio, like the school song, and add <b>Marathi voice-overs</b>. Audio features vary by model.',1000)),
 page(3,n,h1('From a school’s<br>letter.',104)+board('MESSAGE','BHAIRAVNATH VIDYALAYA, DONDE, KHED',
   '<div style="padding:40px 6px 20px"><div class=q style="font-size:60px;line-height:1.15">“The water bell concept is very suitable for students.”</div></div>',400)),
 cta(4,n,f'Sound that runs<br>{LIME}your day.</span>','Bells, prayers, music and announcements, each at the time you set.')]
# 5 schools wrote
P['lc-05-what-schools-wrote']=[page(1,1,h1('What schools<br>wrote to us.',112)+board('INBOX · FEEDBACK LETTERS','2024–25',
   ''.join(f'<div class=r3><div><span class=tg>{t}</span></div><div><div class=q>“{q}”</div><p>{w}</p></div></div>' for t,q,w in [('BHOSARI','The bell rings on time and accurately.','Mahatma Phule Vidyalaya, Bhosari, Pune'),('RAIGAD','All activities happen sharply at bell time.','N.M. Joshi Vidyabhavan, Goregaon, Mangaon, Raigad'),('SANGVI','The earlier problem of not being able to hear announcements has been completely solved.','Nrusinha High School, Sangvi, Pune')]),420))]
# 6 six point check
n=4
box='<span style="display:inline-block;width:30px;height:30px;border:3px solid #A3CF44;border-radius:6px"></span>'
P['lc-06-six-point-check']=[
 page(1,n,h1('Can your bell<br>system do<br>these six?')+board('SELF-CHECK','COUNT AS YOU GO',''.join(f'<div class=r style="grid-template-columns:70px 1fr"><div>{box}</div><div class=n style="font-size:36px">{t}</div></div>' for t in ['Set its own clock','Manual override','Password lock','Live announcements','Separate speaker zones','Run through power cuts']),560)),
 page(2,n,h1('Checks 1–3:<br>control.',104)+board('CONTROL','3 CHECKS',trow('✓ 01','Sets its own clock','Internet time calibration.')+trow('✓ 02','Manual override','Take over any bell or announcement by hand.')+trow('✓ 03','Password lock','Nobody changes the schedule by accident.'),400)),
 page(3,n,h1('Checks 4–6:<br>reach.',104)+board('REACH','3 CHECKS',trow('✓ 04','Live announcements','Dual mic inputs.')+trow('✓ 05','Separate speaker zones','Reach every block.')+trow('✓ 06','Battery backup','Keeps running through power cuts.'),400)),
 cta(4,n,f'Your score?<br>{LIME}Six for six.</span>','Smart School 360 does all six <b>from one touchscreen.</b> WhatsApp 98349 75938.',rows=frow('0-2','Time to upgrade','','red')+frow('3-4','Halfway there','','amb')+frow('5-6','Well covered','✓'),hl='SCORE',hr='OUT OF 6')]
# 7 FAQ
n=4
P['lc-07-principals-faq']=[
 page(1,n,h1('The five questions<br>principals<br>ask first.',104)+board('INBOX · FIRST CALLS','5 ANSWERED',
   ''.join(frow(f'Q{i}',q,'ANSWERED',nsize=34).replace('<i>Q</i>','<i>Q</i>') for i,q in enumerate(['What happens in a power cut?','Is there a yearly fee?','Are speakers included?','Can it announce in Marathi?','Who sets it all up?'],1)).replace('<div class=f>','<div class=f style="width:90px">'),480)),
 page(2,n,h1('Cost and power.',104)+board('Q1–Q3','ANSWERED',trow('Q1','What happens in a power cut?','The bells keep ringing. Battery backup with auto-charging.')+trow('Q2','Is there a yearly fee?','No. One-time purchase, 1-year warranty.')+trow('Q3','Are speakers included?','Quoted separately, based on your campus.'),300)),
 page(3,n,h1('Language and setup.',96)+board('Q4–Q5','ANSWERED',trow('Q4','Can it announce in Marathi?','Yes. Voice announcements recorded by our team.')+trow('Q5','Who sets it all up?','We do: site survey, installation, programming, and training for your principal, office and support staff.'),300)),
 cta(4,n,f'Another question?<br>{LIME}Ask us.</span>','We’ll answer it on a call, with your campus layout in front of us.')]
# 8 siren
P['lc-08-emergency-siren']=[page(1,1,h1('One button.<br>Whole campus<br><span style="color:#FF5A3C">alerted.</span>',112,120,'color:#F2F2EC')+board('<span style="color:#FF5A3C">● EMERGENCY · ALL ZONES</span>','<span style="color:#FF5A3C">SIREN</span>',
   trow('STEP 01','Tap the red triangle','On the main screen.','red')+trow('STEP 02','Confirm','So it can’t go off by accident.','red')+trow('STEP 03','Every zone sounds','Overrides bells and announcements until staff stop it.','red'),560),dark=True,left='Build it into your next drill')]
# 9 model
P['lc-09-which-model-fits']=[page(1,1,h1('How big is<br>your campus?',112)+board('CHOOSE YOUR MODEL','SAME SCREEN · SIREN · BATTERY',
   trow('Z1','Small schools','Up to 2 zones. Classrooms and office.','grey')+trow('Z2','Most schools <span style="font:700 16px Roboto Mono;letter-spacing:2px;color:#A3CF44;vertical-align:middle">· MOST POPULAR</span>','4 zones. Classrooms, grounds and corridors.')+trow('Z3','Large campuses','Full-campus coverage. Several blocks and grounds.','grey'),400)
   +note('One-time purchase, no annual subscription. <b>We’ll recommend the right model in a free online demo.</b>',1040),left='WhatsApp 98349 75938')]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,h in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(h); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

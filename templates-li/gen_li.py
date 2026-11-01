import os, json, html
def esc(s): return s
def page(body,dark=False): return f'<html><head><meta charset=utf-8><link rel=stylesheet href=li.css></head><body class="{"dark" if dark else ""}">{body}</body></html>'
def hdr(k): return f'<div class="hdr mono"><span class=co><img src=logo.png>Cortek Electro</span><span class=k>{k}</span></div>'
def ftr(i,n,left='smartschool360.co.in'):
    r=f'{i:02d} / {n:02d}' if n>1 else 'Smart School 360'
    if n>1 and i==1: r='Swipe &rarr;&nbsp;&nbsp;'+r
    return f'<div class="ftr mono"><span>{left}</span><span>{r}</span></div>'
def cover(i,n,k,title,sub,vis,size=104,ttop=210,stop=None,vtop=760,vh=420,tag=None):
    stop=stop or ttop+ (size*1.02*title.count('<br>')+size*1.02)+40
    if vis=='product': v=f'<div class="vis prod" style="top:{vtop}px;height:{vh}px"><img src=product.png></div>'
    else: v=f'<div class=vis style="top:{vtop}px;height:{vh}px;background-image:url({vis})">{f"<span class=\"tag mono\">{tag}</span>" if tag else ""}</div>'
    return page(hdr(k)+f'<h1 style="top:{ttop}px;font-size:{size}px">{title}</h1><div class=sub style="top:{stop:.0f}px">{sub}</div>'+v+ftr(i,n))
def lst(i,n,k,kick,title,items,size=84,ltop=None,dark=False):
    ltop=ltop or 300+int(size*1.02*(title.count('<br>')+1))+50
    its=''.join(f'<div class=it><div class=n>{num}</div><div><h3>{t}</h3>{f"<p>{d}</p>" if d else ""}</div></div>' for num,t,d in items)
    return page(hdr(k)+f'<div class="kick mono" style="top:210px">{kick}</div><h1 style="top:256px;font-size:{size}px">{title}</h1><div class=list style="top:{ltop}px">{its}</div>'+ftr(i,n),dark)
def stats(i,n,k,kick,title,sts,note='',size=84,cols=2):
    s=''.join(f'<div class="st{" on" if on else ""}"><div class=v>{v}</div><div class=l>{l}</div></div>' for v,l,on in sts)
    return page(hdr(k)+f'<div class="kick mono" style="top:210px">{kick}</div><h1 style="top:256px;font-size:{size}px">{title}</h1><div class=stats style="top:560px;grid-template-columns:repeat({cols},1fr)">{s}</div><div class=sub style="top:930px;font-size:32px">{note}</div>'+ftr(i,n))
def qas(i,n,k,kick,pairs,title):
    q=''.join(f'<div class=qa><h3>{a}</h3><p>{b}</p></div>' for a,b in pairs)
    return page(hdr(k)+f'<div class="kick mono" style="top:210px">{kick}</div><h1 style="top:256px;font-size:84px">{title}</h1><div class=list style="top:{460 if "<br>" not in title else 546}px">{q}</div>'+ftr(i,n))
def cta(i,n,k,title,sub,chips):
    c=''.join(f'<span class="chip mono">{x}</span>' for x in chips)
    return page(hdr(k)+f'<h1 style="top:210px;font-size:104px">{title}</h1><div class=sub style="top:450px">{sub}</div>'
      +f'<div class="vis prod" style="top:610px;height:330px"><img src=product.png style="width:64%"></div><div class=chips style="top:975px">{c}</div>'
      +f'<div class=btn style="top:1060px"><b>Book a free online demo</b><span>WhatsApp 98349 75938</span></div>'+ftr(i,n),dark=True)
P={}
K='Company update'
P['li-01-company-update']=[
 cover(1,4,K,'It’s been a while.<br>Here’s what<br>we’ve <span class=hl>built.</span>','<b>Smart School 360</b>: one touchscreen that runs a school’s bells, prayers, announcements and emergency siren.','product',ttop=200,vtop=790,vh=380),
 lst(2,4,K,'Since our last update','Three things<br><span class=hl>worth sharing</span>',[('01','Smart School 360','Our complete bell and PA system, run from one touchscreen.'),('02','Three models, Z1 to Z3','From small schools to large multi-block campuses.'),('03','A government pilot','Z.P. Primary School, Nighoje (Khed), with permission from the DEO (Primary), Pune.')]),
 lst(3,4,K,'What it runs','One device,<br><span class=hl>the whole day</span>',[('01','Period bells','On a timetable you set once.',),('02','Prayers and anthem','Played on time, every day.'),('03','Live announcements','Across every speaker zone.'),('04','Emergency siren + battery','One tap alerts the campus, even in a power cut.')],size=84),
 cta(4,4,K,'See it on<br><span class=hl>your timetable.</span>','We survey, install, program and train your staff, in Marathi, Hindi or English.',['Bells','Prayers','Announcements','Siren','Battery backup'])]
K='For principals'
P['li-02-who-rings-the-bell']=[
 cover(1,4,K,'Who rings<br>the bell at<br><span class=hl>your school?</span>','If the answer is <b>“a person”</b>, your timetable is only as reliable as their memory.','14-corridor-clock-motion-blur.png',ttop=200,vtop=790,vh=380,tag='Illustrative photo'),
 lst(2,4,K,'Where it goes wrong','4 ways a manual<br><span class=hl>bell fails</span>',[('01','Bell duty is on leave','Nobody else knows the timings.'),('02','A meeting runs late','One long period shifts the whole day.'),('03','Two mediums, one campus','Their bells clash all day.'),('04','The far block can’t hear it','Half the school misses the bell.')]),
 lst(3,4,K,'The change','Enter it once.<br><span class=hl>It runs itself.</span>',[('01','Your timetable, set once','We program every bell, prayer and announcement.'),('02','One touchscreen','Change a period or announce from the office.'),('03','Staff get their time back','Nobody stops work to watch the clock.')]),
 cta(4,4,K,'Every bell,<br><span class=hl>on time.</span>','Set it once. Smart School 360 runs the day from one touchscreen.',['Bells','Prayers','Announcements','Battery backup'])]
K='Case study'
P['li-03-nighoje-zp-pilot']=[
 cover(1,5,K,'A ZP school.<br><span class=hl>Zero missed bells.</span>','Pilot at <b>Z.P. Primary School, Nighoje</b> (Khed, Pune), with permission from the DEO (Primary), Pune.','09-assembly-stage-prayer.png',size=100,ttop=200,vtop=720,vh=450,tag='Illustrative photo'),
 lst(2,5,K,'What was installed','One system,<br><span class=hl>every job</span>',[('01','Programmed bells','Every period on time.'),('02','Marathi announcements','Clear voice-overs.'),('03','Automatic prayers','Morning and evening.'),('04','PA, wireless mic, siren','Battery backup with auto-charging.')]),
 stats(3,5,K,'Pilot report · Nov 2025','What the pilot<br><span class=hl>recorded</span>',[('0','missed bells',1),('100%','uptime, including power cuts',0)],note='Clear sound confirmed in <b>every classroom, corridor and outdoor area.</b>'),
 lst(4,5,K,'What officials said','Recommended<br><span class=hl>for more schools</span>',[('BEO','Block Education Officer, Khed','Recommended expanding the system to more schools.'),('DEO','DEO (Primary), Pune','Recommended expansion across the district and state, and CSR sponsorship for rural schools.')]),
 cta(5,5,K,'Bring it to<br><span class=hl>your schools.</span>','For ZP schools, school groups and CSR education programmes.',['Bulk orders','CSR projects','Marathi voice','Battery backup'])]
K='Beyond the bell'
P['li-04-more-than-a-bell']=[
 cover(1,4,K,'A school bell<br>can do more<br>than <span class=hl>ring.</span>','The same schedule that runs your periods can run the <b>small routines</b> that shape a school day.','13-classroom-teacher-blackboard.png',ttop=200,vtop=790,vh=380,tag='Illustrative photo'),
 lst(2,4,K,'Four sounds, on schedule','Routines that<br><span class=hl>run themselves</span>',[('01','Water bell','A reminder to drink water between periods.'),('02','Morning prayer','Before assembly, every day.'),('03','Anthem and pledge','On time, without anyone pressing play.'),('04','Meditation audio','Calm audio to settle a class.')]),
 page(hdr(K)+'<div class="kick mono" style="top:210px">From a school’s letter</div><div class=list style="top:330px"><div class=quote style="border:0"><q style="font-size:76px;line-height:1.12;letter-spacing:-2px">The water bell concept is very suitable for students.</q><div class="who mono" style="font-size:20px;margin-top:40px">Bhairavnath Vidyalaya, Donde, Khed</div></div></div><div class=sub style="top:880px">Schools can also upload their own audio, like the school song or event music, and add <b>Marathi voice-overs</b>. Audio features vary by model.</div>'+ftr(3,4)),
 cta(4,4,K,'Sound that runs<br><span class=hl>your school day.</span>','Bells, prayers, music and announcements, each at the time you set.',['Water bell','Custom audio','Marathi voice','Anthem'])]
qs=[('The bell rings on time and accurately.','Mahatma Phule Vidyalaya, Bhosari, Pune'),('All activities happen sharply at bell time.','N.M. Joshi Vidyabhavan, Goregaon, Mangaon, Raigad'),('The earlier problem of not being able to hear announcements has been completely solved.','Nrusinha High School, Sangvi, Pune')]
P['li-05-what-schools-wrote']=[page(hdr('Customer feedback')+'<div class="kick mono" style="top:210px">From feedback letters · 2024–25</div><h1 style="top:256px;font-size:92px">What schools<br><span class=hl>wrote to us</span></h1><div class=list style="top:540px">'+''.join(f'<div class=quote style="padding:48px 0"><q>{q}</q><div class="who mono">{w}</div></div>' for q,w in qs)+'</div>'+ftr(1,1))]
K='Self-check'
P['li-06-six-point-check']=[
 cover(1,4,K,'Can your bell<br>system do<br><span class=hl>these six?</span>','A two-minute self-check for school offices. <b>Count as you go.</b>','product',ttop=200,vtop=790,vh=380),
 lst(2,4,K,'Check 1–3','Control',[('01','Sets its own clock','Internet time calibration.'),('02','Manual override','Take over any bell or announcement.'),('03','Password lock','Nobody changes the schedule by accident.')]),
 lst(3,4,K,'Check 4–6','Reach',[('04','Live announcements','Dual mic inputs.'),('05','Separate speaker zones','Reach every block.'),('06','Battery backup','Keeps running through power cuts.')]),
 cta(4,4,K,'Six for six,<br><span class=hl>one touchscreen.</span>','0–2: time to upgrade. 3–4: halfway there. 5–6: well covered.',['Internet time','Override','Password','Dual mic','Zones','Battery'])]
K='Principals FAQ'
P['li-07-principals-faq']=[
 cover(1,4,K,'The five questions<br>principals<br><span class=hl>ask first.</span>','Heard on almost every first call. <b>Answered plainly.</b>','06-students-teachers-waving-at-gate.png',size=96,ttop=200,vtop=760,vh=410,tag='Illustrative photo'),
 qas(2,4,K,'Questions 1–3',[('What happens in a power cut?','<b>The bells keep ringing.</b> Battery backup with auto-charging.'),('Is there a yearly fee?','<b>No.</b> One-time purchase, 1-year warranty.'),('Are speakers included?','<b>Quoted separately</b>, based on your campus.')],'Cost and power'),
 qas(3,4,K,'Questions 4–5',[('Can it announce in Marathi?','<b>Yes.</b> Voice announcements recorded by our team.'),('Who sets it all up?','<b>We do.</b> Survey, installation, programming, and training for your principal, office and support staff.')],'Language and setup'),
 cta(4,4,K,'Another question?<br><span class=hl>Ask us.</span>','We’ll answer it on a call, with your campus in front of us.',['No yearly fee','Marathi voice','Battery backup','1-year warranty'])]
P['li-08-emergency-siren']=[page(hdr('School safety')+'<div class="kick mono" style="top:210px">Emergency siren</div><h1 style="top:256px;font-size:92px">One button.<br><span class=hl>Whole campus</span><br><span class=hl>alerted.</span></h1>'
 +'<div class=vis style="top:620px;height:250px;background-image:url(07-corridor-students-walking.png);background-position:center 45%"><span class="tag mono">Illustrative photo</span></div>'
 +'<div class=list style="top:900px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px">'+''.join(f'<div class=st style="padding:30px"><div class="mono" style="color:var(--olive);font-size:22px">{a}</div><h3 style="font-size:34px;font-weight:600;margin-top:16px;letter-spacing:-.5px">{b}</h3><p style="font-size:22px;color:var(--mute);margin-top:8px;line-height:1.35">{c}</p></div>' for a,b,c in [('Step 01','Tap the red triangle','On the main screen.'),('Step 02','Confirm','Stops accidental alarms.'),('Step 03','Every zone sounds','Overrides bells until staff stop it.')])+'</div>'+ftr(1,1,'Build it into your next drill'))]
mc=lambda m,a,z,d,on: f'<div class="st{" on" if on else ""}" style="padding:34px 30px;position:relative"><div class=v style="font-size:110px">{m}</div><h3 style="font-size:30px;font-weight:600;margin-top:14px">{a}</h3><p style="font-size:23px;margin-top:10px;line-height:1.35;color:{"#C9CCD1" if on else "var(--mute)"}"><b style="color:{"#fff" if on else "var(--ink)"}">{z}</b><br>{d}</p>{"<div class=mono style=\"position:absolute;top:30px;right:26px;font-size:14px;color:var(--lime)\">Popular</div>" if on else ""}</div>'
P['li-09-which-model-fits']=[page(hdr('Choosing a model')+'<div class="kick mono" style="top:210px">One question decides it</div><h1 style="top:256px;font-size:96px">How big is<br><span class=hl>your campus?</span></h1>'
 +'<div class="vis prod" style="top:520px;height:300px"><img src=product.png style="width:52%"></div>'
 +'<div class=stats style="top:850px;grid-template-columns:repeat(3,1fr);gap:20px">'+mc('Z1','Small schools','Up to 2 zones','Classrooms + office',0)+mc('Z2','Most schools','4 zones','Classrooms, grounds, corridors',1)+mc('Z3','Large campuses','Full campus','Several blocks and grounds',0)+'</div>'+ftr(1,1,'Same touchscreen, siren, battery'))]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,h in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(h); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

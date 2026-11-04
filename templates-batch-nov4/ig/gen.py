import os, json
ARROW='<svg width=26 height=16 viewBox="0 0 26 16"><path d="M0 8h23M16 1l7 7-7 7" stroke="#0B0907" stroke-width="2.6" fill="none"/></svg>'
BRAND='<span class=brand><img src=logo.png>SMART SCHOOL <b>360</b></span>'
def page(cls, body, grain=True):
    return f'<html><head><link rel=stylesheet href=base.css><link rel=stylesheet href=extra.css></head><body class="{cls}{" grain" if grain else ""}">{body}</body></html>'
def top(right): return f'<div class=top>{BRAND}{right}</div>'
def chip(t): return f'<span class="chip o"><span class=dot style="color:var(--lime)"></span>{t}</span>'
def cnt(i,n): return f'<span class=count>{i:02d} / {n:02d}</span>'
def pager(i,n,color):
    dots=''.join(f'<i{" class=on" if k==i else ""}></i>' for k in range(1,n+1))
    return f'<div class=pager style="color:{color}">{dots}</div>'
def bottom(i,n,color,right):
    return f'<div class=bottom>{pager(i,n,color) if n>1 else "<span></span>"}{right}</div>'
SW=f'<span class=swipe>Swipe {ARROW}</span>'
def nxt(t='Keep swiping →'): return f'<span class=next>{t.upper()}</span>'
URL='<span class=next>SMARTSCHOOL360.CO.IN</span>'

def clock(): return '''<div style="position:absolute;right:-190px;top:150px;width:680px;height:680px;border-radius:50%;border:3px solid rgba(255,255,255,.14)">
<div style="position:absolute;left:50%;top:50%;width:230px;height:14px;background:var(--lime);border-radius:6px;transform-origin:0 50%;transform:translate(0,-50%) rotate(-62deg)"></div>
<div style="position:absolute;left:50%;top:50%;width:290px;height:8px;background:#fff;border-radius:6px;transform-origin:0 50%;transform:translate(0,-50%) rotate(18deg)"></div>
<div style="position:absolute;left:50%;top:50%;width:40px;height:40px;margin:-20px;border-radius:50%;background:var(--lime);box-shadow:0 0 0 10px var(--ink)"></div></div>
<div style="position:absolute;right:-190px;top:150px;width:680px;height:680px;border-radius:50%;background:repeating-conic-gradient(from -1deg,rgba(255,255,255,.55) 0 2deg,transparent 2deg 30deg);-webkit-mask:radial-gradient(circle,transparent 296px,#000 297px,#000 330px,transparent 331px)"></div>
<div style="position:absolute;right:-260px;top:80px;width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,rgba(163,207,68,.2) 0%,rgba(163,207,68,0) 62%)"></div>'''

def cover_graphic(i,n,chiptxt,hook,sub,graphic,top_px=600,size=168):
    return page('dark', graphic+top(chip(chiptxt))+f'<div class=copy style="top:{top_px}px"><div class=h style="font-size:{size}px">{hook}</div><p>{sub}</p></div>'+bottom(i,n,'#fff',SW if n>1 else URL))
def cover_photo(i,n,img,chiptxt,tag,hook,sub,h=900,tagtop=610,copytop=690,size=168,pos='center 40%'):
    return page('dark', f'<div class=ph style="height:{h}px;background-image:url({img});background-position:{pos}"></div>'+top(chip(chiptxt).replace('chip o','chip o" style="background:rgba(11,9,7,.45);border-color:rgba(255,255,255,.3)'))
      +f'<div class=z style="left:var(--m);top:{tagtop}px"><span class=chip style="background:var(--lime);color:var(--ink)">{tag}</span></div>'
      +f'<div class=copy style="top:{copytop}px"><div class=h style="font-size:{size}px">{hook}</div><p>{sub}</p></div>'+bottom(i,n,'#fff',SW if n>1 else URL))
def cards(i,n,theme,eyebrow,title,items,gtop=520,cols=2,h=300,size=124):
    cs=''.join(f'<div class="card{" inv" if inv else ""}" style="height:{h}px"><div class=n>{num}</div><h3>{t}</h3><p>{d}</p></div>' for num,t,d,inv in items)
    return page(theme, top(cnt(i,n))+f'<div class=eyebrow>{eyebrow}</div><div class="title h" style="font-size:{size}px">{title}</div><div class=grid style="top:{gtop}px;grid-template-columns:repeat({cols},1fr)">{cs}</div>'+bottom(i,n,'var(--ink)' if theme!='dark' else '#fff',nxt()), grain=theme!='light')
def rows(i,n,theme,eyebrow,title,items,rtop=520,size=124,right=None):
    rs=''.join(f'<div class=row><div class=k>{k}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for k,t,d in items)
    return page(theme, top(cnt(i,n))+f'<div class=eyebrow>{eyebrow}</div><div class="title h" style="font-size:{size}px">{title}</div><div style="position:absolute;left:var(--m);right:var(--m);top:{rtop}px">{rs}</div>'+bottom(i,n,'var(--ink)' if theme!='dark' else '#fff',right or nxt()), grain=theme!='light')
def qas(i,n,eyebrow,pairs,qtop=250):
    qs=''.join(f'<div class=qa style="margin-bottom:28px"><div class=q><b>Q.</b><h3>{q}</h3></div><div class=a><b>A.</b><p>{a}</p></div></div>' for q,a in pairs)
    return page('light', top(cnt(i,n))+f'<div class=eyebrow>{eyebrow}</div><div style="position:absolute;left:var(--m);right:var(--m);top:{qtop}px">{qs}</div>'+bottom(i,n,'var(--ink)',nxt()), grain=False)
def cta(i,n,eyebrow,title,feats,size=138,stage_top=540,img='product.png',imgw=760):
    fs=''.join(f'<span class=chip>{f}</span>' for f in feats)
    return page('lime', top(cnt(i,n) if n>1 else '<span></span>')+f'<div class=eyebrow>{eyebrow}</div><div class="title h" style="font-size:{size}px">{title}</div><div class=stage style="top:{stage_top}px;height:430px"><img src={img} style="width:{imgw}px"></div><div class=feats style="top:{stage_top+460}px">{fs}</div><div class=cta><div class=l>Book a free online demo<small>WhatsApp 98349 75938</small></div><span class=btn>smartschool360.co.in</span></div>')

P={}
# Post 1
n=4
P['post-1-who-rings-your-school-bell']=[
 cover_graphic(1,n,'For principals','Who rings<br>your <span>school bell?</span>','If the answer is <b>“a person”</b>, your timetable is only as reliable as their memory.',clock()),
 cards(2,n,'light','Where it goes wrong','4 ways a<br><span>manual bell</span> fails',[('01','Bell duty is on leave','Nobody else knows the timings.',0),('02','A meeting runs late','One long period shifts the whole day.',1),('03','Two mediums share a campus','Their bells clash all day.',1),('04','Far block can’t hear it','Half the school misses the bell.',0)]),
 rows(3,n,'dark','How it changes','Enter it once.<br><span>It runs itself.</span>',[('1','Your timetable, set once','We program every bell, prayer and announcement for you.'),('2','One touchscreen','Change a period or play an announcement from the office.'),('3','Staff get their time back','Nobody stops work to watch the clock.')],rtop=540),
 cta(4,n,'The fix','Set it once.<br>Every bell on time.',['Bells','Prayers','Announcements','Battery backup'])]
# Post 2
n=4
P['post-2-three-timetables-one-tap']=[
 cover_photo(1,n,'12-exam-hall.png','For exam coordinators','Prelims season','Exam timings.<br><span>One tap.</span>','Keep a separate exam timetable ready. <b>Switch to it on exam morning</b>, switch back when papers end.'),
 cards(2,n,'light','Three timetables, one device','Every school runs<br><span>3 timetables</span>',[('A0','Regular','Your everyday school day.',0),('A1','Exam','Board timings, warning bells, silent zones.',1),('A2','Vacation or special','Holiday and Saturday programmes.',0)],cols=1,h=200,gtop=520).replace('class=card','class=card').replace('<div class=n>','<div class=n style="font-size:70px;float:left;width:150px">'),
 rows(3,n,'dark','How it works','Program once.<br><span>Tap to switch.</span>',[('1','Start of term','We program all three timetables with you.'),('2','Exam morning','Tap A1. The exam timings take over.'),('3','Exams end','Tap A0. Your regular schedule was never touched.')],rtop=540),
 cta(4,n,'No reprogramming','Exam week,<br>sorted.',['A0 Regular','A1 Exam','A2 Vacation','Battery backup'])]
# Post 3 (no AI imagery)
n=5
big='<div class=circle style="right:80px;top:200px;width:420px;height:420px"><div class=n>0</div><div class=l>Missed bells</div></div>'
P['post-3-nighoje-zp-pilot']=[
 cover_graphic(1,n,'Government pilot','A ZP school.<br><span>Zero missed bells.</span>','Pilot at <b>Z.P. Primary School, Nighoje</b> (Khed, Pune), with permission from the DEO (Primary), Pune.',big,top_px=680,size=150),
 cards(2,n,'light','What was installed','One system,<br><span>every job</span>',[('01','Programmed bells','Every period on time.',0),('02','Marathi announcements','Clear voice-overs.',1),('03','Automatic prayers','Morning and evening.',1),('04','PA + emergency siren','One tap reaches every speaker.',0)],h=260,gtop=520)+'',
 page('dark', top(cnt(3,n))+'<div class=eyebrow>The results · Nov 2025 report</div><div class="title h" style="font-size:124px">What the<br><span>pilot recorded</span></div>'
   +'<div class=grid style="top:560px;grid-template-columns:1fr 1fr">'
   +'<div class="card inv" style="height:330px"><div class=n style="font-size:150px">0</div><h3>missed bells</h3></div>'
   +'<div class="card" style="height:330px"><div class=n style="font-size:150px">100%</div><h3>uptime, incl. power cuts</h3></div></div>'
   +'<div style="position:absolute;left:var(--m);right:var(--m);top:920px;font:500 30px/1.4 Barlow;color:#A9A39B">Clear sound confirmed in <b style="color:#fff">every classroom, corridor and outdoor area</b>, backed by battery with auto-charging.</div>'
   +bottom(3,n,'#fff',nxt())),
 rows(4,n,'light','What officials said','Recommended<br><span>for more schools</span>',[('B','Block Education Officer, Khed','Recommended expanding the system to more schools.'),('D','DEO (Primary), Pune','Recommended expansion across the district and state, and CSR sponsorship for rural schools.')],rtop=560),
 cta(5,n,'For ZP schools and CSR teams','Bring it to<br>your schools.',['Bulk orders','CSR projects','Marathi voice','Battery backup'])]
# Post 4 single (checklist)
items=[('1','Get the board’s exact timings','Including the warning bell.'),('2','Keep exam timings separate','Never edit your regular schedule.'),('3','Mark silent areas','Decide where bells must stay quiet.'),('4','Switch off music and prayers','During paper time.'),('5','Test during a power cut','Before exam day, not on it.')]
rs=''.join(f'<div class=row style="padding:22px 0"><div class=k style="width:64px;height:64px;font-size:38px;border-radius:18px">{k}</div><div><h3 style="font-size:40px">{t}</h3><p style="font-size:23px;margin-top:4px">{d}</p></div></div>' for k,t,d in items)
P['post-4-exam-bell-checklist']=[page('light', '<div class=ph style="height:420px;background-image:url(13-classroom-teacher-blackboard.png);background-position:center 45%"></div><div style="position:absolute;inset:0 0 auto 0;height:420px;background:linear-gradient(180deg,rgba(11,9,7,.55),rgba(11,9,7,0) 40%,rgba(246,244,240,0) 70%,var(--off))"></div>'
  +'<div class=top>'+BRAND.replace('<span class=brand>','<span class=brand style="color:#fff">').replace('<b>','<b style="color:var(--lime)">')+'<span class=chip style="background:var(--lime);color:var(--ink)">Save this</span></div>'
  +'<div style="position:absolute;left:var(--m);top:400px;font:700 20px Barlow;letter-spacing:5px;color:var(--olive)">BEFORE PRELIMS</div><div class=h style="position:absolute;left:var(--m);right:var(--m);top:440px;font-size:112px">Exam bell <span style="color:var(--olive)">checklist</span></div>'
  +f'<div style="position:absolute;left:var(--m);right:var(--m);top:580px">{rs}</div>'
  +'<div class=bottom><span class=next>SHARE WITH YOUR EXAM COORDINATOR</span><span class=next>SMARTSCHOOL360.CO.IN</span></div>', grain=False)]
# Post 5 FAQ
n=5
big5='<div class=circle style="right:80px;top:190px;width:400px;height:400px"><div class=n>5</div><div class=l>Questions</div></div>'
P['post-5-principals-faq']=[
 cover_graphic(1,n,'You asked','What principals<br><span>ask us first</span>','The five questions we hear on almost every first call, <b>answered plainly.</b>',big5,top_px=660,size=150),
 qas(2,n,'You asked · 1–2',[('What happens in a power cut?','<strong>The bells keep ringing.</strong> Battery backup with auto charging.'),('Is there a yearly fee?','<strong>None.</strong> It’s a one-time purchase.')]),
 qas(3,n,'You asked · 3–4',[('Are speakers included?','<strong>Quoted separately</strong>, based on your campus.'),('Can it announce in Marathi?','<strong>Yes.</strong> Voice announcements recorded by our team.')]),
 rows(4,n,'dark','You asked · 5','Who sets<br><span>it all up?</span>',[('1','We install','Site survey, fitting and wiring.'),('2','We program','Your timetable, prayers and announcements.'),('3','We train','Principal, office staff and support staff.')],rtop=540),
 cta(5,n,'Got another question?','Still curious?<br>Ask us.',['No yearly fee','Marathi voice','Battery backup','1-year warranty'])]
# Post 6 single siren
P['post-6-emergency-siren']=[page('dark','<div class=ph style="height:760px;background-image:url(07-corridor-students-walking.png);background-position:center 40%"></div>'+top(chip('School safety').replace('chip o','chip o" style="background:rgba(11,9,7,.45);border-color:rgba(255,255,255,.3)'))
  +'<div class=copy style="top:420px"><div class=h style="font-size:140px">One button.<br><span>Whole campus alerted.</span></div></div>'
  +'<div class=grid style="top:880px;grid-template-columns:repeat(3,1fr);gap:18px">'
  +''.join(f'<div class=card style="height:250px;padding:30px"><div class=n style="font-size:70px">{k}</div><h3 style="font-size:34px">{t}</h3><p style="font-size:21px">{d}</p></div>' for k,t,d in [('01','Tap the red triangle','On the main screen.'),('02','Confirm','Stops accidental alarms.'),('03','All zones sound','Overrides bells until staff stop it.')])
  +'</div>'+bottom(1,1,'#fff','<span class=next>PLAN YOUR DRILL AROUND IT</span>'))]
# Post 7 single model
mc=lambda m,a,z,d,pop: f'<div class="card{" inv" if pop else ""}" style="height:330px;padding:34px;position:relative">{"<span class=chip style=\"position:absolute;top:-20px;left:30px;background:var(--lime);color:var(--ink);font-size:15px;padding:8px 16px\">Most popular</span>" if pop else ""}<div class=n style="font-size:96px">{m}</div><h3 style="font-size:32px">{a}</h3><p style="font-size:24px;margin-top:14px"><b style="color:{"#fff" if pop else "var(--ink)"}">{z}</b><br>{d}</p></div>'
P['post-7-which-model-fits']=[page('light', top('<span class=chip style="background:var(--lime);color:var(--ink)">Free online demo</span>')
  +'<div class=eyebrow>Choose your model</div><div class="title h" style="font-size:118px">Which one fits<br><span>your campus?</span></div>'
  +'<div class=stage style="top:500px;height:300px"><img src=product.png style="width:520px"></div>'
  +'<div class=grid style="top:850px;grid-template-columns:repeat(3,1fr);gap:18px">'+mc('Z1','Small schools','Up to 2 zones','Classrooms + office',0)+mc('Z2','Most schools','4 zones','Classrooms, grounds, corridors',1)+mc('Z3','Large campuses','Full-campus','Several blocks and grounds',0)+'</div>'
  +'<div class=bottom><span class=next>SAME TOUCHSCREEN, SIREN, BATTERY</span><span class=next>WHATSAPP 98349 75938</span></div>', grain=False)]

os.makedirs('out',exist_ok=True)
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

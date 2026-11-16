import os,json
exec(open('gen.py').read().split('P={}')[0])
DEV='<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=Mukta:wght@500;700;800&display=block">'
_page=page
def page(cls,body,grain=True): return _page(cls,body,grain).replace('</head>',DEV+'</head>')
P={}

# 1. Annual day / sports day (carousel, 4)
n=4
P['post-1-annual-day']=[
 cover_photo(1,n,'assembly.png','Annual day · Sports day','Event season','<style>.ph:after{background:linear-gradient(180deg,rgba(11,9,7,.55) 0%,rgba(11,9,7,0) 20%,rgba(11,9,7,0) 50%,rgba(11,9,7,.9) 82%,#0B0907 100%)!important}</style>Big day?<br><span>Bells sorted.</span>','One system runs the bells, the mic and the music. <b>Switch to your event timetable with one tap.</b>',h=900,tagtop=640,copytop=710,size=150,pos='center 40%'),
 rows(2,n,'dark','On the day','One system,<br><span>whole programme</span>',[('A2','Event timetable','Tap A2. Rehearsal and event timings take over.'),('2','Mic for the anchor','Live announcements to every active zone.'),('3','Music from the MP3 player','Stored music, with its own volume.'),('4','Silent mode for speeches','Scheduled bells pause. Mic and music keep working.')],rtop=500,size=118),
 cards(3,n,'light','The week before','Set it up<br><span>once</span>',[('01','Program A2','Rehearsal and event-day timings.',0),('02','Choose your zones','Sound only where the event is.',1),('03','Set the volumes','Mic, music and each zone separately.',1),('04','Siren stays ready','One tap reaches every zone.',0)],h=290,gtop=500),
 cta(4,n,'Event season','Your big day,<br>on time.',['A2 Event mode','Live mic','MP3 music','Zone control'])]

# 2. Power cut (single)
batt='''<div style="position:absolute;left:0;right:0;top:150px;height:560px">
<div style="position:absolute;left:50%;top:52%;width:900px;height:520px;transform:translate(-50%,-50%);background:radial-gradient(ellipse,rgba(163,207,68,.22) 0%,rgba(163,207,68,0) 65%)"></div>
<img src=product-clean.png style="position:absolute;left:50%;top:150px;width:760px;transform:translateX(-50%)">
<div style="position:absolute;right:80px;top:40px;display:flex;align-items:center;gap:16px;background:#171411;border:2px solid #2a2622;border-radius:999px;padding:14px 26px 14px 18px">
<div style="width:72px;height:36px;border:4px solid var(--lime);border-radius:8px;position:relative;padding:4px"><div style="width:80%;height:100%;background:var(--lime);border-radius:3px"></div><div style="position:absolute;right:-12px;top:8px;width:6px;height:12px;background:var(--lime);border-radius:2px"></div></div>
<span style="font:700 20px Barlow;letter-spacing:3px;color:#fff">ON BATTERY</span></div></div>'''
P['post-2-power-cut']=[cover_graphic(1,1,'When the power goes out','Power cut at 10:59?<br><span>The 11:00 bell rings.</span>','Inbuilt battery backup with auto charging keeps every bell, prayer and announcement on schedule. <b>A battery indicator warns you before it runs low.</b>',batt,top_px=760,size=128)]

# 3. Marathi announcements (single, photo)
P['post-3-marathi-announcements']=[cover_photo(1,1,'slates.jpg','For Marathi-medium schools','<span style="font-family:Mukta;letter-spacing:0;font-size:24px;text-transform:none">मराठीत घोषणा</span>','<style>.ph:after{background:linear-gradient(180deg,rgba(11,9,7,.6) 0%,rgba(11,9,7,0) 20%,rgba(11,9,7,0) 55%,rgba(11,9,7,.92) 85%,#0B0907 100%)!important}</style>Announcements<br><span>in Marathi.</span>','Prayer time, recess, dismissal. <b>Clear Marathi voice-overs</b>, played automatically at the time you set.',h=880,tagtop=700,copytop=770,size=140,pos='center 45%')]

# 4. No IT team (single, photo)
P['post-4-no-it-team']=[cover_photo(1,1,'office.png','For office staff','No IT team needed','<style>.ph:after{background:linear-gradient(180deg,rgba(11,9,7,.55) 0%,rgba(11,9,7,0) 20%,rgba(11,9,7,0) 55%,rgba(11,9,7,.92) 85%,#0B0907 100%)!important}</style>Run by your office.<br><span>Not by IT.</span>','We install it, program your timetable and <b>train your principal, office admin and support staff</b>. Everyday use is a few taps on one touchscreen.',h=860,tagtop=680,copytop=750,size=132,pos='center 30%')]

# 5. Trusts with 3+ schools (single, graphic)
big='''<div style="position:absolute;right:-120px;top:120px;width:640px;height:640px;border-radius:50%;background:radial-gradient(circle,rgba(163,207,68,.18) 0%,rgba(163,207,68,0) 65%)"></div>
<div style="position:absolute;left:var(--m);top:200px;font:800 420px/.8 'Barlow Condensed';letter-spacing:-12px;color:var(--lime)">3+</div>
<div style="position:absolute;left:560px;top:250px;display:grid;grid-template-columns:repeat(3,120px);gap:20px">'''+''.join('<div style="height:120px;border-radius:24px;background:#171411;border:2px solid #2a2622;display:flex;align-items:center;justify-content:center"><img src=logo.png style="width:46px;border-radius:10px;opacity:.9"></div>' for _ in range(6))+'''</div>
<div style="position:absolute;left:560px;top:540px;font:700 20px Barlow;letter-spacing:3px;color:#8C867F">ONE PROPOSAL<br>FOR EVERY CAMPUS</div>'''
P['post-5-three-plus-schools']=[cover_graphic(1,1,'For trusts and school groups','Running 3 or<br><span>more schools?</span>','One custom proposal for all your campuses, with <b>a dedicated installation team and staggered payment on request.</b> Tailored quotes for government schools and NGOs.',big,top_px=700,size=140)]

# 6. New-term checklist (carousel, 3)
n=3
P['post-6-new-term-checklist']=[
 cover_photo(1,n,'gate.png','New year, new term','Before January','<style>.ph:after{background:linear-gradient(180deg,rgba(11,9,7,.55) 0%,rgba(11,9,7,0) 20%,rgba(11,9,7,0) 50%,rgba(11,9,7,.9) 82%,#0B0907 100%)!important}</style>Start 2027<br><span>on time.</span>','A 5-point bell check for the new term. <b>Save it for your first staff meeting.</b>',h=900,tagtop=660,copytop=730,size=160,pos='center 35%'),
 rows(2,n,'light','5 checks for the new term','The bell<br><span>checklist</span>',[('1','New term timings in A0','Any period that moved, update it now.'),('2','Exam timetable ready in A1','Prelims and boards come fast.'),('3','Battery indicator healthy','Test one bell with the power off.'),('4','Zone volumes right','Loud on the ground, soft near the library.'),('5','Password with admins only','No accidental changes to the schedule.')],rtop=470,size=118),
 cta(3,n,'Need help with any of these?','Every bell<br>on time in 2027.',['Timetables','Battery backup','Zones','Password lock'])]

manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

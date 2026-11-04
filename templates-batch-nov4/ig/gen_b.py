import os,json
exec(open('gen.py').read().split('P={}')[0])
P={}
ring=lambda x,y,s: f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;border:8px solid var(--lime);box-shadow:0 0 0 14px rgba(163,207,68,.25)"></div>'
# 1 no accidental bells
g=('<img src=password.png style="position:absolute;left:80px;top:200px;width:560px;border-radius:22px;box-shadow:0 30px 60px rgba(0,0,0,.5)">'
   '<img src=are-you-sure.png style="position:absolute;left:440px;top:400px;width:560px;border-radius:22px;border:3px solid #24201C;box-shadow:0 30px 60px rgba(0,0,0,.6)">'
   '<span class=chip style="position:absolute;left:110px;top:540px;background:var(--lime);color:var(--ink);z-index:3">Password lock</span>'
   '<span class=chip style="position:absolute;left:700px;top:370px;background:var(--lime);color:var(--ink);z-index:3">Are you sure?</span>')
P['post-1-no-accidental-bells']=[cover_graphic(1,1,'For office staff','No accidental<br><span>bells.</span>','Programming and settings sit behind a password. <b>Every manual bell asks “Are you sure?”</b> before it plays.',g,top_px=820,size=150)]
# 2 mic + bell
steps=[('10:58','Mic on','You start the morning announcement.','#fff','var(--ink)'),('11:00','Bell rings','The scheduled bell takes priority, right on time.','var(--lime)','var(--ink)'),('11:00','Mic back','Your announcement carries on by itself.','var(--ink)','#fff')]
tl=''.join(f'<div style="display:flex;gap:34px;align-items:center;margin-bottom:22px"><div style="flex:none;width:210px;height:150px;border-radius:26px;background:{bg};color:{fg};display:flex;align-items:center;justify-content:center;font:800 76px \'Barlow Condensed\';{"box-shadow:0 18px 40px rgba(11,9,7,.07)" if bg=="#fff" else ""}">{t}</div><div><div style="font:800 52px/1 \'Barlow Condensed\'">{h}</div><div style="margin-top:8px;font:500 27px/1.35 Barlow;color:#6B655E">{d}</div></div></div>' for t,h,d,bg,fg in steps)
P['post-2-mic-and-bell']=[page('light',top('<span class="chip o"><span class=dot style="color:var(--olive)"></span>Live announcements</span>')
 +'<div class=eyebrow>Mic and bells, together</div><div class="title h" style="font-size:118px">Mid-announcement?<br><span>The bell still rings.</span></div>'
 +f'<div style="position:absolute;left:var(--m);right:var(--m);top:560px">{tl}</div>'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:1120px;font:500 28px/1.4 Barlow;color:#6B655E">No one has to stop talking to ring the bell, and no one has to restart the mic.</div>'
 +bottom(1,1,'var(--ink)',URL),grain=False)]
# 3 play manually
shot='<img src=play-manually.png style="position:absolute;left:140px;top:190px;width:800px;border-radius:24px">'+'<div style="position:absolute;left:160px;top:440px;width:648px;height:190px;border-radius:18px;border:7px solid var(--lime);box-shadow:0 0 0 12px rgba(163,207,68,.25)"></div>'
P['post-3-play-manually']=[cover_graphic(1,1,'Plan changed?','Ring it<br><span>from here.</span>','Morning prayer, evening prayer, short bell, long bell and <b>8 manual buttons</b>. Tap, confirm, and it plays in every active zone.',shot,top_px=760,size=160)]
# 4 to the second
P['post-4-to-the-second']=[page('lime',top('<span class=chip style="background:var(--ink);color:var(--lime)">Wi-Fi time</span>')
 +'<div class=eyebrow>Not roughly. Exactly.</div><div class="title h" style="font-size:150px">Set to<br>the second.</div>'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:620px;height:330px;border-radius:32px;background:var(--ink);display:flex;align-items:center;justify-content:center;gap:6px;font:800 250px/1 \'Barlow Condensed\';color:#fff;letter-spacing:-4px">07:30<span style="color:var(--lime)">:00</span></div>'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:1000px;font:500 34px/1.38 Barlow;color:#2c3a10">Every bell is programmed to the second. <b style="color:var(--ink)">The clock sets itself from the internet</b>, so it never drifts.</div>'
 +bottom(1,1,'var(--ink)','<span class=next style="color:var(--ink)">SMARTSCHOOL360.CO.IN</span>'))]
# 5 carousel install
n=5
big='<div class=circle style="right:80px;top:200px;width:420px;height:420px"><div class=n>6</div><div class=l>Steps</div></div>'
P['post-5-first-call-to-first-bell']=[
 cover_graphic(1,n,'After you say yes','From first call<br><span>to first bell.</span>','Exactly what happens next. <b>No IT team needed</b> at your school.',big,top_px=700,size=156),
 rows(2,n,'light','Steps 1 to 3','We come<br><span>to you.</span>',[('1','Site survey','We visit and plan the speaker zones for your campus.'),('2','Install','Controller, speakers and wiring fitted.'),('3','Program','Your timetable, prayers and announcements, entered for you.')],rtop=540),
 rows(3,n,'dark','Steps 4 to 6','Then it<br><span>runs itself.</span>',[('4','Test','Every bell and every zone checked for sound.'),('5','Train','Principal, office staff and support staff.'),('6','Go live','Your school day runs on its own.')],rtop=540),
 cards(4,n,'light','Your part','Just two<br><span>things.</span>',[('01','Share your timetable','Periods, prayers, breaks, exam days.',0),('02','Pick a day for the visit','We handle the rest, in Marathi, Hindi or English.',1)],cols=1,h=250,gtop=560),
 cta(5,n,'Start with step zero','See it before<br>you decide.',['Site survey','Installation','Programming','Staff training'])]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

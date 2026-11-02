import os,json
exec(open('gen.py').read().split('P={}')[0])
P={}
n=4
P['post-1-exam-timetables']=[
 cover_photo(1,n,'12-exam-hall.png','For exam coordinators','Prelims season','Exam timings.<br><span>One tap.</span>','Keep a separate exam timetable ready. <b>Switch to it on exam morning</b>, switch back when papers end.'),
 cards(2,n,'light','Three timetables, one device','Every school runs<br><span>3 timetables</span>',[('A0','Regular','Your everyday school day.',0),('A1','Exam','Adjusted bell times for exam days.',1),('A2','Vacation or special','Holidays, Saturday lessons and events.',0)],cols=3,h=380,gtop=560)[:-14]+'<div style="position:absolute;left:var(--m);right:var(--m);top:990px;font:500 30px/1.4 Barlow;color:#6B655E">All three live on the same device. Switch between them with one tap on <b style="color:var(--ink)">MODE</b>.</div></body></html>',
 rows(3,n,'dark','How it works','Program once.<br><span>Tap to switch.</span>',[('1','Start of term','We program all three timetables with you.'),('2','Exam morning','Tap A1. The exam timings take over.'),('3','Exams end','Tap A0. Your regular schedule was never touched.')],rtop=540),
 cta(4,n,'No reprogramming','Exam week,<br>sorted.',['A0 Regular','A1 Exam','A2 Vacation','Battery backup'])]
# post 2 silent mode
shot='<img src=main-screen.png style="position:absolute;left:160px;top:190px;width:760px;border-radius:24px">'+'<div style="position:absolute;left:427px;top:257px;width:150px;height:150px;border-radius:50%;border:8px solid var(--lime);box-shadow:0 0 0 14px rgba(163,207,68,.25)"></div>'+'<span class=chip style="position:absolute;left:445px;top:420px;background:var(--lime);color:var(--ink)">Tap ✕</span>'
P['post-2-silent-mode']=[cover_graphic(1,1,'VIP visit or assembly','One tap.<br><span>Bells pause.</span>','Silent mode pauses every scheduled bell. <b>The mic and music still work.</b> Tap again and the schedule carries on from the next bell.',shot,top_px=790,size=160)]
# post 3 weekday prayers
days=[('MON','Morning prayer'),('TUE','National anthem'),('WED','School prayer'),('THU','Pledge'),('FRI','School song'),('SAT','Calm audio')]
rws=''.join(f'<div style="display:flex;align-items:center;gap:28px;padding:18px 0;border-top:2px solid rgba(11,9,7,.08)"><span style="width:110px;font:800 44px \'Barlow Condensed\';color:var(--olive)">{d}</span><span style="font:700 26px Barlow;letter-spacing:2px;color:var(--mute)">07:30</span><span style="font:800 40px \'Barlow Condensed\'">{a}</span></div>' for d,a in days)
P['post-3-weekday-prayers']=[page('light',top('<span class="chip o"><span class=dot style="color:var(--olive)"></span>Example timetable</span>')+'<div class=eyebrow>Same time, different audio</div><div class="title h" style="font-size:120px">A different prayer<br><span>every morning.</span></div>'
 +f'<div style="position:absolute;left:var(--m);width:520px;top:520px">{rws}</div>'+'<img src=play-manually-p1.png style="position:absolute;right:70px;top:610px;width:380px;border-radius:20px">'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:1120px;font:500 28px/1.4 Barlow;color:#6B655E">Set each day once. It plays at 07:30 on its own, every week.</div>'+bottom(1,1,'var(--ink)',URL),grain=False)]
# post 4 zone volume
zs=[('Classrooms',60),('Office',35),('Ground',95),('Library',15),('Corridors',50)]
meters=''.join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center"><div style="width:64px;height:170px;border-radius:14px;background:#24201C;position:relative;overflow:hidden"><div style="position:absolute;left:0;right:0;bottom:0;height:{v}%;background:var(--lime)"></div></div><div style="margin-top:14px;font:800 30px \'Barlow Condensed\'">{nm}</div><div style="font:700 18px Barlow;letter-spacing:2px;color:#8C867F">ZONE {k+1}</div></div>' for k,(nm,v) in enumerate(zs))
P['post-4-zone-volume']=[page('dark',top('<span class="chip o"><span class=dot style="color:var(--lime)"></span>Zone by zone</span>')+'<div class=eyebrow>Up to 5 speaker zones</div><div class="title h" style="font-size:110px">Loud on the ground.<br><span>Soft in the library.</span></div>'
 +'<img src=zone-selection.png style="position:absolute;left:240px;top:470px;width:600px;border-radius:24px">'
 +f'<div style="position:absolute;left:var(--m);right:var(--m);top:940px;display:flex;gap:10px">{meters}</div>'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:1310px"></div>'+bottom(1,1,'#fff',URL))]
os.makedirs('out',exist_ok=True)
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

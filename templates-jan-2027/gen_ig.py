import os,json
exec(open('gen.py').read().split('P={}')[0])
DEV='<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=Mukta:wght@500;700;800&display=block">'
_page=page
def page(cls,body,grain=True): return _page(cls,body,grain).replace('</head>',DEV+'</head>')
P={}
M='font-family:Mukta;letter-spacing:0'

# 2. Quiz carousel: how many bells a day
n=4
day=[('07:25','First bell'),('07:30','Prayer'),('07:45','Period 1'),('08:25','Period 2'),('09:05','Period 3'),('09:25','Water bell'),('09:45','Period 4'),('10:25','Recess'),('10:45','Period 5'),('11:25','Period 6'),('12:05','Lunch'),('12:35','Period 7'),('13:15','Period 8'),('13:55','Dismissal')]
cells=''.join(f'<div style="display:flex;align-items:center;gap:18px;padding:16px 22px;border-radius:18px;background:#fff;box-shadow:0 8px 20px rgba(11,9,7,.05)"><span style="width:44px;height:44px;border-radius:12px;background:{"var(--lime)" if k%2==0 else "var(--ink)"};color:{"var(--ink)" if k%2==0 else "var(--lime)"};display:flex;align-items:center;justify-content:center;font:800 26px \'Barlow Condensed\'">{k+1}</span><span style="font:700 24px Barlow;letter-spacing:1px;color:var(--mute);width:78px">{t}</span><span style="font:800 32px \'Barlow Condensed\'">{a}</span></div>' for k,(t,a) in enumerate(day))
q='<div style="position:absolute;right:-60px;top:170px;font:800 760px/.8 \'Barlow Condensed\';color:transparent;-webkit-text-stroke:4px rgba(163,207,68,.35)">?</div>'
P['post-2-bell-quiz']=[
 cover_graphic(1,n,'Quick quiz','How many times<br>does a school bell<br><span>ring in one day?</span>','Guess a number, <b>then swipe</b> for the answer.',q,top_px=640,size=136),
 page('light',top(cnt(2,n))+'<div class=eyebrow>An example 8-period day</div><div class="title h" style="font-size:118px">The answer:<br><span>14 bells.</span></div>'
   +f'<div style="position:absolute;left:var(--m);right:var(--m);top:500px;display:grid;grid-template-columns:1fr 1fr;gap:14px">{cells}</div>'
   +'<div style="position:absolute;left:var(--m);right:var(--m);top:1150px;font:500 28px/1.4 Barlow;color:#6B655E">Did you guess right? <b style="color:var(--ink)">Comment your guess</b>, and how many your school rings.</div>'+bottom(2,n,'var(--ink)',nxt()),grain=False),
 page('dark',top(cnt(3,n))+'<div class=eyebrow>Now multiply it</div>'
   +'<div style="position:absolute;left:var(--m);right:var(--m);top:250px;display:flex;align-items:baseline;gap:30px;font:800 200px/.9 \'Barlow Condensed\'"><span>14</span><span style="font-size:90px;color:#8C867F">×</span><span>220</span></div>'
   +'<div style="position:absolute;left:var(--m);top:450px;font:700 22px Barlow;letter-spacing:4px;color:#8C867F">BELLS A DAY &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SCHOOL DAYS</div>'
   +'<div style="position:absolute;left:var(--m);right:var(--m);top:540px;border-top:3px solid #24201C;padding-top:40px;font:800 290px/.85 \'Barlow Condensed\';color:var(--lime);letter-spacing:-6px">3,000+</div>'
   +'<div style="position:absolute;left:var(--m);right:var(--m);top:860px;font:800 62px/1 \'Barlow Condensed\'">bells a year.</div>'
   +'<div style="position:absolute;left:var(--m);right:var(--m);top:960px;font:500 32px/1.4 Barlow;color:#BDB7AF">Each one needs <b style="color:#fff">someone watching the clock</b>. Or a system that never forgets.</div>'
   +bottom(3,n,'#fff',nxt())),
 cta(4,n,'Every one of them','3,000 bells.<br>Zero reminders.',['Bells','Prayers','Water bell','Announcements'])]

# 3. Poll: which would you switch on first
opts=[('1','💧','Water bell','A reminder to drink water between periods.'),('2','🗣️','Marathi announcements','Clear voice-overs at the time you set.'),('3','🙏','A different prayer daily','Same time, new prayer each weekday.'),('4','🚨','Emergency siren','One tap reaches every zone.')]
tiles=''.join(f'<div style="position:relative;background:{"#171411" if k in (1,2) else "#1d1a17"};border:2px solid #2a2622;border-radius:28px;padding:34px 34px 36px;height:330px"><div style="position:absolute;right:28px;top:20px;font:800 120px/1 \'Barlow Condensed\';color:var(--lime)">{n_}</div><div style="font-size:64px">{e}</div><div style="margin-top:22px;font:800 44px/1 \'Barlow Condensed\';max-width:300px">{t}</div><div style="margin-top:12px;font:500 24px/1.35 Barlow;color:#A9A39B">{d}</div></div>' for k,(n_,e,t,d) in enumerate(opts))
P['post-3-switch-on-first']=[page('dark',top(chip('Reply with a number'))+'<div class=eyebrow>Quick poll</div><div class="title h" style="font-size:112px">Which would you<br><span>switch on first?</span></div>'
 +f'<div style="position:absolute;left:var(--m);right:var(--m);top:500px;display:grid;grid-template-columns:1fr 1fr;gap:22px">{tiles}</div>'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:1230px;font:700 26px Barlow;letter-spacing:2px;color:#fff">REPLY <span style="color:var(--lime)">1, 2, 3 OR 4</span> IN THE COMMENTS</div>')]

# 5. Makar Sankranti greeting
kite=lambda x,y,s,r,c: f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;transform:rotate({r}deg)"><div style="position:absolute;inset:0;transform:rotate(45deg) scale(.72);background:{c};border-radius:8px"></div><div style="position:absolute;left:50%;top:0;bottom:0;width:3px;background:rgba(11,9,7,.35)"></div><div style="position:absolute;left:0;right:0;top:50%;height:3px;background:rgba(11,9,7,.35)"></div></div>'
string='<svg style="position:absolute;left:0;top:0" width="1080" height="1350"><path d="M760 330 C 700 520, 900 640, 820 900" stroke="rgba(11,9,7,.35)" stroke-width="3" fill="none"/><path d="M560 250 C 500 420, 640 520, 600 700" stroke="rgba(11,9,7,.25)" stroke-width="3" fill="none"/></svg>'
dots=''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{d}px;height:{d}px;border-radius:50%;background:{c}"></div>' for x,y,d,c in [(90,1010,26,'#fff'),(140,1050,18,'#0B0907'),(190,1012,22,'#fff'),(960,1060,24,'#fff'),(910,1100,16,'#0B0907')])
P['post-5-makar-sankranti']=[page('lime',string+kite(640,150,240,-12,'#0B0907')+kite(470,120,150,10,'#fff')+kite(860,300,110,18,'#fff')+top('<span></span>')
 +'<div class=eyebrow style="top:520px">Happy Makar Sankranti</div>'
 +f'<div class="title" style="top:570px;{M};font:800 118px/1.1 Mukta">तिळगूळ घ्या,<br>गोड गोड बोला.</div>'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:880px;font:500 34px/1.4 Barlow;max-width:820px">Wishing every student, teacher and school family a sweet and bright Sankranti.</div>'
 +dots+'<div class=bottom><span style="font:700 20px Barlow;letter-spacing:3px">FROM ALL OF US AT CORTEK ELECTRO</span><span style="font:700 20px Barlow;letter-spacing:3px">14 · 01 · 2027</span></div>',grain=False)]

# 6. Spot the mistake
tt=[('07:45','Period 1',0),('08:25','Period 2',0),('09:05','Period 3',0),('09:45','Period 4',0),('10:25','Recess',0),('10:40','Period 5',0),('11:25','Period 6',0)]
rs=''.join(f'<div style="display:flex;align-items:center;padding:17px 30px;border-top:2px solid #EEEBE6"><span style="width:200px;font:700 44px Barlow;letter-spacing:1px">{t}</span><span style="font:800 46px \'Barlow Condensed\'">{a}</span><span style="margin-left:auto;font:700 18px Barlow;letter-spacing:3px;color:var(--mute)">BELL {k+1:02d}</span></div>' for k,(t,a,_) in enumerate(tt))
P['post-6-spot-the-mistake']=[page('light',top(chip('Puzzle'))+'<div class=eyebrow>One of these bells is wrong</div><div class="title h" style="font-size:120px">Spot the<br><span>mistake.</span></div>'
 +'<div style="position:absolute;left:var(--m);top:500px;right:var(--m);background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 18px 40px rgba(11,9,7,.07)">'
 +'<div style="padding:22px 30px;font:700 18px Barlow;letter-spacing:4px;color:var(--mute);background:#FAF9F7">TIME &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; BELL · RECESS IS 20 MINUTES</div>'+rs+'</div>'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:1245px;font:700 24px Barlow;letter-spacing:2px">COMMENT THE <span style="color:var(--olive)">TIME</span> YOU THINK IS WRONG</div>',grain=False)]

# 7. Republic Day (image, also Reel end card)
flag='<div style="position:absolute;left:0;right:0;top:0;height:14px;display:flex"><div style="flex:1;background:#FF9933"></div><div style="flex:1;background:#fff"></div><div style="flex:1;background:#138808"></div></div>'
chakra='<svg style="position:absolute;right:-180px;top:180px;opacity:.16" width="760" height="760" viewBox="-100 -100 200 200"><circle r="92" fill="none" stroke="#fff" stroke-width="6"/><circle r="12" fill="#fff"/>'+''.join(f'<line x1="0" y1="0" x2="0" y2="-90" stroke="#fff" stroke-width="3" transform="rotate({i*15})"/>' for i in range(24))+'</svg>'
P['post-7-republic-day']=[page('dark',flag+chakra+top('<span></span>')
 +'<div class=eyebrow style="top:600px">26 January 2027</div>'
 +'<div class="title h" style="top:650px;font-size:150px">Happy<br><span>Republic Day.</span></div>'
 +f'<div style="position:absolute;left:var(--m);right:var(--m);top:1000px;{M};font:700 52px/1.2 Mukta;color:#fff">प्रजासत्ताक दिनाच्या हार्दिक शुभेच्छा!</div>'
 +'<div style="position:absolute;left:var(--m);right:var(--m);top:1090px;font:500 30px/1.4 Barlow;color:#BDB7AF">To every school starting the day with the anthem and the flag.</div>'
 +bottom(1,1,'#fff',URL))]

manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

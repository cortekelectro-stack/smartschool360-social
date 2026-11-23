import os,json
exec(open('gen3.py').read().split('P={}')[0])
H=H.replace('</head>','<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=Mukta:wght@600;700;800&display=block"></head>')
def pg(body,cls='',bg=''): return H+f'<body class="{cls}" style="{bg}">{body}</body></html>'
P={}
W='smartschool360.co.in'
T=lambda top,txt,size=100,col='': f'<div class=abs style="left:80px;right:80px;top:{top}px;font:900 {size}px/0.95 Inter Tight;letter-spacing:-{size//25}px;{col}">{txt}</div>'
S=lambda top,txt,col='var(--mute)',right=80: f'<div class=abs style="left:80px;right:{right}px;top:{top}px;font:500 30px/1.4 Inter Tight;color:{col}">{txt}</div>'

# L1 water bell: product showcase on paper
P['l1-water-bell']=[pg(hd()+'<div class="abs m" style="left:80px;top:200px;color:var(--mute)">09:25 · Between Period 3 and 4</div>'+T(240,'The bell that<br>isn\'t for class.',100)
 +'<div class=abs style="left:80px;right:80px;top:520px;height:470px;border-radius:32px;background:#fff;box-shadow:0 24px 60px rgba(11,12,10,.08);overflow:hidden"><img src=device-front-white.png style="position:absolute;left:50%;top:50%;width:640px;transform:translate(-50%,-50%)"></div>'
 +'<div class=abs style="left:80px;top:1040px;display:flex;align-items:center;gap:20px"><span style="font-size:54px">💧</span><span style="font:800 52px Inter Tight;letter-spacing:-1.5px">The water bell.</span></div>'
 +S(1120,'A scheduled reminder for students to drink water between periods.','var(--mute)')
 +ft('Free online demo',W,'color:var(--mute)'),bg='background:var(--paper)')]

# L2 data: bells a year
P['l2-bells-a-year']=[pg(hd('Smart School 360','color:#F4F3EE')+'<div class="abs m" style="left:80px;top:210px;color:#8D8F87">An example 8-period school day</div>'
 +'<div class=abs style="left:80px;top:250px;font:900 120px/1 Inter Tight;letter-spacing:-5px;color:#F4F3EE">14 <span style="color:#55574F">×</span> 220</div>'
 +'<div class="abs m" style="left:80px;top:395px;color:#8D8F87">Bells a day &nbsp;·&nbsp; School days</div>'
 +'<div class=abs style="left:80px;right:80px;top:470px;border-top:3px solid #2A2C26"></div>'
 +'<div class=abs style="left:60px;top:500px;font:900 330px/1 Inter Tight;letter-spacing:-18px;color:var(--lime)">3,080</div>'
 +T(860,'bells a year.',84,'color:#F4F3EE')
 +S(990,'Each one rung by someone watching the clock, or by a system that never forgets.','#A9AAA3',160)
 +ft('Free online demo',W,'color:#8D8F87'),'dark',bg='background:#0B0C0A')]

# L3 poll
opts=[('1','Water bell'),('2','Marathi announcements'),('3','A different prayer each day'),('4','Emergency siren')]
rr=''.join(f'<div style="display:flex;align-items:center;gap:36px;padding:30px 36px;border-radius:24px;background:{"#0B0C0A;color:#F4F3EE" if k==0 else "#fff"};margin-bottom:18px"><span style="font:900 72px/1 Inter Tight;color:{"var(--lime)" if k==0 else "var(--ink)"};width:60px">{n}</span><span style="font:800 44px Inter Tight;letter-spacing:-1.5px">{t}</span></div>' for k,(n,t) in enumerate(opts))
P['l3-poll']=[pg(hd()+'<div class="abs m" style="left:80px;top:200px;color:var(--ink)">Quick poll for school leaders</div>'+T(240,'Which would you<br>switch on first?',100)
 +f'<div class=abs style="left:80px;right:80px;top:520px">{rr}</div>'
 +S(1150,'Reply with a number in the comments.','var(--ink)')
 +ft('Smart School 360',W,'color:var(--ink)'),bg='background:var(--lime)')]

# L4 Sankranti
P['l4-makar-sankranti']=[pg(hd()+'<div class="abs m" style="left:80px;top:250px;color:var(--mute)">14 January 2027</div>'
 +'<div class=abs style="left:80px;right:80px;top:300px;font:800 120px/1.12 Mukta;color:var(--ink)">तिळगूळ घ्या,<br>गोड गोड बोला.</div>'
 +T(640,'Happy<br>Makar Sankranti.',92)
 +S(880,'Wishing every student, teacher and school family a sweet and bright Sankranti.','var(--mute)',200)
 +'<svg class=abs style="right:80px;top:960px" width="200" height="230" viewBox="0 0 260 300"><path d="M130 10 L230 110 L130 210 L30 110 Z" fill="#A3CF44"/><path d="M130 10 V210 M30 110 H230" stroke="#0B0C0A" stroke-width="3"/><path d="M130 210 C 110 250, 160 260, 140 300" stroke="#0B0C0A" stroke-width="3" fill="none"/></svg>'
 +ft('Cortek Electro',W,'color:var(--mute)'),bg='background:#fff')]

# L5 spot the mistake
tt=[('07:45','Period 1'),('08:25','Period 2'),('09:05','Period 3'),('09:45','Period 4'),('10:25','Recess (20 min)'),('10:40','Period 5'),('11:25','Period 6')]
rows=''.join(f'<div style="padding:17px 34px;border-top:2px solid #23251F;display:flex"><span style="width:200px;font:700 36px Roboto Mono;color:var(--lime)">{t}</span><span style="font:700 34px Roboto Mono;color:#F4F3EE;letter-spacing:1px">{a.upper()}</span></div>' for t,a in tt)
P['l5-spot-the-mistake']=[pg(hd()+T(190,'One bell is wrong.<br>Can you spot it?',92)
 +f'<div class=abs style="left:80px;right:80px;top:450px;background:var(--ink);border-radius:28px;overflow:hidden"><div class=m style="padding:24px 34px;color:#8D8F87;font-size:16px">Time &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Bell</div>{rows}</div>'
 +S(1190,'Comment the time you think is wrong.','var(--ink)')
 +ft('Puzzle',W,'color:var(--ink)'),bg='background:var(--paper)')]

# L6 Republic Day
P['l6-republic-day']=[pg('<div class=abs style="left:0;right:0;top:0;height:16px;display:flex"><div style="flex:1;background:#FF9933"></div><div style="flex:1;background:#fff"></div><div style="flex:1;background:#138808"></div></div>'
 +hd('Smart School 360','color:#F4F3EE')+'<div class="abs m" style="left:80px;top:420px;color:var(--lime)">26 January 2027</div>'
 +T(470,'Happy<br>Republic Day.',130,'color:#F4F3EE')
 +'<div class=abs style="left:80px;right:80px;top:790px;font:700 54px/1.2 Mukta;color:#F4F3EE">प्रजासत्ताक दिनाच्या हार्दिक शुभेच्छा!</div>'
 +S(900,'To every school that starts the day with the flag and the anthem.','#A9AAA3',200)
 +ft('Cortek Electro',W,'color:#8D8F87'),'dark',bg='background:#0B0C0A')]

manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post'; open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

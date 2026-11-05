import math,os
D=os.path.dirname(os.path.abspath(__file__))
def diya(w, flame=True, glow=True, uid='a'):
    # clay lamp with flame; viewBox 200x160
    g=f'''<svg width="{w}" height="{w*0.8:.0f}" viewBox="0 0 200 160" style="overflow:visible">
<defs>
<radialGradient id="gl{uid}" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFC24A" stop-opacity=".75"/><stop offset=".35" stop-color="#FF8A1F" stop-opacity=".28"/><stop offset="1" stop-color="#FF8A1F" stop-opacity="0"/></radialGradient>
<linearGradient id="fl{uid}" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#FF6A13"/><stop offset=".45" stop-color="#FFB627"/><stop offset="1" stop-color="#FFF4C2"/></linearGradient>
<linearGradient id="cl{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D9682E"/><stop offset="1" stop-color="#8A3315"/></linearGradient>
</defs>
{f'<circle cx="100" cy="52" r="110" fill="url(#gl{uid})"/>' if glow else ''}
<path d="M14 92 Q100 82 186 92 Q176 150 100 152 Q24 150 14 92Z" fill="url(#cl{uid})"/>
<path d="M14 92 Q100 82 186 92 Q100 104 14 92Z" fill="#5A1F0B"/>
<path d="M186 92 Q196 86 199 76 Q190 94 176 98Z" fill="#B44E22"/>
<path d="M40 118 Q100 128 160 118" stroke="#F2B544" stroke-width="3" fill="none" stroke-dasharray="2 9" stroke-linecap="round"/>
<path d="M30 104 Q100 114 170 104" stroke="#F2B544" stroke-width="2.5" fill="none" opacity=".7"/>
{f'<path d="M100 18 C116 44 118 62 112 74 C108 82 92 82 88 74 C82 62 86 44 100 18Z" fill="url(#fl{uid})"/><path d="M100 50 C106 60 106 68 103 73 C101 76 99 76 97 73 C94 68 94 60 100 50Z" fill="#fff8de"/><rect x="98.5" y="74" width="3" height="14" rx="1.5" fill="#3a1608"/>' if flame else ''}
</svg>'''
    return g

def rangoli(size, uid='r'):
    c=size/2; parts=[]
    # outer 12 hour-marker petals (clock nod)
    for i in range(12):
        a=i*30
        parts.append(f'<g transform="rotate({a} {c} {c})"><path d="M{c} {c-size*0.49} Q{c+size*0.055} {c-size*0.41} {c} {c-size*0.33} Q{c-size*0.055} {c-size*0.41} {c} {c-size*0.49}Z" fill="{"#A3CF44" if i%3==0 else "#F2B544"}"/></g>')
    for i in range(24):
        a=i*15+7.5
        parts.append(f'<g transform="rotate({a} {c} {c})"><circle cx="{c}" cy="{c-size*0.42}" r="{size*0.009}" fill="#FFF4C2" opacity=".8"/></g>')
    parts.append(f'<circle cx="{c}" cy="{c}" r="{size*0.315}" fill="none" stroke="#F2B544" stroke-width="3" stroke-dasharray="1 14" stroke-linecap="round"/>')
    for i in range(8):
        a=i*45
        parts.append(f'<g transform="rotate({a} {c} {c})"><path d="M{c} {c-size*0.30} Q{c+size*0.09} {c-size*0.2} {c} {c-size*0.12} Q{c-size*0.09} {c-size*0.2} {c} {c-size*0.30}Z" fill="none" stroke="#E2603A" stroke-width="5"/><circle cx="{c}" cy="{c-size*0.205}" r="{size*0.014}" fill="#A3CF44"/></g>')
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'+''.join(parts)+'</svg>'

FONTS="@import url('https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Marathi&display=block');"
ig=f'''<html><head><link rel=stylesheet href=base.css><style>{FONTS}
body{{background:radial-gradient(ellipse at 50% 30%,#2A1A0C 0%,#140D07 45%,#0B0907 80%);color:#fff}}
.rg{{position:absolute;left:50%;top:170px;transform:translateX(-50%);opacity:.95}}
.dc{{position:absolute;left:50%;top:365px;transform:translateX(-50%)}}
.copy{{position:absolute;left:var(--m);right:var(--m);top:790px;z-index:2}}.copy .h{{font-size:176px}}.copy .h span{{color:#F2B544}}.copy p{{color:#BDB7AF;font-weight:500;line-height:1.38}}.copy p b{{color:#fff;font-weight:600}}
.mr{{font:400 40px 'Tiro Devanagari Marathi';color:var(--lime);margin-bottom:14px;letter-spacing:.5px}}
.copy p{{margin-top:28px;font-size:33px;max-width:880px}}
.row{{position:absolute;left:0;right:0;bottom:150px;display:flex;justify-content:center;gap:34px;border:0;padding:0}}
.sig{{font:700 20px Barlow;letter-spacing:3px;text-transform:uppercase;color:#BDB7AF}}.web{{font:700 20px Barlow;letter-spacing:3px;color:var(--lime)}}
.chip.o{{border:2px solid rgba(242,181,68,.45);color:#fff}}
</style></head><body class=grain>
<div class=rg>{rangoli(560)}</div>
<div class=dc>{diya(300,uid='m')}</div>
<div class=top><span class=brand><img src=logo.png>SMART SCHOOL <b>360</b></span><span class="chip o"><span class=dot style="color:#F2B544"></span>Festival of lights</span></div>
<div class=copy><div class=mr>शुभ दीपावली</div><div class=h>Happy <span>Diwali.</span></div>
<p>The school bell is on holiday. <b>May every other bell this Diwali ring for joy.</b></p></div>
<div class=bottom><span class=sig>From team Cortek Electro</span><span class=web>SMARTSCHOOL360.CO.IN</span></div>
</body></html>'''
open(D+'/ig.html','w').write(ig)

li=f'''<html><head><link rel=stylesheet href=li.css><style>{FONTS}
body{{background:var(--paper)}}
.lines{{position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent 0 179px,rgba(11,12,10,.05) 179px 180px)}}
.mr{{font:400 46px 'Tiro Devanagari Marathi';color:#B4561F}}
.big{{font:900 168px/.88 'Inter Tight';letter-spacing:-8px}}
.big span{{color:#D9682E}}
.dy{{position:absolute;right:90px;top:200px}}
.rule{{position:absolute;left:80px;right:80px;top:760px;height:3px;background:var(--ink)}}
.msg{{position:absolute;left:80px;right:80px;top:820px;font:600 46px/1.18 'Inter Tight';letter-spacing:-1.2px}}
.msg em{{font-style:normal;color:var(--mute);font-weight:500}}
</style></head><body>
<div class=lines></div>
<div class=hd><div class=lg><img src=logo.png><span class=m>Cortek Electro</span></div><span class=m>Smart School 360</span></div>
<div class=dy>{diya(400,uid='l')}</div>
<div class="abs m" style="left:80px;top:230px;color:var(--mute)">Deepavali 2026</div>
<div class="abs mr" style="left:80px;top:290px">शुभ दीपावली</div>
<div class="abs big" style="left:74px;top:390px">Happy<br><span>Diwali.</span></div>
<div class=rule></div>
<div class=msg>To every principal, teacher, office admin and peon who keeps a school running on time: thank you.<br><br><em>May this festival of lights bring you rest, warmth and a well-earned holiday.</em></div>
<div class=ft><span class=m style="color:var(--mute)">From the team in Pune</span><span class=m style="color:var(--mute)">smartschool360.co.in</span></div>
</body></html>'''
open(D+'/li.html','w').write(li)

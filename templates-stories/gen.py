CSS="""@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&display=block');
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#0B0907;--lime:#A3CF44;--off:#F6F4F0;--mute:#8C867F}
html,body{width:1080px;height:1920px;overflow:hidden;font-family:Barlow,sans-serif;-webkit-font-smoothing:antialiased;background:var(--ink);color:var(--off)}
.a{position:absolute}.L{left:90px;right:90px}
.brand{display:inline-flex;align-items:center;gap:16px;font:800 34px 'Barlow Condensed';letter-spacing:.6px}
.brand img{width:50px;height:50px;border-radius:11px}.brand b{color:var(--lime)}
.chip{display:inline-flex;align-items:center;gap:12px;border-radius:999px;padding:14px 28px;font:700 22px Barlow;letter-spacing:3px;text-transform:uppercase}
.dot{width:9px;height:9px;border-radius:50%;background:currentColor}
.h{font-family:'Barlow Condensed';font-weight:800;letter-spacing:-2px;line-height:.9}
.g{color:var(--lime)}
.p{font-size:40px;line-height:1.35;color:#CFCAC3}
.btn{display:inline-flex;align-items:center;gap:16px;background:var(--lime);color:var(--ink);border-radius:999px;padding:26px 44px;font:700 38px Barlow}
"""
def page(body,bg='var(--ink)',fg='var(--off)'):
    return f'<html><head><meta charset=utf-8><style>{CSS}</style></head><body style="background:{bg};color:{fg}">{body}</body></html>'
brand=lambda c='var(--off)',b='var(--lime)':f'<div class="a L" style="top:250px;color:{c}"><span class=brand><img src=logo.png>SMART SCHOOL <b style="color:{b}">360</b></span></div>'
S={}
# 1. 2 Nov: hello / what we do (full product photo on white card)
S['s1-hello']=page(brand()+
 '<div class="a L" style="top:400px"><div class="chip" style="border:2px solid #3a3631;color:var(--lime)"><i class=dot></i>New on Instagram</div>'
 '<div class=h style="font-size:150px;margin-top:44px">Hello from<br><span class=g>Pune.</span></div>'
 '<div class=p style="margin-top:36px;max-width:840px">One touchscreen that runs a school\'s whole day: bells, prayers, announcements and the emergency siren.</div></div>'
 '<div class=a style="left:90px;right:90px;top:1060px;height:560px;border-radius:36px;background:#fff url(photo.png) center/auto 118% no-repeat"></div>')
# 2. 4 Nov: teaser for feed post
S['s2-who-rings']=page(brand()+
 '<svg class=a style="right:-260px;top:330px;opacity:.9" width="900" height="900" viewBox="0 0 200 200"><circle cx=100 cy=100 r=96 fill=none stroke="#2b2824" stroke-width="1.2"/>'
 +''.join(f'<line x1=100 y1=8 x2=100 y2=18 stroke="#6b655e" stroke-width="1.6" transform="rotate({i*30} 100 100)"/>' for i in range(12))+
 '<line x1=100 y1=100 x2=100 y2=34 stroke="#A3CF44" stroke-width="3" stroke-linecap=round transform="rotate(54 100 100)"/><line x1=100 y1=100 x2=100 y2=56 stroke="#F6F4F0" stroke-width="3" stroke-linecap=round transform="rotate(330 100 100)"/><circle cx=100 cy=100 r=5 fill="#A3CF44"/></svg>'
 '<div class="a L" style="top:1000px"><div class=h style="font-size:170px">Who rings<br>your <span class=g>school<br>bell?</span></div>'
 '<div class=p style="margin-top:40px">New post on our page today.<br>Tap our name to see it.</div></div>')
# 3. 5 Nov: poll-style question (works without a sticker: reply YES/NO)
S['s3-poll']=page(brand('var(--ink)','var(--ink)')+
 '<div class="a L" style="top:420px"><div class="chip" style="background:var(--ink);color:var(--lime)"><i class=dot></i>Quick question</div>'
 '<div class=h style="font-size:156px;margin-top:48px;color:var(--ink)">Is your school bell still rung by hand?</div></div>'
 '<div class="a L" style="top:1150px;display:flex;gap:28px">'
 '<div style="flex:1;background:var(--ink);color:var(--off);border-radius:32px;padding:56px 0;text-align:center;font:800 110px \'Barlow Condensed\'">YES</div>'
 '<div style="flex:1;background:#F6F4F0;color:var(--ink);border-radius:32px;padding:56px 0;text-align:center;font:800 110px \'Barlow Condensed\'">NO</div></div>'
 '<div class="a L" style="top:1470px;font:600 38px Barlow;color:#24301a">Reply YES or NO. We read every message.</div>',bg='var(--lime)',fg='var(--ink)')
# 4. 6 Nov: Nighoje teaser
S['s4-zero']=page(brand()+
 '<div class=a style="left:90px;top:400px;width:560px;height:560px;border-radius:50%;background:var(--lime);color:var(--ink);display:flex;flex-direction:column;align-items:center;justify-content:center">'
 '<div class=h style="font-size:400px;line-height:.8">0</div><div style="font:700 30px Barlow;letter-spacing:3px;margin-top:20px">MISSED BELLS</div></div>'
 '<div class="a L" style="top:1040px"><div class="chip" style="border:2px solid #3a3631;color:var(--lime)"><i class=dot></i>Government pilot</div>'
 '<div class=h style="font-size:150px;margin-top:40px">A ZP school.<br><span class=g>Zero missed bells.</span></div>'
 '<div class=p style="margin-top:36px">Z.P. Primary School, Nighoje (Khed). The full story is on our page today.</div></div>')
# 5. 7 Nov: demo
S['s5-demo']=page(
 '<div class=a style="inset:0;background:url(knobs.png) center 30%/cover"></div>'
 '<div class=a style="left:0;right:0;bottom:0;height:1250px;background:linear-gradient(180deg,rgba(11,9,7,0),rgba(11,9,7,.96) 45%)"></div>'+brand()+
 '<div class="a L" style="top:1000px"><div class=h style="font-size:160px">See it run<br><span class=g>your timetable.</span></div>'
 '<div class=p style="margin-top:36px">Book a free online demo. We\'ll show you how it works for your school.</div>'
 '<div style="margin-top:44px"><span class=btn>WhatsApp 98349 75938</span></div></div>')
import json
for k,v in S.items(): open(k+'.html','w').write(v)
json.dump(list(S),open('list.json','w'))

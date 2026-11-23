import json,subprocess,os
CSS="""@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Barlow:wght@500;600;700&family=Mukta:wght@700;800&display=block');
*{margin:0;padding:0;box-sizing:border-box}:root{--ink:#0B0907;--lime:#A3CF44;--off:#F6F4F0;--m:80px}
html,body{width:1080px;height:1920px;overflow:hidden;font-family:Barlow,sans-serif;color:#fff;position:relative;-webkit-font-smoothing:antialiased}
.grad{position:absolute;left:0;right:0;bottom:0;height:1100px;background:linear-gradient(180deg,rgba(11,9,7,0),rgba(11,9,7,.75) 45%,rgba(11,9,7,.92))}
.tgrad{position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(180deg,rgba(11,9,7,.6),rgba(11,9,7,0))}
.brand{position:absolute;left:var(--m);top:200px;z-index:2;display:inline-flex;align-items:center;gap:16px;font:800 38px 'Barlow Condensed';letter-spacing:.6px}
.brand img{width:52px;height:52px;border-radius:12px}.brand b{color:var(--lime)}
.copy{position:absolute;left:var(--m);right:var(--m);bottom:430px;z-index:2}
.chip{display:inline-block;background:var(--lime);color:var(--ink);border-radius:999px;padding:14px 28px;font:700 26px Barlow;letter-spacing:3px;text-transform:uppercase;margin-bottom:34px}
.h{font:800 150px/.9 'Barlow Condensed';letter-spacing:-2px}.h span{color:var(--lime)}
.copy p{margin-top:34px;font:500 42px/1.35 Barlow;color:#D6D0C8;max-width:900px}
.dev{position:absolute;left:50px;right:50px;top:380px;background:#111;border-radius:44px;padding:34px;box-shadow:0 30px 80px rgba(0,0,0,.6),inset 0 0 0 3px #2a2622}
.dev img{display:block;width:100%;border-radius:14px}
.ring{position:absolute;border:8px solid var(--lime);border-radius:50%;box-shadow:0 0 0 12px rgba(163,207,68,.25)}
.prod{position:absolute;left:0;right:0;top:0;height:1150px;background:var(--off);display:flex;align-items:center;justify-content:center}
.prod img{width:920px;mix-blend-mode:multiply}
.end{position:absolute;inset:0;background:var(--ink);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 var(--m) 200px}
.end img{width:190px;border-radius:40px;margin-bottom:50px}.end .h{font-size:136px}
.end p{margin-top:40px;font:500 42px/1.4 Barlow;color:#C9C3BB}
.cta{margin-top:60px;background:var(--lime);color:var(--ink);border-radius:999px;padding:28px 52px;font:700 44px Barlow}
.url{margin-top:30px;font:600 36px Barlow}"""
BRAND='<div class=tgrad></div><div class=brand><img src=logo.png>SMART SCHOOL <b>360</b></div>'
def copy(chip,h,p): return f'<div class=grad></div>{BRAND}<div class=copy><span class=chip>{chip}</span><div class=h>{h}</div><p>{p}</p></div>'
def screen(img,chip,h,p,ring=None):
    r=''
    if ring: x,y,d=ring; r=f'<div class=ring style="left:{84+x*1.14-d/2}px;top:{414+y*1.14-d/2}px;width:{d}px;height:{d}px"></div>'
    return f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 30%,#2b2a22,#0B0907 70%)"></div>{BRAND}<div class=dev><img src={img}></div>{r}<div class=copy><span class=chip>{chip}</span><div class=h>{h}</div><p>{p}</p></div>'
def prod(chip,h,p): return f'<div style="position:absolute;inset:0;background:var(--ink)"></div><div class=prod><img src=device-front-white.png></div>{BRAND}<div class=copy><span class=chip>{chip}</span><div class=h>{h}</div><p>{p}</p></div>'
END='<div class=end><img src=logo.png><div class=h>SMART SCHOOL <span>360</span></div><p>Automatic school bell + PA system.<br>One-time purchase. No subscription.</p><div class=cta>Free online demo: 98349 75938</div><div class=url>WhatsApp or call · smartschool360.co.in</div></div>'
# scene: (kind, dur, html, clip-src, clip-start, crop-x 0..1)
ITEMS=[("❌","The school bus"),("❌","The staff meeting"),("❌","Monday attendance"),("✅","The bell.")]
def LIST(k):
    rows="".join(f'<div style="display:flex;gap:30px;align-items:center;margin-bottom:40px;font:800 {120 if i==3 else 96}px/1 \'Barlow Condensed\';color:{"var(--lime)" if i==3 else "#fff"}"><span style="font-size:80px">{e}</span>{t}</div>' for i,(e,t) in enumerate(ITEMS[:k]))
    return f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 30%,#2b2a22,#0B0907 70%)"></div>{BRAND}<div style="position:absolute;left:var(--m);top:560px;font:700 32px Barlow;letter-spacing:4px;color:#8C867F">THINGS THAT ARE NEVER ON TIME</div><div style="position:absolute;left:var(--m);right:var(--m);top:680px">{rows}</div>'
R={
"reel-water-bell":[
 ("clip",3.4,copy("Sound on 🔊","This bell<br><span>isn't for class.</span>","Between Period 3 and Period 4, something else rings."),"walk.mp4",0.5,0.55),
 ("still",2.8,prod("09:25","It's the<br><span>water bell.</span>","A reminder for every student to drink water.")),
 ("clip",2.8,copy("Set it once","Rings on its own.<br><span>Every day.</span>","Add it to your timetable like any other bell."),"boys.mp4",1.0,0.42),
 ("still",2.6,END)],
"reel-never-on-time":[
 ("clip",2.6,copy("School life","Things that are<br><span>never on time:</span>",""),"run.mp4",0.4,0.5),
 ("still",1.3,LIST(1)),("still",1.3,LIST(2)),("still",1.3,LIST(3)),
 ("still",2.3,LIST(4)),
 ("still",2.4,prod("Smart School 360","Every bell.<br><span>On time.</span>","Automatically, every day.")),
 ("still",2.6,END)],
"reel-republic-day":[
 ("clip",3.6,copy("26 January 2027","Happy<br><span>Republic Day.</span>",""),"parade.mp4",2.0,0.5),
 ("clip",3.4,'<div class=grad></div>'+BRAND+'<div class=copy><div style="font:800 96px/1.15 Mukta">प्रजासत्ताक दिनाच्या<br><span style="color:var(--lime)">हार्दिक शुभेच्छा!</span></div><p>To every school that starts the day with the flag and the anthem.</p></div>',"parade.mp4",14.0,0.45),
 ("still",2.6,END)]}
T=0.35;FPS=30
open('scenes.json','w').write(json.dumps({f"{r}-{i}":(s[0],s[2]) for r,sc in R.items() for i,s in enumerate(sc)}))
for k,(kind,html) in json.load(open('scenes.json')).items():
    bg='' if kind=='clip' else ''
    open(k+'.html','w').write(f"<html><head><style>{CSS}{'html,body{background:transparent}' if kind=='clip' else 'body{background:#0B0907}'}</style></head><body>{html}</body></html>")
subprocess.run(['node','shot.js'],check=True)
def chime(t): return f"0.45*sin(2*PI*659*(t-{t}))*exp(-1.8*(t-{t}))*gte(t,{t})+0.25*sin(2*PI*1318*(t-{t}))*exp(-2.6*(t-{t}))*gte(t,{t})+0.15*sin(2*PI*1976*(t-{t}))*exp(-3.5*(t-{t}))*gte(t,{t})"
for name,sc in R.items():
    total=sum(s[1] for s in sc); cuts=[];acc=0
    for s in sc[:-1]: acc+=s[1];cuts.append(acc)
    args=["ffmpeg","-y","-loglevel","error"];f=[]
    for i,s in enumerate(sc):
        l=s[1]+(T if i>0 else 0)
        if s[0]=="clip":
            args+=["-ss",str(s[4]),"-t",f"{l:.3f}","-i",s[3],"-loop","1","-t",f"{l:.3f}","-i",f"{name}-{i}.png"]
            vi=len([a for a in args if a=="-i"])-2
            f.append(f"[{vi}:v]fps={FPS},crop=ih*9/16:ih:(iw-ih*9/16)*{s[5]}:0,scale=1080:1920,setsar=1,eq=saturation=1.08:contrast=1.04[c{i}];[c{i}][{vi+1}:v]overlay=0:0,trim=duration={l:.3f},setpts=PTS-STARTPTS,format=yuv420p[v{i}]")
        else:
            args+=["-loop","1","-t",f"{l:.3f}","-i",f"{name}-{i}.png"]
            vi=len([a for a in args if a=="-i"])-1; n=int(l*FPS)+2
            f.append(f"[{vi}:v]scale=2160:3840,zoompan=z='1+0.035*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS},trim=duration={l:.3f},setpts=PTS-STARTPTS,format=yuv420p,setsar=1[v{i}]")
    prev="v0"
    for i in range(1,len(sc)):
        f.append(f"[{prev}][v{i}]xfade=transition=fade:duration={T}:offset={cuts[i-1]-T:.3f}[x{i}]");prev=f"x{i}"
    # soft pad bed + chime at key cut
    key={"reel-water-bell":lambda:cuts[0],"reel-never-on-time":lambda:cuts[3]}.get(name,lambda:None)()
    pad="0.035*(sin(2*PI*220*t)+sin(2*PI*277.2*t)+sin(2*PI*329.6*t))*(0.7+0.3*sin(2*PI*0.25*t))"
    if name=="reel-emergency-siren":
        a,b=cuts[2],cuts[4]
        extra=f"+0.12*sin(2*PI*(700*t+150*sin(2*PI*0.8*t)/(2*PI*0.8)))*between(t,{a},{b})"
    elif key is None: extra=""
    else: extra="+"+chime(key)+"+"+chime(cuts[-1])
    f.append(f"aevalsrc='{pad}{extra}':s=48000:d={total},afade=t=in:d=0.4,afade=t=out:st={total-0.8}:d=0.8,volume=1.6[a]")
    args+=["-filter_complex",";".join(f),"-map",f"[{prev}]","-map","[a]","-c:v","libx264","-preset","medium","-crf","19","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-movflags","+faststart",name+".mp4"]
    subprocess.run(args,check=True); print(name,total)

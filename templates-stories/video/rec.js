const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/s1.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
await p.evaluate(()=>document.getAnimations().forEach(a=>a.pause()));
const fps=30,dur=8;for(let i=0;i<fps*dur;i++){const t=i*1000/fps;
await p.evaluate(t=>document.getAnimations().forEach(a=>a.currentTime=t),t);
await p.screenshot({path:__dirname+'/frames/f'+String(i).padStart(4,'0')+'.jpg',type:'jpeg',quality:92});}
await b.close();})();

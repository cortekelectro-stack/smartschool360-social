const {chromium}=require('playwright');const m=require('./manifest.json');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const post in m){for(const name of m[post]){await p.goto('file://'+__dirname+'/'+name+'__'+post+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:__dirname+'/out/'+post+'/'+name+'.png'});}}
await b.close();})();

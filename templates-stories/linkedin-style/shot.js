const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});fs.mkdirSync('out',{recursive:true});
for(const n of JSON.parse(fs.readFileSync('list.json'))){await p.goto('file://'+process.cwd()+'/'+n+'.html');await p.waitForTimeout(700);await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:'out/'+n+'.png'});}
await b.close();})();

document.fonts.ready.then(()=>{const h=document.querySelector('h1'),b=document.querySelector('.board'),n=document.querySelector('.note'),c=document.querySelector('.cta');if(!h||!b)return;
if(c){const bt=b.offsetTop+b.offsetHeight;let y=bt+44;if(n){n.style.top=y+'px';y+=n.offsetHeight+56;}c.style.top=y+'px';return;}
const t0=h.getBoundingClientRect().bottom+56,bh=b.offsetHeight,nh=n?n.offsetHeight+48:0,avail=1350-130-t0,st=t0+Math.max(0,(avail-bh-nh)/2);b.style.top=st+'px';if(n)n.style.top=(st+bh+48)+'px';});

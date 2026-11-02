import os,json
exec(open('gen.py').read().split('P={}')[0])
P={}
n=4
big='<div class=circle style="right:80px;top:200px;width:420px;height:420px"><div class=n>4</div><div class=l>NAAC criteria</div></div>'
P['post-7-naac']=[
 cover_graphic(1,n,'For colleges','NAAC visit<br><span>coming up?</span>','Smart School 360 gives you evidence assessors can see under <b>Criteria 2, 4, 6 and 7.</b>',big,top_px=680,size=150),
 cards(2,n,'light','Where it counts','Four criteria,<br><span>one install</span>',[('C2','Teaching-learning','Every period on time. Prayer and anthem automated.',0),('C4','Infrastructure','Campus PA, zone audio and an emergency siren.',1),('C6','Governance','ICT-based scheduling with internet time sync.',1),('C7','Best practices','Water bell, siren drills, a punctuality culture.',0)],h=300,gtop=520),
 rows(3,n,'dark','Your evidence file','What you can<br><span>show assessors</span>',[('1','Installation certificate','PA infrastructure and zone setup.'),('2','Timetable printout','Structured schedule and period discipline.'),('3','Siren drill records','Safety infrastructure in use.'),('4','Staff training record','Done on installation day.')],rtop=520),
 cta(4,n,'Before your assessment','One day.<br>Fully documented.',['1-day install','Certificate','Staff training','Drill records'])]
manifest={}
for post,slides in P.items():
    os.makedirs(f'out/{post}',exist_ok=True); manifest[post]=[]
    for k,html in enumerate(slides,1):
        name='post' if len(slides)==1 else f'slide-{k:02d}'
        open(f'{name}__{post}.html','w').write(html); manifest[post].append(name)
json.dump(manifest,open('manifest.json','w'))

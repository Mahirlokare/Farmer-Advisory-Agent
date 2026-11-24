import { useState } from 'react'
import { Sprout, CloudSun, Languages, Leaf, Send, MapPin, ShieldCheck, Bot, User } from 'lucide-react'

const API = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
const copy = {
 en:{tag:'Agriculture, made accessible',title:'A smarter growing season starts here.',sub:'Ask naturally. Get practical AI assistance in your language.',crop:'Your crop',location:'Your village / district',question:'What would you like help with?',ask:'Ask Bharat Krishi AI',weather:'Weather',safe:'AI guidance can be incomplete. Verify high-impact or time-sensitive decisions with your KVK or agriculture officer.'},
 hi:{tag:'कृषि सहायता, आपकी भाषा में',title:'बेहतर खेती की शुरुआत यहीं से।',sub:'अपनी भाषा में सवाल पूछें और व्यावहारिक AI सहायता पाएं।',crop:'आपकी फसल',location:'गाँव / ज़िला',question:'आपको किस बारे में सहायता चाहिए?',ask:'भारत कृषि AI से पूछें',weather:'मौसम',safe:'AI सलाह अधूरी हो सकती है। महत्वपूर्ण निर्णयों की पुष्टि कृषि विज्ञान केंद्र या कृषि अधिकारी से करें।'},
 mr:{tag:'शेतीसाठी मदत, आपल्या भाषेत',title:'चांगल्या हंगामाची सुरुवात इथून.',sub:'नैसर्गिकपणे प्रश्न विचारा आणि आपल्या भाषेत AI मार्गदर्शन मिळवा.',crop:'तुमचे पीक',location:'गाव / जिल्हा',question:'तुम्हाला कशाबद्दल मदत हवी आहे?',ask:'भारत कृषी AI ला विचारा',weather:'हवामान',safe:'AI सल्ला अपूर्ण असू शकतो. महत्त्वाच्या निर्णयांची खात्री कृषी विज्ञान केंद्र किंवा कृषी अधिकाऱ्यांकडून करा.'},
 gu:{tag:'ખેતી સહાય, તમારી ભાષામાં',title:'સારી ખેતીની શરૂઆત અહીંથી.',sub:'સહજ રીતે પ્રશ્ન પૂછો અને તમારી ભાષામાં AI સહાય મેળવો.',crop:'તમારો પાક',location:'ગામ / જિલ્લો',question:'તમને શેમાં મદદ જોઈએ છે?',ask:'ભારત કૃષિ AI ને પૂછો',weather:'હવામાન',safe:'AI સલાહ અધૂરી હોઈ શકે છે. મહત્વપૂર્ણ નિર્ણયોની પુષ્ટિ કૃષિ અધિકારી પાસે કરો.'},
 ta:{tag:'விவசாய உதவி உங்கள் மொழியில்',title:'சிறந்த விளைச்சலுக்கான தொடக்கம்.',sub:'இயல்பாகக் கேளுங்கள்; உங்கள் மொழியில் AI உதவி பெறுங்கள்.',crop:'உங்கள் பயிர்',location:'கிராமம் / மாவட்டம்',question:'எதில் உதவி தேவை?',ask:'பாரத் கிருஷி AI-யிடம் கேளுங்கள்',weather:'வானிலை',safe:'AI ஆலோசனை முழுமையற்றதாக இருக்கலாம். முக்கிய முடிவுகளை வேளாண் அதிகாரியிடம் உறுதிப்படுத்தவும்.'},
 te:{tag:'వ్యవసాయ సహాయం మీ భాషలో',title:'మెరుగైన పంట కాలానికి ఇదే ఆరంభం.',sub:'సహజంగా ప్రశ్న అడగండి; మీ భాషలో AI సహాయం పొందండి.',crop:'మీ పంట',location:'గ్రామం / జిల్లా',question:'మీకు ఏ విషయంలో సహాయం కావాలి?',ask:'భారత్ కృషి AIని అడగండి',weather:'వాతావరణం',safe:'AI సలహా అసంపూర్ణంగా ఉండవచ్చు. ముఖ్యమైన నిర్ణయాలను వ్యవసాయ అధికారితో నిర్ధారించండి.'}
}
const langs=[['en','English'],['hi','हिन्दी'],['mr','मराठी'],['gu','ગુજરાતી'],['ta','தமிழ்'],['te','తెలుగు']]
export default function App(){
 const [lang,setLang]=useState('mr'),[crop,setCrop]=useState(''),[location,setLocation]=useState(''),[question,setQuestion]=useState(''),[history,setHistory]=useState([]),[result,setResult]=useState(null),[loading,setLoading]=useState(false),[error,setError]=useState('')
 const t=copy[lang]
 async function ask(e){
  e.preventDefault();setLoading(true);setError('');setResult(null)
  try{
   const r=await fetch(API+'/api/v1/advisory',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({language:lang,crop,location,question,conversation_history:history.slice(-12)})})
   const data=await r.json()
   if(!r.ok)throw new Error(typeof data.detail==='string'?data.detail:(data.detail?.message||'The AI assistant could not answer. Please try again.'))
   setResult(data);setHistory(prev=>[...prev,{role:'user',content:question},{role:'assistant',content:data.answer}].slice(-12));setQuestion('')
  }catch(e){setError(e.message)}finally{setLoading(false)}
 }
 return <main><nav><div className="brand"><span className="logo"><Sprout size={23}/></span><span>Bharat <b>Krishi AI</b></span></div><label className="language"><Languages size={17}/><select value={lang} onChange={e=>setLang(e.target.value)}>{langs.map(([v,n])=><option value={v} key={v}>{n}</option>)}</select></label></nav>
 <section className="hero"><div className="eyebrow"><Leaf size={15}/>{t.tag}</div><h1>{t.title}</h1><p>{t.sub}</p><div className="chips"><span><MapPin size={14}/> Pan-India</span><span><Languages size={14}/> 6 languages</span><span><Bot size={14}/> AI-powered assistant</span></div></section>
 <section className="panel"><div className="panelhead"><div><small>CONVERSATIONAL FARMER ASSISTANT</small><h2>{t.ask}</h2></div><span className="online"><i/> AI assistant</span></div>
 <form onSubmit={ask}><div className="fields"><label>{t.crop}<input required value={crop} onChange={e=>setCrop(e.target.value)} placeholder="e.g. Cotton / कपास / कापूस"/></label><label>{t.location}<input required value={location} onChange={e=>setLocation(e.target.value)} placeholder="e.g. Nashik, Maharashtra"/></label></div>
 {history.length>0&&<div className="conversation">{history.map((m,i)=><div className={m.role==='user'?'bubble user':'bubble assistant'} key={i}><b>{m.role==='user'?<><User size={14}/> You</>:<><Bot size={14}/> Bharat Krishi AI</>}</b><p>{m.content}</p></div>)}</div>}
 <label>{t.question}<textarea required minLength="5" value={question} onChange={e=>setQuestion(e.target.value)} placeholder="Ask naturally: crop planning, irrigation, pests, soil, prices, schemes, or a follow-up question..."/></label><button disabled={loading}>{loading?'Thinking…':t.ask}<Send size={17}/></button></form>
 {error&&<p className="error">{error}</p>}{result&&<div className="result"><b>AI response</b><p>{result.answer}</p><small>{result.disclaimer}</small></div>}</section>
 <section className="features"><article><span><Sprout/></span><h3>Ask in your own words</h3><p>Conversational answers tailored to your crop, location and follow-up context.</p></article><article><span><CloudSun/></span><h3>{t.weather}</h3><p>Weather service is available separately; live data is not silently assumed by the AI.</p></article><article><span><ShieldCheck/></span><h3>Responsible AI</h3><p>Clear uncertainty and no fabricated disease diagnoses, chemical doses or live market facts.</p></article></section>
 <footer>{t.safe}<br/><br/>Built for India's farming communities · Bharat Krishi AI</footer></main>
}

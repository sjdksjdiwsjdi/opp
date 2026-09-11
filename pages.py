# pages.py - پنل تخت جمشید · نسخه کیهانی (Cosmic Aurora Edition)
# redesigned with deep-space theme, glassmorphism, neon glow, holographic gradients
# تمام APIها و IDهای اصلی حفظ شده‌اند

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>✦ PERSEPOLIS · ورود به کیهان</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg-deep:#030418;
  --bg-mid:#0a0e2a;
  --bg-surface:rgba(10,14,35,0.55);
  --bg-surface-2:rgba(15,20,45,0.75);
  --border-subtle:rgba(100,200,255,0.08);
  --border-glow:rgba(0,240,255,0.35);
  --border-glow-strong:rgba(0,240,255,0.6);
  --cyan:#00f0ff;
  --cyan-soft:rgba(0,240,255,0.15);
  --magenta:#ff2e9a;
  --magenta-soft:rgba(255,46,154,0.15);
  --purple:#7b2ff7;
  --purple-soft:rgba(123,47,247,0.15);
  --gold:#D4A843;
  --gold2:#F5D060;
  --t1:#e8efff;
  --t2:#94a3b8;
  --t3:#64748b;
  --success:#10ffa0;
  --danger:#ff4d6d;
  --glow-cyan:0 0 30px rgba(0,240,255,0.25),0 0 60px rgba(0,240,255,0.12);
  --glow-magenta:0 0 30px rgba(255,46,154,0.25),0 0 60px rgba(255,46,154,0.12);
  --shadow-deep:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(0,240,255,0.04);
  --transition:cubic-bezier(0.34,1.56,0.64,1)
}
html,body{height:100%}
body{
  font-family:'Vazirmatn',sans-serif;
  min-height:100vh;
  display:flex;align-items:center;justify-content:center;
  background:radial-gradient(ellipse at top,#0a0e2a 0%,#030418 50%,#000 100%);
  padding:20px;color:var(--t1);position:relative;overflow:hidden;
}

/* === ستاره‌های متحرک === */
#starfield{position:fixed;inset:0;z-index:0;pointer-events:none}
.star{position:absolute;border-radius:50%;background:#fff;animation:twinkle 3s ease-in-out infinite}
@keyframes twinkle{0%,100%{opacity:0.15;transform:scale(0.6)}50%{opacity:1;transform:scale(1.4)}}

/* === سحابی‌های شناور === */
.nebula{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;pointer-events:none;animation:nebulaFloat 14s ease-in-out infinite}
.nebula-1{width:600px;height:600px;background:radial-gradient(circle,rgba(0,240,255,0.18),transparent 70%);top:-200px;right:-150px}
.nebula-2{width:500px;height:500px;background:radial-gradient(circle,rgba(255,46,154,0.15),transparent 70%);bottom:-150px;left:-100px;animation-delay:-7s}
.nebula-3{width:400px;height:400px;background:radial-gradient(circle,rgba(123,47,247,0.12),transparent 70%);top:40%;left:30%;animation-delay:-3s}
@keyframes nebulaFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(40px,-30px) scale(1.08)}66%{transform:translate(-30px,40px) scale(0.95)}}

/* === خطوط هولوگرافیک متحرک === */
.grid-lines{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:0.15;background-image:linear-gradient(rgba(0,240,255,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(0,240,255,0.3) 1px,transparent 1px);background-size:50px 50px;mask-image:radial-gradient(ellipse at center,#000 0%,transparent 70%);animation:gridShift 20s linear infinite}
@keyframes gridShift{0%{background-position:0 0}100%{background-position:50px 50px}}

/* === زبانه زبان === */
.lang-toggle{position:fixed;top:24px;left:24px;z-index:50;display:flex;gap:4px;background:var(--bg-surface);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:14px;padding:4px;box-shadow:0 8px 30px rgba(0,0,0,0.3)}
.lang-toggle button{background:none;border:none;color:var(--t3);font-family:inherit;font-size:11px;font-weight:700;padding:6px 12px;border-radius:10px;cursor:pointer;transition:all .3s var(--transition)}
.lang-toggle button.active{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#000;box-shadow:var(--glow-cyan)}
.lang-toggle button:hover:not(.active){color:var(--t1);background:rgba(0,240,255,0.05)}

/* === کارت ورود === */
.container{position:relative;z-index:10;display:grid;grid-template-columns:1fr 1fr;max-width:1140px;width:100%;background:var(--bg-surface);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-radius:28px;border:1px solid var(--border-subtle);overflow:hidden;box-shadow:var(--shadow-deep);animation:cardRise .8s var(--transition)}
@keyframes cardRise{from{opacity:0;transform:translateY(40px) scale(0.95)}to{opacity:1;transform:translateY(0) scale(1)}}
.container::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(0,240,255,0.04),transparent 50%,rgba(255,46,154,0.03));pointer-events:none;z-index:0}
.container::after{content:'';position:absolute;inset:-2px;border-radius:28px;padding:2px;background:linear-gradient(135deg,rgba(0,240,255,0.5),transparent 30%,transparent 70%,rgba(255,46,154,0.5));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:0.4;pointer-events:none;animation:borderGlow 6s ease-in-out infinite}
@keyframes borderGlow{0%,100%{opacity:0.3}50%{opacity:0.7}}

.login-section{position:relative;z-index:1;padding:52px 44px}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:36px}
.brand-icon{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:var(--glow-cyan);animation:iconPulse 4s ease-in-out infinite;position:relative}
.brand-icon::before{content:'';position:absolute;inset:-3px;border-radius:16px;background:linear-gradient(135deg,var(--cyan),var(--magenta));z-index:-1;filter:blur(10px);opacity:0.6;animation:iconPulse 4s ease-in-out infinite}
@keyframes iconPulse{0%,100%{box-shadow:0 0 30px rgba(0,240,255,0.4)}50%{box-shadow:0 0 50px rgba(255,46,154,0.5)}}
.brand-text{font-size:18px;font-weight:900;background:linear-gradient(135deg,#fff,var(--cyan),var(--magenta));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:0.5px}
.brand-sub{font-size:10px;color:var(--t3);letter-spacing:1.2px;text-transform:uppercase;margin-top:2px}

.welcome{font-size:26px;font-weight:800;color:var(--t1);margin-bottom:6px;background:linear-gradient(135deg,#fff,rgba(255,255,255,0.7));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.sub-text{font-size:13px;color:var(--t3);margin-bottom:30px}

.field{margin-bottom:18px;position:relative}
.field label{display:block;font-size:10px;font-weight:700;color:var(--t2);margin-bottom:6px;letter-spacing:0.5px;text-transform:uppercase}
.field input{width:100%;padding:14px 16px 14px 42px;border-radius:12px;border:1px solid var(--border-subtle);background:rgba(0,0,15,0.4);color:var(--t1);font-family:inherit;font-size:14px;outline:none;transition:all .3s var(--transition)}
.field input:focus{border-color:var(--cyan);box-shadow:0 0 0 4px rgba(0,240,255,0.08),0 0 30px rgba(0,240,255,0.15);background:rgba(0,240,255,0.03)}
.field input::placeholder{color:var(--t3)}
.field .input-icon{position:absolute;left:14px;top:36px;color:var(--t3);font-size:16px;transition:color .3s}
.field input:focus + .input-icon,.field:focus-within .input-icon{color:var(--cyan)}

.options{display:flex;justify-content:space-between;align-items:center;margin:16px 0 22px;font-size:12px}
.options label{display:flex;align-items:center;gap:8px;color:var(--t2);cursor:pointer}
.options label input[type="checkbox"]{accent-color:var(--cyan);width:16px;height:16px;cursor:pointer}

.btn-login{width:100%;padding:14px;border-radius:12px;border:none;cursor:pointer;background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));background-size:200% 200%;animation:gradientFlow 5s ease infinite;color:#000;font-family:inherit;font-size:15px;font-weight:800;transition:all .3s var(--transition);box-shadow:0 4px 30px rgba(0,240,255,0.3);position:relative;overflow:hidden}
.btn-login::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.4),transparent);transform:translateX(-100%);transition:transform .6s}
.btn-login:hover{transform:translateY(-2px);box-shadow:0 8px 40px rgba(0,240,255,0.5),0 0 60px rgba(255,46,154,0.3)}
.btn-login:hover::before{transform:translateX(100%)}
.btn-login:disabled{opacity:.5;cursor:not-allowed;transform:none}
@keyframes gradientFlow{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}

.or-divider{display:flex;align-items:center;gap:14px;margin:22px 0;color:var(--t3);font-size:11px;letter-spacing:1px;text-transform:uppercase}
.or-divider::before,.or-divider::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--border-subtle),transparent)}

.connect-btn{width:100%;padding:12px;border-radius:12px;border:1px solid var(--border-subtle);background:rgba(255,255,255,0.02);color:var(--t1);font-family:inherit;font-size:13px;font-weight:700;cursor:pointer;transition:all .3s var(--transition);display:flex;align-items:center;justify-content:center;gap:8px}
.connect-btn:hover{background:rgba(0,240,255,0.06);border-color:var(--cyan);box-shadow:var(--glow-cyan)}

.error-box{display:none;background:rgba(255,77,109,0.08);border:1px solid rgba(255,77,109,0.25);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:var(--danger);align-items:center;gap:8px;animation:shake .4s}
.error-box.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}

/* === پنل راست (اطلاعات) === */
.info-section{position:relative;background:linear-gradient(135deg,rgba(0,240,255,0.04),rgba(123,47,247,0.04),rgba(255,46,154,0.06));padding:52px 40px;display:flex;flex-direction:column;justify-content:center;border-right:1px solid var(--border-subtle);overflow:hidden}
.info-section::before{content:'';position:absolute;top:50%;left:50%;width:400px;height:400px;background:radial-gradient(circle,rgba(0,240,255,0.08),transparent 70%);transform:translate(-50%,-50%);animation:orbPulse 6s ease-in-out infinite;pointer-events:none}
@keyframes orbPulse{0%,100%{transform:translate(-50%,-50%) scale(1);opacity:0.6}50%{transform:translate(-50%,-50%) scale(1.2);opacity:0.9}}
.info-title{font-size:24px;font-weight:900;color:var(--t1);margin-bottom:8px;position:relative;z-index:1;background:linear-gradient(135deg,#fff,var(--cyan));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.info-sub{font-size:13px;color:var(--t2);margin-bottom:28px;position:relative;z-index:1;letter-spacing:0.5px}
.features{display:grid;grid-template-columns:1fr 1fr;gap:14px;position:relative;z-index:1}
.feature{background:rgba(255,255,255,0.03);backdrop-filter:blur(10px);border-radius:14px;padding:18px 14px;text-align:center;border:1px solid var(--border-subtle);transition:all .3s var(--transition);cursor:default}
.feature:hover{background:rgba(0,240,255,0.05);border-color:var(--cyan);transform:translateY(-3px);box-shadow:var(--glow-cyan)}
.feature .icon{font-size:32px;display:block;margin-bottom:8px;filter:drop-shadow(0 0 10px rgba(0,240,255,0.4))}
.feature .name{font-size:12px;font-weight:700;color:var(--t1);letter-spacing:0.3px}
.feature .desc{font-size:9px;color:var(--t3);margin-top:4px;letter-spacing:0.5px}

@media(max-width:900px){.container{grid-template-columns:1fr}.info-section{display:none}.login-section{padding:36px 28px}}
@media(max-width:480px){.login-section{padding:28px 20px}.welcome{font-size:21px}.brand-icon{width:46px;height:46px;font-size:22px}}
</style>
</head>
<body>
<canvas id="starfield"></canvas>
<div class="nebula nebula-1"></div><div class="nebula nebula-2"></div><div class="nebula nebula-3"></div>
<div class="grid-lines"></div>

<div class="lang-toggle">
    <button class="active" onclick="setLang('fa')">🇮🇷 فارسی</button>
    <button onclick="setLang('en')">🇬🇧 English</button>
</div>

<div class="container">
    <div class="login-section">
        <div class="brand">
            <div class="brand-icon">🏛️</div>
            <div>
                <div class="brand-text">PERSEPOLIS</div>
                <div class="brand-sub">COSMIC PANEL · v2.0</div>
            </div>
        </div>
        <div class="welcome" id="welcome-text">خوش آمدید</div>
        <div class="sub-text" id="sub-text">وارد پنل مدیریت شوید</div>
        <div class="error-box" id="error-box"><i class="ti ti-alert-circle"></i><span id="error-text"></span></div>
        <form id="login-form" onsubmit="handleLogin(event)">
            <div class="field">
                <label id="label-username">نام کاربری</label>
                <input type="text" id="username" placeholder="admin" value="admin" dir="ltr">
                <i class="ti ti-user input-icon"></i>
            </div>
            <div class="field">
                <label id="label-password">رمز عبور</label>
                <input type="password" id="password" placeholder="••••••••" dir="ltr">
                <i class="ti ti-lock input-icon"></i>
            </div>
            <div class="options"><label><input type="checkbox" id="remember"> <span id="remember-text">مرا به خاطر بسپار</span></label></div>
            <button class="btn-login" type="submit" id="login-btn"><i class="ti ti-login-2"></i> <span id="login-text">ورود</span></button>
        </form>
        <div class="or-divider"><span id="or-text">یا</span></div>
        <button class="connect-btn" onclick="quickConnect()"><i class="ti ti-bolt"></i> <span id="connect-text">ورود با یک کلیک</span></button>
    </div>
    <div class="info-section">
        <div class="info-title" id="info-title">✦ Persepolis</div>
        <div class="info-sub" id="info-sub">سریع‌ترین و امن‌ترین اتصال کیهانی</div>
        <div class="features">
            <div class="feature"><span class="icon">🛡️</span><div class="name" id="f-secure">امن</div><div class="desc" id="f-secure-d">حریم خصوصی شما</div></div>
            <div class="feature"><span class="icon">⚡</span><div class="name" id="f-fast">سریع</div><div class="desc" id="f-fast-d">سرعت برق آسا</div></div>
            <div class="feature"><span class="icon">🌍</span><div class="name" id="f-global">جهانی</div><div class="desc" id="f-global-d">سرورهای جهانی</div></div>
            <div class="feature"><span class="icon">🛰️</span><div class="name" id="f-anon">ناشناس</div><div class="desc" id="f-anon-d">خصوصی بمانید</div></div>
        </div>
    </div>
</div>

<script>
// === ستاره‌های متحرک (Canvas) ===
const canvas = document.getElementById('starfield');
const ctx = canvas.getContext('2d');
let stars = [];
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    stars = [];
    const count = Math.floor((canvas.width * canvas.height) / 8000);
    for (let i = 0; i < count; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 1.5 + 0.3,
            o: Math.random() * 0.8 + 0.2,
            s: Math.random() * 0.05 + 0.01,
            tw: Math.random() * Math.PI * 2,
            color: Math.random() > 0.85 ? '#00f0ff' : (Math.random() > 0.7 ? '#ff2e9a' : '#ffffff')
        });
    }
}
function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(s => {
        s.tw += 0.02;
        const op = s.o * (0.5 + 0.5 * Math.sin(s.tw));
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = s.color;
        ctx.globalAlpha = op;
        ctx.shadowBlur = 8;
        ctx.shadowColor = s.color;
        ctx.fill();
    });
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
    requestAnimationFrame(drawStars);
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();
drawStars();

// === ترجمه‌ها ===
const translations={
fa:{
welcome:"خوش آمدید به کیهان",
sub:"وارد پنل مدیریت شوید",
username:"نام کاربری",
password:"رمز عبور",
remember:"مرا به خاطر بسپار",
login:"ورود به پنل",
or:"یا",
connect:"ورود با یک کلیک",
secure:"امن",
secure_d:"حریم خصوصی شما",
fast:"سریع",
fast_d:"سرعت برق آسا",
global:"جهانی",
global_d:"سرورهای جهانی",
anon:"ناشناس",
anon_d:"خصوصی بمانید",
info_title:"✦ Persepolis",
info_sub:"سریع‌ترین و امن‌ترین اتصال کیهانی"
},
en:{
welcome:"Welcome to the Cosmos",
sub:"Login to the panel",
username:"Username",
password:"Password",
remember:"Remember me",
login:"Enter Panel",
or:"OR",
connect:"Quick Login",
secure:"Secure",
secure_d:"Your Privacy",
fast:"Fast",
fast_d:"Lightning Speed",
global:"Global",
global_d:"Worldwide Servers",
anon:"Anonymous",
anon_d:"Stay Private",
info_title:"✦ Persepolis",
info_sub:"Fastest & Most Secure Connection"
}};

let currentLang=localStorage.getItem('persepolis-lang')||'fa';
const ADMIN_USERNAME="admin";
const ADMIN_PASSWORD="PERSEPOLIS";

function setLang(lang){
  currentLang=lang;
  localStorage.setItem('persepolis-lang',lang);
  document.querySelectorAll('.lang-toggle button').forEach(b=>b.classList.toggle('active',b.textContent.includes(lang==='fa'?'فارسی':'English')));
  updateTexts();
}
function updateTexts(){
  const t=translations[currentLang];
  document.getElementById('welcome-text').textContent=t.welcome;
  document.getElementById('sub-text').textContent=t.sub;
  document.getElementById('label-username').textContent=t.username;
  document.getElementById('label-password').textContent=t.password;
  document.getElementById('remember-text').textContent=t.remember;
  document.getElementById('login-text').textContent=t.login;
  document.getElementById('or-text').textContent=t.or;
  document.getElementById('connect-text').textContent=t.connect;
  document.getElementById('f-secure').textContent=t.secure;
  document.getElementById('f-secure-d').textContent=t.secure_d;
  document.getElementById('f-fast').textContent=t.fast;
  document.getElementById('f-fast-d').textContent=t.fast_d;
  document.getElementById('f-global').textContent=t.global;
  document.getElementById('f-global-d').textContent=t.global_d;
  document.getElementById('f-anon').textContent=t.anon;
  document.getElementById('f-anon-d').textContent=t.anon_d;
  document.getElementById('info-title').textContent=t.info_title;
  document.getElementById('info-sub').textContent=t.info_sub;
}

async function handleLogin(e){
  e.preventDefault();
  const btn=document.getElementById('login-btn');
  const err=document.getElementById('error-box');
  const errText=document.getElementById('error-text');
  err.classList.remove('show');
  btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> '+ (currentLang==='fa'?'در حال ورود...':'Loading...');

  try{
    const username=document.getElementById('username').value;
    const password=document.getElementById('password').value;
    const remember=document.getElementById('remember').checked;

    const r=await fetch('/api/login',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({username,password,remember})
    });

    if(!r.ok){
      const d=await r.json().catch(()=>({}));
      errText.textContent=d.detail||(currentLang==='fa'?'یوزرنیم یا رمز عبور اشتباه است':'Wrong username or password');
      err.classList.add('show');
      btn.disabled=false;
      btn.innerHTML='<i class="ti ti-login-2"></i> '+translations[currentLang].login;
      return;
    }
    // انیمیشن خروج
    document.querySelector('.container').style.animation='cardOut .5s ease forwards';
    setTimeout(()=>{window.location.href='/dashboard';},400);
  }catch(e){
    errText.textContent=currentLang==='fa'?'خطا در ارتباط با سرور':'Connection error';
    err.classList.add('show');
    btn.disabled=false;
    btn.innerHTML='<i class="ti ti-login-2"></i> '+translations[currentLang].login;
  }
}

function quickConnect(){
  document.getElementById('username').value=ADMIN_USERNAME;
  document.getElementById('password').value=ADMIN_PASSWORD;
  document.getElementById('remember').checked=true;
  document.getElementById('login-form').dispatchEvent(new Event('submit'));
}

document.getElementById('password').addEventListener('keydown',(e)=>{if(e.key==='Enter')document.getElementById('login-form').dispatchEvent(new Event('submit'))});
document.getElementById('username').addEventListener('keydown',(e)=>{if(e.key==='Enter')document.getElementById('login-form').dispatchEvent(new Event('submit'))});

// === افزودن استایل انیمیشن خروج ===
const styleOut=document.createElement('style');
styleOut.textContent='@keyframes cardOut{to{opacity:0;transform:scale(0.92) translateY(-20px)}}@keyframes spin{to{transform:rotate(360deg)}}';
document.head.appendChild(styleOut);

setLang(currentLang);
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>✦ PERSEPOLIS · کیهان</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/plugins/rangePlugin.js"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/l10n/fa.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg-deep:#030418;
  --bg-mid:#0a0e2a;
  --bg-surface:rgba(10,14,35,0.55);
  --bg-surface-2:rgba(15,20,45,0.75);
  --bg-card:rgba(10,14,35,0.6);
  --bg-card-hover:rgba(15,20,45,0.75);
  --border-subtle:rgba(100,200,255,0.08);
  --border-glow:rgba(0,240,255,0.25);
  --border-strong:rgba(0,240,255,0.4);
  --cyan:#00f0ff;
  --cyan-soft:rgba(0,240,255,0.1);
  --magenta:#ff2e9a;
  --magenta-soft:rgba(255,46,154,0.1);
  --purple:#7b2ff7;
  --purple-soft:rgba(123,47,247,0.1);
  --gold:#D4A843;
  --gold2:#F5D060;
  --green:#10ffa0;
  --green-bg:rgba(16,255,160,0.08);
  --green-t:#10ffa0;
  --red:#ff4d6d;
  --red-bg:rgba(255,77,109,0.08);
  --red-t:#ff6b8a;
  --amber:#ffb800;
  --amber-bg:rgba(255,184,0,0.08);
  --amber-t:#ffcc4d;
  --t1:#e8efff;
  --t2:#94a3b8;
  --t3:#64748b;
  --sidebar-w:200px;
  --radius:14px;
  --shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(0,240,255,0.03);
  --glow-cyan:0 0 30px rgba(0,240,255,0.2);
  --transition:cubic-bezier(0.34,1.56,0.64,1)
}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg-deep);color:var(--t1);min-height:100vh;display:flex;font-size:13px;position:relative;overflow-x:hidden;transition:background .4s,color .4s}

/* === ستاره‌های متحرک === */
#starfield-bg{position:fixed;inset:0;z-index:0;pointer-events:none}

/* === سحابی‌ها === */
.nebula-bg{position:fixed;border-radius:50%;filter:blur(140px);z-index:0;pointer-events:none;animation:nebulaFloat 16s ease-in-out infinite}
.nebula-bg-1{width:500px;height:500px;background:radial-gradient(circle,rgba(0,240,255,0.06),transparent 70%);top:-200px;left:-150px}
.nebula-bg-2{width:400px;height:400px;background:radial-gradient(circle,rgba(255,46,154,0.05),transparent 70%);bottom:-150px;right:-100px;animation-delay:-8s}
@keyframes nebulaFloat{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(40px,-30px) scale(1.1)}}

/* === ساید بار === */
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg-surface);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-left:1px solid var(--border-subtle);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .4s var(--transition),background .4s;box-shadow:var(--shadow)}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--border-subtle);position:relative}
.logo-icon{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0;box-shadow:0 0 30px rgba(0,240,255,0.3);animation:logoPulse 4s ease-in-out infinite}
@keyframes logoPulse{0%,100%{box-shadow:0 0 30px rgba(0,240,255,0.3)}50%{box-shadow:0 0 50px rgba(255,46,154,0.4)}}
.logo-name{font-size:14px;font-weight:900;background:linear-gradient(135deg,#fff,var(--cyan));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:0.5px}
.logo-sub{font-size:8px;color:var(--t3);letter-spacing:1.5px;text-transform:uppercase}
.nav-wrap{flex:1;overflow-y:auto;padding:10px 0;position:relative;z-index:1}
.nav-wrap::-webkit-scrollbar{width:4px}
.nav-wrap::-webkit-scrollbar-track{background:transparent}
.nav-wrap::-webkit-scrollbar-thumb{background:var(--cyan-soft);border-radius:4px}
.nav-it{display:flex;align-items:center;gap:10px;padding:10px 12px;color:var(--t3);font-size:12px;cursor:pointer;border-right:2px solid transparent;transition:all .3s var(--transition);margin:2px 6px;border-radius:10px;position:relative;overflow:hidden}
.nav-it i{font-size:16px;width:20px;text-align:center;flex-shrink:0;transition:transform .3s}
.nav-it:hover{background:rgba(0,240,255,0.04);color:var(--t1)}
.nav-it:hover i{transform:scale(1.15);color:var(--cyan)}
.nav-it.on{background:linear-gradient(90deg,rgba(0,240,255,0.12),rgba(0,240,255,0.02));color:var(--cyan);border-right-color:var(--cyan);font-weight:700;box-shadow:inset 0 0 20px rgba(0,240,255,0.05)}
.nav-it.on i{color:var(--cyan);filter:drop-shadow(0 0 8px var(--cyan))}
.nav-it.on::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--cyan);box-shadow:0 0 10px var(--cyan)}
.sb-foot{padding:12px 14px;border-top:1px solid var(--border-subtle)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:6px;background:var(--red-bg);color:var(--red-t);border-radius:10px;padding:8px;font-size:11px;font-weight:600;font-family:inherit;border:1px solid rgba(255,77,109,0.15);cursor:pointer;width:100%;transition:all .3s var(--transition)}
.logout-btn:hover{background:rgba(255,77,109,0.15);transform:scale(1.03);box-shadow:0 0 20px rgba(255,77,109,0.3)}

/* === موبایل تاپ === */
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:54px;background:var(--bg-surface);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-bottom:1px solid var(--border-subtle);z-index:150;align-items:center;justify-content:space-between;padding:0 12px;transition:background .4s}
.mob-top .ml{display:flex;align-items:center;gap:8px}
.mob-logo{width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--cyan),var(--purple));display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:var(--glow-cyan)}
.mob-title{color:var(--t1);font-size:12px;font-weight:800;background:linear-gradient(135deg,#fff,var(--cyan));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.menu-btn{background:rgba(0,240,255,0.05);border:1px solid var(--border-subtle);color:var(--cyan);width:34px;height:34px;border-radius:10px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .3s var(--transition)}
.menu-btn:hover{background:rgba(0,240,255,0.1);transform:scale(1.05)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:190;backdrop-filter:blur(8px)}
.overlay.show{display:block}

/* === بخش اصلی === */
.main{margin-right:var(--sidebar-w);flex:1;padding:20px 24px 80px;min-width:0;transition:margin .4s;position:relative;z-index:1}
.topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;padding:18px 22px;background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);position:relative;overflow:hidden}
.topbar::before{content:'';position:absolute;top:-30px;right:-30px;width:200px;height:200px;background:radial-gradient(circle,rgba(0,240,255,0.05),transparent 70%);pointer-events:none}
.tb-title{font-size:16px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.tb-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.tb-sub{font-size:10px;color:var(--t3);margin-top:2px;letter-spacing:0.5px}
.tb-right{display:flex;align-items:center;gap:8px}

.badge{display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:10px;font-weight:700;letter-spacing:0.3px}
.bg-fire{background:rgba(255,46,154,0.1);border:1px solid rgba(255,46,154,0.2);color:var(--magenta);box-shadow:0 0 15px rgba(255,46,154,0.15)}
.bg-green{background:var(--green-bg);border:1px solid rgba(16,255,160,0.2);color:var(--green-t)}
.dot{width:6px;height:6px;border-radius:50%;display:inline-block}
.dg{background:var(--green);animation:dotPulse 1.5s ease-in-out infinite;box-shadow:0 0 8px var(--green)}
.dr{background:var(--red);animation:dotPulse 1.8s ease-in-out infinite;box-shadow:0 0 8px var(--red)}
.da{background:var(--amber);animation:dotPulse 2s ease-in-out infinite;box-shadow:0 0 8px var(--amber)}
.db{background:var(--cyan);animation:dotPulse 1.2s ease-in-out infinite;box-shadow:0 0 8px var(--cyan)}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.7)}}
.pulse{animation:pulseAnim 2s infinite}
@keyframes pulseAnim{0%,100%{opacity:1}50%{opacity:.25}}

/* === کارت‌های آماری === */
.stats-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-bottom:18px}
.stat-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:16px 10px;transition:all .4s var(--transition);text-align:center;position:relative;overflow:hidden;cursor:default}
.stat-card::before{content:'';position:absolute;top:-50%;right:-50%;width:150px;height:150px;background:radial-gradient(circle,rgba(0,240,255,0.06),transparent 70%);pointer-events:none;transition:transform .5s}
.stat-card::after{content:'';position:absolute;inset:0;background:linear-gradient(135deg,transparent,rgba(0,240,255,0.03),transparent);opacity:0;transition:opacity .3s}
.stat-card:hover{border-color:var(--border-strong);transform:translateY(-4px) scale(1.02);box-shadow:0 8px 30px rgba(0,240,255,0.15)}
.stat-card:hover::before{transform:scale(1.5)}
.stat-card:hover::after{opacity:1}
.stat-card .icon{font-size:22px;margin-bottom:6px;display:block;filter:drop-shadow(0 0 8px rgba(0,240,255,0.4))}
.stat-card .number{font-size:20px;font-weight:900;color:var(--t1);line-height:1.2;background:linear-gradient(135deg,#fff,rgba(0,240,255,0.8));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat-card .number.small{font-size:14px}
.stat-card .label{font-size:10px;color:var(--t3);margin-top:4px;font-weight:600;letter-spacing:0.3px}
.stat-card .sub{font-size:8px;color:var(--t3);margin-top:2px;opacity:.7}

/* === نمودار === */
.chart-section{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:18px;margin:14px 0;transition:all .3s;position:relative;overflow:hidden}
.chart-section::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--cyan),transparent);opacity:0.5}
.chart-section .chart-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.chart-section .chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.chart-section .chart-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.chart-section .chart-sub{font-size:10px;color:var(--t3);letter-spacing:0.5px}
.chart-section .chart-actions{display:flex;gap:6px;flex-wrap:wrap}

.stat-mini{background:var(--bg-card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--border-subtle);border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:10px;transition:all .3s var(--transition)}
.stat-mini:hover{transform:translateY(-2px);border-color:var(--border-strong);box-shadow:0 4px 20px rgba(0,240,255,0.1)}
.stat-mini-icon{font-size:18px;filter:drop-shadow(0 0 6px rgba(0,240,255,0.3))}
.stat-mini-num{font-size:18px;font-weight:900;color:var(--t1)}
.stat-mini-label{font-size:10px;color:var(--t3);letter-spacing:0.3px}

/* === جدول کاربران === */
.users-table{width:100%;border-collapse:collapse;font-size:12px}
.users-table thead th{padding:12px 14px;text-align:right;color:var(--cyan);font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:0.5px;border-bottom:1px solid var(--border-strong);background:rgba(0,240,255,0.03)}
.users-table tbody td{padding:10px 14px;border-bottom:1px solid var(--border-subtle);color:var(--t1);vertical-align:middle}
.users-table tbody tr{transition:all .3s var(--transition)}
.users-table tbody tr:hover{background:rgba(0,240,255,0.03)}
.users-table tbody tr:hover .user-name-cell .avatar{transform:scale(1.1) rotate(-5deg)}
.users-table .status-badge{display:inline-flex;align-items:center;gap:5px;padding:3px 12px;border-radius:14px;font-size:10px;font-weight:700}
.users-table .status-badge .status-dot{width:6px;height:6px;border-radius:50%;display:inline-block;animation:statusPulse 1.5s ease-in-out infinite}
.users-table .status-badge.active .status-dot{background:var(--green-t);box-shadow:0 0 6px var(--green-t)}
.users-table .status-badge.expired .status-dot{background:var(--red-t);box-shadow:0 0 6px var(--red-t)}
.users-table .status-badge.disabled .status-dot{background:var(--amber-t);box-shadow:0 0 6px var(--amber-t)}
@keyframes statusPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.6)}}
.users-table .status-badge.active{background:var(--green-bg);color:var(--green-t);border:1px solid rgba(16,255,160,0.2)}
.users-table .status-badge.expired{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(255,77,109,0.2)}
.users-table .status-badge.disabled{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(255,184,0,0.2)}
.users-table .usage-bar{display:flex;align-items:center;gap:8px}
.users-table .usage-bar .bar{width:80px;height:4px;border-radius:4px;background:rgba(0,240,255,0.05);overflow:hidden;position:relative}
.users-table .usage-bar .bar .fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--cyan),var(--magenta),var(--purple));transition:width .8s var(--transition);box-shadow:0 0 8px var(--cyan)}
.users-table .usage-text{font-size:9px;color:var(--t2);white-space:nowrap;font-family:monospace}
.users-table .action-btns{display:flex;gap:4px;justify-content:center;flex-wrap:wrap}
.users-table .action-btns .btn{padding:3px 7px;font-size:9px;border-radius:6px}
.user-name-cell{display:flex;align-items:center;gap:8px}
.user-name-cell .avatar{width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,var(--cyan),var(--purple));display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:#000;flex-shrink:0;transition:transform .3s var(--transition);box-shadow:0 0 12px rgba(0,240,255,0.3)}
.user-name-cell .name{font-weight:700;color:var(--t1);font-size:12px}
.user-name-cell .uuid-short{font-size:8px;color:var(--t3);font-family:monospace;letter-spacing:0.5px}

/* === دکمه‌ها === */
.btn{font-family:inherit;font-size:11px;font-weight:700;border-radius:8px;padding:6px 12px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:all .3s var(--transition);white-space:nowrap;letter-spacing:0.3px}
.btn i{font-size:12px;transition:transform .3s}
.btn:hover i{transform:scale(1.15)}
.btn-p{background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));background-size:200% 200%;animation:btnGradient 5s ease infinite;color:#000;box-shadow:0 3px 15px rgba(0,240,255,0.25)}
@keyframes btnGradient{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 6px 25px rgba(0,240,255,0.4),0 0 40px rgba(255,46,154,0.2)}
.btn-o{background:rgba(255,255,255,0.02);border:1px solid var(--border-subtle);color:var(--t2)}
.btn-o:hover{background:rgba(0,240,255,0.05);border-color:var(--cyan);color:var(--cyan);transform:translateY(-1px)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(255,77,109,.2)}
.btn-d:hover{background:rgba(255,77,109,.15);transform:translateY(-1px);box-shadow:0 4px 15px rgba(255,77,109,0.3)}
.btn-pur{background:rgba(0,240,255,0.08);color:var(--cyan);border:1px solid rgba(0,240,255,.15)}
.btn-pur:hover{background:rgba(0,240,255,.15);transform:translateY(-1px);box-shadow:var(--glow-cyan)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(255,184,0,0.15)}
.btn-amber:hover{background:rgba(255,184,0,.15);transform:translateY(-1px)}
.btn-sm{padding:3px 8px;font-size:9px;border-radius:6px}
.btn-icon{width:24px;height:24px;padding:0;justify-content:center}
.btn-generate{background:rgba(0,240,255,0.08);color:var(--cyan);border:1px solid rgba(0,240,255,0.15);padding:6px 12px;flex-shrink:0}
.btn-generate:hover{background:rgba(0,240,255,0.15);transform:scale(1.05);box-shadow:var(--glow-cyan)}

/* === مودال‌ها === */
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.8);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.modal-bg.open{display:flex;animation:modalFade .3s ease}
@keyframes modalFade{from{opacity:0}to{opacity:1}}
.modal{background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--border-strong);border-radius:18px;padding:24px 22px;max-width:580px;width:calc(100% - 20px);max-height:90vh;overflow-y:auto;position:relative;animation:modalIn .4s var(--transition);box-shadow:0 30px 100px rgba(0,0,0,0.6),0 0 60px rgba(0,240,255,0.15)}
.modal::before{content:'';position:absolute;top:0;left:20px;right:20px;height:2px;background:linear-gradient(90deg,transparent,var(--cyan),var(--magenta),transparent);opacity:0.7}
@keyframes modalIn{from{opacity:0;transform:scale(0.92) translateY(20px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-close{position:absolute;top:12px;left:12px;background:rgba(255,255,255,0.05);border:1px solid var(--border-subtle);color:var(--t2);width:28px;height:28px;border-radius:8px;font-size:14px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:all .3s var(--transition)}
.modal-close:hover{background:var(--red-bg);color:var(--red-t);transform:rotate(90deg);border-color:var(--red-t)}
.modal-title{font-size:16px;font-weight:800;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px;padding-bottom:14px;border-bottom:1px solid var(--border-subtle)}
.modal-title i{color:var(--cyan);font-size:18px;filter:drop-shadow(0 0 6px var(--cyan))}
.fg{display:flex;flex-direction:column;gap:4px;margin-bottom:10px}
.fg label{font-size:10px;color:var(--cyan);font-weight:700;text-transform:uppercase;letter-spacing:0.5px;display:flex;align-items:center;gap:4px}
.fg label i{font-size:11px}
.fi{width:100%;padding:8px 12px;border-radius:8px;border:1px solid var(--border-subtle);background:rgba(0,0,15,0.4);color:var(--t1);font-family:inherit;font-size:11px;outline:none;transition:all .3s var(--transition)}
.fi:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,240,255,0.08),0 0 20px rgba(0,240,255,0.1);background:rgba(0,240,255,0.03)}
.fi::placeholder{color:var(--t3)}
select.fi{appearance:none;cursor:pointer;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2300f0ff' stroke-width='3'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:left 12px center;padding-left:30px}
.fi-date{color:var(--t1);background:rgba(0,0,15,0.4);border:1px solid var(--border-subtle);border-radius:8px;padding:8px 12px;width:100%;font-family:inherit;font-size:11px;outline:none;transition:all .3s var(--transition);cursor:pointer}
.fi-date:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,240,255,0.08)}
.fi-date::placeholder{color:var(--t3)}
.fg-row{display:flex;gap:8px;align-items:center}
.fg-row .fg{flex:1}

/* === اتصالات === */
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.conn-card{background:var(--bg-card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--border-subtle);border-radius:12px;padding:12px 14px;transition:all .3s var(--transition);position:relative;overflow:hidden}
.conn-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--cyan),transparent);opacity:0.5}
.conn-card:hover{border-color:var(--border-strong);transform:translateY(-3px);box-shadow:0 8px 30px rgba(0,240,255,0.15)}
.conn-card .ip{font-family:monospace;font-size:12px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-card .label{font-size:9px;color:var(--t3);margin-top:4px;letter-spacing:0.3px}
.conn-card .conn-info{display:flex;justify-content:space-between;margin-top:6px;font-size:9px;color:var(--t2);gap:4px;flex-wrap:wrap}
.conn-status-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--green-t);animation:pulseAnim 1.5s infinite;margin-left:4px;box-shadow:0 0 8px var(--green-t)}

/* === تنظیمات === */
.settings-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:18px 20px;max-width:500px;margin-bottom:12px;position:relative;overflow:hidden;transition:all .3s var(--transition)}
.settings-card:hover{border-color:var(--border-strong)}
.settings-card::before{content:'';position:absolute;top:-50%;right:-50%;width:200px;height:200px;background:radial-gradient(circle,rgba(0,240,255,0.04),transparent 70%);pointer-events:none}
.settings-card .title{font-size:14px;font-weight:800;color:var(--t1);margin-bottom:12px;display:flex;align-items:center;gap:8px}
.settings-card .title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.settings-card .field{margin-bottom:10px}
.settings-card .field label{font-size:10px;color:var(--t3);display:block;margin-bottom:4px;font-weight:700}
.settings-card .field input{width:100%;padding:8px 12px;border-radius:8px;border:1px solid var(--border-subtle);background:rgba(0,0,15,0.4);color:var(--t1);font-family:inherit;font-size:11px;outline:none;transition:.3s var(--transition)}
.settings-card .field input:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,240,255,0.08)}
.settings-card .btn{width:100%;justify-content:center;margin-top:6px;font-size:12px;padding:8px}
.settings-card .toggle-row{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--border-subtle)}
.settings-card .toggle-row .toggle-label{font-size:12px;color:var(--t2);display:flex;align-items:center;gap:6px}
.switch{position:relative;width:42px;height:22px;background:var(--t3);border-radius:11px;cursor:pointer;transition:all .4s var(--transition);flex-shrink:0}
.switch.on{background:linear-gradient(135deg,var(--cyan),var(--purple));box-shadow:0 0 12px rgba(0,240,255,0.4)}
.switch .slider{position:absolute;top:2px;right:2px;width:18px;height:18px;background:#fff;border-radius:50%;transition:all .4s var(--transition);box-shadow:0 2px 6px rgba(0,0,0,0.3)}
.switch.on .slider{right:22px}

/* === Toast === */
.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--border-strong);color:var(--t1);border-radius:12px;padding:10px 18px;font-size:12px;opacity:0;transition:all .4s var(--transition);z-index:999;pointer-events:none;box-shadow:0 8px 30px rgba(0,0,0,0.5),0 0 30px rgba(0,240,255,0.1);display:flex;align-items:center;gap:6px;font-weight:600}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,255,160,.3);background:rgba(16,255,160,0.1);color:var(--green-t);box-shadow:0 8px 30px rgba(16,255,160,0.2)}
.toast.err{border-color:rgba(255,77,109,.3);background:rgba(255,77,109,0.1);color:var(--red-t);box-shadow:0 8px 30px rgba(255,77,109,0.2)}
.toast.warn{border-color:rgba(255,184,0,.3);background:rgba(255,184,0,0.1);color:var(--amber-t);box-shadow:0 8px 30px rgba(255,184,0,0.2)}

.empty{text-align:center;padding:40px 20px;color:var(--t3)}
.empty i{font-size:36px;opacity:.3;display:block;margin-bottom:10px;filter:drop-shadow(0 0 10px rgba(0,240,255,0.2))}
.empty p{font-size:11px;letter-spacing:0.3px}

/* === ناوبری پایین (موبایل) === */
.bottom-nav{display:none;position:fixed;bottom:0;right:0;left:0;background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-top:1px solid var(--border-subtle);z-index:300;padding:6px 4px 8px;justify-content:space-around;align-items:center}
.bottom-nav .nav-item{display:flex;flex-direction:column;align-items:center;gap:2px;color:var(--t3);font-size:8px;cursor:pointer;padding:4px 8px;border-radius:10px;transition:all .3s var(--transition);border:none;background:none;font-family:inherit;min-width:44px;position:relative}
.bottom-nav .nav-item i{font-size:18px;transition:all .3s var(--transition)}
.bottom-nav .nav-item:hover{color:var(--cyan);transform:translateY(-2px)}
.bottom-nav .nav-item.active{color:var(--cyan)}
.bottom-nav .nav-item.active i{transform:scale(1.15);filter:drop-shadow(0 0 6px var(--cyan))}
.bottom-nav .nav-item .notif-dot{position:absolute;top:2px;right:6px;width:6px;height:6px;background:var(--red);border-radius:50%;animation:pulseAnim 1.5s infinite;box-shadow:0 0 6px var(--red)}

/* === صفحات === */
.pg{display:none;animation:pageIn .4s var(--transition)}
.pg.on{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}

@media(max-width:768px){
  .bottom-nav{display:flex !important}
  .main{padding-bottom:70px !important;margin-right:0 !important;padding-top:64px !important}
  .sidebar{transform:translateX(100%);padding-bottom:60px}
  .sidebar.open{transform:translateX(0)}
  .mob-top{display:flex}
  .stats-grid{grid-template-columns:repeat(3,1fr)}
}
@media(max-width:480px){
  .stats-grid{grid-template-columns:1fr 1fr}
  .main{padding:58px 10px 70px}
  .bottom-nav .nav-item{min-width:36px;padding:3px 6px}
  .bottom-nav .nav-item i{font-size:16px}
  .bottom-nav .nav-item span{font-size:7px}
  .users-table thead th{font-size:8px;padding:8px 6px}
  .users-table tbody td{font-size:10px;padding:8px 6px}
  .users-table .usage-bar .bar{width:40px}
  .stat-mini{padding:8px 10px}
  .stat-mini-num{font-size:14px}
  .topbar{padding:14px 16px}
  .tb-title{font-size:14px}
}
@media(min-width:769px){.bottom-nav{display:none !important}}

/* === تم روشن === */
body.light-theme{
  --bg-deep:#eef1f8;
  --bg-mid:#e1e6f0;
  --bg-surface:rgba(255,255,255,0.7);
  --bg-surface-2:rgba(255,255,255,0.85);
  --bg-card:rgba(255,255,255,0.75);
  --bg-card-hover:rgba(255,255,255,0.9);
  --border-subtle:rgba(0,100,200,0.1);
  --border-glow:rgba(0,150,255,0.3);
  --border-strong:rgba(0,150,255,0.45);
  --t1:#0f1729;
  --t2:#475569;
  --t3:#94a3b8;
  --shadow:0 8px 32px rgba(0,0,0,0.08),0 0 60px rgba(0,150,255,0.04)
}
body.light-theme .nebula-bg{display:none}
body.light-theme .stat-card .number{background:linear-gradient(135deg,#0f1729,rgba(0,150,200,0.8));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
body.light-theme .fi{background:rgba(255,255,255,0.7)}
body.light-theme .logo-name{background:linear-gradient(135deg,#0f1729,#0099cc);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
body.light-theme .nav-it.on{background:linear-gradient(90deg,rgba(0,150,255,0.12),rgba(0,150,255,0.02))}
body.light-theme .btn-p{color:#fff}

/* === RGB Mode === */
body.rgb-mode{animation:rgbShift 8s linear infinite}
@keyframes rgbShift{0%{filter:hue-rotate(0deg)}100%{filter:hue-rotate(360deg)}}

/* === شیمر برای نوار سهمیه === */
@keyframes shimmer{0%{transform:translateX(100%)}100%{transform:translateX(-200%)}}

/* ========================================
   ✦ WTF Factor #1: Command Palette (Ctrl+K) ✦
   ======================================== */
.cmdk-overlay{display:none;position:fixed;inset:0;z-index:600;background:rgba(0,0,0,0.7);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);align-items:flex-start;justify-content:center;padding-top:12vh}
.cmdk-overlay.open{display:flex;animation:cmdkFade .2s ease}
@keyframes cmdkFade{from{opacity:0}to{opacity:1}}
.cmdk-box{width:90%;max-width:640px;background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--border-strong);border-radius:16px;overflow:hidden;box-shadow:0 30px 100px rgba(0,0,0,0.6),0 0 60px rgba(0,240,255,0.15);animation:cmdkIn .35s var(--transition)}
@keyframes cmdkIn{from{opacity:0;transform:translateY(-30px) scale(0.96)}to{opacity:1;transform:translateY(0) scale(1)}}
.cmdk-input-wrap{padding:18px 20px;border-bottom:1px solid var(--border-subtle);display:flex;align-items:center;gap:12px}
.cmdk-input-wrap i{color:var(--cyan);font-size:20px;filter:drop-shadow(0 0 6px var(--cyan))}
.cmdk-input{flex:1;background:transparent;border:none;outline:none;color:var(--t1);font-family:inherit;font-size:16px;font-weight:600}
.cmdk-input::placeholder{color:var(--t3)}
.cmdk-kbd{font-size:10px;color:var(--t3);background:rgba(255,255,255,0.05);padding:3px 8px;border-radius:6px;border:1px solid var(--border-subtle);font-family:monospace}
.cmdk-list{max-height:400px;overflow-y:auto;padding:8px}
.cmdk-list::-webkit-scrollbar{width:4px}
.cmdk-list::-webkit-scrollbar-track{background:transparent}
.cmdk-list::-webkit-scrollbar-thumb{background:var(--cyan-soft);border-radius:4px}
.cmdk-category{font-size:10px;font-weight:700;color:var(--cyan);text-transform:uppercase;letter-spacing:1px;padding:8px 12px 4px;text-shadow:0 0 6px rgba(0,240,255,0.4)}
.cmdk-item{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:10px;cursor:pointer;transition:all .15s;color:var(--t1);font-size:13px;font-weight:600}
.cmdk-item:hover,.cmdk-item.active{background:rgba(0,240,255,0.08);color:var(--cyan)}
.cmdk-item.active{box-shadow:inset 3px 0 0 var(--cyan)}
.cmdk-item .cmdk-icon{width:32px;height:32px;border-radius:8px;background:rgba(0,240,255,0.05);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;color:var(--cyan)}
.cmdk-item .cmdk-text{flex:1;min-width:0}
.cmdk-item .cmdk-text .cmdk-title{font-size:13px;font-weight:700;color:var(--t1);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cmdk-item .cmdk-text .cmdk-desc{font-size:10px;color:var(--t3);margin-top:1px}
.cmdk-item .cmdk-shortcut{font-size:9px;color:var(--t3);background:rgba(255,255,255,0.05);padding:3px 6px;border-radius:5px;border:1px solid var(--border-subtle);font-family:monospace}
.cmdk-empty{text-align:center;padding:30px;color:var(--t3);font-size:12px}
.cmdk-empty i{font-size:32px;opacity:0.3;display:block;margin-bottom:8px}

/* ========================================
   ✦ WTF Factor #2: Counter Up Animation ✦
   ======================================== */
.counter-num{display:inline-block;transition:color .3s}
.counter-num.counting{color:var(--cyan);text-shadow:0 0 12px rgba(0,240,255,0.6)}

/* ========================================
   ✦ WTF Factor #3: World Map with Servers ✦
   ======================================== */
.world-map-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:18px 20px;margin-top:14px;position:relative;overflow:hidden}
.world-map-card .map-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px;margin-bottom:14px}
.world-map-card .map-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.world-map-svg-wrap{position:relative;width:100%;height:240px;background:radial-gradient(ellipse at center,rgba(0,240,255,0.04),transparent 70%);border-radius:12px;overflow:hidden;border:1px solid var(--border-subtle)}
.world-map-svg-wrap svg{width:100%;height:100%;display:block}
.server-marker{position:absolute;transform:translate(-50%,-50%);cursor:pointer;transition:all .3s var(--transition);z-index:2}
.server-marker .server-dot{width:10px;height:10px;border-radius:50%;background:var(--cyan);box-shadow:0 0 12px var(--cyan),0 0 0 0 rgba(0,240,255,0.7);animation:serverPulse 2s infinite}
.server-marker.active .server-dot{background:var(--green-t);box-shadow:0 0 15px var(--green-t)}
.server-marker:hover{transform:translate(-50%,-50%) scale(1.4)}
.server-marker:hover .server-tooltip{opacity:1;transform:translate(-50%,-100%)}
.server-tooltip{position:absolute;left:50%;bottom:100%;transform:translate(-50%,-8px);background:var(--bg-surface-2);backdrop-filter:blur(20px);border:1px solid var(--border-strong);border-radius:8px;padding:8px 12px;font-size:10px;white-space:nowrap;opacity:0;pointer-events:none;transition:all .25s;z-index:10;color:var(--t1);font-weight:600;box-shadow:0 8px 25px rgba(0,0,0,0.4)}
.server-tooltip .server-name{color:var(--cyan);font-weight:800;font-size:11px;margin-bottom:2px}
.server-tooltip .server-stat{font-size:9px;color:var(--t3)}
@keyframes serverPulse{0%{box-shadow:0 0 12px var(--cyan),0 0 0 0 rgba(0,240,255,0.7)}70%{box-shadow:0 0 12px var(--cyan),0 0 0 18px rgba(0,240,255,0)}100%{box-shadow:0 0 12px var(--cyan),0 0 0 0 rgba(0,240,255,0)}}
.server-connection{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1}
.server-connection line{stroke:url(#connGradient);stroke-width:1;opacity:0.4;stroke-dasharray:4 4;animation:dashMove 30s linear infinite}
@keyframes dashMove{to{stroke-dashoffset:-200}}

/* ========================================
   ✦ WTF Factor #4: Speedometer Gauge ✦
   ======================================== */
.speed-gauge-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:18px 20px;margin-top:14px}
.speed-gauge-title{font-size:13px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px;margin-bottom:12px}
.speed-gauge-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.gauge-wrap{position:relative;width:100%;height:180px;display:flex;align-items:center;justify-content:center}
.gauge-svg{width:100%;max-width:280px;height:100%}
.gauge-arc-bg{fill:none;stroke:rgba(0,240,255,0.05);stroke-width:12;stroke-linecap:round}
.gauge-arc-fg{fill:none;stroke:url(#gaugeGradient);stroke-width:12;stroke-linecap:round;transition:stroke-dashoffset .8s cubic-bezier(0.34,1.56,0.64,1);filter:drop-shadow(0 0 8px rgba(0,240,255,0.5))}
.gauge-needle{transform-origin:center;transition:transform .8s cubic-bezier(0.34,1.56,0.64,1)}
.gauge-value{position:absolute;bottom:20px;left:50%;transform:translateX(-50%);text-align:center;pointer-events:none}
.gauge-num{font-size:30px;font-weight:900;color:var(--cyan);font-family:monospace;text-shadow:0 0 14px rgba(0,240,255,0.5);line-height:1}
.gauge-label{font-size:10px;color:var(--t3);margin-top:4px;letter-spacing:0.5px}

/* ========================================
   ✦ WTF Factor #5: Real-time Activity Feed ✦
   ======================================== */
.activity-feed-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:14px 16px;margin-top:14px;max-height:280px;overflow-y:auto}
.activity-feed-card::-webkit-scrollbar{width:4px}
.activity-feed-card::-webkit-scrollbar-track{background:transparent}
.activity-feed-card::-webkit-scrollbar-thumb{background:var(--cyan-soft);border-radius:4px}
.activity-feed-title{font-size:13px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px;margin-bottom:10px;position:sticky;top:0;background:var(--bg-card);backdrop-filter:blur(20px);padding-bottom:6px}
.activity-feed-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.activity-feed-title .live-dot{margin-right:auto;width:8px;height:8px;border-radius:50%;background:var(--green-t);box-shadow:0 0 8px var(--green-t);animation:pulseAnim 1.5s infinite}
.activity-item{display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid rgba(0,240,255,0.04);font-size:11px;animation:activityIn .4s var(--transition)}
.activity-item:last-child{border-bottom:none}
@keyframes activityIn{from{opacity:0;transform:translateX(-15px)}to{opacity:1;transform:translateX(0)}}
.activity-icon{width:24px;height:24px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0;font-weight:700}
.activity-icon.info{background:rgba(0,240,255,0.08);color:var(--cyan)}
.activity-icon.success{background:var(--green-bg);color:var(--green-t)}
.activity-icon.warning{background:var(--amber-bg);color:var(--amber-t)}
.activity-icon.error{background:var(--red-bg);color:var(--red-t)}
.activity-text{flex:1;min-width:0;color:var(--t1);font-weight:600}
.activity-text .activity-user{color:var(--cyan);font-weight:700}
.activity-time{font-size:9px;color:var(--t3);margin-top:2px;font-family:monospace}

/* ========================================
   ✦ WTF Factor #6: Donut Chart for Protocol Distribution ✦
   ======================================== */
.donut-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:18px 20px;margin-top:14px}
.donut-title{font-size:13px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px;margin-bottom:14px}
.donut-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.donut-wrap{display:grid;grid-template-columns:200px 1fr;gap:16px;align-items:center}
.donut-canvas-wrap{position:relative;width:200px;height:200px;margin:0 auto}
.donut-center{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;pointer-events:none}
.donut-center .donut-num{font-size:28px;font-weight:900;color:var(--t1);line-height:1;font-family:monospace}
.donut-center .donut-lbl{font-size:9px;color:var(--t3);margin-top:4px;letter-spacing:0.5px;text-transform:uppercase}
.donut-legend{display:flex;flex-direction:column;gap:8px}
.donut-legend-item{display:flex;align-items:center;gap:8px;font-size:11px;color:var(--t1);font-weight:600}
.donut-legend-item .legend-dot{width:10px;height:10px;border-radius:3px;flex-shrink:0;box-shadow:0 0 6px currentColor}
.donut-legend-item .legend-name{flex:1}
.donut-legend-item .legend-val{color:var(--t3);font-family:monospace;font-weight:700}
@media(max-width:480px){.donut-wrap{grid-template-columns:1fr}}

/* ========================================
   ✦ WTF Factor #7: Desktop Notifications ✦
   ======================================== */
.notif-perm-card{background:rgba(0,240,255,0.04);border:1px solid var(--border-subtle);border-radius:10px;padding:10px 12px;margin-top:10px;font-size:11px;color:var(--t2);display:flex;align-items:center;gap:8px}
.notif-perm-card i{color:var(--cyan)}
.notif-perm-card button{margin-right:auto;background:rgba(0,240,255,0.08);color:var(--cyan);border:1px solid var(--cyan-soft);padding:4px 10px;border-radius:6px;cursor:pointer;font-family:inherit;font-size:10px;font-weight:700}

/* ========================================
   ✦ WTF Factor #8: Drag & Drop Reorder ✦
   ======================================== */
.users-table tbody tr.dragging{opacity:0.4;background:rgba(0,240,255,0.08) !important}
.users-table tbody tr.drag-over{border-top:2px solid var(--cyan)}
.users-table tbody tr[draggable="true"]{cursor:grab}
.users-table tbody tr[draggable="true"]:active{cursor:grabbing}

/* ========================================
   ✦ WTF Factor #9: Live Search + Filter ✦
   ======================================== */
.search-filter-bar{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:12px 16px;margin-bottom:12px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.search-input-wrap{position:relative;flex:1;min-width:200px}
.search-input-wrap i{position:absolute;right:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none}
.search-input{width:100%;padding:8px 36px 8px 12px;border-radius:8px;border:1px solid var(--border-subtle);background:rgba(0,0,15,0.4);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:all .3s var(--transition)}
.search-input:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,240,255,0.08)}
.search-input::placeholder{color:var(--t3)}
.filter-chip{padding:6px 12px;border-radius:20px;font-size:10px;font-weight:700;cursor:pointer;border:1px solid var(--border-subtle);background:rgba(255,255,255,0.02);color:var(--t3);transition:all .25s var(--transition);font-family:inherit;display:inline-flex;align-items:center;gap:4px}
.filter-chip:hover{background:rgba(0,240,255,0.05);color:var(--t1);border-color:var(--cyan-soft)}
.filter-chip.active{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#000;border-color:var(--cyan);box-shadow:0 0 12px rgba(0,240,255,0.3)}
.filter-chip .chip-count{font-size:9px;background:rgba(0,0,0,0.3);padding:1px 6px;border-radius:10px;font-weight:800}

/* ========================================
   ✦ WTF Factor #10: Particle Cursor Trail ✦
   ======================================== */
#particle-canvas{position:fixed;inset:0;z-index:9999;pointer-events:none}

/* ========================================
   ✦ WTF Factor #11: Player-style Bottom Bar ✦
   ======================================== */
.player-bar{position:fixed;bottom:0;right:0;left:0;z-index:250;background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-top:1px solid var(--border-strong);padding:8px 20px;display:flex;align-items:center;justify-content:space-between;gap:14px;transform:translateY(100%);transition:transform .5s var(--transition);box-shadow:0 -8px 30px rgba(0,0,0,0.4),0 0 30px rgba(0,240,255,0.05)}
.player-bar.show{transform:translateY(0)}
.player-bar-left{display:flex;align-items:center;gap:10px;font-size:11px;font-weight:700;color:var(--t1)}
.player-bar-left .pb-logo{width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 0 15px rgba(0,240,255,0.3);animation:logoPulse 4s ease-in-out infinite}
.player-bar-center{display:flex;align-items:center;gap:18px;font-size:11px}
.player-stat{display:flex;align-items:center;gap:6px;color:var(--t2);font-weight:600}
.player-stat i{color:var(--cyan);font-size:13px;filter:drop-shadow(0 0 4px var(--cyan))}
.player-stat .player-stat-val{color:var(--t1);font-weight:800;font-family:monospace}
.player-bar-right{display:flex;align-items:center;gap:8px}
.player-bar-right button{background:rgba(0,240,255,0.05);border:1px solid var(--border-subtle);color:var(--cyan);width:28px;height:28px;border-radius:8px;cursor:pointer;font-size:13px;display:flex;align-items:center;justify-content:center;transition:all .25s var(--transition)}
.player-bar-right button:hover{background:rgba(0,240,255,0.12);transform:translateY(-2px)}
@media(max-width:768px){.player-bar{padding:6px 12px}.player-bar-center{display:none}}
body.has-player-bar{padding-bottom:50px}
body.has-player-bar .main{padding-bottom:80px}

/* ========================================
   ✦ WTF Factor #12: Animated Theme Switcher (Circular Reveal) ✦
   ======================================== */
.theme-reveal{position:fixed;inset:0;z-index:9998;pointer-events:none;border-radius:50%;transform:scale(0);transition:transform .6s cubic-bezier(0.4,0,0.2,1)}
.theme-reveal.active{transform:scale(1)}

/* === Flatpickr === */
.flatpickr-calendar{background:var(--bg-surface-2) !important;backdrop-filter:blur(40px) !important;-webkit-backdrop-filter:blur(40px) !important;border:1px solid var(--border-strong) !important;border-radius:14px !important;box-shadow:var(--shadow) !important}
.flatpickr-calendar .flatpickr-months .flatpickr-month{color:var(--t1) !important}
.flatpickr-calendar .flatpickr-weekday{color:var(--cyan) !important;font-weight:700 !important}
.flatpickr-calendar .flatpickr-day{color:var(--t1) !important;border-radius:8px !important}
.flatpickr-calendar .flatpickr-day:hover{background:rgba(0,240,255,0.1) !important}
.flatpickr-calendar .flatpickr-day.selected{background:linear-gradient(135deg,var(--cyan),var(--purple)) !important;color:#000 !important;border-color:var(--cyan) !important;box-shadow:0 0 15px rgba(0,240,255,0.4) !important}
.flatpickr-calendar .flatpickr-day.today{border-color:var(--cyan) !important}
.flatpickr-calendar .flatpickr-day.inRange{background:rgba(0,240,255,0.08) !important}
.flatpickr-calendar .flatpickr-day.startRange,.flatpickr-calendar .flatpickr-day.endRange{background:linear-gradient(135deg,var(--cyan),var(--purple)) !important;color:#000 !important}
.flatpickr-calendar .flatpickr-day.disabled{color:var(--t3) !important}
.flatpickr-calendar .flatpickr-current-month .flatpickr-monthDropdown-months{color:var(--t1) !important;background:transparent !important}
.flatpickr-calendar .flatpickr-current-month input.cur-year{color:var(--t1) !important}
.flatpickr-calendar .flatpickr-prev-month,.flatpickr-calendar .flatpickr-next-month{color:var(--t3) !important}
.flatpickr-calendar .flatpickr-prev-month:hover,.flatpickr-calendar .flatpickr-next-month:hover{color:var(--cyan) !important}
.flatpickr-time{background:var(--bg-surface-2) !important;border-top:1px solid var(--border-subtle) !important;border-radius:0 0 14px 14px !important}
.flatpickr-time input{color:var(--t1) !important}
.flatpickr-time .flatpickr-time-separator{color:var(--t3) !important}
.flatpickr-time .numInputWrapper:hover{background:rgba(0,240,255,0.05) !important}
</style>
</head>
<body>
<canvas id="starfield-bg"></canvas>
<div class="nebula-bg nebula-bg-1"></div><div class="nebula-bg nebula-bg-2"></div>
<div class="toast" id="toast"></div>

<!-- Modal User -->
<div class="modal-bg" id="modal-user">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-user')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> <span id="modal-user-title">ساخت کاربر جدید</span></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="fg" style="grid-column:1/2;position:relative;">
        <label><i class="ti ti-tag"></i> <span id="f-label-name">نام کاربری</span></label>
        <div style="display:flex;gap:4px;">
          <input class="fi" id="user-label" placeholder="نام کاربری" style="flex:1">
          <button class="btn btn-generate" onclick="generateRandomUsername()" title="ساخت تصادفی"><i class="ti ti-dice"></i></button>
        </div>
      </div>
      <div class="fg"><label><i class="ti ti-lock"></i> <span id="f-label-password">رمز (اختیاری)</span></label><input class="fi" id="user-password" type="password" placeholder="خالی = بدون رمز" dir="ltr"></div>
      <div class="fg"><label><i class="ti ti-database"></i> <span id="f-label-quota">حجم (GB)</span></label><input class="fi" id="user-quota" type="number" min="0" step="0.5" value="2"></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> <span id="f-label-expiry">انقضا</span></label>
        <input class="fi-date" id="user-expiry-date" type="text" placeholder="انتخاب تاریخ">
      </div>
      <div class="fg"><label><i class="ti ti-devices"></i> <span id="f-label-devices">دستگاه</span></label><input class="fi" id="user-devices" type="number" min="0" max="10" value="1"></div>
      <div class="fg"><label><i class="ti ti-fingerprint"></i> <span id="f-label-fingerprint">انگشت‌نگاری</span></label>
        <select class="fi" id="user-fingerprint">
          <option value="chrome">🌐 Chrome</option><option value="firefox">🦊 Firefox</option>
          <option value="safari">🧭 Safari</option><option value="edge">🌊 Edge</option>
          <option value="ios">📱 iOS</option><option value="android">🤖 Android</option>
          <option value="safari_ios">🍏 Safari iOS</option><option value="random">🎲 Random</option><option value="none">🚫 None</option>
        </select>
      </div>
      <div class="fg">
        <label><i class="ti ti-settings"></i> <span id="f-label-protocol">پروتکل</span></label>
        <select class="fi" id="user-protocol">
          <option value="vless-ws">🚀 VLESS-WS</option>
          <option value="vless-grpc">⚡ VLESS-gRPC</option>
          <option value="vless-xhttp">🛡️ VLESS-XHTTP</option>
          <option value="vless-http2">📶 VLESS-HTTP/2</option>
          <option value="trojan-ws">🔒 Trojan-WS</option>
          <option value="shadowsocks">🌊 Shadowsocks</option>
        </select>
      </div>
      <div class="fg">
        <label><i class="ti ti-cloud"></i> <span id="f-label-http">HTTP نسخه</span></label>
        <select class="fi" id="user-http">
          <option value="h2">🚀 HTTP/2</option>
          <option value="h3">⚡ HTTP/3 (QUIC)</option>
          <option value="h1">📶 HTTP/1.1</option>
          <option value="auto">🔄 Auto</option>
        </select>
      </div>
    </div>
    <div style="display:flex;gap:8px;margin-top:14px"><button class="btn btn-p" onclick="saveUser()" style="flex:2"><i class="ti ti-check"></i> <span id="btn-create-user">ساخت کاربر</span></button><button class="btn btn-o" onclick="closeModal('modal-user')" style="flex:1"><span id="btn-cancel">انصراف</span></button></div>
  </div>
</div>

<!-- Modal Edit -->
<div class="modal-bg" id="modal-edit">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> <span id="modal-edit-title">ویرایش کاربر</span></div>
    <input type="hidden" id="edit-uuid">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="fg" style="grid-column:1/2;"><label><i class="ti ti-tag"></i> <span id="e-label-name">نام</span></label><input class="fi" id="edit-label" placeholder="نام کاربری"></div>
      <div class="fg" id="edit-password-section"><label><i class="ti ti-lock"></i> <span id="e-label-password">رمز جدید</span></label><input class="fi" id="edit-password" type="password" placeholder="برای تغییر" dir="ltr"></div>
      <div class="fg"><label><i class="ti ti-database"></i> <span id="e-label-quota">حجم (GB)</span></label><input class="fi" id="edit-quota" type="number" min="0" step="0.5"></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> <span id="e-label-expiry">انقضا</span></label>
        <input class="fi-date" id="edit-expiry-date" type="text" placeholder="انتخاب تاریخ">
      </div>
      <div class="fg"><label><i class="ti ti-devices"></i> <span id="e-label-devices">دستگاه</span></label><input class="fi" id="edit-devices" type="number" min="0" max="10"></div>
      <div class="fg"><label><i class="ti ti-toggle-left"></i> <span id="e-label-status">وضعیت</span></label><select class="fi" id="edit-status"><option value="true">✅ فعال</option><option value="false">❌ غیرفعال</option></select></div>
    </div>
    <div class="fg"><label><i class="ti ti-fingerprint"></i> <span id="e-label-fingerprint">انگشت‌نگاری</span></label>
      <select class="fi" id="edit-fingerprint">
        <option value="chrome">🌐 Chrome</option><option value="firefox">🦊 Firefox</option>
        <option value="safari">🧭 Safari</option><option value="edge">🌊 Edge</option>
        <option value="ios">📱 iOS</option><option value="android">🤖 Android</option>
        <option value="safari_ios">🍏 Safari iOS</option><option value="random">🎲 Random</option><option value="none">🚫 None</option>
      </select>
    </div>
    <div class="fg">
      <label><i class="ti ti-settings"></i> <span id="e-label-protocol">پروتکل</span></label>
      <select class="fi" id="edit-protocol">
        <option value="vless-ws">🚀 VLESS-WS</option>
        <option value="vless-grpc">⚡ VLESS-gRPC</option>
        <option value="vless-xhttp">🛡️ VLESS-XHTTP</option>
        <option value="vless-http2">📶 VLESS-HTTP/2</option>
        <option value="trojan-ws">🔒 Trojan-WS</option>
        <option value="shadowsocks">🌊 Shadowsocks</option>
      </select>
    </div>
    <div class="fg">
      <label><i class="ti ti-cloud"></i> <span id="e-label-http">HTTP نسخه</span></label>
      <select class="fi" id="edit-http">
        <option value="h2">🚀 HTTP/2</option>
        <option value="h3">⚡ HTTP/3 (QUIC)</option>
        <option value="h1">📶 HTTP/1.1</option>
        <option value="auto">🔄 Auto</option>
      </select>
    </div>
    <div style="display:flex;gap:8px;margin-top:14px"><button class="btn btn-p" onclick="saveEdit()" style="flex:2"><i class="ti ti-check"></i> <span id="btn-save">ذخیره</span></button><button class="btn btn-o" onclick="closeModal('modal-edit')" style="flex:1"><span id="btn-cancel2">انصراف</span></button></div>
  </div>
</div>

<!-- Modal Delete -->
<div class="modal-bg" id="modal-delete">
  <div class="modal" style="max-width:360px">
    <button class="modal-close" onclick="closeModal('modal-delete')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-trash"></i> <span id="modal-delete-title">حذف کاربر</span></div>
    <input type="hidden" id="delete-uuid">
    <p style="font-size:11px;color:var(--t2);margin-bottom:12px" id="delete-desc">برای حذف، رمز کانفیگ را وارد کنید.</p>
    <div class="fg"><label><i class="ti ti-lock"></i> <span id="d-label-password">رمز</span></label><input class="fi" id="delete-password" type="password" placeholder="رمز کانفیگ" dir="ltr"></div>
    <div style="display:flex;gap:8px;margin-top:14px"><button class="btn btn-d" onclick="confirmDelete()" style="flex:2"><i class="ti ti-trash"></i> <span id="btn-delete">حذف</span></button><button class="btn btn-o" onclick="closeModal('modal-delete')" style="flex:1"><span id="btn-cancel3">انصراف</span></button></div>
  </div>
</div>

<!-- Modal QR Code -->
<div class="modal-bg" id="modal-qr">
  <div class="modal" style="max-width:420px;text-align:center">
    <button class="modal-close" onclick="closeModal('modal-qr')"><i class="ti ti-x"></i></button>
    <div class="modal-title" style="justify-content:center"><i class="ti ti-qrcode"></i> <span id="qr-title">QR Code</span></div>
    <div id="qrcode-container" style="display:flex;justify-content:center;padding:14px 0;"></div>
    <p style="font-size:10px;color:var(--t3);margin-top:6px" id="qr-desc">اسکن کنید تا ساب‌لینک اضافه شود</p>
    <button class="btn btn-p btn-sm" onclick="downloadQR()" style="margin-top:10px"><i class="ti ti-download"></i> <span id="qr-download">دانلود QR</span></button>
  </div>
</div>

<div class="mob-top">
  <div class="ml"><div class="mob-logo">🏛️</div><span class="mob-title">PERSEPOLIS</span></div>
  <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
</div>
<div class="overlay" id="overlay"></div>

<aside class="sidebar" id="sb">
  <div class="logo"><div class="logo-icon">🏛️</div><div><div class="logo-name">PERSEPOLIS</div><div class="logo-sub">COSMIC PANEL</div></div></div>
  <div class="nav-wrap">
    <div class="nav-it on" data-pg="dashboard"><i class="ti ti-layout-dashboard"></i> <span id="nav-home">خانه</span></div>
    <div class="nav-it" data-pg="users"><i class="ti ti-users"></i> <span id="nav-users">کاربران</span></div>
    <div class="nav-it" data-pg="quota"><i class="ti ti-gauge"></i> <span id="nav-quota">مصرف مجاز</span></div>
    <div class="nav-it" data-pg="inbound"><i class="ti ti-plug"></i> <span id="nav-inbound">اینباند</span></div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> <span id="nav-connections">اتصالات</span></div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> <span id="nav-settings">تنظیمات</span></div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-notes"></i> <span id="nav-logs">لاگ‌ها</span></div>
    <div class="nav-it" data-pg="backup"><i class="ti ti-database"></i> <span id="nav-backup">بکاپ</span></div>
  </div>
  <div class="sb-foot"><button class="logout-btn" onclick="logout()"><i class="ti ti-logout"></i> <span id="nav-logout">خروج</span></button></div>
</aside>

<div class="bottom-nav" id="bottomNav">
  <button class="nav-item active" data-pg="dashboard" onclick="navTo('dashboard')"><i class="ti ti-layout-dashboard"></i><span id="b-home">خانه</span></button>
  <button class="nav-item" data-pg="users" onclick="navTo('users')"><i class="ti ti-users"></i><span id="b-users">کاربران</span></button>
  <button class="nav-item" data-pg="quota" onclick="navTo('quota')"><i class="ti ti-gauge"></i><span id="b-quota">سهمیه</span></button>
  <button class="nav-item" data-pg="inbound" onclick="navTo('inbound')"><i class="ti ti-plug"></i><span id="b-inbound">اینباند</span></button>
  <button class="nav-item" data-pg="settings" onclick="navTo('settings')"><i class="ti ti-settings"></i><span id="b-settings">تنظیمات</span></button>
</div>

<main class="main">
<!-- صفحه خانه -->
<section class="pg on" id="pg-dashboard">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> <span id="dash-title">خانه</span></div><div class="tb-sub" id="last-update">بروزرسانی: لحظه‌ای</div></div>
    <div class="tb-right">
      <span class="badge bg-fire" id="online-badge"><span class="dot dg"></span> ۰ آنلاین</span>
      <button class="btn btn-p btn-sm" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> <span id="dash-add-user">کاربر</span></button>
    </div>
  </div>
  
  <div class="stats-grid">
    <div class="stat-card"><span class="icon">📊</span><div class="number" id="stat-traffic">۰</div><div class="label" id="s-traffic">ترافیک</div><div class="sub">MB</div></div>
    <div class="stat-card"><span class="icon">📨</span><div class="number" id="stat-requests">۰</div><div class="label" id="s-requests">درخواست‌ها</div><div class="sub" id="s-count">تعداد</div></div>
    <div class="stat-card"><span class="icon">⏱️</span><div class="number" id="stat-uptime">۰۰:۰۰:۰۰</div><div class="label" id="s-uptime">آپتایم</div><div class="sub" id="s-time">زمان</div></div>
    <div class="stat-card"><span class="icon">💾</span><div class="number small" id="stat-disk">۰ GB</div><div class="label" id="s-disk">فضای دیسک</div><div class="sub" id="stat-disk-used">استفاده</div></div>
    <div class="stat-card"><span class="icon">📶</span><div class="number small" id="stat-speed">۰ B/s</div><div class="label" id="s-speed">سرعت</div><div class="sub" id="s-live">لحظه‌ای</div></div>
    <div class="stat-card"><span class="icon">👥</span><div class="number" id="stat-users">۰</div><div class="label" id="s-users">کاربران</div><div class="sub" id="stat-users-active">۰ فعال</div></div>
  </div>

  <div class="chart-section">
    <div class="chart-header">
      <div>
        <span class="chart-title"><i class="ti ti-chart-bar"></i> <span id="chart-title-text">مصرف روزانه</span></span>
        <span class="chart-sub" id="chart-sub-text">آخرین ۷ روز</span>
      </div>
      <div class="chart-actions">
        <button class="btn btn-sm btn-pur" onclick="loadChart('7d')" id="chart-7d">۷ روز</button>
        <button class="btn btn-sm btn-o" onclick="loadChart('30d')" id="chart-30d">۳۰ روز</button>
        <button class="btn btn-sm btn-o" onclick="loadChart('90d')" id="chart-90d">۹۰ روز</button>
      </div>
    </div>
    <div style="position:relative;height:200px;width:100%">
      <canvas id="trafficChart"></canvas>
    </div>
  </div>

  <div style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:14px 16px;margin-top:6px;transition:background .4s">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
      <span style="font-size:12px;font-weight:800;color:var(--t1)">🆕 <span id="recent-users-title">کاربران اخیر</span></span>
      <button class="btn btn-sm btn-o" onclick="loadDashboard()"><i class="ti ti-refresh"></i></button>
    </div>
    <div id="recent-users" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:6px"></div>
  </div>
  
  <!-- سرعت‌سنج زنده (Speedometer Gauge) -->
  <div class="speed-gauge-card">
    <div class="speed-gauge-title"><i class="ti ti-speedmeter"></i> <span id="gauge-title">سرعت زنده</span></div>
    <div class="gauge-wrap">
      <svg class="gauge-svg" viewBox="0 0 200 120">
        <defs>
          <linearGradient id="gaugeGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#00f0ff"/>
            <stop offset="50%" stop-color="#7b2ff7"/>
            <stop offset="100%" stop-color="#ff2e9a"/>
          </linearGradient>
        </defs>
        <!-- Background arc (180 degrees) -->
        <path class="gauge-arc-bg" d="M 20 100 A 80 80 0 0 1 180 100" />
        <!-- Foreground arc -->
        <path id="gaugeArc" class="gauge-arc-fg" d="M 20 100 A 80 80 0 0 1 180 100" stroke-dasharray="251.3" stroke-dashoffset="251.3" />
        <!-- Needle -->
        <g id="gaugeNeedle" class="gauge-needle" style="transform:rotate(-90deg);transform-origin:100px 100px">
          <line x1="100" y1="100" x2="100" y2="35" stroke="#00f0ff" stroke-width="2.5" stroke-linecap="round" filter="drop-shadow(0 0 6px #00f0ff)"/>
          <circle cx="100" cy="100" r="6" fill="#00f0ff" filter="drop-shadow(0 0 6px #00f0ff)"/>
          <circle cx="100" cy="100" r="3" fill="#0a0e2a"/>
        </g>
        <!-- Tick marks -->
        <text x="20" y="115" fill="#64748b" font-size="8">0</text>
        <text x="100" y="25" fill="#64748b" font-size="8" text-anchor="middle">50</text>
        <text x="180" y="115" fill="#64748b" font-size="8" text-anchor="end">100+</text>
      </svg>
      <div class="gauge-value">
        <div class="gauge-num" id="gaugeNum">0 B/s</div>
        <div class="gauge-label" id="gaugeLabel">سرعت دانلود لحظه‌ای</div>
      </div>
    </div>
  </div>
  
  <!-- نقشه جهان با سرورها + نمودار Donut پروتکل‌ها (در یک ردیف) -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px" id="map-donut-row">
    
    <!-- نقشه جهان -->
    <div class="world-map-card">
      <div class="map-title"><i class="ti ti-world"></i> <span id="map-title">سرورهای جهان</span></div>
      <div class="world-map-svg-wrap" id="worldMapWrap">
        <svg viewBox="0 0 800 400" preserveAspectRatio="xMidYMid meet" style="position:absolute;inset:0">
          <defs>
            <linearGradient id="connGradient" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.5"/>
              <stop offset="100%" stop-color="#ff2e9a" stop-opacity="0.5"/>
            </linearGradient>
          </defs>
          <!-- Simplified world continents as dots pattern -->
          <g fill="rgba(0,240,255,0.15)">
            <!-- North America -->
            <circle cx="160" cy="130" r="3"/><circle cx="180" cy="140" r="3"/><circle cx="200" cy="130" r="3"/><circle cx="170" cy="150" r="3"/><circle cx="210" cy="150" r="3"/><circle cx="190" cy="160" r="3"/><circle cx="220" cy="170" r="3"/><circle cx="150" cy="170" r="3"/><circle cx="230" cy="180" r="3"/><circle cx="180" cy="180" r="3"/><circle cx="200" cy="190" r="3"/><circle cx="170" cy="200" r="3"/><circle cx="220" cy="200" r="3"/><circle cx="250" cy="190" r="3"/>
            <!-- South America -->
            <circle cx="280" cy="240" r="3"/><circle cx="290" cy="260" r="3"/><circle cx="300" cy="280" r="3"/><circle cx="280" cy="290" r="3"/><circle cx="300" cy="300" r="3"/><circle cx="290" cy="310" r="3"/><circle cx="270" cy="280" r="3"/>
            <!-- Europe -->
            <circle cx="400" cy="130" r="3"/><circle cx="420" cy="140" r="3"/><circle cx="410" cy="120" r="3"/><circle cx="430" cy="130" r="3"/><circle cx="440" cy="150" r="3"/><circle cx="400" cy="150" r="3"/><circle cx="380" cy="140" r="3"/>
            <!-- Africa -->
            <circle cx="420" cy="200" r="3"/><circle cx="440" cy="220" r="3"/><circle cx="430" cy="240" r="3"/><circle cx="450" cy="260" r="3"/><circle cx="420" cy="270" r="3"/><circle cx="440" cy="290" r="3"/><circle cx="410" cy="280" r="3"/><circle cx="450" cy="310" r="3"/>
            <!-- Asia -->
            <circle cx="500" cy="130" r="3"/><circle cx="520" cy="140" r="3"/><circle cx="540" cy="130" r="3"/><circle cx="560" cy="150" r="3"/><circle cx="580" cy="140" r="3"/><circle cx="600" cy="160" r="3"/><circle cx="620" cy="170" r="3"/><circle cx="640" cy="180" r="3"/><circle cx="660" cy="190" r="3"/><circle cx="510" cy="170" r="3"/><circle cx="530" cy="180" r="3"/><circle cx="570" cy="190" r="3"/><circle cx="590" cy="200" r="3"/><circle cx="610" cy="210" r="3"/><circle cx="630" cy="220" r="3"/><circle cx="650" cy="230" r="3"/><circle cx="670" cy="220" r="3"/>
            <!-- Australia -->
            <circle cx="650" cy="300" r="3"/><circle cx="670" cy="310" r="3"/><circle cx="690" cy="320" r="3"/><circle cx="660" cy="330" r="3"/><circle cx="680" cy="340" r="3"/>
          </g>
        </svg>
        <!-- Connection lines (will be added by JS) -->
        <svg class="server-connection" id="serverConnections" viewBox="0 0 100 100" preserveAspectRatio="none"></svg>
        <!-- Server markers (will be positioned by JS) -->
        <div id="serverMarkers" style="position:absolute;inset:0"></div>
      </div>
    </div>
    
    <!-- Donut Chart -->
    <div class="donut-card">
      <div class="donut-title"><i class="ti ti-chart-donut"></i> <span id="donut-title-text">توزیع پروتکل‌ها</span></div>
      <div class="donut-wrap">
        <div class="donut-canvas-wrap">
          <canvas id="protocolDonut" width="200" height="200"></canvas>
          <div class="donut-center">
            <div class="donut-num" id="donutNum">0</div>
            <div class="donut-lbl" id="donutLbl">کاربر</div>
          </div>
        </div>
        <div class="donut-legend" id="donutLegend">
          <div class="empty"><i class="ti ti-loader" style="font-size:18px"></i><p style="font-size:10px">در حال بارگذاری...</p></div>
        </div>
      </div>
    </div>
    
  </div>
  
  <!-- Activity Feed زنده -->
  <div class="activity-feed-card">
    <div class="activity-feed-title">
      <i class="ti ti-activity"></i>
      <span id="activity-title">فعالیت‌های زنده</span>
      <span class="live-dot"></span>
    </div>
    <div id="activityFeed">
      <div class="empty"><i class="ti ti-loader" style="font-size:18px"></i><p style="font-size:10px">در حال بارگذاری...</p></div>
    </div>
  </div>
</section>

<!-- صفحه کاربران -->
<section class="pg" id="pg-users">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-users"></i> <span id="users-title">کاربران</span></div><div class="tb-sub" id="users-sub">لیست کانفیگ‌ها، سهمیه و انقضا</div></div><div class="tb-right"><button class="btn btn-o btn-sm" onclick="loadUsers()"><i class="ti ti-refresh"></i></button></div></div>
  
  <!-- نوار سرچ و فیلتر (WTF #9) -->
  <div class="search-filter-bar">
    <div class="search-input-wrap">
      <input type="text" class="search-input" id="userSearch" placeholder="جست‌وجوی کاربر..." oninput="applyUserFilters()">
      <i class="ti ti-search"></i>
    </div>
    <button class="filter-chip active" data-filter="all" onclick="setUserFilter('all')">همه <span class="chip-count" id="chip-all">0</span></button>
    <button class="filter-chip" data-filter="active" onclick="setUserFilter('active')">فعال <span class="chip-count" id="chip-active">0</span></button>
    <button class="filter-chip" data-filter="expired" onclick="setUserFilter('expired')">منقضی <span class="chip-count" id="chip-expired">0</span></button>
    <button class="filter-chip" data-filter="disabled" onclick="setUserFilter('disabled')">غیرفعال <span class="chip-count" id="chip-disabled">0</span></button>
    <button class="filter-chip" data-filter="high-usage" onclick="setUserFilter('high-usage')">مصرف بالا <span class="chip-count" id="chip-high">0</span></button>
  </div>
  
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:14px;">
    <div class="stat-mini"><span class="stat-mini-icon">👥</span><div><div class="stat-mini-num" id="users-total">0</div><div class="stat-mini-label" id="u-total">کل کاربران</div></div></div>
    <div class="stat-mini"><span class="stat-mini-icon">🟢</span><div><div class="stat-mini-num" id="users-active">0</div><div class="stat-mini-label" id="u-active">فعال</div></div></div>
    <div class="stat-mini"><span class="stat-mini-icon">🔴</span><div><div class="stat-mini-num" id="users-expired">0</div><div class="stat-mini-label" id="u-expired">منقضی</div></div></div>
    <div class="stat-mini"><span class="stat-mini-icon">📊</span><div><div class="stat-mini-num" id="users-traffic">0</div><div class="stat-mini-label" id="u-traffic">مصرف کل</div></div></div>
  </div>
  <div style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);overflow:hidden">
    <div style="overflow-x:auto;"><table class="users-table" id="users-table"><thead><tr><th id="th-name">نام</th><th id="th-account">اکانت</th><th id="th-status">وضعیت</th><th id="th-usage">مصرف دیتا</th><th id="th-duration">مدت</th><th style="text-align:center;" id="th-actions">عملیات</th></tr></thead><tbody id="users-tbody"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--t3);" id="no-users">هیچ کاربری وجود ندارد</td></tr></tbody></table></div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-top:1px solid var(--border-subtle);flex-wrap:wrap;gap:8px;"><div style="font-size:10px;color:var(--t3);"><span id="users-count-label">۰ کاربر</span></div><div style="display:flex;gap:6px;"><button class="btn btn-p btn-sm" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> <span id="add-user-btn">افزودن کاربر جدید</span></button></div></div>
  </div>
</section>

<!-- صفحه مصرف مجاز -->
<section class="pg" id="pg-quota">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-gauge"></i> <span id="quota-title">مصرف مجاز</span></div><div class="tb-sub" id="quota-sub">مصرف کل سرور نسبت به سقف مجاز</div></div><div class="tb-right"><button class="btn btn-sm btn-o" onclick="loadQuota()"><i class="ti ti-refresh"></i></button></div></div>
  
  <!-- کارت اصلی سهمیه -->
  <div class="settings-card" style="max-width:none">
    <div class="title"><i class="ti ti-chart-dots"></i> <span id="quota-overview-title">نمای کلی مصرف</span></div>
    
    <!-- اعداد بزرگ -->
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:20px">
      <div style="text-align:center;padding:18px 10px;background:rgba(0,240,255,0.04);border-radius:12px;border:1px solid var(--border-subtle)">
        <div style="font-size:11px;color:var(--t3);font-weight:700;letter-spacing:0.5px;text-transform:uppercase" id="q-used-label">مصرف شده</div>
        <div style="font-size:28px;font-weight:900;color:var(--cyan);margin-top:6px;font-family:monospace;text-shadow:0 0 12px rgba(0,240,255,0.4)" id="q-used-value">0 GB</div>
      </div>
      <div style="text-align:center;padding:18px 10px;background:rgba(255,46,154,0.04);border-radius:12px;border:1px solid var(--border-subtle)">
        <div style="font-size:11px;color:var(--t3);font-weight:700;letter-spacing:0.5px;text-transform:uppercase" id="q-limit-label">سقف مجاز</div>
        <div style="font-size:28px;font-weight:900;color:var(--magenta);margin-top:6px;font-family:monospace;text-shadow:0 0 12px rgba(255,46,154,0.4)" id="q-limit-value">100 GB</div>
      </div>
      <div style="text-align:center;padding:18px 10px;background:rgba(16,255,160,0.04);border-radius:12px;border:1px solid var(--border-subtle)">
        <div style="font-size:11px;color:var(--t3);font-weight:700;letter-spacing:0.5px;text-transform:uppercase" id="q-remaining-label">باقی مانده</div>
        <div style="font-size:28px;font-weight:900;color:var(--green-t);margin-top:6px;font-family:monospace;text-shadow:0 0 12px rgba(16,255,160,0.4)" id="q-remaining-value">100 GB</div>
      </div>
    </div>
    
    <!-- نوار پیشرفت خطی اصلی -->
    <div style="margin-top:18px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
        <span style="font-size:12px;font-weight:700;color:var(--t1)" id="q-progress-label">میزان مصرف</span>
        <span style="font-size:14px;font-weight:900;color:var(--cyan);font-family:monospace" id="q-percent">0.0%</span>
      </div>
      <div id="q-progress-bar-bg" style="height:24px;border-radius:14px;background:rgba(0,240,255,0.06);overflow:hidden;border:1px solid var(--border-subtle);position:relative">
        <div id="q-progress-fill" style="height:100%;border-radius:14px;background:linear-gradient(90deg,#00f0ff,#7b2ff7,#ff2e9a);background-size:200% 200%;animation:gradientFlow 5s ease infinite;width:0%;transition:width 1.2s cubic-bezier(0.34,1.56,0.64,1);box-shadow:0 0 15px rgba(0,240,255,0.5);position:relative">
          <div style="position:absolute;top:0;right:0;width:40px;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.4),transparent);animation:shimmer 2s linear infinite"></div>
        </div>
      </div>
      <div style="display:flex;justify-content:space-between;margin-top:6px;font-size:9px;color:var(--t3)">
        <span>0 GB</span>
        <span id="q-mid-label">50 GB</span>
        <span id="q-end-label">100 GB</span>
      </div>
    </div>
    
    <!-- هشدار تموم شدن سهمیه -->
    <div id="q-alert" style="display:none;margin-top:18px;padding:16px 18px;background:rgba(255,77,109,0.12);border:1px solid rgba(255,77,109,0.35);border-radius:12px;align-items:center;gap:10px;animation:pulseAnim 2s infinite;box-shadow:0 0 25px rgba(255,77,109,0.2)">
      <i class="ti ti-alert-octagon" style="font-size:24px;color:var(--red-t);flex-shrink:0"></i>
      <div>
        <div style="font-size:14px;font-weight:800;color:var(--red-t)" id="q-alert-title">⚠️ مصرف مجاز شما تمام شد</div>
        <div style="font-size:10px;color:var(--t2);margin-top:3px" id="q-alert-desc">لطفا با مدیر سیستم تماس بگیرید یا سهمیه را افزایش دهید</div>
      </div>
    </div>
  </div>
  
  <!-- توزیع مصرف بین کاربران -->
  <div style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:16px 18px;margin-top:14px">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
      <span style="font-size:13px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px"><i class="ti ti-users" style="color:var(--cyan)"></i> <span id="q-users-title">مصرف به تفکیک کاربران</span></span>
      <span style="font-size:10px;color:var(--t3)" id="q-users-sub">برترین مصرف‌کنندگان</span>
    </div>
    <div id="q-users-list" style="display:flex;flex-direction:column;gap:10px">
      <div class="empty"><i class="ti ti-users"></i><p style="font-size:10px">در حال بارگذاری...</p></div>
    </div>
  </div>
  
  <!-- نمودار مصرف تجمعی -->
  <div class="chart-section" style="margin-top:14px">
    <div class="chart-header">
      <div>
        <span class="chart-title"><i class="ti ti-chart-line"></i> <span id="q-cumulative-title">مصرف تجمعی</span></span>
        <span class="chart-sub" id="q-cumulative-sub">انباشت مصرف نسبت به سقف مجاز</span>
      </div>
    </div>
    <div style="position:relative;height:200px;width:100%">
      <canvas id="quotaChart"></canvas>
    </div>
  </div>
</section>

<!-- صفحه اینباند -->
<section class="pg" id="pg-inbound">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-plug"></i> <span id="inbound-title">اینباند</span></div><div class="tb-sub" id="inbound-sub">تنظیمات ورودی</div></div></div>
  <div style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:18px 20px;margin-bottom:14px">
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">
      <div style="text-align:center;padding:12px 8px;background:rgba(0,240,255,0.04);border-radius:10px;border:1px solid var(--border-subtle)"><div style="font-size:18px;font-weight:900;color:var(--cyan)" id="inbound-port">۴۴۳</div><div style="font-size:9px;color:var(--t3);margin-top:2px" id="inb-port-label">پورت</div></div>
      <div style="text-align:center;padding:12px 8px;background:rgba(123,47,247,0.04);border-radius:10px;border:1px solid var(--border-subtle)"><div style="font-size:16px;font-weight:900;color:var(--purple)" id="inbound-protocol">VLESS-WS</div><div style="font-size:9px;color:var(--t3);margin-top:2px" id="inb-protocol-label">پروتکل</div></div>
      <div style="text-align:center;padding:12px 8px;background:rgba(255,46,154,0.04);border-radius:10px;border:1px solid var(--border-subtle)"><div style="font-size:13px;font-weight:900;color:var(--magenta)" id="inbound-host">—</div><div style="font-size:9px;color:var(--t3);margin-top:2px" id="inb-host-label">هاست</div></div>
      <div style="text-align:center;padding:12px 8px;background:rgba(16,255,160,0.04);border-radius:10px;border:1px solid var(--border-subtle)"><div style="font-size:14px;font-weight:900;color:var(--green-t)">✅ <span id="inb-status-label">فعال</span></div><div style="font-size:9px;color:var(--t3);margin-top:2px" id="inb-status-title">وضعیت</div></div>
    </div>
  </div>
</section>

<!-- صفحه اتصالات -->
<section class="pg" id="pg-connections">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-plug-connected"></i> <span id="conn-title">اتصالات</span></div><div class="tb-sub" id="conn-count">۰ اتصال</div></div><div class="tb-right"><span class="badge bg-green"><span class="dot dg pulse"></span> <span id="conn-active-label">فعال</span></span><button class="btn btn-sm btn-o" onclick="loadConnections()"><i class="ti ti-refresh"></i></button></div></div>
  <div id="conns-grid" class="conn-grid"><div class="empty"><i class="ti ti-plug-off"></i><p id="no-conn">هیچ اتصالی وجود ندارد</p></div></div>
</section>

<!-- صفحه تنظیمات -->
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> <span id="settings-title">تنظیمات</span></div><div class="tb-sub" id="settings-sub">مدیریت پنل</div></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-color-swatch"></i> <span id="set-theme-title">تم پنل</span></div><div style="display:flex;gap:8px;margin-top:6px;"><button class="btn" onclick="setTheme('dark')" id="theme-dark-btn" style="flex:1;font-size:12px;padding:8px 14px;background:rgba(0,0,30,0.4);border:1px solid var(--border-strong);color:var(--cyan);">🌙 <span id="set-dark">کیهانی</span></button><button class="btn" onclick="setTheme('light')" id="theme-light-btn" style="flex:1;font-size:12px;padding:8px 14px;background:var(--bg-card);border:1px solid var(--border-subtle);color:var(--t2);">☀️ <span id="set-light">روشن</span></button></div><div style="font-size:10px;color:var(--t3);margin-top:8px;">💡 <span id="set-current-theme">تم فعلی</span>: <span id="current-theme-label">کیهانی</span></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-language"></i> <span id="set-lang-title">زبان پنل</span></div><div style="display:flex;gap:8px;margin-top:6px"><button class="btn btn-pur" onclick="setLang('fa')" style="flex:1;font-size:12px;padding:8px 14px" id="lang-fa-btn">🇮🇷 فارسی</button><button class="btn btn-o" onclick="setLang('en')" style="flex:1;font-size:12px;padding:8px 14px" id="lang-en-btn">🇬🇧 English</button></div><div style="font-size:10px;color:var(--t3);margin-top:8px">💡 <span id="set-current-lang">زبان فعلی</span>: <span id="current-lang-label">فارسی</span></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-color-palette"></i> <span id="set-rgb-title">حالت RGB متحرک</span></div><div class="toggle-row"><div class="toggle-label"><i class="ti ti-color-swatch" style="background:linear-gradient(135deg,#ff0000,#00ff00,#0000ff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent"></i> چرخش رنگ‌های RGB</div><div class="switch" id="rgb-switch" onclick="toggleRGB()"><div class="slider"></div></div></div></div>
  
</section>

<!-- صفحه لاگ‌ها -->
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-notes"></i> <span id="logs-title">لاگ‌ها</span></div><div class="tb-sub" id="logs-count">۰ لاگ</div></div><div class="tb-right"><button class="btn btn-sm btn-o" onclick="loadLogs()"><i class="ti ti-refresh"></i></button></div></div>
  <div style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:12px 14px;max-height:450px;overflow-y:auto"><div id="logs-container" style="font-family:monospace;font-size:10px;color:var(--t2);direction:ltr;text-align:left;line-height:1.7"></div></div>
</section>

<!-- صفحه بکاپ -->
<section class="pg" id="pg-backup">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-database"></i> <span id="backup-title">بکاپ</span></div><div class="tb-sub" id="backup-sub">ذخیره و بازیابی</div></div></div>
  <div class="settings-card"><div class="title"><i class="ti ti-download"></i> <span id="backup-download-title">بکاپ‌گیری</span></div><div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn btn-p btn-sm" onclick="createBackup()" style="flex:2"><i class="ti ti-download"></i> <span id="backup-download-btn">دانلود</span></button><button class="btn btn-o btn-sm" onclick="document.getElementById('restore-input').click()" style="flex:1"><i class="ti ti-upload"></i> <span id="backup-restore-btn">بازیابی</span></button><input type="file" id="restore-input" accept=".json" style="display:none" onchange="restoreBackup(event)"></div></div>
</section>
</main>

<!-- ==================== WTF #1: Command Palette (Ctrl+K) ==================== -->
<div class="cmdk-overlay" id="cmdkOverlay" onclick="if(event.target===this)closeCmdk()">
  <div class="cmdk-box">
    <div class="cmdk-input-wrap">
      <i class="ti ti-search"></i>
      <input type="text" class="cmdk-input" id="cmdkInput" placeholder="جست‌وجو یا دستور... (مثلاً: کاربر جدید، QR، تم)" oninput="filterCmdk()" autocomplete="off">
      <span class="cmdk-kbd">ESC</span>
    </div>
    <div class="cmdk-list" id="cmdkList"></div>
  </div>
</div>

<!-- ==================== WTF #10: Particle Canvas (Cursor Trail) ==================== -->
<canvas id="particle-canvas"></canvas>

<!-- ==================== WTF #11: Player-style Bottom Bar ==================== -->
<div class="player-bar" id="playerBar">
  <div class="player-bar-left">
    <div class="pb-logo">🏛️</div>
    <div>
      <div style="font-size:12px;font-weight:800;color:var(--t1)">PERSEPOLIS</div>
      <div style="font-size:8px;color:var(--t3);letter-spacing:1px">COSMIC · v2.0</div>
    </div>
  </div>
  <div class="player-bar-center">
    <div class="player-stat"><i class="ti ti-users"></i> <span id="pb-users">0</span></div>
    <div class="player-stat"><i class="ti ti-bolt"></i> <span id="pb-online">0</span></div>
    <div class="player-stat"><i class="ti ti-activity"></i> <span id="pb-traffic">0 MB</span></div>
    <div class="player-stat"><i class="ti ti-clock"></i> <span id="pb-uptime">00:00:00</span></div>
  </div>
  <div class="player-bar-right">
    <button onclick="openCmdk()" title="Command Palette (Ctrl+K)"><i class="ti ti-command"></i></button>
    <button onclick="navTo('dashboard')" title="خانه"><i class="ti ti-home"></i></button>
    <button onclick="navTo('quota')" title="سهمیه"><i class="ti ti-gauge"></i></button>
    <button onclick="togglePlayerBar()" title="بستن نوار"><i class="ti ti-x"></i></button>
  </div>
</div>

<!-- ==================== WTF #12: Theme Reveal ==================== -->
<div class="theme-reveal" id="themeReveal"></div>

<script>
// === ستاره‌های متحرک (Canvas) ===
const canvasBg = document.getElementById('starfield-bg');
const ctxBg = canvasBg.getContext('2d');
let starsBg = [];
function resizeCanvasBg() {
    canvasBg.width = window.innerWidth;
    canvasBg.height = window.innerHeight;
    starsBg = [];
    const count = Math.floor((canvasBg.width * canvasBg.height) / 12000);
    for (let i = 0; i < count; i++) {
        starsBg.push({
            x: Math.random() * canvasBg.width,
            y: Math.random() * canvasBg.height,
            r: Math.random() * 1.2 + 0.2,
            o: Math.random() * 0.6 + 0.2,
            tw: Math.random() * Math.PI * 2,
            color: Math.random() > 0.85 ? '#00f0ff' : (Math.random() > 0.7 ? '#ff2e9a' : '#ffffff')
        });
    }
}
function drawStarsBg() {
    ctxBg.clearRect(0, 0, canvasBg.width, canvasBg.height);
    starsBg.forEach(s => {
        s.tw += 0.015;
        const op = s.o * (0.5 + 0.5 * Math.sin(s.tw));
        ctxBg.beginPath();
        ctxBg.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctxBg.fillStyle = s.color;
        ctxBg.globalAlpha = op;
        ctxBg.shadowBlur = 6;
        ctxBg.shadowColor = s.color;
        ctxBg.fill();
    });
    ctxBg.globalAlpha = 1;
    ctxBg.shadowBlur = 0;
    requestAnimationFrame(drawStarsBg);
}
window.addEventListener('resize', resizeCanvasBg);
resizeCanvasBg();
drawStarsBg();

// ===== ترجمه‌ها =====
const translations = {
  fa: {
    nav_home: 'خانه', nav_users: 'کاربران', nav_inbound: 'اینباند',
    nav_connections: 'اتصالات', nav_settings: 'تنظیمات', nav_logs: 'لاگ‌ها',
    nav_backup: 'بکاپ', nav_logout: 'خروج', nav_quota: 'مصرف مجاز',
    b_quota: 'سهمیه',
    quota_title: 'مصرف مجاز', quota_sub: 'مصرف کل سرور نسبت به سقف مجاز',
    quota_overview_title: 'نمای کلی مصرف',
    q_used_label: 'مصرف شده', q_limit_label: 'سقف مجاز', q_remaining_label: 'باقی مانده',
    q_progress_label: 'میزان مصرف',
    q_alert_title: '⚠️ مصرف مجاز شما تمام شد',
    q_alert_desc: 'لطفا با مدیر سیستم تماس بگیرید یا سهمیه را افزایش دهید',
    q_users_title: 'مصرف به تفکیک کاربران', q_users_sub: 'برترین مصرف‌کنندگان',
    q_cumulative_title: 'مصرف تجمعی', q_cumulative_sub: 'انباشت مصرف نسبت به سقف مجاز',
    // WTF Factor translations
    cmdk_placeholder: 'جست‌وجو یا دستور... (مثلاً: کاربر جدید، QR، تم)',
    cmdk_cat_navigation: 'ناوبری',
    cmdk_cat_actions: 'عملیات',
    cmdk_cat_settings: 'تنظیمات',
    cmdk_cat_users: 'کاربران',
    cmdk_no_results: 'نتیجه‌ای یافت نشد',
    cmdk_open_user: 'ساخت کاربر جدید', cmdk_open_user_d: 'باز کردن مودال ساخت کاربر',
    cmdk_nav_dashboard: 'رفتن به خانه', cmdk_nav_dashboard_d: 'صفحه اصلی داشبورد',
    cmdk_nav_users: 'رفتن به کاربران', cmdk_nav_users_d: 'لیست کاربران',
    cmdk_nav_quota: 'رفتن به مصرف مجاز', cmdk_nav_quota_d: 'سهمیه کل سرور',
    cmdk_nav_inbound: 'رفتن به اینباند', cmdk_nav_inbound_d: 'تنظیمات ورودی',
    cmdk_nav_connections: 'رفتن به اتصالات', cmdk_nav_connections_d: 'اتصالات فعال',
    cmdk_nav_settings: 'رفتن به تنظیمات', cmdk_nav_settings_d: 'تنظیمات پنل',
    cmdk_nav_logs: 'رفتن به لاگ‌ها', cmdk_nav_logs_d: 'لاگ‌های سیستم',
    cmdk_nav_backup: 'رفتن به بکاپ', cmdk_nav_backup_d: 'بکاپ‌گیری',
    cmdk_logout: 'خروج از پنل', cmdk_logout_d: 'خروج و بازگشت به صفحه ورود',
    cmdk_toggle_theme: 'تغییر تم (روشن/کیهانی)', cmdk_toggle_theme_d: 'سوییچ بین تم روشن و تاریک',
    cmdk_toggle_rgb: 'تغییر حالت RGB', cmdk_toggle_rgb_d: 'چرخش رنگ‌های RGB',
    cmdk_refresh: 'بروزرسانی داده‌ها', cmdk_refresh_d: 'بارگذاری مجدد داشبورد',
    cmdk_backup: 'بکاپ‌گیری', cmdk_backup_d: 'دانلود فایل بکاپ',
    gauge_title: 'سرعت زنده', gauge_label: 'سرعت دانلود لحظه‌ای',
    map_title: 'سرورهای جهان',
    donut_title: 'توزیع پروتکل‌ها', donut_label: 'کاربر',
    activity_title: 'فعالیت‌های زنده',
    activity_user_created: 'کاربر {user} ساخته شد',
    activity_user_deleted: 'کاربر {user} حذف شد',
    activity_user_edited: 'کاربر {user} ویرایش شد',
    activity_quota_warning: 'سهمیه کاربر {user} نزدیک اتمام است',
    activity_quota_exhausted: 'مصرف مجاز شما تمام شد',
    activity_login: 'ورود به پنل',
    notif_enable: 'فعال‌سازی اطلاع‌رسانی دسکتاپ',
    notif_desc: 'برای رویدادهای مهم (سهمیه تمام شد، کاربر ساخته شد) مطلع شوید',
    notif_enable_btn: 'فعال‌سازی',
    search_placeholder: 'جست‌وجوی کاربر...',
    filter_all: 'همه', filter_active: 'فعال', filter_expired: 'منقضی',
    filter_disabled: 'غیرفعال', filter_high_usage: 'مصرف بالا',
    dash_title: 'خانه', dash_add_user: 'کاربر',
    s_traffic: 'ترافیک', s_requests: 'درخواست‌ها', s_uptime: 'آپتایم',
    s_disk: 'فضای دیسک', s_speed: 'سرعت', s_users: 'کاربران',
    s_count: 'تعداد', s_time: 'زمان', s_live: 'لحظه‌ای',
    chart_title: 'مصرف روزانه', chart_sub: 'آخرین ۷ روز',
    recent_users: 'کاربران اخیر',
    users_title: 'کاربران', users_sub: 'لیست کانفیگ‌ها، سهمیه و انقضا',
    u_total: 'کل کاربران', u_active: 'فعال', u_expired: 'منقضی', u_traffic: 'مصرف کل',
    th_name: 'نام', th_account: 'اکانت', th_status: 'وضعیت', th_usage: 'مصرف دیتا',
    th_duration: 'مدت', th_actions: 'عملیات',
    add_user_btn: 'افزودن کاربر جدید', no_users: 'هیچ کاربری وجود ندارد',
    inbound_title: 'اینباند', inbound_sub: 'تنظیمات ورودی',
    inb_port: 'پورت', inb_protocol: 'پروتکل', inb_host: 'هاست', inb_status: 'وضعیت',
    conn_title: 'اتصالات', conn_active: 'فعال', no_conn: 'هیچ اتصالی وجود ندارد',
    settings_title: 'تنظیمات', settings_sub: 'مدیریت پنل',
    set_theme: 'تم پنل', set_dark: 'کیهانی', set_light: 'روشن',
    set_current_theme: 'تم فعلی', set_lang: 'زبان پنل', set_current_lang: 'زبان فعلی',
    set_rgb: 'حالت RGB متحرک',
    backup_title: 'بکاپ', backup_sub: 'ذخیره و بازیابی',
    backup_download: 'بکاپ‌گیری', backup_download_btn: 'دانلود', backup_restore_btn: 'بازیابی',
    logs_title: 'لاگ‌ها',
    modal_user_title: 'ساخت کاربر جدید',
    f_label_name: 'نام کاربری', f_label_quota: 'حجم (GB)',
    f_label_expiry: 'انقضا', f_label_devices: 'دستگاه',
    f_label_fingerprint: 'انگشت‌نگاری', f_label_protocol: 'پروتکل',
    f_label_http: 'HTTP نسخه', f_label_password: 'رمز (اختیاری)',
    btn_create_user: 'ساخت کاربر', btn_cancel: 'انصراف',
    modal_edit_title: 'ویرایش کاربر',
    e_label_name: 'نام', e_label_password: 'رمز جدید',
    e_label_quota: 'حجم (GB)', e_label_expiry: 'انقضا',
    e_label_devices: 'دستگاه', e_label_status: 'وضعیت',
    e_label_fingerprint: 'انگشت‌نگاری', e_label_protocol: 'پروتکل',
    e_label_http: 'HTTP نسخه',
    btn_save: 'ذخیره',
    modal_delete_title: 'حذف کاربر', delete_desc: 'برای حذف، رمز کانفیگ را وارد کنید.',
    d_label_password: 'رمز', btn_delete: 'حذف',
    qr_title: 'QR Code', qr_desc: 'اسکن کنید تا ساب‌لینک اضافه شود',
    qr_download: 'دانلود QR'
  },
  en: {
    nav_home: 'Home', nav_users: 'Users', nav_inbound: 'Inbound',
    nav_connections: 'Connections', nav_settings: 'Settings', nav_logs: 'Logs',
    nav_backup: 'Backup', nav_logout: 'Logout', nav_quota: 'Quota',
    b_quota: 'Quota',
    quota_title: 'Allowed Quota', quota_sub: 'Total server usage vs allowed limit',
    quota_overview_title: 'Usage Overview',
    q_used_label: 'Used', q_limit_label: 'Allowed Limit', q_remaining_label: 'Remaining',
    q_progress_label: 'Usage Progress',
    q_alert_title: '⚠️ Your allowed quota has been exhausted',
    q_alert_desc: 'Please contact the administrator or increase the quota',
    q_users_title: 'Per-user usage', q_users_sub: 'Top consumers',
    q_cumulative_title: 'Cumulative Usage', q_cumulative_sub: 'Accumulated usage vs allowed limit',
    // WTF Factor translations
    cmdk_placeholder: 'Search or command... (e.g.: new user, QR, theme)',
    cmdk_cat_navigation: 'Navigation',
    cmdk_cat_actions: 'Actions',
    cmdk_cat_settings: 'Settings',
    cmdk_cat_users: 'Users',
    cmdk_no_results: 'No results found',
    cmdk_open_user: 'Create New User', cmdk_open_user_d: 'Open create user modal',
    cmdk_nav_dashboard: 'Go to Dashboard', cmdk_nav_dashboard_d: 'Main dashboard page',
    cmdk_nav_users: 'Go to Users', cmdk_nav_users_d: 'Users list',
    cmdk_nav_quota: 'Go to Quota', cmdk_nav_quota_d: 'Server total quota',
    cmdk_nav_inbound: 'Go to Inbound', cmdk_nav_inbound_d: 'Inbound settings',
    cmdk_nav_connections: 'Go to Connections', cmdk_nav_connections_d: 'Active connections',
    cmdk_nav_settings: 'Go to Settings', cmdk_nav_settings_d: 'Panel settings',
    cmdk_nav_logs: 'Go to Logs', cmdk_nav_logs_d: 'System logs',
    cmdk_nav_backup: 'Go to Backup', cmdk_nav_backup_d: 'Backup',
    cmdk_logout: 'Logout from panel', cmdk_logout_d: 'Logout and return to login page',
    cmdk_toggle_theme: 'Toggle Theme (Light/Cosmic)', cmdk_toggle_theme_d: 'Switch between light and dark themes',
    cmdk_toggle_rgb: 'Toggle RGB Mode', cmdk_toggle_rgb_d: 'Rotate RGB colors',
    cmdk_refresh: 'Refresh Data', cmdk_refresh_d: 'Reload dashboard data',
    cmdk_backup: 'Backup', cmdk_backup_d: 'Download backup file',
    gauge_title: 'Live Speed', gauge_label: 'Live download speed',
    map_title: 'World Servers',
    donut_title: 'Protocol Distribution', donut_label: 'users',
    activity_title: 'Live Activity',
    activity_user_created: 'User {user} created',
    activity_user_deleted: 'User {user} deleted',
    activity_user_edited: 'User {user} edited',
    activity_quota_warning: 'User {user} quota near limit',
    activity_quota_exhausted: 'Your allowed quota is exhausted',
    activity_login: 'Logged in to panel',
    notif_enable: 'Enable Desktop Notifications',
    notif_desc: 'Get notified for important events (quota exhausted, user created)',
    notif_enable_btn: 'Enable',
    search_placeholder: 'Search users...',
    filter_all: 'All', filter_active: 'Active', filter_expired: 'Expired',
    filter_disabled: 'Disabled', filter_high_usage: 'High Usage',
    dash_title: 'Dashboard', dash_add_user: 'User',
    s_traffic: 'Traffic', s_requests: 'Requests', s_uptime: 'Uptime',
    s_disk: 'Disk', s_speed: 'Speed', s_users: 'Users',
    s_count: 'Count', s_time: 'Time', s_live: 'Live',
    chart_title: 'Daily Usage', chart_sub: 'Last 7 days',
    recent_users: 'Recent Users',
    users_title: 'Users', users_sub: 'Link list, quota and expiry',
    u_total: 'Total Users', u_active: 'Active', u_expired: 'Expired', u_traffic: 'Total Usage',
    th_name: 'Name', th_account: 'Account', th_status: 'Status', th_usage: 'Data Usage',
    th_duration: 'Duration', th_actions: 'Actions',
    add_user_btn: 'Add New User', no_users: 'No users found',
    inbound_title: 'Inbound', inbound_sub: 'Inbound Settings',
    inb_port: 'Port', inb_protocol: 'Protocol', inb_host: 'Host', inb_status: 'Status',
    conn_title: 'Connections', conn_active: 'Active', no_conn: 'No active connections',
    settings_title: 'Settings', settings_sub: 'Panel Settings',
    set_theme: 'Theme', set_dark: 'Cosmic', set_light: 'Light',
    set_current_theme: 'Current Theme', set_lang: 'Language', set_current_lang: 'Current Language',
    set_rgb: 'RGB Mode',
    backup_title: 'Backup', backup_sub: 'Save & Restore',
    backup_download: 'Backup', backup_download_btn: 'Download', backup_restore_btn: 'Restore',
    logs_title: 'Logs',
    modal_user_title: 'Create New User',
    f_label_name: 'Username', f_label_quota: 'Quota (GB)',
    f_label_expiry: 'Expiry', f_label_devices: 'Devices',
    f_label_fingerprint: 'Fingerprint', f_label_protocol: 'Protocol',
    f_label_http: 'HTTP Version', f_label_password: 'Password (Optional)',
    btn_create_user: 'Create User', btn_cancel: 'Cancel',
    modal_edit_title: 'Edit User',
    e_label_name: 'Name', e_label_password: 'New Password',
    e_label_quota: 'Quota (GB)', e_label_expiry: 'Expiry',
    e_label_devices: 'Devices', e_label_status: 'Status',
    e_label_fingerprint: 'Fingerprint', e_label_protocol: 'Protocol',
    e_label_http: 'HTTP Version',
    btn_save: 'Save',
    modal_delete_title: 'Delete User', delete_desc: 'Enter the config password to delete.',
    d_label_password: 'Password', btn_delete: 'Delete',
    qr_title: 'QR Code', qr_desc: 'Scan to add subscription',
    qr_download: 'Download QR'
  }
};

let currentLang = localStorage.getItem('persepolis-lang') || 'fa';
let currentTheme = localStorage.getItem('persepolis-theme') || 'dark';
let trafficChart = null;
let chartPeriod = '7d';
let qrCodeInstance = null;
let expiryPicker = null;
let editExpiryPicker = null;

// ===== تولید یوزرنیم رندوم =====
function generateRandomUsername() {
    const prefixes = ['Cyber', 'Tech', 'Shadow', 'Neon', 'Nova', 'Apex', 'Zen', 'Vex', 'Zion', 'Knight', 'Phoenix', 'Falcon', 'Titan', 'Ghost', 'Raven', 'Wolf', 'Eagle', 'Hawk', 'Storm', 'Blaze', 'Quantum', 'Echo', 'Omega', 'Alpha', 'Delta', 'Sigma', 'Cipher', 'Dragon', 'Tiger', 'Viper'];
    const suffixes = ['X', 'Z', 'Y', 'V', 'W', 'K', 'G', 'P', 'R', 'M', 'H', 'T', 'N', 'S', 'D', 'F', 'Q', 'L', 'J', 'C'];
    const middle = ['flow', 'star', 'dark', 'light', 'storm', 'fire', 'ice', 'wind', 'cloud', 'shadow', 'nova', 'neon', 'cyber', 'ghost', 'raven', 'wolf', 'titan', 'zen', 'vex', 'apex', 'surge', 'pulse', 'cipher'];
    
    let username = '';
    const useMiddle = Math.random() > 0.4;
    
    if (useMiddle) {
        username = prefixes[Math.floor(Math.random() * prefixes.length)] + 
                    middle[Math.floor(Math.random() * middle.length)] +
                    Math.floor(Math.random() * 100);
    } else {
        username = prefixes[Math.floor(Math.random() * prefixes.length)] + 
                    suffixes[Math.floor(Math.random() * suffixes.length)] +
                    Math.floor(Math.random() * 1000);
    }
    
    document.getElementById('user-label').value = username;
    toast('✅ ' + (currentLang === 'fa' ? 'نام کاربری ساخته شد' : 'Username generated'), 'ok');
}

// ===== توابع =====
function t(key) { return translations[currentLang]?.[key] || key; }

function setTheme(theme) {
  currentTheme = theme;
  localStorage.setItem('persepolis-theme', theme);
  if (theme === 'light') {
    document.body.classList.add('light-theme');
    document.getElementById('current-theme-label').textContent = currentLang === 'fa' ? 'روشن' : 'Light';
    document.getElementById('theme-dark-btn').className = 'btn btn-o';
    document.getElementById('theme-dark-btn').style.cssText = 'flex:1;font-size:12px;padding:8px 14px;background:var(--bg-card);border:1px solid var(--border-subtle);color:var(--t2);';
    document.getElementById('theme-light-btn').className = 'btn btn-pur';
    document.getElementById('theme-light-btn').style.cssText = 'flex:1;font-size:12px;padding:8px 14px;background:rgba(0,150,255,0.1);border:1px solid var(--border-strong);color:#0099cc;';
  } else {
    document.body.classList.remove('light-theme');
    document.getElementById('current-theme-label').textContent = currentLang === 'fa' ? 'کیهانی' : 'Cosmic';
    document.getElementById('theme-dark-btn').className = 'btn btn-pur';
    document.getElementById('theme-dark-btn').style.cssText = 'flex:1;font-size:12px;padding:8px 14px;background:rgba(0,240,255,0.08);border:1px solid var(--border-strong);color:var(--cyan);';
    document.getElementById('theme-light-btn').className = 'btn btn-o';
    document.getElementById('theme-light-btn').style.cssText = 'flex:1;font-size:12px;padding:8px 14px;background:var(--bg-card);border:1px solid var(--border-subtle);color:var(--t2);';
  }
  fetch('/api/settings/theme', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ theme: theme })
  }).catch(() => {});
}

async function loadThemeFromServer() {
  try {
    const r = await fetch('/api/settings');
    const data = await r.json();
    if (data.theme) {
      currentTheme = data.theme;
      localStorage.setItem('persepolis-theme', data.theme);
      setTheme(data.theme);
    } else {
      setTheme(currentTheme);
    }
  } catch(e) { setTheme(currentTheme); }
}

function setLang(lang) {
  currentLang = lang;
  localStorage.setItem('persepolis-lang', lang);
  document.getElementById('lang-fa-btn').className = 'btn ' + (lang === 'fa' ? 'btn-pur' : 'btn-o');
  document.getElementById('lang-en-btn').className = 'btn ' + (lang === 'en' ? 'btn-pur' : 'btn-o');
  document.getElementById('current-lang-label').textContent = lang === 'fa' ? 'فارسی' : 'English';
  updateUITexts();
  fetch('/api/settings/language', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ language: lang })
  }).catch(() => {});
  
  if (expiryPicker) expiryPicker.set('locale', lang === 'fa' ? 'fa' : 'en');
  if (editExpiryPicker) editExpiryPicker.set('locale', lang === 'fa' ? 'fa' : 'en');
}

function updateUITexts() {
  const t = translations[currentLang];
  if (!t) return;
  
  document.getElementById('nav-home').textContent = t.nav_home;
  document.getElementById('nav-users').textContent = t.nav_users;
  document.getElementById('nav-inbound').textContent = t.nav_inbound;
  document.getElementById('nav-connections').textContent = t.nav_connections;
  document.getElementById('nav-settings').textContent = t.nav_settings;
  document.getElementById('nav-logs').textContent = t.nav_logs;
  document.getElementById('nav-backup').textContent = t.nav_backup;
  document.getElementById('nav-logout').textContent = t.nav_logout;
  document.getElementById('nav-quota').textContent = t.nav_quota;
  
  document.getElementById('b-home').textContent = t.nav_home;
  document.getElementById('b-users').textContent = t.nav_users;
  document.getElementById('b-quota').textContent = t.b_quota;
  document.getElementById('b-inbound').textContent = t.nav_inbound;
  document.getElementById('b-settings').textContent = t.nav_settings;
  
  document.getElementById('quota-title').textContent = t.quota_title;
  document.getElementById('quota-sub').textContent = t.quota_sub;
  document.getElementById('quota-overview-title').textContent = t.quota_overview_title;
  document.getElementById('q-used-label').textContent = t.q_used_label;
  document.getElementById('q-limit-label').textContent = t.q_limit_label;
  document.getElementById('q-remaining-label').textContent = t.q_remaining_label;
  document.getElementById('q-progress-label').textContent = t.q_progress_label;
  document.getElementById('q-alert-title').textContent = t.q_alert_title;
  document.getElementById('q-alert-desc').textContent = t.q_alert_desc;
  document.getElementById('q-users-title').textContent = t.q_users_title;
  document.getElementById('q-users-sub').textContent = t.q_users_sub;
  document.getElementById('q-cumulative-title').textContent = t.q_cumulative_title;
  document.getElementById('q-cumulative-sub').textContent = t.q_cumulative_sub;
  
  // WTF Factor translations
  document.getElementById('gauge-title').textContent = t.gauge_title;
  document.getElementById('gauge-label').textContent = t.gauge_label;
  document.getElementById('map-title').textContent = t.map_title;
  document.getElementById('donut-title-text').textContent = t.donut_title;
  document.getElementById('donut-lbl').textContent = t.donut_label;
  document.getElementById('activity-title').textContent = t.activity_title;
  document.getElementById('cmdk-input') && (document.getElementById('cmdkInput').placeholder = t.cmdk_placeholder);
  const searchInput = document.getElementById('userSearch');
  if (searchInput) searchInput.placeholder = t.search_placeholder;
  
  document.getElementById('dash-title').textContent = t.dash_title;
  document.getElementById('dash-add-user').textContent = t.dash_add_user;
  document.getElementById('s-traffic').textContent = t.s_traffic;
  document.getElementById('s-requests').textContent = t.s_requests;
  document.getElementById('s-uptime').textContent = t.s_uptime;
  document.getElementById('s-disk').textContent = t.s_disk;
  document.getElementById('s-speed').textContent = t.s_speed;
  document.getElementById('s-users').textContent = t.s_users;
  document.getElementById('s-count').textContent = t.s_count;
  document.getElementById('s-time').textContent = t.s_time;
  document.getElementById('s-live').textContent = t.s_live;
  document.getElementById('chart-title-text').textContent = t.chart_title;
  document.getElementById('chart-sub-text').textContent = t.chart_sub;
  document.getElementById('recent-users-title').textContent = t.recent_users;
  
  document.getElementById('users-title').textContent = t.users_title;
  document.getElementById('users-sub').textContent = t.users_sub;
  document.getElementById('u-total').textContent = t.u_total;
  document.getElementById('u-active').textContent = t.u_active;
  document.getElementById('u-expired').textContent = t.u_expired;
  document.getElementById('u-traffic').textContent = t.u_traffic;
  document.getElementById('th-name').textContent = t.th_name;
  document.getElementById('th-account').textContent = t.th_account;
  document.getElementById('th-status').textContent = t.th_status;
  document.getElementById('th-usage').textContent = t.th_usage;
  document.getElementById('th-duration').textContent = t.th_duration;
  document.getElementById('th-actions').textContent = t.th_actions;
  document.getElementById('add-user-btn').textContent = t.add_user_btn;
  document.getElementById('no-users').textContent = t.no_users;
  
  document.getElementById('inbound-title').textContent = t.inbound_title;
  document.getElementById('inbound-sub').textContent = t.inbound_sub;
  document.getElementById('inb-port-label').textContent = t.inb_port;
  document.getElementById('inb-protocol-label').textContent = t.inb_protocol;
  document.getElementById('inb-host-label').textContent = t.inb_host;
  document.getElementById('inb-status-label').textContent = t.inb_status;
  document.getElementById('inb-status-title').textContent = t.inb_status;
  
  document.getElementById('conn-title').textContent = t.conn_title;
  document.getElementById('conn-active-label').textContent = t.conn_active;
  document.getElementById('no-conn').textContent = t.no_conn;
  
  document.getElementById('settings-title').textContent = t.settings_title;
  document.getElementById('settings-sub').textContent = t.settings_sub;
  document.getElementById('set-theme-title').textContent = t.set_theme;
  document.getElementById('set-dark').textContent = t.set_dark;
  document.getElementById('set-light').textContent = t.set_light;
  document.getElementById('set-current-theme').textContent = t.set_current_theme;
  document.getElementById('set-lang-title').textContent = t.set_lang;
  document.getElementById('set-current-lang').textContent = t.set_current_lang;
  document.getElementById('set-rgb-title').textContent = t.set_rgb;
  
  document.getElementById('backup-title').textContent = t.backup_title;
  document.getElementById('backup-sub').textContent = t.backup_sub;
  document.getElementById('backup-download-title').textContent = t.backup_download;
  document.getElementById('backup-download-btn').textContent = t.backup_download_btn;
  document.getElementById('backup-restore-btn').textContent = t.backup_restore_btn;
  
  document.getElementById('logs-title').textContent = t.logs_title;
  
  document.getElementById('modal-user-title').textContent = t.modal_user_title;
  document.getElementById('f-label-name').textContent = t.f_label_name;
  document.getElementById('f-label-quota').textContent = t.f_label_quota;
  document.getElementById('f-label-expiry').textContent = t.f_label_expiry;
  document.getElementById('f-label-devices').textContent = t.f_label_devices;
  document.getElementById('f-label-fingerprint').textContent = t.f_label_fingerprint;
  document.getElementById('f-label-protocol').textContent = t.f_label_protocol;
  document.getElementById('f-label-http').textContent = t.f_label_http;
  document.getElementById('f-label-password').textContent = t.f_label_password;
  document.getElementById('btn-create-user').textContent = t.btn_create_user;
  document.getElementById('btn-cancel').textContent = t.btn_cancel;
  
  document.getElementById('modal-edit-title').textContent = t.modal_edit_title;
  document.getElementById('e-label-name').textContent = t.e_label_name;
  document.getElementById('e-label-password').textContent = t.e_label_password;
  document.getElementById('e-label-quota').textContent = t.e_label_quota;
  document.getElementById('e-label-expiry').textContent = t.e_label_expiry;
  document.getElementById('e-label-devices').textContent = t.e_label_devices;
  document.getElementById('e-label-status').textContent = t.e_label_status;
  document.getElementById('e-label-fingerprint').textContent = t.e_label_fingerprint;
  document.getElementById('e-label-protocol').textContent = t.e_label_protocol;
  document.getElementById('e-label-http').textContent = t.e_label_http;
  document.getElementById('btn-save').textContent = t.btn_save;
  document.getElementById('btn-cancel2').textContent = t.btn_cancel;
  
  document.getElementById('modal-delete-title').textContent = t.modal_delete_title;
  document.getElementById('delete-desc').textContent = t.delete_desc;
  document.getElementById('d-label-password').textContent = t.d_label_password;
  document.getElementById('btn-delete').textContent = t.btn_delete;
  document.getElementById('btn-cancel3').textContent = t.btn_cancel;
  
  document.getElementById('qr-title').textContent = t.qr_title;
  document.getElementById('qr-desc').textContent = t.qr_desc;
  document.getElementById('qr-download').textContent = t.qr_download;
  
  document.getElementById('current-theme-label').textContent = currentTheme === 'light' ? (currentLang === 'fa' ? 'روشن' : 'Light') : (currentLang === 'fa' ? 'کیهانی' : 'Cosmic');
  document.getElementById('current-lang-label').textContent = currentLang === 'fa' ? 'فارسی' : 'English';
}

// ===== توابع عمومی =====
function toast(msg, type = '') {
  const tEl = document.getElementById('toast');
  tEl.textContent = msg;
  tEl.className = 'toast show' + (type ? ' ' + type : '');
  clearTimeout(tEl._timeout);
  tEl._timeout = setTimeout(() => tEl.classList.remove('show'), 2500);
}

function fmtB(b) {
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(1) + ' MB';
  if (b < 1024**4) return (b/1024**3).toFixed(2) + ' GB';
  return (b/1024**4).toFixed(2) + ' TB';
}

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function openModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }

// ===== احراز هویت =====
async function authF(url, opts = {}) {
  const r = await fetch(url, opts);
  if (r.status === 401) { location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}

async function logout() {
  try { await fetch('/api/logout', { method: 'POST' }); } catch(e) {}
  location.href = '/login';
}

// ===== ناوبری =====
function navTo(name) {
  document.querySelectorAll('.nav-it').forEach(n => n.classList.toggle('on', n.dataset.pg === name));
  document.querySelectorAll('.pg').forEach(p => p.classList.toggle('on', p.id === 'pg-' + name));
  document.querySelectorAll('.bottom-nav .nav-item').forEach(n => n.classList.toggle('active', n.dataset.pg === name));
  closeSb();
  const loaders = {
    dashboard: loadDashboard,
    users: loadUsers,
    quota: loadQuota,
    inbound: loadInbound,
    connections: loadConnections,
    logs: loadLogs,
    settings: () => {}
  };
  if (loaders[name]) loaders[name]();
}

document.querySelectorAll('.nav-it, .bottom-nav .nav-item').forEach(el => {
  el.addEventListener('click', () => navTo(el.dataset.pg));
});

const sb = document.getElementById('sb'), overlay = document.getElementById('overlay');
function openSb() { sb.classList.add('open'); overlay.classList.add('show'); }
function closeSb() { sb.classList.remove('open'); overlay.classList.remove('show'); }
document.getElementById('open-sb').addEventListener('click', openSb);
overlay.addEventListener('click', closeSb);

// ===== نمودار مصرف =====
async function loadChart(period) {
  chartPeriod = period || '7d';
  document.querySelectorAll('#chart-7d, #chart-30d, #chart-90d').forEach(btn => {
    btn.className = 'btn btn-sm btn-o';
  });
  const btnMap = {'7d':'chart-7d','30d':'chart-30d','90d':'chart-90d'};
  if (btnMap[period]) {
    document.getElementById(btnMap[period]).className = 'btn btn-sm btn-pur';
  }
  
  let days = 7;
  if (period === '30d') days = 30;
  if (period === '90d') days = 90;
  
  try {
    // تلاش برای گرفتن داده‌های آماری
    let dailyData = {};
    let totalUsedBytes = 0;
    
    try {
      const r = await authF('/api/stats');
      const data = await r.json();
      const hourly = data.hourly || {};
      
      for (const [key, bytes] of Object.entries(hourly)) {
        // key می‌تونه YYYY-MM-DD:HH یا YYYY-MM-DD باشه
        const dayKey = key.split(':')[0] || key;
        if (!dailyData[dayKey]) dailyData[dayKey] = 0;
        dailyData[dayKey] += bytes || 0;
        totalUsedBytes += bytes || 0;
      }
    } catch(e) { console.warn('stats API unavailable, using fallback', e); }
    
    // اگر داده‌ای نداشتیم، از /api/links برای ساخت داده روزانه استفاده می‌کنیم
    if (Object.keys(dailyData).length === 0) {
      try {
        const r2 = await authF('/api/links');
        const usersData = await r2.json();
        const links = usersData.links || [];
        const today = new Date();
        const startDate = new Date();
        startDate.setDate(startDate.getDate() - days + 1);
        
        links.forEach(l => {
          if (l.created_at) {
            try {
              const cDate = new Date(l.created_at);
              if (cDate >= startDate) {
                const dayKey = cDate.toISOString().split('T')[0];
                if (!dailyData[dayKey]) dailyData[dayKey] = 0;
                const dailyAvg = (l.used_bytes || 0) / Math.max(1, days);
                dailyData[dayKey] += dailyAvg;
              }
            } catch(e) {}
          }
          totalUsedBytes += l.used_bytes || 0;
        });
      } catch(e) { console.warn('links API fallback failed', e); }
    }
    
    // اگر باز هم خالی بود، داده‌های ثابت نمایش بدیم
    if (Object.keys(dailyData).length === 0) {
      // داده‌های نمونه برای نمایش نمودار خالی
      for (let i = 0; i < days; i++) {
        const d = new Date();
        d.setDate(d.getDate() - (days - 1 - i));
        dailyData[d.toISOString().split('T')[0]] = 0;
      }
    }
    
    // ساخت آرایه نهایی برای روزهای اخیر
    const labels = [];
    const values = [];
    const startDate = new Date();
    startDate.setDate(startDate.getDate() - days + 1);
    startDate.setHours(0, 0, 0, 0);
    
    for (let i = 0; i < days; i++) {
      const d = new Date(startDate);
      d.setDate(d.getDate() + i);
      const key = d.toISOString().split('T')[0];
      labels.push(key);
      values.push(dailyData[key] || 0);
    }
    
    const mbValues = values.map(v => Number((v / (1024 * 1024)).toFixed(2)));
    
    const labelsFa = labels.map(d => {
      const date = new Date(d);
      return date.toLocaleDateString(currentLang === 'fa' ? 'fa-IR' : 'en-US', { weekday: 'short', day: 'numeric' });
    });
    
    if (trafficChart) { trafficChart.destroy(); }
    
    const ctx = document.getElementById('trafficChart').getContext('2d');
    const gradient = ctx.createLinearGradient(0, 0, 0, 200);
    gradient.addColorStop(0, 'rgba(0, 240, 255, 0.4)');
    gradient.addColorStop(0.5, 'rgba(123, 47, 247, 0.2)');
    gradient.addColorStop(1, 'rgba(0, 240, 255, 0.02)');
    
    const lineGradient = ctx.createLinearGradient(0, 0, ctx.canvas.width, 0);
    lineGradient.addColorStop(0, '#00f0ff');
    lineGradient.addColorStop(0.5, '#7b2ff7');
    lineGradient.addColorStop(1, '#ff2e9a');
    
    trafficChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labelsFa,
        datasets: [{
          label: currentLang === 'fa' ? 'مصرف (MB)' : 'Usage (MB)',
          data: mbValues,
          borderColor: lineGradient,
          backgroundColor: gradient,
          borderWidth: 2.5,
          fill: true,
          tension: 0.4,
          pointBackgroundColor: '#00f0ff',
          pointBorderColor: '#0a0e2a',
          pointBorderWidth: 2,
          pointRadius: 3,
          pointHoverRadius: 6,
          pointHoverBackgroundColor: '#ff2e9a',
          pointHoverBorderColor: '#fff'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: 'rgba(10, 14, 35, 0.95)',
            borderColor: '#00f0ff',
            borderWidth: 1,
            titleColor: '#00f0ff',
            bodyColor: '#e8efff',
            padding: 10,
            cornerRadius: 8,
            displayColors: false,
            callbacks: {
              label: function(context) { return context.parsed.y + ' MB'; }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: { color: '#64748b', font: { size: 9 }, callback: function(value) { return value + ' MB'; } },
            grid: { color: 'rgba(0, 240, 255, 0.05)' }
          },
          x: {
            ticks: { color: '#64748b', font: { size: 9 } },
            grid: { display: false }
          }
        },
        interaction: { intersect: false, mode: 'index' }
      }
    });
  } catch(e) { console.error('loadChart error', e); }
}

// ===== بارگذاری داشبورد =====
async function loadDashboard() {
  try {
    const r = await authF('/api/dashboard/stats');
    const data = await r.json();
    document.getElementById('stat-traffic').textContent = (data.traffic.total / (1024 * 1024)).toFixed(1);
    document.getElementById('stat-requests').textContent = data.requests || 0;
    document.getElementById('stat-uptime').textContent = data.uptime || '00:00:00';
    document.getElementById('stat-disk').textContent = data.disk.total_fmt || '0 GB';
    document.getElementById('stat-disk-used').textContent = (currentLang === 'fa' ? 'استفاده: ' : 'Used: ') + (data.disk.used_fmt || '0');
    document.getElementById('stat-speed').textContent = data.speed.download_fmt || '0 B/s';
    document.getElementById('stat-users').textContent = data.links_count || 0;
    document.getElementById('stat-users-active').textContent = (data.active_links || 0) + (currentLang === 'fa' ? ' فعال' : ' active');
    document.getElementById('online-badge').innerHTML = '<span class="dot dg"></span> ' + (data.connections || 0) + (currentLang === 'fa' ? ' آنلاین' : ' online');
    document.getElementById('last-update').textContent = (currentLang === 'fa' ? 'بروزرسانی: ' : 'Updated: ') + new Date().toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US');
    
    const usersR = await authF('/api/links');
    const usersData = await usersR.json();
    const links = usersData.links || [];
    const recent = links.slice(0, 4);
    const grid = document.getElementById('recent-users');
    if (!recent.length) {
      grid.innerHTML = '<div class="empty" style="padding:14px"><i class="ti ti-users"></i><p style="font-size:10px">' + (currentLang === 'fa' ? 'هیچ کاربری وجود ندارد' : 'No users') + '</p></div>';
    } else {
      grid.innerHTML = recent.map(l => `<div style="background:rgba(0,240,255,0.04);border:1px solid var(--border-subtle);border-radius:10px;padding:8px 10px;display:flex;justify-content:space-between;align-items:center;transition:all .3s"><div><div style="font-size:10px;font-weight:700;color:var(--t1)">${esc(l.label)}</div><div style="font-size:8px;color:var(--t3);margin-top:2px">${l.active ? '🟢' : '🔴'} ${l.uuid.slice(0,8)}…</div></div><div style="font-size:9px;color:var(--cyan);font-family:monospace;font-weight:700">${fmtB(l.used_bytes||0)}</div></div>`).join('');
    }
    
    loadChart(chartPeriod);
  } catch(e) { console.error(e); }
}

// ===== بارگذاری مصرف مجاز (سهمیه کل سرور) =====
let quotaChart = null;
const SERVER_QUOTA_LIMIT_GB = 100;  // سقف مجاز پیش‌فرض ۱۰۰ گیگابایت

async function loadQuota() {
  try {
    // گرفتن دیتای کل سرور
    let totalUsedBytes = 0;
    let linksList = [];
    
    try {
      const r = await authF('/api/links');
      const data = await r.json();
      linksList = data.links || [];
      linksList.forEach(l => { totalUsedBytes += (l.used_bytes || 0); });
    } catch(e) { console.warn('links API failed for quota', e); }
    
    // گرفتن ترافیک کل از داشبورد (اگه قابل دسترسی بود)
    try {
      const r2 = await authF('/api/dashboard/stats');
      const data2 = await r2.json();
      if (data2.traffic && data2.traffic.total) {
        // اگه دیتای ترافیک کل بود، از حداکثر اون و مجموع لینک‌ها استفاده می‌کنیم
        totalUsedBytes = Math.max(totalUsedBytes, data2.traffic.total);
      }
    } catch(e) {}
    
    const limitBytes = SERVER_QUOTA_LIMIT_GB * 1024 * 1024 * 1024;
    const usedBytes = totalUsedBytes;
    const remainingBytes = Math.max(0, limitBytes - usedBytes);
    const percent = Math.min(100, (usedBytes / limitBytes) * 100);
    const usedGB = usedBytes / (1024 * 1024 * 1024);
    const remainingGB = remainingBytes / (1024 * 1024 * 1024);
    const isExhausted = usedBytes >= limitBytes;
    const isWarning = percent >= 80 && !isExhausted;
    
    // آپدیت اعداد
    document.getElementById('q-used-value').textContent = usedGB.toFixed(2) + ' GB';
    document.getElementById('q-limit-value').textContent = SERVER_QUOTA_LIMIT_GB + ' GB';
    document.getElementById('q-remaining-value').textContent = remainingGB.toFixed(2) + ' GB';
    document.getElementById('q-percent').textContent = percent.toFixed(1) + '%';
    document.getElementById('q-mid-label').textContent = (SERVER_QUOTA_LIMIT_GB / 2) + ' GB';
    document.getElementById('q-end-label').textContent = SERVER_QUOTA_LIMIT_GB + ' GB';
    
    // آپدیت نوار پیشرفت
    const fill = document.getElementById('q-progress-fill');
    fill.style.width = percent + '%';
    
    // اگه به سقف رسید، رنگ قرمز و نمایش هشدار
    const barBg = document.getElementById('q-progress-bar-bg');
    const percentEl = document.getElementById('q-percent');
    const alertBox = document.getElementById('q-alert');
    const remainingEl = document.getElementById('q-remaining-value');
    
    if (isExhausted) {
      fill.style.background = 'linear-gradient(90deg,#ff4d6d,#ff2e9a,#ff4d6d)';
      fill.style.boxShadow = '0 0 25px rgba(255,77,109,0.6)';
      barBg.style.borderColor = 'rgba(255,77,109,0.5)';
      barBg.style.background = 'rgba(255,77,109,0.08)';
      percentEl.style.color = 'var(--red-t)';
      percentEl.textContent = (currentLang === 'fa' ? 'تمام شد! ' : 'Exhausted! ') + percent.toFixed(1) + '%';
      remainingEl.style.color = 'var(--red-t)';
      remainingEl.textContent = '0 GB';
      alertBox.style.display = 'flex';
    } else if (isWarning) {
      fill.style.background = 'linear-gradient(90deg,#ffb800,#ff8800,#ff2e9a)';
      fill.style.boxShadow = '0 0 20px rgba(255,184,0,0.5)';
      barBg.style.borderColor = 'rgba(255,184,0,0.4)';
      barBg.style.background = 'rgba(255,184,0,0.06)';
      percentEl.style.color = 'var(--amber-t)';
      remainingEl.style.color = 'var(--amber-t)';
      alertBox.style.display = 'none';
    } else {
      fill.style.background = 'linear-gradient(90deg,#00f0ff,#7b2ff7,#ff2e9a)';
      fill.style.boxShadow = '0 0 15px rgba(0,240,255,0.5)';
      barBg.style.borderColor = 'var(--border-subtle)';
      barBg.style.background = 'rgba(0,240,255,0.06)';
      percentEl.style.color = 'var(--cyan)';
      remainingEl.style.color = 'var(--green-t)';
      alertBox.style.display = 'none';
    }
    
    // نمایش توزیع مصرف بین کاربران (برترین‌ها)
    const usersList = document.getElementById('q-users-list');
    if (!linksList.length) {
      usersList.innerHTML = '<div class="empty"><i class="ti ti-users"></i><p style="font-size:10px">' + (currentLang === 'fa' ? 'هیچ کاربری وجود ندارد' : 'No users') + '</p></div>';
    } else {
      // مرتب‌سازی بر اساس مصرف و انتخاب ۵ کاربر برتر
      const top = linksList.slice().sort((a, b) => (b.used_bytes||0) - (a.used_bytes||0)).slice(0, 5);
      usersList.innerHTML = top.map((l, idx) => {
        const used = l.used_bytes || 0;
        const limit = l.limit_bytes || 0;
        const pct = limit > 0 ? Math.min(100, (used / limit) * 100) : 0;
        const usedFmt = fmtB(used);
        const limitFmt = limit === 0 ? '∞' : fmtB(limit);
        const avatarLetter = (l.label || 'U')[0].toUpperCase();
        const isOver = limit > 0 && used >= limit;
        const barColor = isOver ? 'linear-gradient(90deg,#ff4d6d,#ff2e9a)' : 
                         pct >= 80 ? 'linear-gradient(90deg,#ffb800,#ff8800)' :
                         'linear-gradient(90deg,#00f0ff,#7b2ff7)';
        return `<div style="background:rgba(0,240,255,0.03);border:1px solid var(--border-subtle);border-radius:10px;padding:10px 12px">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px">
            <div style="width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--cyan),var(--purple));display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;color:#000;flex-shrink:0">${avatarLetter}</div>
            <div style="flex:1;min-width:0">
              <div style="font-size:11px;font-weight:700;color:var(--t1);overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(l.label)}</div>
              <div style="font-size:8px;color:var(--t3);font-family:monospace;margin-top:2px">${l.uuid.slice(0,8)}…</div>
            </div>
            <div style="text-align:left;flex-shrink:0">
              <div style="font-size:11px;font-weight:800;color:${isOver?'var(--red-t)':(pct>=80?'var(--amber-t)':'var(--cyan)')};font-family:monospace">${usedFmt} / ${limitFmt}</div>
              <div style="font-size:8px;color:var(--t3);margin-top:1px">${pct.toFixed(1)}% ${isOver?(currentLang==='fa'?'تمام شد':'exhausted'):''}</div>
            </div>
          </div>
          <div style="height:5px;border-radius:3px;background:rgba(0,240,255,0.05);overflow:hidden">
            <div style="height:100%;border-radius:3px;background:${barColor};width:${pct}%;transition:width .8s ease;box-shadow:0 0 6px rgba(0,240,255,0.3)"></div>
          </div>
        </div>`;
      }).join('');
    }
    
    // ساخت نمودار مصرف تجمعی
    drawQuotaChart(usedGB, SERVER_QUOTA_LIMIT_GB, isExhausted, isWarning);
    
  } catch(e) { console.error('loadQuota error', e); }
}

function drawQuotaChart(usedGB, limitGB, isExhausted, isWarning) {
  try {
    if (quotaChart) { quotaChart.destroy(); }
    
    const ctx = document.getElementById('quotaChart').getContext('2d');
    
    // ساخت داده‌های تجمعی برای ۱۴ روز اخیر (با فرض توزیع یکنواخت)
    const days = 14;
    const labels = [];
    const cumulativeData = [];
    const dailyAvg = usedGB / days;
    
    for (let i = 0; i < days; i++) {
      const d = new Date();
      d.setDate(d.getDate() - (days - 1 - i));
      labels.push(d.toLocaleDateString(currentLang === 'fa' ? 'fa-IR' : 'en-US', { weekday: 'short', day: 'numeric' }));
      cumulativeData.push(Number((dailyAvg * (i + 1)).toFixed(2)));
    }
    
    const lineColor = isExhausted ? '#ff4d6d' : isWarning ? '#ffb800' : '#00f0ff';
    const fillColor = isExhausted ? 'rgba(255,77,109,0.3)' : isWarning ? 'rgba(255,184,0,0.2)' : 'rgba(0,240,255,0.2)';
    
    const gradient = ctx.createLinearGradient(0, 0, 0, 200);
    gradient.addColorStop(0, fillColor);
    gradient.addColorStop(1, 'rgba(0,0,0,0.02)');
    
    quotaChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: currentLang === 'fa' ? 'مصرف تجمعی (GB)' : 'Cumulative (GB)',
            data: cumulativeData,
            borderColor: lineColor,
            backgroundColor: gradient,
            borderWidth: 2.5,
            fill: true,
            tension: 0.4,
            pointBackgroundColor: lineColor,
            pointBorderColor: '#0a0e2a',
            pointBorderWidth: 2,
            pointRadius: 3,
            pointHoverRadius: 6
          },
          {
            label: currentLang === 'fa' ? 'سقف مجاز' : 'Allowed Limit',
            data: labels.map(() => limitGB),
            borderColor: isExhausted ? '#ff4d6d' : '#ff2e9a',
            borderWidth: 2,
            borderDash: [6, 4],
            fill: false,
            pointRadius: 0,
            tension: 0
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
            position: 'top',
            labels: { color: '#94a3b8', font: { size: 10 }, boxWidth: 12, padding: 8 }
          },
          tooltip: {
            backgroundColor: 'rgba(10, 14, 35, 0.95)',
            borderColor: lineColor,
            borderWidth: 1,
            titleColor: lineColor,
            bodyColor: '#e8efff',
            padding: 10,
            cornerRadius: 8,
            callbacks: {
              label: function(context) { return context.dataset.label + ': ' + context.parsed.y + ' GB'; }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            suggestedMax: limitGB,
            ticks: { color: '#64748b', font: { size: 9 }, callback: function(value) { return value + ' GB'; } },
            grid: { color: 'rgba(0, 240, 255, 0.05)' }
          },
          x: {
            ticks: { color: '#64748b', font: { size: 9 } },
            grid: { display: false }
          }
        },
        interaction: { intersect: false, mode: 'index' }
      }
    });
  } catch(e) { console.error('drawQuotaChart error', e); }
}

// ===== بارگذاری اینباند =====
async function loadInbound() {
  try {
    const r = await authF('/api/inbound');
    const data = await r.json();
    document.getElementById('inbound-port').textContent = data.port || 443;
    document.getElementById('inbound-protocol').textContent = (data.protocol || 'vless-ws').toUpperCase();
    document.getElementById('inbound-host').textContent = data.host || '—';
  } catch(e) { console.error(e); }
}

// ===== بارگذاری کاربران =====
async function loadUsers() {
  try {
    const r = await authF('/api/links');
    const { links = [] } = await r.json();
    const tbody = document.getElementById('users-tbody');
    const total = links.length;
    const active = links.filter(l => l.active && !l.expired).length;
    const expired = links.filter(l => l.expired).length;
    const totalTraffic = links.reduce((sum, l) => sum + (l.used_bytes || 0), 0);
    
    document.getElementById('users-total').textContent = total;
    document.getElementById('users-active').textContent = active;
    document.getElementById('users-expired').textContent = expired;
    document.getElementById('users-traffic').textContent = fmtB(totalTraffic);
    document.getElementById('users-count-label').textContent = total + (currentLang === 'fa' ? ' کاربر' : ' users');
    
    if (!links.length) {
      tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;padding:30px;color:var(--t3);">' + (currentLang === 'fa' ? 'هیچ کاربری وجود ندارد' : 'No users found') + '</td></tr>';
      return;
    }
    
    const fpEmoji = { chrome: '🌐', firefox: '🦊', safari: '🧭', edge: '🌊', ios: '📱', android: '🤖', safari_ios: '🍏', random: '🎲', none: '🚫' };
    const protocolIcons = { 'vless-ws':'🚀', 'vless-grpc':'⚡', 'vless-xhttp':'🛡️', 'vless-http2':'📶', 'trojan-ws':'🔒', 'shadowsocks':'🌊' };
    
    tbody.innerHTML = links.map(l => {
      const isActive = l.active && !l.expired;
      const statusClass = isActive ? 'active' : (l.expired ? 'expired' : 'disabled');
      const statusText = isActive ? (currentLang === 'fa' ? 'فعال' : 'Active') : (l.expired ? (currentLang === 'fa' ? 'منقضی' : 'Expired') : (currentLang === 'fa' ? 'غیرفعال' : 'Disabled'));
      const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
      const usedFmt = fmtB(l.used_bytes || 0);
      const limitFmt = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
      const fp = l.fingerprint || 'chrome';
      const fpName = { chrome: 'Chrome', firefox: 'Firefox', safari: 'Safari', edge: 'Edge', ios: 'iOS', android: 'Android', safari_ios: 'Safari iOS', random: 'Random', none: 'None' }[fp] || fp;
      const protocol = l.protocol || 'vless-ws';
      const protoIcon = protocolIcons[protocol] || '🚀';
      const protoName = { 'vless-ws':'VLESS-WS', 'vless-grpc':'VLESS-gRPC', 'vless-xhttp':'VLESS-XHTTP', 'vless-http2':'VLESS-HTTP/2', 'trojan-ws':'Trojan-WS', 'shadowsocks':'Shadowsocks' }[protocol] || protocol;
      const httpVer = l.http_version || 'h2';
      const httpName = { 'h1':'HTTP/1.1', 'h2':'HTTP/2', 'h3':'HTTP/3', 'auto':'Auto' }[httpVer] || httpVer;
      let duration = '∞';
      if (l.expires_at) {
        try {
          const exp = new Date(l.expires_at);
          const now = new Date();
          const days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
          duration = days > 0 ? days + (currentLang === 'fa' ? ' روز' : ' days') : (currentLang === 'fa' ? 'منقضی' : 'Expired');
        } catch(e) { duration = '—'; }
      }
      const avatarLetter = (l.label || 'U')[0].toUpperCase();
      return `<tr><td><div class="user-name-cell"><div class="avatar">${avatarLetter}</div><div><div class="name">${esc(l.label)}</div><div class="uuid-short">${l.uuid.slice(0,8)}… ${protoIcon} ${protoName}</div></div></div></td><td style="font-size:10px;color:var(--t2);">${fpEmoji[fp] || '🌐'} ${fpName}<br><span style="font-size:8px;color:var(--t3)">${httpName}</span></td><td><span class="status-badge ${statusClass}"><span class="status-dot"></span>${statusText}</span></td><td><div class="usage-bar"><span class="usage-text">${usedFmt} / ${limitFmt}</span><div class="bar"><div class="fill" style="width:${pct}%"></div></div></div></td><td style="font-size:11px;color:var(--t2);">${duration}</td><td><div class="action-btns"><button class="btn btn-pur btn-sm" onclick="showQR('${l.sub_url}')" title="QR Code"><i class="ti ti-qrcode"></i></button><button class="btn btn-pur btn-sm" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('${currentLang === 'fa' ? '✅ کپی ساب' : '✅ Copied'}','ok'))" title="${currentLang === 'fa' ? 'کپی ساب‌لینک' : 'Copy sub'}"><i class="ti ti-link"></i></button><button class="btn btn-amber btn-sm" onclick="resetUsage('${l.uuid}')" title="${currentLang === 'fa' ? 'ریست مصرف' : 'Reset usage'}"><i class="ti ti-rotate"></i></button><button class="btn btn-pur btn-sm" onclick="openEditModal('${l.uuid}')" title="${currentLang === 'fa' ? 'ویرایش' : 'Edit'}"><i class="ti ti-edit"></i></button><button class="btn btn-d btn-sm" onclick="openDeleteModal('${l.uuid}')" title="${currentLang === 'fa' ? 'حذف' : 'Delete'}"><i class="ti ti-trash"></i></button></div></td></tr>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== QR Code =====
function showQR(url) {
  const container = document.getElementById('qrcode-container');
  container.innerHTML = '';
  if (qrCodeInstance) { qrCodeInstance.clear(); qrCodeInstance = null; }
  qrCodeInstance = new QRCode(container, {
    text: url,
    width: 200,
    height: 200,
    colorDark: '#00f0ff',
    colorLight: '#0a0e2a',
    correctLevel: QRCode.CorrectLevel.H
  });
  openModal('modal-qr');
  container.dataset.url = url;
}

function downloadQR() {
  const canvas = document.querySelector('#qrcode-container canvas');
  if (!canvas) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); return; }
  const link = document.createElement('a');
  link.download = 'qrcode.png';
  link.href = canvas.toDataURL('image/png');
  link.click();
  toast('✅ ' + (currentLang === 'fa' ? 'QR دانلود شد' : 'QR downloaded'), 'ok');
}

// ===== مدیریت کاربران با تقویم =====
function initDatePickers() {
  if (expiryPicker) expiryPicker.destroy();
  expiryPicker = flatpickr("#user-expiry-date", {
    locale: currentLang === 'fa' ? 'fa' : 'en',
    dateFormat: "Y-m-d",
    minDate: "today",
    disableMobile: true,
    placeholder: currentLang === 'fa' ? 'انتخاب تاریخ انقضا' : 'Select expiry date',
    allowInput: true,
    onChange: function(selectedDates, dateStr, instance) {
      if (dateStr) document.getElementById('user-expiry-date').value = dateStr;
    }
  });
  
  if (editExpiryPicker) editExpiryPicker.destroy();
  editExpiryPicker = flatpickr("#edit-expiry-date", {
    locale: currentLang === 'fa' ? 'fa' : 'en',
    dateFormat: "Y-m-d",
    minDate: "today",
    disableMobile: true,
    placeholder: currentLang === 'fa' ? 'انتخاب تاریخ انقضا' : 'Select expiry date',
    allowInput: true,
    onChange: function(selectedDates, dateStr, instance) {
      if (dateStr) document.getElementById('edit-expiry-date').value = dateStr;
    }
  });
}

async function saveUser() {
  const label = document.getElementById('user-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('user-quota').value) || 0;
  const expiryDate = document.getElementById('user-expiry-date').value;
  const devices = parseInt(document.getElementById('user-devices').value) || 0;
  const password = document.getElementById('user-password').value.trim();
  const fingerprint = document.getElementById('user-fingerprint').value || 'chrome';
  const protocol = document.getElementById('user-protocol').value || 'vless-ws';
  const http_version = document.getElementById('user-http').value || 'h2';
  
  let expires_days = 0;
  if (expiryDate) {
    const exp = new Date(expiryDate);
    const now = new Date();
    expires_days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
    if (expires_days < 0) expires_days = 0;
  }
  
  try {
    const r = await authF('/api/links', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ label, limit_value: quota, limit_unit: 'GB', expires_days, max_devices: devices, password, fingerprint, protocol, http_version })
    });
    if (!r.ok) throw new Error();
    document.getElementById('user-label').value = 'کاربر';
    document.getElementById('user-quota').value = '2';
    document.getElementById('user-expiry-date').value = '';
    document.getElementById('user-devices').value = '1';
    document.getElementById('user-password').value = '';
    document.getElementById('user-fingerprint').value = 'chrome';
    document.getElementById('user-protocol').value = 'vless-ws';
    document.getElementById('user-http').value = 'h2';
    closeModal('modal-user');
    toast('✅ ' + (currentLang === 'fa' ? 'کاربر ساخته شد' : 'User created'), 'ok');
    loadUsers();
    loadDashboard();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function openEditModal(uuid) {
  try {
    const r = await authF('/api/links');
    const { links = [] } = await r.json();
    const link = links.find(l => l.uuid === uuid);
    if (!link) { toast((currentLang === 'fa' ? 'کاربر یافت نشد' : 'User not found'), 'err'); return; }
    document.getElementById('edit-uuid').value = uuid;
    document.getElementById('edit-label').value = link.label || '';
    document.getElementById('edit-password').value = '';
    document.getElementById('edit-quota').value = link.limit_bytes === 0 ? '' : (link.limit_bytes / (1024 ** 3)).toFixed(1);
    
    if (link.expires_at) {
      const expDate = new Date(link.expires_at);
      const dateStr = expDate.toISOString().split('T')[0];
      document.getElementById('edit-expiry-date').value = dateStr;
      if (editExpiryPicker) editExpiryPicker.setDate(dateStr);
    } else {
      document.getElementById('edit-expiry-date').value = '';
      if (editExpiryPicker) editExpiryPicker.clear();
    }
    
    document.getElementById('edit-devices').value = link.max_devices || 0;
    document.getElementById('edit-status').value = link.active ? 'true' : 'false';
    document.getElementById('edit-fingerprint').value = link.fingerprint || 'chrome';
    document.getElementById('edit-protocol').value = link.protocol || 'vless-ws';
    document.getElementById('edit-http').value = link.http_version || 'h2';
    document.getElementById('edit-password-section').style.display = link.has_password ? 'block' : 'none';
    openModal('modal-edit');
  } catch(e) { toast((currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function saveEdit() {
  const uuid = document.getElementById('edit-uuid').value;
  const password = document.getElementById('edit-password').value.trim();
  const label = document.getElementById('edit-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('edit-quota').value) || 0;
  const expiryDate = document.getElementById('edit-expiry-date').value;
  const devices = parseInt(document.getElementById('edit-devices').value) || 0;
  const active = document.getElementById('edit-status').value === 'true';
  const fingerprint = document.getElementById('edit-fingerprint').value || 'chrome';
  const protocol = document.getElementById('edit-protocol').value || 'vless-ws';
  const http_version = document.getElementById('edit-http').value || 'h2';
  
  let expires_days = 0;
  if (expiryDate) {
    const exp = new Date(expiryDate);
    const now = new Date();
    expires_days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
    if (expires_days < 0) expires_days = 0;
  }
  
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ label, limit_value: quota, limit_unit: 'GB', expires_days, max_devices: devices, active, password, fingerprint, protocol, http_version })
    });
    if (!r.ok) {
      if (r.status === 403) { toast('❌ ' + (currentLang === 'fa' ? 'رمز اشتباه' : 'Wrong password'), 'err'); return; }
      throw new Error();
    }
    closeModal('modal-edit');
    toast('✅ ' + (currentLang === 'fa' ? 'ویرایش شد' : 'Saved'), 'ok');
    loadUsers();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

function openDeleteModal(uuid) {
  document.getElementById('delete-uuid').value = uuid;
  document.getElementById('delete-password').value = '';
  openModal('modal-delete');
}

async function confirmDelete() {
  const uuid = document.getElementById('delete-uuid').value;
  const password = document.getElementById('delete-password').value.trim();
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ password })
    });
    if (!r.ok) {
      if (r.status === 403) { toast('❌ ' + (currentLang === 'fa' ? 'رمز اشتباه' : 'Wrong password'), 'err'); return; }
      throw new Error();
    }
    closeModal('modal-delete');
    toast('✅ ' + (currentLang === 'fa' ? 'حذف شد' : 'Deleted'), 'ok');
    loadUsers();
    loadDashboard();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function resetUsage(uuid) {
  if (!confirm(currentLang === 'fa' ? 'ریست مصرف؟' : 'Reset usage?')) return;
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ reset_usage: true })
    });
    if (!r.ok) throw new Error();
    toast('✅ ' + (currentLang === 'fa' ? 'ریست شد' : 'Reset'), 'ok');
    loadUsers();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

// ===== بارگذاری اتصالات =====
async function loadConnections() {
  try {
    const r = await authF('/api/connections');
    const d = await r.json();
    const grid = document.getElementById('conns-grid');
    const count = d.count || 0;
    document.getElementById('conn-count').textContent = count + (currentLang === 'fa' ? ' اتصال' : ' connections');
    if (!count) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-plug-off"></i><p>' + (currentLang === 'fa' ? 'هیچ اتصالی وجود ندارد' : 'No connections') + '</p></div>';
      return;
    }
    grid.innerHTML = d.connections.map(c => {
      const secs = c.connected_at ? Math.max(0, Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000)) : 0;
      const dur = secs < 60 ? secs + 's' : secs < 3600 ? Math.floor(secs / 60) + 'm' : Math.floor(secs / 3600) + 'h';
      return `<div class="conn-card"><div class="ip"><span class="conn-status-dot"></span> ${esc(c.ip)}</div><div class="label">${esc(c.label || 'نامشخص')}</div><div class="conn-info"><span>📥 ${esc(c.bytes_fmt || '0 B')}</span><span>⏱ ${dur}</span></div></div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== بارگذاری لاگ‌ها =====
async function loadLogs() {
  try {
    const r = await authF('/api/activity');
    const data = await r.json();
    const logs = data.logs || [];
    document.getElementById('logs-count').textContent = logs.length + (currentLang === 'fa' ? ' لاگ' : ' logs');
    const container = document.getElementById('logs-container');
    if (!logs.length) {
      container.innerHTML = '<div class="empty"><i class="ti ti-notes"></i><p>' + (currentLang === 'fa' ? 'هیچ لاگی وجود ندارد' : 'No logs') + '</p></div>';
      return;
    }
    container.innerHTML = logs.map(log => {
      const time = log.time ? new Date(log.time).toLocaleString(currentLang === 'fa' ? 'fa-IR' : 'en-US') : '—';
      const color = log.level === 'err' ? 'var(--red-t)' : log.level === 'warn' ? 'var(--amber-t)' : 'var(--cyan)';
      return `<div style="padding:4px 0;border-bottom:1px solid rgba(0,240,255,0.04);display:flex;gap:8px;flex-wrap:wrap"><span style="color:${color};font-weight:700;text-shadow:0 0 6px ${color}">[${(log.level || 'info').toUpperCase()}]</span><span style="color:var(--t3)">${time}</span><span style="color:var(--t1)">${esc(log.message)}</span></div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== RGB Mode =====
let rgbMode = false;
async function loadRGBStatus() {
  try {
    const r = await authF('/api/settings');
    const data = await r.json();
    rgbMode = data.rgb_mode || false;
    updateRGBUI();
  } catch(e) {}
}

function updateRGBUI() {
  const sw = document.getElementById('rgb-switch');
  if (rgbMode) { document.body.classList.add('rgb-mode'); sw.classList.add('on'); }
  else { document.body.classList.remove('rgb-mode'); sw.classList.remove('on'); }
}

async function toggleRGB() {
  const newState = !rgbMode;
  try {
    const r = await authF('/api/settings/rgb', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ enabled: newState })
    });
    const data = await r.json();
    rgbMode = data.rgb_mode;
    updateRGBUI();
    toast(rgbMode ? '🌈 RGB ' + (currentLang === 'fa' ? 'فعال شد' : 'enabled') : '🌙 RGB ' + (currentLang === 'fa' ? 'غیرفعال شد' : 'disabled'), 'ok');
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

// ===== بکاپ =====
async function createBackup() {
  try {
    const r = await authF('/api/backup');
    const data = await r.json();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `persepolis_backup_${new Date().toISOString().slice(0,10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    toast('✅ ' + (currentLang === 'fa' ? 'بکاپ دانلود شد' : 'Backup downloaded'), 'ok');
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function restoreBackup(event) {
  const file = event.target.files[0];
  if (!file) return;
  try {
    const text = await file.text();
    const data = JSON.parse(text);
    const r = await authF('/api/backup/restore', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!r.ok) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); return; }
    toast('✅ ' + (currentLang === 'fa' ? 'بکاپ بازیابی شد' : 'Backup restored'), 'ok');
    setTimeout(() => location.reload(), 1000);
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا: ' : 'Error: ') + e.message, 'err'); }
  event.target.value = '';
}

// ========================================
// ✦ WTF Factor #1: Command Palette ✦
// ========================================
let cmdkItems = [];
let cmdkActiveIdx = 0;
let cmdkFiltered = [];

function buildCmdkItems() {
  const t = translations[currentLang];
  cmdkItems = [
    {cat: 'actions', icon: 'ti-user-plus', title: t.cmdk_open_user, desc: t.cmdk_open_user_d, shortcut: 'N', action: () => openModal('modal-user')},
    {cat: 'navigation', icon: 'ti-layout-dashboard', title: t.cmdk_nav_dashboard, desc: t.cmdk_nav_dashboard_d, shortcut: 'G H', action: () => navTo('dashboard')},
    {cat: 'navigation', icon: 'ti-users', title: t.cmdk_nav_users, desc: t.cmdk_nav_users_d, shortcut: 'G U', action: () => navTo('users')},
    {cat: 'navigation', icon: 'ti-gauge', title: t.cmdk_nav_quota, desc: t.cmdk_nav_quota_d, shortcut: 'G Q', action: () => navTo('quota')},
    {cat: 'navigation', icon: 'ti-plug', title: t.cmdk_nav_inbound, desc: t.cmdk_nav_inbound_d, shortcut: 'G I', action: () => navTo('inbound')},
    {cat: 'navigation', icon: 'ti-plug-connected', title: t.cmdk_nav_connections, desc: t.cmdk_nav_connections_d, shortcut: 'G C', action: () => navTo('connections')},
    {cat: 'navigation', icon: 'ti-settings', title: t.cmdk_nav_settings, desc: t.cmdk_nav_settings_d, shortcut: 'G S', action: () => navTo('settings')},
    {cat: 'navigation', icon: 'ti-notes', title: t.cmdk_nav_logs, desc: t.cmdk_nav_logs_d, shortcut: 'G L', action: () => navTo('logs')},
    {cat: 'navigation', icon: 'ti-database', title: t.cmdk_nav_backup, desc: t.cmdk_nav_backup_d, shortcut: 'G B', action: () => navTo('backup')},
    {cat: 'settings', icon: 'ti-color-swatch', title: t.cmdk_toggle_theme, desc: t.cmdk_toggle_theme_d, shortcut: 'T', action: () => setTheme(currentTheme === 'dark' ? 'light' : 'dark')},
    {cat: 'settings', icon: 'ti-color-palette', title: t.cmdk_toggle_rgb, desc: t.cmdk_toggle_rgb_d, shortcut: 'R', action: () => toggleRGB()},
    {cat: 'settings', icon: 'ti-logout', title: t.cmdk_logout, desc: t.cmdk_logout_d, shortcut: 'L', action: () => logout()},
    {cat: 'actions', icon: 'ti-refresh', title: t.cmdk_refresh, desc: t.cmdk_refresh_d, shortcut: 'F5', action: () => { loadDashboard(); loadUsers(); loadQuota(); }},
    {cat: 'actions', icon: 'ti-download', title: t.cmdk_backup, desc: t.cmdk_backup_d, shortcut: 'B', action: () => createBackup()}
  ];
}

function initCmdk() {
  buildCmdkItems();
  filterCmdk();
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openCmdk();
    }
    if (e.key === 'Escape') closeCmdk();
  });
}

function openCmdk() {
  document.getElementById('cmdkOverlay').classList.add('open');
  const inp = document.getElementById('cmdkInput');
  inp.value = '';
  inp.focus();
  filterCmdk();
}

function closeCmdk() {
  document.getElementById('cmdkOverlay').classList.remove('open');
}

function filterCmdk() {
  const q = (document.getElementById('cmdkInput').value || '').trim().toLowerCase();
  cmdkFiltered = q ? cmdkItems.filter(it => it.title.toLowerCase().includes(q) || it.desc.toLowerCase().includes(q) || it.cat.includes(q)) : cmdkItems;
  cmdkActiveIdx = 0;
  renderCmdk();
}

function renderCmdk() {
  const t = translations[currentLang];
  const list = document.getElementById('cmdkList');
  if (!cmdkFiltered.length) {
    list.innerHTML = '<div class="cmdk-empty"><i class="ti ti-mood-empty"></i>' + t.cmdk_no_results + '</div>';
    return;
  }
  let html = '';
  let lastCat = '';
  cmdkFiltered.forEach((it, idx) => {
    if (it.cat !== lastCat) {
      const catName = t['cmdk_cat_' + it.cat] || it.cat;
      html += '<div class="cmdk-category">' + catName + '</div>';
      lastCat = it.cat;
    }
    const cls = idx === cmdkActiveIdx ? 'cmdk-item active' : 'cmdk-item';
    html += '<div class="' + cls + '" onclick="execCmdk(' + idx + ')" onmouseenter="setCmdkActive(' + idx + ')"><div class="cmdk-icon"><i class="ti ' + it.icon + '"></i></div><div class="cmdk-text"><div class="cmdk-title">' + it.title + '</div><div class="cmdk-desc">' + it.desc + '</div></div><span class="cmdk-shortcut">' + it.shortcut + '</span></div>';
  });
  list.innerHTML = html;
}

function setCmdkActive(idx) {
  cmdkActiveIdx = idx;
  renderCmdk();
}

function execCmdk(idx) {
  if (!cmdkFiltered[idx]) return;
  closeCmdk();
  setTimeout(() => cmdkFiltered[idx].action(), 150);
}

// ========== keyboard navigation in command palette ==========
document.addEventListener('keydown', (e) => {
  const overlay = document.getElementById('cmdkOverlay');
  if (!overlay.classList.contains('open')) return;
  if (e.key === 'ArrowDown') {
    e.preventDefault();
    cmdkActiveIdx = Math.min(cmdkFiltered.length - 1, cmdkActiveIdx + 1);
    renderCmdk();
  } else if (e.key === 'ArrowUp') {
    e.preventDefault();
    cmdkActiveIdx = Math.max(0, cmdkActiveIdx - 1);
    renderCmdk();
  } else if (e.key === 'Enter') {
    e.preventDefault();
    execCmdk(cmdkActiveIdx);
  }
});

// ========================================
// ✦ WTF Factor #2: Counter Up Animation ✦
// ========================================
function animateCounter(el, target, duration = 1000, suffix = '') {
  const start = parseFloat(el.dataset.currentValue || '0') || 0;
  const startTime = performance.now();
  el.classList.add('counting');
  
  function step(now) {
    const elapsed = now - startTime;
    const progress = Math.min(1, elapsed / duration);
    const eased = 1 - Math.pow(1 - progress, 3);
    const value = start + (target - start) * eased;
    let display = Number.isInteger(target) ? Math.round(value) : value.toFixed(1);
    el.textContent = display + suffix;
    el.dataset.currentValue = value;
    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      el.classList.remove('counting');
    }
  }
  requestAnimationFrame(step);
}

// ========================================
// ✦ WTF Factor #3: World Map with Servers ✦
// ========================================
const SERVER_LOCATIONS = [
  {name: 'Tehran', country: 'Iran', x: 62, y: 38, status: 'active', users: 0, ping: 28},
  {name: 'Frankfurt', country: 'Germany', x: 52, y: 32, status: 'active', users: 0, ping: 42},
  {name: 'Amsterdam', country: 'Netherlands', x: 49, y: 28, status: 'active', users: 0, ping: 48},
  {name: 'London', country: 'UK', x: 47, y: 30, status: 'active', users: 0, ping: 52},
  {name: 'New York', country: 'USA', x: 25, y: 35, status: 'active', users: 0, ping: 95},
  {name: 'Los Angeles', country: 'USA', x: 18, y: 42, status: 'active', users: 0, ping: 145},
  {name: 'Tokyo', country: 'Japan', x: 84, y: 40, status: 'active', users: 0, ping: 280},
  {name: 'Singapore', country: 'Singapore', x: 78, y: 60, status: 'active', users: 0, ping: 190},
  {name: 'Dubai', country: 'UAE', x: 60, y: 45, status: 'active', users: 0, ping: 35},
  {name: 'Istanbul', country: 'Turkey', x: 56, y: 35, status: 'inactive', users: 0, ping: 25},
];

function initServerMap() {
  const markersEl = document.getElementById('serverMarkers');
  const connSvg = document.getElementById('serverConnections');
  if (!markersEl) return;
  
  // رندر مارکرها
  markersEl.innerHTML = SERVER_LOCATIONS.map((s, i) => {
    return '<div class="server-marker ' + s.status + '" style="left:' + s.x + '%;top:' + s.y + '%" data-idx="' + i + '">' +
      '<div class="server-dot"></div>' +
      '<div class="server-tooltip"><div class="server-name">' + s.name + ', ' + s.country + '</div>' +
      '<div class="server-stat">🛰️ Ping: ' + s.ping + 'ms</div>' +
      '<div class="server-stat">👥 Users: <span data-marker-users="' + i + '">0</span></div></div>' +
    '</div>';
  }).join('');
  
  // خطوط اتصال از تهران به همه سرورها
  const tehran = SERVER_LOCATIONS[0];
  let svgContent = '';
  SERVER_LOCATIONS.slice(1).forEach(s => {
    svgContent += '<line x1="' + tehran.x + '" y1="' + tehran.y + '" x2="' + s.x + '" y2="' + s.y + '"/>';
  });
  connSvg.innerHTML = svgContent;
}

function updateServerMapUsers(userCount) {
  SERVER_LOCATIONS.forEach((s, i) => {
    s.users = Math.floor(userCount / SERVER_LOCATIONS.length) + Math.floor(Math.random() * 3);
    const el = document.querySelector('[data-marker-users="' + i + '"]');
    if (el) el.textContent = s.users;
  });
}

// ========================================
// ✦ WTF Factor #4: Speedometer Gauge ✦
// ========================================
function updateSpeedGauge() {
  const speedEl = document.getElementById('stat-speed');
  if (!speedEl) return;
  const speedText = speedEl.textContent || '0 B/s';
  // تبدیل به Mbps برای gauge
  let mbps = 0;
  const match = speedText.match(/([\d.]+)\s*(B\/s|KB\/s|MB\/s|GB\/s)/i);
  if (match) {
    const val = parseFloat(match[1]);
    const unit = match[2].toLowerCase();
    if (unit === 'b/s') mbps = val * 8 / 1000000;
    else if (unit === 'kb/s') mbps = val * 8 / 1000;
    else if (unit === 'mb/s') mbps = val * 8;
    else if (unit === 'gb/s') mbps = val * 8000;
  }
  // حداکثر 100 Mbps
  const pct = Math.min(1, mbps / 100);
  const arc = document.getElementById('gaugeArc');
  const needle = document.getElementById('gaugeNeedle');
  const gaugeNum = document.getElementById('gaugeNum');
  if (arc) {
    const totalLen = 251.3;
    arc.style.strokeDashoffset = totalLen * (1 - pct);
  }
  if (needle) {
    const rotation = -90 + (pct * 180);
    needle.style.transform = 'rotate(' + rotation + 'deg)';
  }
  if (gaugeNum) gaugeNum.textContent = mbps.toFixed(1) + ' Mbps';
}

// ========================================
// ✦ WTF Factor #5: Real-time Activity Feed ✦
// ========================================
let activityLog = [];

function addActivity(type, text, user) {
  const now = new Date();
  const timeStr = now.toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US');
  activityLog.unshift({type, text, user, time: timeStr});
  if (activityLog.length > 30) activityLog.pop();
  renderActivityFeed();
  // اگه notification permission داشتیم، نشون بده
  if (type === 'error' || type === 'warning') {
    showDesktopNotification(type === 'error' ? '⚠️' : '💡', text);
  }
}

function renderActivityFeed() {
  const feedEl = document.getElementById('activityFeed');
  if (!feedEl) return;
  if (!activityLog.length) {
    feedEl.innerHTML = '<div class="empty"><i class="ti ti-activity"></i><p style="font-size:10px">هنوز فعالیتی ثبت نشده</p></div>';
    return;
  }
  const iconMap = {info: 'ti-info-circle', success: 'ti-check', warning: 'ti-alert-triangle', error: 'ti-alert-octagon'};
  feedEl.innerHTML = activityLog.map(a => {
    const userText = a.user ? '<span class="activity-user">' + esc(a.user) + '</span> · ' : '';
    return '<div class="activity-item"><div class="activity-icon ' + a.type + '"><i class="ti ' + (iconMap[a.type] || 'ti-info-circle') + '"></i></div><div class="activity-text">' + userText + a.text + '<div class="activity-time">' + a.time + '</div></div></div>';
  }).join('');
}

async function loadActivityFeed() {
  try {
    const r = await authF('/api/activity');
    const data = await r.json();
    const logs = (data.logs || []).slice(0, 15).reverse();
    activityLog = logs.map(l => {
      const type = l.level === 'err' ? 'error' : l.level === 'warn' ? 'warning' : 'info';
      return {type, text: l.message || l.text || '', user: l.user || '', time: l.time ? new Date(l.time).toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US') : ''};
    });
    activityLog.reverse();
    // اضافه کردن ورود به پنل به‌عنوان اولین فعالیت
    activityLog.unshift({type: 'success', text: translations[currentLang].activity_login, user: '', time: new Date().toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US')});
    renderActivityFeed();
  } catch(e) {
    activityLog = [{type: 'success', text: translations[currentLang].activity_login, user: '', time: new Date().toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US')}];
    renderActivityFeed();
  }
}

// ========================================
// ✦ WTF Factor #6: Donut Chart for Protocol Distribution ✦
// ========================================
let protocolDonutChart = null;

async function loadProtocolDonut() {
  try {
    const r = await authF('/api/links');
    const data = await r.json();
    const links = data.links || [];
    
    const protocolCounts = {};
    links.forEach(l => {
      const p = l.protocol || 'vless-ws';
      protocolCounts[p] = (protocolCounts[p] || 0) + 1;
    });
    
    const protocols = Object.keys(protocolCounts);
    const counts = protocols.map(p => protocolCounts[p]);
    const total = counts.reduce((a, b) => a + b, 0);
    
    const colorMap = {
      'vless-ws': '#00f0ff',
      'vless-grpc': '#7b2ff7',
      'vless-xhttp': '#ff2e9a',
      'vless-http2': '#ffb800',
      'trojan-ws': '#10ffa0',
      'shadowsocks': '#ff6b8a'
    };
    const iconMap = {'vless-ws':'🚀','vless-grpc':'⚡','vless-xhttp':'🛡️','vless-http2':'📶','trojan-ws':'🔒','shadowsocks':'🌊'};
    const nameMap = {'vless-ws':'VLESS-WS','vless-grpc':'VLESS-gRPC','vless-xhttp':'VLESS-XHTTP','vless-http2':'VLESS-HTTP/2','trojan-ws':'Trojan-WS','shadowsocks':'Shadowsocks'};
    
    const colors = protocols.map(p => colorMap[p] || '#888888');
    
    const ctx = document.getElementById('protocolDonut').getContext('2d');
    if (protocolDonutChart) protocolDonutChart.destroy();
    
    if (!total) {
      document.getElementById('donutNum').textContent = '0';
      document.getElementById('donutLegend').innerHTML = '<div class="empty" style="padding:14px"><i class="ti ti-users" style="font-size:18px"></i><p style="font-size:10px">هیچ کاربری وجود ندارد</p></div>';
      return;
    }
    
    protocolDonutChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: protocols.map(p => nameMap[p] || p),
        datasets: [{
          data: counts,
          backgroundColor: colors,
          borderColor: '#0a0e2a',
          borderWidth: 2,
          hoverOffset: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '70%',
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: 'rgba(10, 14, 35, 0.95)',
            borderColor: '#00f0ff',
            borderWidth: 1,
            titleColor: '#00f0ff',
            bodyColor: '#e8efff',
            padding: 10,
            cornerRadius: 8
          }
        }
      }
    });
    
    document.getElementById('donutNum').textContent = total;
    
    // Legend
    document.getElementById('donutLegend').innerHTML = protocols.map((p, i) => {
      const pct = ((counts[i] / total) * 100).toFixed(1);
      return '<div class="donut-legend-item"><span class="legend-dot" style="background:' + colors[i] + ';color:' + colors[i] + '"></span><span class="legend-name">' + iconMap[p] + ' ' + (nameMap[p] || p) + '</span><span class="legend-val">' + counts[i] + ' (' + pct + '%)</span></div>';
    }).join('');
  } catch(e) { console.error('donut load error', e); }
}

// ========================================
// ✦ WTF Factor #7: Desktop Notifications ✦
// ========================================
function showDesktopNotification(emoji, body) {
  if (!('Notification' in window)) return;
  if (Notification.permission !== 'granted') return;
  try {
    new Notification('✦ PERSEPOLIS', {
      body: emoji + ' ' + body,
      icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="80" font-size="80">🏛️</text></svg>',
      badge: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="%2300f0ff"/></svg>',
      tag: 'persepolis-' + Date.now()
    });
  } catch(e) { console.warn('Notification error', e); }
}

function addNotifPermissionCard() {
  const settingsSection = document.getElementById('pg-settings');
  if (!settingsSection) return;
  if (!('Notification' in window)) return;
  if (Notification.permission === 'granted') return;
  
  const t = translations[currentLang];
  const card = document.createElement('div');
  card.className = 'notif-perm-card';
  card.innerHTML = '<i class="ti ti-bell"></i><div style="flex:1"><div style="font-weight:700;color:var(--t1)">' + t.notif_enable + '</div><div>' + t.notif_desc + '</div></div><button onclick="requestNotifPermission()">' + t.notif_enable_btn + '</button>';
  settingsSection.appendChild(card);
}

function requestNotifPermission() {
  Notification.requestPermission().then(p => {
    if (p === 'granted') {
      toast('✅ ' + (currentLang === 'fa' ? 'اطلاع‌رسانی فعال شد' : 'Notifications enabled'), 'ok');
      showDesktopNotification('🎉', currentLang === 'fa' ? 'اطلاع‌رسانی دسکتاپ فعال شد' : 'Desktop notifications enabled');
      document.querySelectorAll('.notif-perm-card').forEach(c => c.remove());
    }
  });
}

// ========================================
// ✦ WTF Factor #8: Drag & Drop Reorder ✦
// ========================================
function initDragAndDrop() {
  const tbody = document.getElementById('users-tbody');
  if (!tbody) return;
  let draggedRow = null;
  
  tbody.addEventListener('dragstart', (e) => {
    if (!e.target.closest('tr[data-uuid]')) return;
    draggedRow = e.target.closest('tr[data-uuid]');
    draggedRow.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
  });
  
  tbody.addEventListener('dragend', (e) => {
    if (draggedRow) draggedRow.classList.remove('dragging');
    document.querySelectorAll('.drag-over').forEach(r => r.classList.remove('drag-over'));
    draggedRow = null;
  });
  
  tbody.addEventListener('dragover', (e) => {
    e.preventDefault();
    const target = e.target.closest('tr[data-uuid]');
    if (target && target !== draggedRow) {
      document.querySelectorAll('.drag-over').forEach(r => r.classList.remove('drag-over'));
      target.classList.add('drag-over');
    }
  });
  
  tbody.addEventListener('drop', (e) => {
    e.preventDefault();
    const target = e.target.closest('tr[data-uuid]');
    if (target && draggedRow && target !== draggedRow) {
      const rows = Array.from(tbody.querySelectorAll('tr[data-uuid]'));
      const fromIdx = rows.indexOf(draggedRow);
      const toIdx = rows.indexOf(target);
      if (fromIdx < toIdx) {
        target.parentNode.insertBefore(draggedRow, target.nextSibling);
      } else {
        target.parentNode.insertBefore(draggedRow, target);
      }
      saveUserOrder();
    }
  });
}

function saveUserOrder() {
  const order = Array.from(document.querySelectorAll('#users-tbody tr[data-uuid]')).map(tr => tr.dataset.uuid);
  try { localStorage.setItem('persepolis-user-order', JSON.stringify(order)); } catch(e) {}
}

// ========================================
// ✦ WTF Factor #9: Live Search + Filter ✦
// ========================================
let userFilter = 'all';
let allUsersCache = [];

function setUserFilter(filter) {
  userFilter = filter;
  document.querySelectorAll('.filter-chip').forEach(c => c.classList.toggle('active', c.dataset.filter === filter));
  applyUserFilters();
}

function applyUserFilters() {
  const q = (document.getElementById('userSearch').value || '').toLowerCase().trim();
  const tbody = document.getElementById('users-tbody');
  if (!tbody || !allUsersCache.length) return;
  
  const filtered = allUsersCache.filter(l => {
    const isActive = l.active && !l.expired;
    // filter chips
    if (userFilter === 'active' && !isActive) return false;
    if (userFilter === 'expired' && !l.expired) return false;
    if (userFilter === 'disabled' && (l.active || l.expired)) return false;
    if (userFilter === 'high-usage') {
      const pct = l.limit_bytes > 0 ? (l.used_bytes / l.limit_bytes) * 100 : 0;
      if (pct < 80) return false;
    }
    // text search
    if (q) {
      const text = (l.label + ' ' + l.uuid + ' ' + (l.protocol || '')).toLowerCase();
      if (!text.includes(q)) return false;
    }
    return true;
  });
  
  if (!filtered.length) {
    tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;padding:30px;color:var(--t3);">' + (currentLang === 'fa' ? 'هیچ کاربری یافت نشد' : 'No users found') + '</td></tr>';
    return;
  }
  
  tbody.innerHTML = filtered.map(l => {
    const isActive = l.active && !l.expired;
    const statusClass = isActive ? 'active' : (l.expired ? 'expired' : 'disabled');
    const statusText = isActive ? (currentLang === 'fa' ? 'فعال' : 'Active') : (l.expired ? (currentLang === 'fa' ? 'منقضی' : 'Expired') : (currentLang === 'fa' ? 'غیرفعال' : 'Disabled'));
    const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
    const usedFmt = fmtB(l.used_bytes || 0);
    const limitFmt = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
    const fp = l.fingerprint || 'chrome';
    const fpEmoji = { chrome: '🌐', firefox: '🦊', safari: '🧭', edge: '🌊', ios: '📱', android: '🤖', safari_ios: '🍏', random: '🎲', none: '🚫' };
    const fpName = { chrome: 'Chrome', firefox: 'Firefox', safari: 'Safari', edge: 'Edge', ios: 'iOS', android: 'Android', safari_ios: 'Safari iOS', random: 'Random', none: 'None' }[fp] || fp;
    const protocol = l.protocol || 'vless-ws';
    const protoIcon = { 'vless-ws':'🚀', 'vless-grpc':'⚡', 'vless-xhttp':'🛡️', 'vless-http2':'📶', 'trojan-ws':'🔒', 'shadowsocks':'🌊' }[protocol] || '🚀';
    const protoName = { 'vless-ws':'VLESS-WS', 'vless-grpc':'VLESS-gRPC', 'vless-xhttp':'VLESS-XHTTP', 'vless-http2':'VLESS-HTTP/2', 'trojan-ws':'Trojan-WS', 'shadowsocks':'Shadowsocks' }[protocol] || protocol;
    const httpVer = l.http_version || 'h2';
    const httpName = { 'h1':'HTTP/1.1', 'h2':'HTTP/2', 'h3':'HTTP/3', 'auto':'Auto' }[httpVer] || httpVer;
    let duration = '∞';
    if (l.expires_at) {
      try {
        const exp = new Date(l.expires_at);
        const now = new Date();
        const days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
        duration = days > 0 ? days + (currentLang === 'fa' ? ' روز' : ' days') : (currentLang === 'fa' ? 'منقضی' : 'Expired');
      } catch(e) { duration = '—'; }
    }
    const avatarLetter = (l.label || 'U')[0].toUpperCase();
    return '<tr data-uuid="' + l.uuid + '" draggable="true"><td><div class="user-name-cell"><div class="avatar">' + avatarLetter + '</div><div><div class="name">' + esc(l.label) + '</div><div class="uuid-short">' + l.uuid.slice(0,8) + '… ' + protoIcon + ' ' + protoName + '</div></div></div></td><td style="font-size:10px;color:var(--t2);">' + (fpEmoji[fp] || '🌐') + ' ' + fpName + '<br><span style="font-size:8px;color:var(--t3)">' + httpName + '</span></td><td><span class="status-badge ' + statusClass + '"><span class="status-dot"></span>' + statusText + '</span></td><td><div class="usage-bar"><span class="usage-text">' + usedFmt + ' / ' + limitFmt + '</span><div class="bar"><div class="fill" style="width:' + pct + '%"></div></div></div></td><td style="font-size:11px;color:var(--t2);">' + duration + '</td><td><div class="action-btns"><button class="btn btn-pur btn-sm" onclick="showQR(\'' + l.sub_url + '\')" title="QR Code"><i class="ti ti-qrcode"></i></button><button class="btn btn-pur btn-sm" onclick="navigator.clipboard.writeText(\'' + esc(l.sub_url) + '\').then(()=>toast(\'' + (currentLang === 'fa' ? '✅ کپی ساب' : '✅ Copied') + '\',\'ok\'))" title="' + (currentLang === 'fa' ? 'کپی ساب‌لینک' : 'Copy sub') + '"><i class="ti ti-link"></i></button><button class="btn btn-amber btn-sm" onclick="resetUsage(\'' + l.uuid + '\')" title="' + (currentLang === 'fa' ? 'ریست مصرف' : 'Reset usage') + '"><i class="ti ti-rotate"></i></button><button class="btn btn-pur btn-sm" onclick="openEditModal(\'' + l.uuid + '\')" title="' + (currentLang === 'fa' ? 'ویرایش' : 'Edit') + '"><i class="ti ti-edit"></i></button><button class="btn btn-d btn-sm" onclick="openDeleteModal(\'' + l.uuid + '\')" title="' + (currentLang === 'fa' ? 'حذف' : 'Delete') + '"><i class="ti ti-trash"></i></button></div></td></tr>';
  }).join('');
  
  // آپدیت chip counts
  const counts = {
    all: allUsersCache.length,
    active: allUsersCache.filter(l => l.active && !l.expired).length,
    expired: allUsersCache.filter(l => l.expired).length,
    disabled: allUsersCache.filter(l => !l.active && !l.expired).length,
    'high-usage': allUsersCache.filter(l => l.limit_bytes > 0 && (l.used_bytes / l.limit_bytes) >= 0.8).length
  };
  document.getElementById('chip-all').textContent = counts.all;
  document.getElementById('chip-active').textContent = counts.active;
  document.getElementById('chip-expired').textContent = counts.expired;
  document.getElementById('chip-disabled').textContent = counts.disabled;
  document.getElementById('chip-high').textContent = counts['high-usage'];
}

// ========================================
// ✦ WTF Factor #10: Particle Cursor Trail ✦
// ========================================
function initParticleCursor() {
  const canvas = document.getElementById('particle-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let particles = [];
  let lastMouse = {x: 0, y: 0};
  
  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);
  
  document.addEventListener('mousemove', (e) => {
    const dx = e.clientX - lastMouse.x;
    const dy = e.clientY - lastMouse.y;
    const speed = Math.sqrt(dx*dx + dy*dy);
    if (speed > 2) {
      const count = Math.min(3, Math.floor(speed / 5));
      for (let i = 0; i < count; i++) {
        particles.push({
          x: e.clientX + (Math.random() - 0.5) * 6,
          y: e.clientY + (Math.random() - 0.5) * 6,
          vx: (Math.random() - 0.5) * 1.5,
          vy: (Math.random() - 0.5) * 1.5 - 0.5,
          life: 1,
          size: Math.random() * 2 + 1,
          color: Math.random() > 0.5 ? '#00f0ff' : (Math.random() > 0.5 ? '#ff2e9a' : '#7b2ff7')
        });
      }
    }
    lastMouse = {x: e.clientX, y: e.clientY};
  });
  
  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles = particles.filter(p => p.life > 0);
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.02;
      p.life -= 0.025;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.globalAlpha = p.life;
      ctx.shadowBlur = 8;
      ctx.shadowColor = p.color;
      ctx.fill();
    });
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
    requestAnimationFrame(animate);
  }
  animate();
}

// ========================================
// ✦ WTF Factor #11: Player-style Bottom Bar ✦
// ========================================
let playerBarVisible = true;

function initPlayerBar() {
  const bar = document.getElementById('playerBar');
  if (!bar) return;
  setTimeout(() => {
    bar.classList.add('show');
    document.body.classList.add('has-player-bar');
  }, 800);
  updatePlayerBar();
}

function togglePlayerBar() {
  playerBarVisible = !playerBarVisible;
  const bar = document.getElementById('playerBar');
  if (playerBarVisible) {
    bar.classList.add('show');
    document.body.classList.add('has-player-bar');
  } else {
    bar.classList.remove('show');
    document.body.classList.remove('has-player-bar');
  }
}

function updatePlayerBar() {
  try {
    const users = document.getElementById('stat-users')?.textContent || '0';
    const online = document.getElementById('online-badge')?.textContent || '0';
    const traffic = document.getElementById('stat-traffic')?.textContent || '0';
    const uptime = document.getElementById('stat-uptime')?.textContent || '00:00:00';
    const pbUsers = document.getElementById('pb-users');
    const pbOnline = document.getElementById('pb-online');
    const pbTraffic = document.getElementById('pb-traffic');
    const pbUptime = document.getElementById('pb-uptime');
    if (pbUsers) pbUsers.textContent = users + (currentLang === 'fa' ? ' کاربر' : ' users');
    if (pbOnline) pbOnline.textContent = online;
    if (pbTraffic) pbTraffic.textContent = traffic + ' MB';
    if (pbUptime) pbUptime.textContent = uptime;
  } catch(e) {}
}

// ========================================
// ✦ WTF Factor #12: Animated Theme Switcher (Circular Reveal) ✦
// ========================================
function animatedThemeSwitch(newTheme, x, y) {
  const reveal = document.getElementById('themeReveal');
  if (!reveal) { setTheme(newTheme); return; }
  if (x === undefined) x = window.innerWidth / 2;
  if (y === undefined) y = window.innerHeight / 2;
  const maxR = Math.hypot(Math.max(x, window.innerWidth - x), Math.max(y, window.innerHeight - y));
  reveal.style.left = (x - maxR) + 'px';
  reveal.style.top = (y - maxR) + 'px';
  reveal.style.width = (maxR * 2) + 'px';
  reveal.style.height = (maxR * 2) + 'px';
  reveal.style.background = newTheme === 'light' ? '#eef1f8' : '#030418';
  reveal.classList.remove('active');
  void reveal.offsetWidth; // trigger reflow
  reveal.classList.add('active');
  setTimeout(() => { setTheme(newTheme); }, 300);
  setTimeout(() => { reveal.classList.remove('active'); }, 800);
}

// Override theme button clicks to use animated switcher
document.addEventListener('click', (e) => {
  const btn = e.target.closest('[onclick*="setTheme"]');
  if (!btn) return;
  e.preventDefault();
  const match = btn.getAttribute('onclick').match(/setTheme\('(\w+)'\)/);
  if (match) {
    const newTheme = match[1];
    if (newTheme !== currentTheme) animatedThemeSwitch(newTheme, e.clientX, e.clientY);
  }
});

// ========================================
// ✦ Keyboard Shortcuts (Ctrl+K already handled) ✦
// ========================================
function initKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    // Alt+1 to Alt+7 برای ناوبری سریع
    if (e.altKey && e.key >= '1' && e.key <= '7') {
      e.preventDefault();
      const pages = ['dashboard', 'users', 'quota', 'inbound', 'connections', 'settings', 'logs'];
      navTo(pages[parseInt(e.key) - 1]);
    }
    // Ctrl+/ برای toggle player bar
    if ((e.ctrlKey || e.metaKey) && e.key === '/') {
      e.preventDefault();
      togglePlayerBar();
    }
  });
}

// ===== راه‌اندازی اولیه =====
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    if (!d.authenticated) location.href = '/login';
  } catch(e) { location.href = '/login'; }
  
  await loadThemeFromServer();
  setLang(currentLang);
  await loadRGBStatus();
  initDatePickers();
  
  loadDashboard();
  loadInbound();
  loadUsers();
  loadConnections();
  loadLogs();
  loadQuota();
  
  // === WTF Factors initialization ===
  initCmdk();
  initParticleCursor();
  initPlayerBar();
  initDragAndDrop();
  initServerMap();
  loadActivityFeed();
  loadProtocolDonut();
  initKeyboardShortcuts();
  
  // اضافه کردن کارت درخواست notification به تنظیمات
  addNotifPermissionCard();
  
  // رفع placeholder cmdk
  const cmdkInput = document.getElementById('cmdkInput');
  if (cmdkInput) cmdkInput.placeholder = (currentLang === 'fa' ? 'جست‌وجو یا دستور... (مثلاً: کاربر جدید، QR، تم)' : 'Search or command...');
  
  setInterval(() => {
    if (document.getElementById('pg-dashboard').classList.contains('on')) loadDashboard();
    if (document.getElementById('pg-connections').classList.contains('on')) loadConnections();
    if (document.getElementById('pg-users').classList.contains('on')) loadUsers();
    if (document.getElementById('pg-quota').classList.contains('on')) loadQuota();
    updatePlayerBar();
    updateSpeedGauge();
  }, 10000);
});
</script>
</body></html>"""


# ===== تابع ساب‌لینک کیهانی · طراحی کارتی پیشرفته =====
def get_sub_page_html(uuid: str, link: dict) -> str:
    """صفحه ساب‌لینک با طراحی کیهانی، شیشه‌ای و افکت‌های نئونی"""
    from datetime import datetime
    
    used = link.get('used_bytes', 0)
    limit = link.get('limit_bytes', 0)
    active = link.get('active', True)
    expired = link.get('expired', False)
    label = link.get('label', 'کاربر')
    fingerprint = link.get('fingerprint', 'chrome')
    max_devices = link.get('max_devices', 0)
    protocol = link.get('protocol', 'vless-ws')
    http_version = link.get('http_version', 'h2')
    active_connections = link.get('active_connections', 0)
    sub_url = link.get('sub_url', '')
    used_val = link.get('used_val', '0')
    used_unit = link.get('used_unit', 'B')
    limit_val = link.get('limit_val', '∞')
    limit_unit = link.get('limit_unit', '')
    percent = link.get('percent', 0)
    days_left = link.get('days_left', 'نامحدود')
    vless_link = link.get('vless_link', '')
    protocol_name = link.get('protocol_name', 'VLESS-WS')
    protocol_icon = link.get('protocol_icon', '🚀')
    http_name = link.get('http_name', 'HTTP/2')
    
    is_allowed = active and not expired
    host = get_host() if 'get_host' in dir() else 'localhost'
    
    def fmt_bytes(b):
        if not b or b == 0:
            return '0 B'
        if b < 1024:
            return f'{b} B'
        if b < 1024**2:
            return f'{b/1024:.1f} KB'
        if b < 1024**3:
            return f'{b/1024**2:.2f} MB'
        return f'{b/1024**3:.2f} GB'
    
    used_fmt = fmt_bytes(used)
    limit_fmt = 'نامحدود' if limit == 0 else fmt_bytes(limit)
    
    # منوی تم‌های کیهانی
    theme_names = {
        'cosmic_neon':'🌌 نئون کیهانی',
        'cosmic_aurora':'✨ شفق قطبی',
        'cosmic_void':'🕳️ خلاء سیاه',
        'cosmic_purple':'🔮 بنفش کیهانی',
        'cosmic_sunset':'🌅 غروب کیهانی',
        'cosmic_ocean':'🌊 اقیانوس عمیق',
        'cosmic_gold':'🏛️ طلایی تخت جمشید',
        'cosmic_mint':'🌱 سبز نعنایی',
        'cosmic_rose':'🌸 رز کیهانی',
        'cosmic_matrix':'💻 ماتریکس'
    }
    theme_colors = {
        'cosmic_neon':'linear-gradient(135deg,#00f0ff,#7b2ff7)',
        'cosmic_aurora':'linear-gradient(135deg,#10ffa0,#00f0ff,#7b2ff7)',
        'cosmic_void':'linear-gradient(135deg,#0a0a1a,#1a1a3a)',
        'cosmic_purple':'linear-gradient(135deg,#7b2ff7,#ff2e9a)',
        'cosmic_sunset':'linear-gradient(135deg,#ff2e9a,#ffb800)',
        'cosmic_ocean':'linear-gradient(135deg,#0066ff,#00f0ff)',
        'cosmic_gold':'linear-gradient(135deg,#D4A843,#F5D060)',
        'cosmic_mint':'linear-gradient(135deg,#10ffa0,#00f0ff)',
        'cosmic_rose':'linear-gradient(135deg,#ff2e9a,#ffb6c1)',
        'cosmic_matrix':'linear-gradient(135deg,#00ff00,#008800)'
    }
    
    menu_items = ""
    for t in ['cosmic_neon','cosmic_aurora','cosmic_void','cosmic_purple','cosmic_sunset','cosmic_ocean','cosmic_gold','cosmic_mint','cosmic_rose','cosmic_matrix']:
        menu_items += f"""
        <div class="menu-item" data-theme="{t}" onclick="selectTheme('{t}')">
            <span class="dot" style="background:{theme_colors[t]}"></span>
            {theme_names[t]}
            <span class="check">✓</span>
        </div>
        """
    
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>✦ {{label}} · Persepolis</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#030418;--card:rgba(10,14,35,0.55);--card-border:rgba(0,240,255,0.12);
  --text:#e8efff;--text2:#94a3b8;--text3:#64748b;
  --accent:#00f0ff;--accent2:#7b2ff7;--accent3:#ff2e9a;
  --green:#10ffa0;--green-bg:rgba(16,255,160,0.08);--green-text:#10ffa0;
  --red:#ff4d6d;--red-bg:rgba(255,77,109,0.08);--red-text:#ff6b8a;
  --shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(0,240,255,0.04);
  --transition:all 0.4s cubic-bezier(0.34,1.56,0.64,1);--radius:18px
}}
[data-theme="cosmic_neon"]{{--bg:#030418;--card:rgba(10,14,35,0.55);--card-border:rgba(0,240,255,0.12);--accent:#00f0ff;--accent2:#7b2ff7;--accent3:#ff2e9a;--text:#e8efff;--text2:#94a3b8;--text3:#64748b}}
[data-theme="cosmic_aurora"]{{--bg:#020815;--card:rgba(8,15,30,0.6);--card-border:rgba(16,255,160,0.12);--accent:#10ffa0;--accent2:#00f0ff;--accent3:#7b2ff7;--text:#d4ffe8;--text2:#7eb8a0;--text3:#4a7868}}
[data-theme="cosmic_void"]{{--bg:#000005;--card:rgba(15,15,25,0.7);--card-border:rgba(100,100,200,0.1);--accent:#8a8aff;--accent2:#aaaaff;--accent3:#cc66ff;--text:#e0e0ff;--text2:#9090c0;--text3:#505078}}
[data-theme="cosmic_purple"]{{--bg:#08051a;--card:rgba(20,10,40,0.6);--card-border:rgba(123,47,247,0.15);--accent:#7b2ff7;--accent2:#ff2e9a;--accent3:#00f0ff;--text:#f0e8ff;--text2:#a890c0;--text3:#685088}}
[data-theme="cosmic_sunset"]{{--bg:#1a0810;--card:rgba(40,15,25,0.6);--card-border:rgba(255,46,154,0.12);--accent:#ff2e9a;--accent2:#ffb800;--accent3:#7b2ff7;--text:#ffe8e8;--text2:#c0a090;--text3:#806058}}
[data-theme="cosmic_ocean"]{{--bg:#001525;--card:rgba(8,25,50,0.6);--card-border:rgba(0,150,255,0.15);--accent:#00f0ff;--accent2:#0066ff;--accent3:#10ffa0;--text:#e0f0ff;--text2:#80b0d0;--text3:#5080a0}}
[data-theme="cosmic_gold"]{{--bg:#0a0805;--card:rgba(25,20,8,0.6);--card-border:rgba(212,168,67,0.12);--accent:#D4A843;--accent2:#F5D060;--accent3:#B8922E;--text:#F5ECD7;--text2:#C4A35A;--text3:#8A7A4A}}
[data-theme="cosmic_mint"]{{--bg:#001510;--card:rgba(8,30,20,0.6);--card-border:rgba(16,255,160,0.12);--accent:#10ffa0;--accent2:#00f0ff;--accent3:#7b2ff7;--text:#d0ffe8;--text2:#80c0a0;--text3:#508070}}
[data-theme="cosmic_rose"]{{--bg:#1a0515;--card:rgba(40,15,30,0.6);--card-border:rgba(255,46,154,0.12);--accent:#ff2e9a;--accent2:#ffb6c1;--accent3:#7b2ff7;--text:#ffe8f0;--text2:#c090a0;--text3:#806070}}
[data-theme="cosmic_matrix"]{{--bg:#000a00;--card:rgba(0,20,0,0.65);--card-border:rgba(0,255,0,0.15);--accent:#00ff00;--accent2:#00cc00;--accent3:#008800;--text:#c0ffc0;--text2:#80a080;--text3:#506050}}

@keyframes twinkle{{0%,100%{{opacity:0.15}}50%{{opacity:0.9}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
@keyframes cardIn{{from{{opacity:0;transform:translateY(40px) scale(0.92);filter:blur(10px)}}to{{opacity:1;transform:translateY(0) scale(1);filter:blur(0)}}}}
@keyframes float{{0%,100%{{transform:translate(0,0) scale(1)}}50%{{transform:translate(20px,-20px) scale(1.05)}}}}
@keyframes shimmer{{0%{{background-position:-200% 0}}100%{{background-position:200% 0}}}}
@keyframes gradientFlow{{0%{{background-position:0% 50%}}50%{{background-position:100% 50%}}100%{{background-position:0% 50%}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes orbit{{0%{{transform:rotate(0deg) translateX(120px) rotate(0deg)}}100%{{transform:rotate(360deg) translateX(120px) rotate(-360deg)}}}}

body{{font-family:'Vazirmatn',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:16px;background:radial-gradient(ellipse at top,var(--bg),#000 80%);color:var(--text);transition:var(--transition);position:relative;overflow-x:hidden}}

#starfield{{position:fixed;inset:0;z-index:0;pointer-events:none}}
.nebula{{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;pointer-events:none;animation:float 12s ease-in-out infinite}}
.nebula1{{width:500px;height:500px;background:radial-gradient(circle,rgba(0,240,255,0.1),transparent 70%);top:-150px;right:-100px}}
.nebula2{{width:400px;height:400px;background:radial-gradient(circle,rgba(255,46,154,0.08),transparent 70%);bottom:-100px;left:-80px;animation-delay:-6s}}
.nebula3{{width:350px;height:350px;background:radial-gradient(circle,rgba(123,47,247,0.08),transparent 70%);top:40%;left:30%;animation-delay:-3s}}

/* خطوط هولوگرافیک */
.grid-bg{{position:fixed;inset:0;z-index:0;opacity:0.1;background-image:linear-gradient(rgba(0,240,255,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(0,240,255,0.3) 1px,transparent 1px);background-size:40px 40px;mask-image:radial-gradient(ellipse at center,#000 0%,transparent 60%);-webkit-mask-image:radial-gradient(ellipse at center,#000 0%,transparent 60%);pointer-events:none;animation:gridShift 20s linear infinite}}
@keyframes gridShift{{from{{background-position:0 0}}to{{background-position:40px 40px}}}}

/* === دراپ‌داون تم === */
.theme-dropdown{{position:fixed;top:20px;left:50%;transform:translateX(-50%);z-index:100}}
.theme-dropdown .toggle-btn{{background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--card-border);border-radius:14px;padding:10px 20px;color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:13px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:10px;transition:var(--transition);box-shadow:0 8px 40px rgba(0,0,0,0.3)}}
.theme-dropdown .toggle-btn:hover{{border-color:var(--accent);transform:scale(1.02);box-shadow:0 0 30px rgba(0,240,255,0.2)}}
.theme-dropdown .toggle-btn .arrow{{transition:transform .3s;font-size:12px}}
.theme-dropdown .toggle-btn .arrow.open{{transform:rotate(180deg)}}
.theme-dropdown .menu{{display:none;position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%);background:var(--card);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--card-border);border-radius:14px;padding:8px;min-width:220px;box-shadow:0 12px 50px rgba(0,0,0,0.5),0 0 30px rgba(0,240,255,0.1);animation:cardIn .3s ease}}
.theme-dropdown .menu.open{{display:block}}
.theme-dropdown .menu-item{{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;cursor:pointer;transition:var(--transition);color:var(--text2);font-size:13px;font-weight:600}}
.theme-dropdown .menu-item:hover{{background:rgba(0,240,255,0.06);color:var(--text);transform:translateX(-3px)}}
.theme-dropdown .menu-item .dot{{display:inline-block;width:20px;height:20px;border-radius:6px;flex-shrink:0;border:1px solid rgba(255,255,255,0.1);box-shadow:0 0 10px rgba(0,240,255,0.2)}}
.theme-dropdown .menu-item .check{{margin-right:auto;opacity:0;transition:opacity .2s;color:var(--accent);font-weight:900}}
.theme-dropdown .menu-item.active .check{{opacity:1}}
.theme-dropdown .menu-item.active{{background:rgba(0,240,255,0.06);color:var(--text)}}

/* === کارت اصلی === */
.card{{position:relative;z-index:10;background:var(--card);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--card-border);border-radius:var(--radius);padding:28px 24px 24px;max-width:520px;width:100%;box-shadow:var(--shadow);animation:cardIn 0.7s var(--transition);transition:var(--transition);margin-top:70px}}
.card::before{{content:'';position:absolute;inset:0;border-radius:var(--radius);padding:1px;background:linear-gradient(135deg,rgba(0,240,255,0.5),transparent 30%,transparent 70%,rgba(255,46,154,0.5));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:0.4;pointer-events:none;animation:borderGlow 6s ease-in-out infinite}}
@keyframes borderGlow{{0%,100%{{opacity:0.3}}50%{{opacity:0.7}}}}
.card::after{{content:'';position:absolute;top:0;left:30px;right:30px;height:2px;background:linear-gradient(90deg,transparent,var(--accent),var(--accent3),transparent);opacity:0.6;pointer-events:none}}

/* هدر */
.card-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;padding-bottom:14px;border-bottom:1px solid var(--card-border);position:relative}}
.brand{{display:flex;align-items:center;gap:10px}}
.brand-icon{{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3));display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 0 30px rgba(0,240,255,0.3);animation:iconPulse 4s ease-in-out infinite;position:relative}}
.brand-icon::before{{content:'';position:absolute;inset:-3px;border-radius:14px;background:inherit;filter:blur(10px);opacity:0.5;z-index:-1}}
@keyframes iconPulse{{0%,100%{{box-shadow:0 0 30px rgba(0,240,255,0.4);transform:scale(1)}}50%{{box-shadow:0 0 50px rgba(255,46,154,0.5);transform:scale(1.05)}}}}
.brand-text{{font-size:13px;font-weight:900;background:linear-gradient(135deg,#fff,var(--accent),var(--accent3));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:0.5px}}
.brand-sub{{font-size:7px;color:var(--text3);letter-spacing:1.5px;text-transform:uppercase;margin-top:1px}}
.theme-toggle-btn{{background:rgba(0,240,255,0.05);border:1px solid var(--card-border);color:var(--text2);width:34px;height:34px;border-radius:10px;cursor:pointer;font-size:16px;transition:var(--transition)}}
.theme-toggle-btn:hover{{background:rgba(0,240,255,0.1);transform:rotate(20deg);color:var(--accent);box-shadow:0 0 15px rgba(0,240,255,0.3)}}

/* نام کاربر */
.user-name-row{{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:8px}}
.user-name{{font-size:22px;font-weight:900;color:var(--text);display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.user-name .proto-badge{{font-size:10px;font-weight:700;background:linear-gradient(135deg,rgba(0,240,255,0.12),rgba(255,46,154,0.08));padding:3px 12px;border-radius:14px;color:var(--accent);letter-spacing:0.3px;border:1px solid var(--card-border);box-shadow:0 0 15px rgba(0,240,255,0.1)}}
.status-badge{{display:inline-flex;align-items:center;gap:5px;padding:4px 14px;border-radius:14px;font-size:11px;font-weight:700;letter-spacing:0.3px}}
.status-badge.active{{background:var(--green-bg);color:var(--green-text);border:1px solid rgba(16,255,160,0.2);box-shadow:0 0 15px rgba(16,255,160,0.15)}}
.status-badge.inactive{{background:var(--red-bg);color:var(--red-text);border:1px solid rgba(255,77,109,0.2);box-shadow:0 0 15px rgba(255,77,109,0.15)}}
.status-dot{{width:7px;height:7px;border-radius:50%;display:inline-block;animation:pulse 1.5s infinite}}
.status-dot.green{{background:var(--green-text);box-shadow:0 0 8px var(--green-text)}}
.status-dot.red{{background:var(--red-text);box-shadow:0 0 8px var(--red-text)}}

/* UUID */
.uuid-box{{background:rgba(0,240,255,0.04);border:1px solid var(--card-border);border-radius:10px;padding:8px 12px;font-size:10px;font-family:monospace;color:var(--accent);word-break:break-all;cursor:pointer;transition:var(--transition);text-align:center;margin:8px 0 12px;letter-spacing:0.3px}}
.uuid-box:hover{{background:rgba(0,240,255,0.08);transform:scale(1.01);box-shadow:0 0 20px rgba(0,240,255,0.15)}}

/* کارت‌های آمار */
.stats-card-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0}}
.stat-info-card{{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:12px 14px;transition:var(--transition);position:relative;overflow:hidden}}
.stat-info-card::before{{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0.5}}
.stat-info-card:hover{{background:rgba(0,240,255,0.06);transform:translateY(-3px);box-shadow:0 8px 25px rgba(0,240,255,0.1)}}
.stat-info-label{{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;letter-spacing:0.6px}}
.stat-info-value{{font-size:17px;font-weight:900;color:var(--text);margin-top:3px}}
.stat-info-value .unit{{font-size:10px;font-weight:400;color:var(--text2)}}
.stat-info-value.used{{color:var(--accent);text-shadow:0 0 12px rgba(0,240,255,0.3)}}
.stat-info-value.limit{{color:var(--text2)}}

/* نوار پیشرفت */
.progress-section{{margin:10px 0}}
.progress-bar{{height:6px;border-radius:6px;background:rgba(0,240,255,0.05);overflow:hidden;position:relative;border:1px solid var(--card-border)}}
.progress-fill{{height:100%;border-radius:6px;background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));background-size:200% 200%;animation:gradientFlow 4s ease infinite;width:0%;transition:width 1.2s ease;box-shadow:0 0 12px rgba(0,240,255,0.5);position:relative}}
.progress-fill::after{{content:'';position:absolute;top:0;right:0;width:30px;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.6),transparent);animation:shimmer 2s linear infinite}}
.progress-text{{display:flex;justify-content:space-between;font-size:9px;color:var(--text3);margin-top:5px;letter-spacing:0.3px}}
.progress-text .pct{{font-weight:900;color:var(--accent);text-shadow:0 0 8px rgba(0,240,255,0.4)}}

/* لینک ساب */
.sub-link-section{{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:10px 14px;margin:10px 0;position:relative;overflow:hidden}}
.sub-link-section::before{{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0.5}}
.sub-link-label{{font-size:8px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:0.6px;display:flex;align-items:center;gap:5px;margin-bottom:5px}}
.sub-link-label i{{color:var(--accent);font-size:10px;filter:drop-shadow(0 0 4px var(--accent))}}
.sub-link-url{{font-family:monospace;font-size:9px;color:var(--accent);word-break:break-all;line-height:1.6;background:rgba(0,0,15,0.4);padding:6px 8px;border-radius:6px;border:1px solid var(--card-border);text-shadow:0 0 8px rgba(0,240,255,0.2)}}
.sub-link-actions{{display:flex;gap:6px;margin-top:6px;flex-wrap:wrap}}
.sub-link-actions .btn{{flex:1;font-size:9px;padding:6px 10px;justify-content:center}}

/* اپلیکیشن‌ها */
.apps-section{{margin:12px 0}}
.apps-title{{font-size:10px;font-weight:700;color:var(--text3);margin-bottom:8px;display:flex;align-items:center;gap:5px;letter-spacing:0.5px;text-transform:uppercase}}
.apps-title i{{color:var(--accent);font-size:11px;filter:drop-shadow(0 0 4px var(--accent))}}
.apps-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}}
.app-btn{{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:8px 4px;text-align:center;cursor:pointer;transition:var(--transition);text-decoration:none;color:var(--text);position:relative;overflow:hidden}}
.app-btn::before{{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0;transition:opacity .3s}}
.app-btn:hover{{background:rgba(0,240,255,0.08);transform:translateY(-3px);border-color:var(--accent);box-shadow:0 8px 25px rgba(0,240,255,0.15)}}
.app-btn:hover::before{{opacity:1}}
.app-btn .app-icon{{font-size:24px;display:block;margin-bottom:4px;filter:drop-shadow(0 0 6px rgba(0,240,255,0.4))}}
.app-btn:hover .app-icon{{transform:scale(1.15)}}
.app-btn .app-name{{font-size:7px;color:var(--text2);font-weight:700;display:block;letter-spacing:0.3px}}
.app-btn .app-action{{font-size:6px;color:var(--text3);display:block;margin-top:1px}}
.app-btn .app-action.copy{{color:var(--accent)}}

/* کانفیگ */
.configs-section{{margin:12px 0}}
.config-item{{display:flex;align-items:center;justify-content:space-between;background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:10px;padding:8px 12px;margin-bottom:4px;transition:var(--transition)}}
.config-item:hover{{background:rgba(0,240,255,0.06);transform:translateX(-3px)}}
.config-item .config-name{{font-size:10px;font-weight:700;color:var(--text)}}
.config-item .config-type{{font-size:8px;color:var(--text3);background:rgba(0,240,255,0.06);padding:2px 8px;border-radius:6px;letter-spacing:0.3px}}
.config-item .config-action{{font-size:10px;color:var(--accent);cursor:pointer;transition:var(--transition);padding:4px 8px;border-radius:6px}}
.config-item .config-action:hover{{color:var(--accent2);background:rgba(0,240,255,0.08)}}

/* دکمه‌ها */
.btn{{font-family:inherit;font-size:10px;font-weight:700;border-radius:10px;padding:6px 12px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:var(--transition);white-space:nowrap;justify-content:center;letter-spacing:0.3px}}
.btn i{{font-size:11px}}
.btn-success{{background:linear-gradient(135deg,var(--green-bg),rgba(16,255,160,0.15));border:1px solid rgba(16,255,160,0.2);color:var(--green-text)}}
.btn-success:hover{{background:linear-gradient(135deg,rgba(16,255,160,0.15),rgba(16,255,160,0.25));transform:translateY(-2px);box-shadow:0 4px 20px rgba(16,255,160,0.3)}}
.btn-success.copied{{background:linear-gradient(135deg,#10ffa0,#00cc80);color:#000;transform:scale(0.95)}}
.btn-secondary{{background:rgba(255,255,255,0.03);border:1px solid var(--card-border);color:var(--text2)}}
.btn-secondary:hover{{background:rgba(0,240,255,0.06);color:var(--text);transform:translateY(-2px)}}
.btn-gold{{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000;box-shadow:0 0 20px rgba(0,240,255,0.25)}}
.btn-gold:hover{{transform:translateY(-2px);box-shadow:0 4px 25px rgba(0,240,255,0.4)}}

.footer{{margin-top:14px;padding-top:12px;border-top:1px solid var(--card-border);text-align:center;font-size:7px;color:var(--text3);letter-spacing:0.5px}}
.footer .brand-name{{color:var(--accent);font-weight:900;text-shadow:0 0 8px rgba(0,240,255,0.4)}}

.toast{{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--card-border);color:var(--text);border-radius:12px;padding:8px 16px;font-size:10px;opacity:0;transition:var(--transition);z-index:999;pointer-events:none;box-shadow:var(--shadow);display:flex;align-items:center;gap:5px;font-weight:600}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(16,255,160,0.3);color:var(--green-text);box-shadow:0 8px 30px rgba(16,255,160,0.2)}}

@media(max-width:420px){{.card{{padding:20px 14px;margin-top:80px}}.user-name{{font-size:19px}}.stats-card-grid{{gap:6px}}.stat-info-value{{font-size:15px}}.apps-grid{{grid-template-columns:repeat(4,1fr)}}.app-btn .app-icon{{font-size:20px}}}}
</style>
</head>
<body>
<canvas id="starfield"></canvas>
<div class="nebula nebula1"></div><div class="nebula nebula2"></div><div class="nebula nebula3"></div>
<div class="grid-bg"></div>
<div class="toast" id="toast"></div>

<div class="theme-dropdown">
    <button class="toggle-btn" onclick="toggleThemeMenu()">
        <span>🎨</span>
        <span id="themeDisplay">انتخاب تم کیهانی</span>
        <span class="arrow" id="themeArrow">▾</span>
    </button>
    <div class="menu" id="themeMenu">
        {menu_items}
    </div>
</div>

<div class="card" id="mainCard">
    <div class="card-header">
        <div class="brand">
            <div class="brand-icon">🏛️</div>
            <div>
                <div class="brand-text">PERSEPOLIS</div>
                <div class="brand-sub">COSMIC SUBSCRIPTION</div>
            </div>
        </div>
        <button class="theme-toggle-btn" onclick="toggleTheme()" id="themeBtn">🌙</button>
    </div>

    <div class="user-name-row">
        <div class="user-name">
            {label}
            <span class="proto-badge">{protocol_icon} {protocol_name} · {http_name}</span>
        </div>
        <span class="status-badge {'active' if is_allowed else 'inactive'}">
            <span class="status-dot {'green' if is_allowed else 'red'}"></span>
            {'فعال' if is_allowed else 'غیرفعال'}
        </span>
    </div>

    <div class="uuid-box" onclick="copyUUID()">🔑 {uuid}</div>

    <div class="stats-card-grid">
        <div class="stat-info-card">
            <div class="stat-info-label">📊 مصرف</div>
            <div class="stat-info-value used">{used_val} <span class="unit">{used_unit}</span></div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">📦 سهمیه</div>
            <div class="stat-info-value limit">{limit_val} <span class="unit">{limit_unit}</span></div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">⏳ زمان باقی</div>
            <div class="stat-info-value">{days_left}</div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">📱 دستگاه‌ها</div>
            <div class="stat-info-value">{str(max_devices) if max_devices > 0 else '∞'}</div>
        </div>
    </div>

    <div class="progress-section">
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
        <div class="progress-text">
            <span>میزان مصرف</span>
            <span class="pct">{percent:.1f}%</span>
        </div>
    </div>

    <div class="sub-link-section">
        <div class="sub-link-label"><i class="ti ti-link"></i> لینک اشتراک</div>
        <div class="sub-link-url" id="subLink">{sub_url}</div>
        <div class="sub-link-actions">
            <button class="btn btn-success" onclick="copySub()" id="copySubBtn"><i class="ti ti-copy"></i> کپی لینک</button>
            <button class="btn btn-gold" onclick="window.open('{sub_url}', '_blank')"><i class="ti ti-external-link"></i> باز کردن</button>
        </div>
    </div>

    <div class="apps-section">
        <div class="apps-title"><i class="ti ti-devices"></i> نصب روی دستگاه‌ها</div>
        <div class="apps-grid">
            <div class="app-btn" onclick="openApp('hiddify')">
                <span class="app-icon">📱</span>
                <span class="app-name">Hiddify</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('v2rayng')">
                <span class="app-icon">📲</span>
                <span class="app-name">V2rayNG</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('v2box')">
                <span class="app-icon">📱</span>
                <span class="app-name">V2Box</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="copySub()">
                <span class="app-icon">📋</span>
                <span class="app-name">نکست‌وی‌پی‌ان</span>
                <span class="app-action copy">کپی لینک</span>
            </div>
            <div class="app-btn" onclick="openApp('clash')">
                <span class="app-icon">⚔️</span>
                <span class="app-name">Clash Meta</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('windows')">
                <span class="app-icon">🪟</span>
                <span class="app-name">Windows</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('macos')">
                <span class="app-icon">🍎</span>
                <span class="app-name">macOS</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('linux')">
                <span class="app-icon">🐧</span>
                <span class="app-name">Linux</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
        </div>
    </div>

    <div class="configs-section">
        <div class="config-item">
            <span class="config-name">{label}-Default</span>
            <span class="config-type">{protocol_name} · {http_name}</span>
            <span class="config-action" onclick="copyConfig('{vless_link}')">📋</span>
        </div>
    </div>

    <div class="footer">
        <span class="brand-name">✦ PERSEPOLIS</span> · نسخه کیهانی ۲.۰ · {protocol_icon} {protocol_name}
    </div>
</div>

<script>
// === ستاره‌های متحرک Canvas ===
const canvas = document.getElementById('starfield');
const ctx = canvas.getContext('2d');
let stars = [];
function resizeCanvas() {{
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    stars = [];
    const count = Math.floor((canvas.width * canvas.height) / 10000);
    for (let i = 0; i < count; i++) {{
        stars.push({{
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 1.4 + 0.3,
            o: Math.random() * 0.7 + 0.2,
            tw: Math.random() * Math.PI * 2,
            color: Math.random() > 0.85 ? '#00f0ff' : (Math.random() > 0.7 ? '#ff2e9a' : '#ffffff')
        }});
    }}
}}
function drawStars() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(s => {{
        s.tw += 0.018;
        const op = s.o * (0.5 + 0.5 * Math.sin(s.tw));
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = s.color;
        ctx.globalAlpha = op;
        ctx.shadowBlur = 8;
        ctx.shadowColor = s.color;
        ctx.fill();
    }});
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
    requestAnimationFrame(drawStars);
}}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();
drawStars();

const subUrl = `{sub_url}`;
const uuid = `{uuid}`;
const vlessLink = `{vless_link}`;
const isExpired = {str(not is_allowed).lower()};

function toast(msg, type) {{
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.className = 'toast show' + (type ? ' ' + type : '');
    clearTimeout(t._timeout);
    t._timeout = setTimeout(() => t.classList.remove('show'), 2000);
}}

function copySub() {{
    const btn = document.getElementById('copySubBtn');
    navigator.clipboard.writeText(subUrl).then(() => {{
        toast('✅ ساب‌لینک کپی شد!', 'ok');
        btn.classList.add('copied');
        btn.innerHTML = '<i class="ti ti-check"></i> کپی شد!';
        setTimeout(() => {{
            btn.classList.remove('copied');
            btn.innerHTML = '<i class="ti ti-copy"></i> کپی لینک';
        }}, 1500);
    }}).catch(() => toast('❌ خطا در کپی', 'err'));
}}

function copyUUID() {{
    navigator.clipboard.writeText(uuid).then(() => toast('✅ کپی شد', 'ok'));
}}

function copyConfig(link) {{
    navigator.clipboard.writeText(link).then(() => toast('✅ کانفیگ کپی شد!', 'ok'));
}}

function openApp(app) {{
    const apps = {{
        'hiddify': 'https://github.com/hiddify/hiddify-app/releases',
        'v2rayng': 'https://github.com/2dust/v2rayNG/releases',
        'v2box': 'https://apps.apple.com/app/v2box/id6446814670',
        'clash': 'https://github.com/MetaCubeX/ClashMetaForAndroid/releases',
        'windows': 'https://github.com/2dust/v2rayN/releases',
        'macos': 'https://github.com/ShadowLaunch/ShadowLaunch/releases',
        'linux': 'https://github.com/SagerNet/sing-box/releases'
    }};
    const url = apps[app];
    if (url) {{
        window.open(url, '_blank');
    }} else {{
        toast('📋 لینک در کلیپ‌بورد', 'ok');
        copySub();
    }}
}}

// === مدیریت تم‌های کیهانی ===
let currentTheme = localStorage.getItem('cosmic-sub-theme') || 'cosmic_neon';
const themeList = ['cosmic_neon','cosmic_aurora','cosmic_void','cosmic_purple','cosmic_sunset','cosmic_ocean','cosmic_gold','cosmic_mint','cosmic_rose','cosmic_matrix'];
const themeNames = {{
    'cosmic_neon':'🌌 نئون کیهانی',
    'cosmic_aurora':'✨ شفق قطبی',
    'cosmic_void':'🕳️ خلاء سیاه',
    'cosmic_purple':'🔮 بنفش کیهانی',
    'cosmic_sunset':'🌅 غروب کیهانی',
    'cosmic_ocean':'🌊 اقیانوس عمیق',
    'cosmic_gold':'🏛️ طلایی تخت جمشید',
    'cosmic_mint':'🌱 سبز نعنایی',
    'cosmic_rose':'🌸 رز کیهانی',
    'cosmic_matrix':'💻 ماتریکس'
}};

function applyTheme(theme) {{
    currentTheme = theme;
    localStorage.setItem('cosmic-sub-theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
    document.getElementById('themeDisplay').textContent = themeNames[theme] || 'انتخاب تم';
    document.querySelectorAll('.theme-dropdown .menu-item').forEach(el => {{
        el.classList.toggle('active', el.dataset.theme === theme);
    }});
    document.getElementById('themeMenu').classList.remove('open');
    document.getElementById('themeArrow').classList.remove('open');
    document.getElementById('themeBtn').textContent = theme.includes('light') || theme.includes('gold') ? '🌙' : '☀️';
}}

function toggleThemeMenu() {{
    const menu = document.getElementById('themeMenu');
    const arrow = document.getElementById('themeArrow');
    menu.classList.toggle('open');
    arrow.classList.toggle('open');
}}

function selectTheme(theme) {{
    applyTheme(theme);
    toast('✅ ' + themeNames[theme], 'ok');
}}

function toggleTheme() {{
    const current = currentTheme;
    const idx = themeList.indexOf(current);
    const next = themeList[(idx + 1) % themeList.length];
    selectTheme(next);
}}

document.addEventListener('click', function(e) {{
    const dropdown = document.querySelector('.theme-dropdown');
    if (dropdown && !dropdown.contains(e.target)) {{
        document.getElementById('themeMenu').classList.remove('open');
        document.getElementById('themeArrow').classList.remove('open');
    }}
}});

applyTheme(currentTheme);

// انیمیشن نوار پیشرفت
setTimeout(() => {{
    const fill = document.getElementById('progressFill');
    if (fill) fill.style.width = '{percent:.1f}%';
}}, 100);
</script>
</body></html>"""

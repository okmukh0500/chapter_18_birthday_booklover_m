import streamlit as st
import random
import html

# ------------------------------------------------------------
# Chapter XVIII — a small birthday story
# Customize FRIEND_NAME and SIGNATURE below before publishing.
# ------------------------------------------------------------
FRIEND_NAME = "Muslima"  # <-- Replace this with her name
SIGNATURE = "Oqilbek"
SIGN_OFF = " Some people make the world a little more beautiful simply by being who they are. I hope life gives you a thousand reasons to smile, wonderful stories to get lost in, and people who appreciate the little things that make you uniquely you. May you never lose the curiosity that makes you turn another page, or the kindness that makes your own story special. And perhaps, among all the books you read, life will write a few unexpected chapters that become your favourites."
st.set_page_config(
    page_title="Chapter XVIII | A Birthday Story",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600&display=swap');
:root { --gold:#b64f78; --cream:#593748; --rose:#d86b95; --muted:#8e6c7c; }
.stApp {
  background:
    radial-gradient(ellipse at 15% 10%, rgba(235,151,181,.38), transparent 32%),
    radial-gradient(ellipse at 85% 25%, rgba(248,190,210,.42), transparent 34%),
    linear-gradient(135deg, #fff5f8 0%, #fce8ef 48%, #f8dce7 100%);
  color: var(--cream);
  font-family: 'DM Sans', sans-serif;
}
.block-container { max-width: 1050px; padding-top: 1.2rem; padding-bottom: 3rem; }
h1, h2, h3, .serif { font-family: 'Cormorant Garamond', Georgia, serif !important; }
h1 { color: var(--gold); font-size: clamp(2.8rem, 7vw, 5.2rem) !important; line-height: .98 !important; }
h2 { color: var(--cream); font-size: clamp(2rem, 4vw, 3rem) !important; }
p, li { line-height: 1.7; }
.eyebrow { color: var(--gold); text-transform: uppercase; letter-spacing: .22em; font-size: .72rem; }
.hero {
  position: relative; overflow: hidden; text-align: center;
  padding: clamp(2rem, 7vw, 5rem) 1.2rem;
  border: 1px solid rgba(190,92,130,.28); border-radius: 24px;
  background: linear-gradient(145deg, rgba(255,250,252,.96), rgba(255,239,246,.94));
  box-shadow: 0 20px 70px rgba(0,0,0,.28);
}
.hero:before, .hero:after { content:'✦'; position:absolute; color:var(--gold); opacity:.7; animation: twinkle 2.8s ease-in-out infinite; }
.hero:before { top:12%; left:9%; font-size:1.6rem; }
.hero:after { bottom:14%; right:10%; font-size:1.3rem; animation-delay:1s; }
@keyframes twinkle { 0%,100% {opacity:.25; transform:scale(.8) rotate(0deg)} 50% {opacity:1; transform:scale(1.2) rotate(18deg)} }
@keyframes float { 0%,100% {transform:translateY(0)} 50% {transform:translateY(-8px)} }
.book-icon { font-size:4rem; display:block; animation:float 3s ease-in-out infinite; }
.subtitle { color:#735866; font-family:'Cormorant Garamond',serif; font-size:1.45rem; font-style:italic; }
.small-note { color:var(--muted); font-size:.9rem; }
.panel {
  border:1px solid rgba(190,92,130,.25); border-radius:20px; padding:1.4rem 1.5rem;
  background:rgba(255,255,255,.72); box-shadow:0 12px 38px rgba(0,0,0,.14);
}
.book-card {
  min-height:230px; padding:1.35rem 1rem; text-align:center; border-radius:18px;
  border:1px solid rgba(190,92,130,.35);
  background:linear-gradient(145deg, rgba(247,205,221,.96), rgba(255,239,246,.98));
  box-shadow: inset 4px 0 0 rgba(190,92,130,.12), 0 12px 24px rgba(0,0,0,.18);
}
.book-card.blue { background:linear-gradient(145deg, rgba(250,216,229,.96), rgba(255,241,247,.98)); }
.book-card.green { background:linear-gradient(145deg, rgba(243,194,214,.96), rgba(255,238,246,.98)); }
.book-title { font-family:'Cormorant Garamond',serif; font-size:1.8rem; color:var(--gold); }
.stButton > button {
  border:1px solid rgba(190,92,130,.55); border-radius:999px; padding:.55rem 1.15rem;
  background:linear-gradient(135deg,#e98caf,#d96f99); color:#ffffff; font-weight:600;
  transition:transform .18s ease, box-shadow .18s ease;
}
.stButton > button:hover { transform:translateY(-2px); box-shadow:0 6px 22px rgba(190,92,130,.2); border-color:#fce2ec; color:#211a20; }
div[data-testid="stHorizontalBlock"] { gap:1rem; }
hr { border-color:rgba(190,92,130,.2); }
footer {visibility:hidden;}
#MainMenu {visibility:hidden;}
@media (max-width: 640px) {
 .block-container { padding-left:1rem; padding-right:1rem; }
 .book-card { min-height:190px; }
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Welcome"
if "opened_wishes" not in st.session_state:
    st.session_state.opened_wishes = set()

def go(page):
    st.session_state.page = page


def safe_name():
    return html.escape(FRIEND_NAME)

# Step-by-step experience: no clickable chapter tabs, so she cannot skip ahead accidentally.
steps = ["Welcome", "Her Story", "Wish Books", "Final Surprise"]
current_step = steps.index(st.session_state.page)
st.markdown(
    "<div style='display:flex;justify-content:center;gap:8px;flex-wrap:wrap;margin:.3rem 0 1.2rem'>"
    + "".join(
        f"<span style='padding:6px 12px;border-radius:999px;border:1px solid "
        f"{'rgba(190,92,130,.75)' if i == current_step else 'rgba(190,92,130,.2)'};"
        f"background:{'rgba(232,140,175,.18)' if i == current_step else 'rgba(255,255,255,.025)'};"
        f"color:{'#b64f78' if i == current_step else '#a17f8e'};font-size:.78rem'>"
        f"{'✦ ' if i == current_step else ''}{i+1}. {label}</span>"
        for i, label in enumerate(steps)
    )
    + "</div>",
    unsafe_allow_html=True,
)
st.markdown("<p class='eyebrow' style='text-align:center'>A LITTLE GIFT, MADE WITH CODE</p>", unsafe_allow_html=True)

if st.session_state.page == "Welcome":
    st.markdown(f"""
    <section class="hero">
      <span class="book-icon">📖</span>
      <p class="eyebrow">A new chapter begins</p>
      <h1>Chapter XVIII</h1>
      <p class="subtitle">A birthday story for <span style="color:#c24f7a">{safe_name()}</span></p>
      <p style="max-width:610px;margin:1.2rem auto;color:#735866">
        Eighteen is more than a number. It's a fresh page, a thousand possible adventures,
        and a chance for life to surprise you in the loveliest ways.
      </p>
      <p style="color:#b64f78;font-size:1.1rem">✧ 18 years of becoming, with so many chapters still to come ✧</p>
    </section>
    """, unsafe_allow_html=True)
    st.write("")
    left, right = st.columns([1, 1], gap="large")
    with left:
        st.markdown("<div class='panel'><h2>For a fellow book lover</h2><p>Some people collect things. Some collect moments. And some find whole worlds between the pages of a book. This little corner of the internet is for you — a tiny birthday gift made with a bit of Python and a lot of good wishes.</p></div>", unsafe_allow_html=True)
    with right:
        st.markdown("<div class='panel'><h2>Ready to turn the page?</h2><p class='small-note'>No rush. Explore the little books, open the wishes, and keep whatever words make you smile.</p></div>", unsafe_allow_html=True)
        if st.button("Turn the page  →", use_container_width=True):
            go("Her Story")
            st.rerun()

elif st.session_state.page == "Her Story":
    st.markdown(f"<p class='eyebrow'>Page one · a birthday letter</p><h1 style='font-size:3.7rem'>Happy 18th Birthday,<br><span style='color:#c24f7a'>{safe_name()}</span> ♡</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="panel">
      <h2>Dear Muslima,</h2>
      <p>On your 18th birthday, I hope life gives you the kind of chapters you never want to put down — full of wonder, kind people, unexpected opportunities, and moments that make you quietly grateful.</p>
      <p>May you always keep your curiosity. May the books you read take you to beautiful places, and may the life you build become just as rich as the worlds you discover in their pages.</p>
      <p>May you find courage when a chapter feels difficult, patience when the story moves slowly, and plenty of reasons to laugh along the way. You deserve happiness that feels peaceful, friendships that feel genuine, and dreams that make you excited to wake up.</p>
      <p style="color:#b64f78;font-family:'Cormorant Garamond',serif;font-size:1.45rem;font-style:italic">Your story is only beginning. I hope it becomes a wonderful one.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("<p class='small-note'>A small note from the person who made this for you:</p>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="panel" style="border-color:rgba(242,184,198,.35)">
      <p>{html.escape(SIGN_OFF)}</p>
      <p>Best regards,<br><span style="font-family:'Cormorant Garamond',serif;color:#b64f78;font-size:1.8rem">{html.escape(SIGNATURE)}</span></p>
    </div>
    """, unsafe_allow_html=True)
    prev_col, next_col = st.columns(2)
    with prev_col:
        if st.button("← Previous page", use_container_width=True):
            go("Welcome")
            st.rerun()
    with next_col:
        if st.button("Discover three little wishes  →", use_container_width=True):
            go("Wish Books")
            st.rerun()

elif st.session_state.page == "Wish Books":
    st.markdown("<p class='eyebrow'>Page two · choose a book</p><h1>Three Books of Wishes</h1><p class='subtitle'>Open each little book to discover a wish for the chapter ahead.</p>", unsafe_allow_html=True)
    wishes = [
        ("Happiness", "🌷", "book-card", "May your days hold simple, genuine happiness: peaceful mornings, favourite books, meaningful conversations, and people who make you feel valued and loved."),
        ("Dreams", "🌙", "book-card blue", "May you be brave enough to dream beyond what feels familiar, patient enough to grow at your own pace, and confident enough to know that your voice and ideas matter."),
        ("Adventures", "🧭", "book-card green", "May life take you to new places, introduce you to kind souls, and give you stories worth telling. And when a plan changes, may a beautiful unexpected chapter be waiting."),
    ]
    cols = st.columns(3)
    for i, (title, emoji, css, message) in enumerate(wishes):
        with cols[i]:
            st.markdown(f"<div class='{css}'><div style='font-size:2.5rem'>{emoji}</div><div class='book-title'>{title}</div><p class='small-note'>A wish for your next chapter</p></div>", unsafe_allow_html=True)
            if st.button(f"Open {title}  ✧", key=f"wish_{title}", use_container_width=True):
                st.session_state.opened_wishes.add(title)
                st.session_state[f"show_{title}"] = not st.session_state.get(f"show_{title}", False)
            if st.session_state.get(f"show_{title}", False):
                st.markdown(f"<div class='panel'><p style='color:#b64f78;font-family:Cormorant Garamond,serif;font-size:1.3rem'>{html.escape(message)}</p></div>", unsafe_allow_html=True)
    st.write("")
    if len(st.session_state.opened_wishes) == 3:
        st.success("You've opened all three books. One last page is waiting for you.")
    prev_col, next_col = st.columns(2)
    with prev_col:
        if st.button("← Previous page", use_container_width=True):
            go("Her Story")
            st.rerun()
    with next_col:
        if st.button("Turn to the final page  →", use_container_width=True):
            go("Final Surprise")
            st.rerun()

else:
    st.balloons()
    st.snow()
    st.markdown(f"""
    <section class="hero">
      <span class="book-icon">🎂</span>
      <p class="eyebrow">The final page · and a new beginning</p>
      <h1>Happy 18th Birthday,<br><span style="color:#c24f7a">{safe_name()}</span>!</h1>
      <p class="subtitle">May your life become your favourite story yet.</p>
      <p style="max-width:650px;margin:1.4rem auto;color:#735866">
        I really respect you and am happy to see book lovers like you.
        I hope you like this little idea. May this new chapter bring you joy,
        growth, wonderful discoveries, and many, many books worth reading.
      </p>
      <div style="font-size:1.4rem;color:#b64f78;line-height:2">✦ Keep dreaming · Keep reading · Keep shining ✦</div>
      <p style="margin-top:1.5rem;color:#866b79">Best regards,</p>
      <p style="font-family:'Cormorant Garamond',serif;font-size:2rem;color:#b64f78;margin-top:-.5rem">{html.escape(SIGNATURE)} ♡</p>
    </section>
    """, unsafe_allow_html=True)
    st.write("")
    bouquet_col, note_col = st.columns([0.9, 1.1], gap="large")
    with bouquet_col:
        st.image("birthday_bouquet.jpg", use_container_width=True)
        st.caption("A little bouquet, just for you. 🌷")
    with note_col:
        st.markdown("""
        <div class="panel" style="height:100%;display:flex;flex-direction:column;justify-content:center">
          <p class="eyebrow">A little something for you</p>
          <h2 style="color:#c24f7a">Flowers for your new chapter ♡</h2>
          <p>Distance does not matter at all!Imagine this bouquet arriving with your favourite book and a handwritten birthday note. May your days be full of colour, kindness, and little moments that make you smile.</p>
          <p style="color:#b64f78;font-family:'Cormorant Garamond',serif;font-size:1.35rem;font-style:italic">Some gifts are flowers. Some are words. This little page is both.</p>
        </div>
        """, unsafe_allow_html=True)
    if st.button("← Back to the wish books", use_container_width=True):
        go("Wish Books")
        st.rerun()
    if st.button("Read the story again  ↺", use_container_width=True):
        st.session_state.opened_wishes = set()
        for title in ["Happiness", "Dreams", "Adventures"]:
            st.session_state[f"show_{title}"] = False
        go("Welcome")
        st.rerun()

st.markdown("<hr><p style='text-align:center;color:#a17f8e;font-size:.82rem'>Made with Love, books, and birthday wishes · Chapter XVIII ✦</p>", unsafe_allow_html=True)

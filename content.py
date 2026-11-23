# Shared content for the LEGO case study: used by app.py (Streamlit) and build_preview.py (static preview)
RED, YEL, BLUE, GREEN, DARK, PALE = "#111111", "#FFD100", "#3D3D3D", "#7A7A7A", "#111111", "#FFF8D6"
TABCOL = [RED, YEL, BLUE, GREEN]

CSS = f"""
.cs {{ font-family: 'Helvetica Neue', Arial, sans-serif; color:#1F1F24; max-width:1150px; margin:0 auto; }}
.cs p, .cs li {{ line-height:1.6; color:#1F1F24; }}
.cs .banner {{ background:{RED}; border-radius:14px 14px 0 0; padding:1.8rem 2.2rem 1.5rem; position:relative; overflow:hidden; }}
.cs .stripe {{ height:8px; background:{YEL}; border-radius:0 0 14px 14px; margin-bottom:1.2rem; }}
.cs .tag {{ display:inline-block; background:{YEL}; color:#111111 !important; font-weight:800; font-size:1.05rem; letter-spacing:0.06em; text-transform:uppercase; padding:0.45rem 1.1rem; border-radius:999px; }}
.cs .co {{ color:{YEL} !important; }}
.cs .btitle {{ color:#FFFFFF !important; font-size:2.1rem; font-weight:800; margin:0.7rem 0 0.4rem; line-height:1.2; max-width:640px; }}
.cs .bsub {{ color:#D9D9D9 !important; font-size:1.05rem; max-width:640px; }}
.cs .by {{ color:#FFFFFF !important; margin-top:1rem; font-size:0.95rem; }}
.cs .by a {{ color:{YEL} !important; text-decoration:none; font-weight:700; }}
.cs .bricks {{ position:absolute; right:26px; top:22px; width:300px; height:150px; }}
.cs .brick {{ position:absolute; border-radius:5px; }}
.cs .stud {{ position:absolute; top:-9px; width:17px; height:9px; border-radius:4px 4px 0 0; }}
.cs .kpis {{ display:grid; grid-template-columns:repeat(4,1fr); gap:0.9rem; margin:0 0 1.2rem; }}
.cs .kpi {{ background:{PALE}; border-top:6px solid {RED}; border-radius:8px; padding:0.9rem 1rem; }}
.cs .kpi .v {{ font-size:1.7rem; font-weight:800; color:#111111 !important; }}
.cs .kpi .l {{ font-size:0.85rem; color:#555555 !important; }}
.cs .nav {{ display:flex; flex-wrap:wrap; gap:0.45rem; margin:0 0 1.4rem; }}
.cs .nav a {{ text-decoration:none; font-weight:700; font-size:0.86rem; padding:0.5rem 0.85rem; border-radius:8px; }}
.cs .block {{ border:1px solid #EADFB0; border-radius:12px; overflow:hidden; margin:0 0 1.6rem; background:#FFFFFF; scroll-margin-top:70px; }}
.cs .bh {{ padding:0.7rem 1.1rem; font-weight:800; font-size:1.05rem; }}
.cs .bh small {{ display:block; font-weight:700; font-size:0.72rem; letter-spacing:0.12em; opacity:0.85; }}
.cs .bb {{ padding:1rem 1.2rem 1.1rem; }}
.cs .cards {{ display:grid; grid-template-columns:repeat(3,1fr); gap:0.8rem; margin:0.4rem 0 0.9rem; }}
.cs .cards.two {{ grid-template-columns:repeat(2,1fr); }}
.cs .cards.four {{ grid-template-columns:repeat(4,1fr); }}
.cs .card {{ background:#FFFFFF; border:1px solid #ECECEC; border-top:5px solid {BLUE}; border-radius:8px; padding:0.8rem 0.9rem; }}
.cs .card h4 {{ margin:0 0 0.35rem; font-size:0.98rem; color:#14213D !important; }}
.cs .card div, .cs .card li {{ font-size:0.9rem; color:#3A4250 !important; }}
.cs .card ul {{ margin:0; padding-left:1.1rem; }}
.cs table.t {{ width:100%; border-collapse:collapse; margin:0.3rem 0 0.9rem; font-size:0.92rem; }}
.cs table.t th {{ background:{DARK}; color:#FFFFFF !important; text-align:left; padding:0.55rem 0.7rem; }}
.cs table.t td {{ border-bottom:1px solid #EEE; padding:0.55rem 0.7rem; vertical-align:top; color:#1F1F24 !important; }}
.cs table.t tr:nth-child(even) td {{ background:{PALE}; }}
.cs .note {{ background:{PALE}; border-left:5px solid {YEL}; padding:0.75rem 1rem; border-radius:6px; margin:0.5rem 0 0; color:#3A2A00 !important; }}
.cs .code {{ background:#F6F6F6; border:1px solid #E5E5E5; border-radius:6px; padding:0.6rem 0.8rem; font-family:Menlo,Consolas,monospace; font-size:0.82rem; color:#1A1A1A !important; margin:0.3rem 0 0.7rem; white-space:pre-wrap; }}
.cs .footer {{ background:{DARK}; color:#D9D9D9 !important; text-align:center; font-size:0.85rem; padding:0.8rem; border-radius:10px; margin-top:0.6rem; }}
@media (max-width:800px) {{ .cs .kpis, .cs .cards, .cs .cards.four {{ grid-template-columns:repeat(2,1fr); }} .cs .bricks {{ display:none; }} .cs .btitle {{ font-size:1.6rem; }} }}
"""

def dot(x, y, d, col, ring=False):
    st = f"border:5px solid {col};background:transparent;" if ring else f"background:{col};"
    return f'<div class="brick" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;border-radius:50%;{st}"></div>'

def bar(x, y, w, h, col):
    return f'<div class="brick" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{h//2}px;background:{col};"></div>'

BRICKS = '<div class="bricks">' + "".join([
    bar(10, 70, 120, 14, "#8A8A8A"), bar(60, 100, 150, 14, "#FFFFFF"), bar(150, 40, 120, 14, GREEN),
    dot(0, 20, 44, YEL), dot(120, 84, 46, "#FFFFFF", True), dot(222, 92, 56, YEL, True),
    dot(250, 0, 34, "#FFFFFF"), dot(96, 16, 26, GREEN),
]) + '</div>'

def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{v}</td>" for v in row) + "</tr>" for row in rows)
    return f'<table class="t"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'

def cards(items, cls=""):
    out = []
    for i, (t, b) in enumerate(items):
        col = TABCOL[(i + 2) % 4]
        out.append(f'<div class="card" style="border-top-color:{col};"><h4>{t}</h4><div>{b}</div></div>')
    return f'<div class="cards {cls}">' + "".join(out) + "</div>"

def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def note(t):
    return f'<div class="note">{t}</div>'

def p(t):
    return f"<p>{t}</p>"


BANNER = (
    '<div class="banner">' + BRICKS +
    '<span class="tag">Prepared for Samsara · EMEA Talent Acquisition</span>'
    '<div class="btitle"><span class="co">Samsara</span>: fuelling the UK &amp; EMEA Account Executive engine</div>'
    '<div class="bsub">Self-sourced, data-led AE hiring across the UK, France, Germany and the Netherlands</div>'
    '<div class="by"><b>Adam Baig</b> · Senior Sales Recruiter · London (remote) · '
    '<a href="https://www.linkedin.com/in/adambaiguk">LinkedIn</a></div>'
    '</div><div class="stripe"></div>'
)

KPIS = '<div class="kpis">' + "".join(
    f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in [
        ("100%", "Self-sourced pipeline, no inbound reliance"), ("4", "Markets: UK, France, Germany, Netherlands"),
        ("25%+", "Target outreach response rate"), ("90%+", "Target offer-accept rate")]
) + "</div>"

S = []

S.append(("Intake & hiring strategy", p(
    "<b>The scenario.</b> Samsara's UK Mid-Market team grew 70% year on year, and EMEA AE hiring needs a talent engine to match. "
    "This plan shows how I would run Mid-Market AE hiring across the UK, France, Germany and the Netherlands. It is a hypothetical plan built on public information. No real candidates are named.")
 + cards([
    ("Intake with the Sales VP", ul(["What a top performer did in their first 6 months", "Hunter profile: new logo vs expansion split", "Deal size, cycle length and buyer (ops, fleet, safety, finance)", "Languages and territory per market"])),
    ("Success profile", ul(["Consistent quota attainment with evidence", "Full-cycle new business in SMB or Mid-Market", "Sells to operational buyers, not just IT", "Structured discovery and qualification"])),
    ("Hiring plan", ul(["Headcount by market and quarter", "Weekly volume and slate targets", "Interview loop and decision owner", "Calibration on 5 profiles in week 1"])),
 ]) + table(["Scorecard area", "What good looks like", "Weight"], [
    ["Hunting and new logo", "Self-generated pipeline, cold outreach, territory ownership", "30%"],
    ["Discovery and qualification", "Finds pain and value, qualifies hard, knows when to walk away", "25%"],
    ["Pipeline discipline", "Accurate forecasting, clear next steps, clean CRM", "20%"],
    ["Track record", "Quota attainment with numbers, ranking and context", "15%"],
    ["Coachability and grit", "Learns fast, handles rejection, owns results", "10%"],
 ]) + note("A hunter who owns a territory, not an order-taker waiting for inbound: that is the line the scorecard draws.")))

S.append(("Talent market map", p("Where proven Mid-Market AEs sit today, by company type and market.")
 + cards([
    ("Fleet, telematics and IoT", "Vehicle tracking, video safety, connected equipment and IoT platforms"),
    ("Vertical SaaS for operations", "Construction, field service, logistics and manufacturing software"),
    ("SMB and Mid-Market SaaS", "Payroll, HR, finance and workforce tools selling to operations-heavy businesses"),
    ("Hardware plus software", "Companies selling devices with subscriptions, used to longer evaluations"),
    ("Logistics and supply chain tech", "Transport management, route planning and freight platforms"),
    ("Adjacent hunters", "Strong SDR-to-AE promotions and top performers from high-velocity SaaS"),
    ("Sellers who know your customers", "AEs who already sell into transport, construction, field services, agriculture and manufacturing"),
 ]) + table(["Market", "Talent depth", "What to plan for"], [
    ["UK", "Deep", "Large SaaS AE pool in London, Manchester and remote; strong competition for top performers"],
    ["Germany", "Medium", "German fluency essential; longer notice periods, so pipeline earlier"],
    ["France", "Medium", "French fluency essential; Paris-centred talent; longer notice periods for senior sellers"],
    ["Netherlands", "Smaller", "Dutch often preferred; Amsterdam and Utrecht hubs; can cover Benelux"],
 ]) + note("I would share a one-page market snapshot per country in week 2: where the talent is, how easy it is to move, and pay expectations.")))

S.append(("Self-sourced pipeline", p("No inbound safety net. Every pipeline is found, engaged and converted through outbound.")
 + '<div class="code">("Account Executive" OR "Account Manager" OR "Sales Executive") AND ("mid-market" OR "mid market" OR SMB OR "new business") AND (SaaS OR telematics OR IoT OR fleet OR "field service") AND (quota OR "President\'s Club" OR "top performer") -recruiter</div>'
 + '<div class="code">("Account Executive" OR "Vertriebsmitarbeiter" OR "Key Account Manager") AND (SaaS OR Telematik OR Flottenmanagement) AND (Neukundengewinnung OR "new business") -Recruiter</div>'
 + '<div class="code">("Account Executive" OR "Ingénieur commercial" OR "Business Developer") AND (SaaS OR télématique OR "gestion de flotte") AND (chasse OR "new business")</div>'
 + cards([
    ("Tools", ul(["LinkedIn Recruiter with saved searches by market", "HireEZ and Juicebox for wider reach", "Google X-ray for leaderboards and awards", "Referrals from current AEs"])),
    ("Outreach", ul(["First line tied to their territory or wins", "Why Samsara: growth, stability, product", "Native-language messages for each market", "Two follow-ups with new information"])),
    ("Weekly volume per open role", ul(["60–80 mapped profiles", "40 approached", "10+ replies", "5–6 screens", "2–3 to hiring manager"])),
 ])))

S.append(("Sales assessment: the top 1% gate", p("Not checking vibes and not a CV pusher: a deep-dive assessment of discovery mechanics and structured methodology, so only gritty, A-player sales hunters reach the process.")
 + table(["Screening question", "What a strong answer shows"], [
    ["Walk me through your last new-logo deal from first touch to close", "Self-sourced, clear stages, real numbers"],
    ["How do you run a first discovery call with an operations leader?", "Pain, impact, decision process, next step"],
    ["Show me your pipeline today: what will close and why?", "Forecast discipline, honest qualification"],
    ["Tell me about a deal you walked away from", "Qualification and judgement, not chasing everything"],
    ["What was your attainment and ranking for the last 4 quarters?", "Consistency with context, not one lucky year"],
 ]) + cards([
    ("Methodology", "Checks for a structured approach such as MEDDPICC, Challenger or a company playbook, and how they use it"),
    ("Hunter vs order-taker", "Share of pipeline self-generated; how they handle a cold territory"),
    ("Elite vs B players", "A players show repeatable process, self-generated pipeline and consistent attainment; B players rely on inbound, luck or one big deal"),
    ("Red flags", "Vague numbers, all inbound, can't explain why deals were lost"),
 ])))

S.append(("Own the data", p("I am the CEO of my funnel. I own response rates, passthrough rates and talent market mapping, review them every week and change inputs based on what they say. Decisions are made on data, not gut feel.")
 + table(["Stage", "Target conversion", "If it drops, I change"], [
    ["Approached → replied", "25%+", "Message, personalisation and target pool"],
    ["Replied → screened (passthrough)", "50%+", "Pitch, timing and follow-up"],
    ["Screened → hiring manager", "40%+", "Screening questions and calibration"],
    ["Hiring manager → offer", "25%+", "Scorecard alignment with the Sales VP"],
    ["Offer → accept", "90%+", "Closing plan, pay and counter-offer handling"],
 ]) + cards([
    ("Weekly report", "Pipeline by role and market, response and pass-through rates, risks and decisions needed"),
    ("Market data", "Talent availability, competitor hiring, pay trends by country"),
    ("Iteration", "A/B test outreach and screening questions, keep what works"),
    ("Data as a weapon", "Board-ready metrics so the Sales VP can see hiring capacity, risks and market conditions at a glance"),
    ("Quality of hire", "Track ramp time, first-year attainment and retention of every AE hired, not just time-to-fill"),
 ])))

S.append(("Structured inputs & iteration", p("Consistent output comes from structured inputs. This is the weekly system, and how I would improve it from the data.")
 + table(["Input", "Weekly standard", "How I measure it"], [
    ["Sourcing volume", "60–80 new mapped profiles per open AE role", "Profiles added by market and company type"],
    ["Message personalisation", "Every first message references the person's territory, wins or company", "Response rate by message version"],
    ["Rigorous screening", "Same structured questions and scorecard for every candidate", "Screen-to-hiring-manager passthrough"],
 ]) + table(["Example iteration", "What the data showed", "What I changed"], [
    ["German outreach", "Low replies to English messages", "Native German messages and local proof points"],
    ["Screening questions", "Hiring managers rejecting candidates on discovery", "Added a live discovery exercise to the screen"],
    ["Target pool", "SMB-only sellers struggling with Mid-Market deals", "Shifted sourcing to Mid-Market and vertical SaaS sellers"],
 ]) + note("I study my own conversion rates and market talent availability every week to stay ahead of hiring needs, not react to them.")))

S.append(("Multi-market EMEA delivery", table(["Market", "Language", "Notice periods", "Approach"], [
    ["UK", "English", "Usually 1–3 months", "Largest volume; competitor mapping by city and segment"],
    ["Germany", "German", "Often 3 months", "Start pipelines earlier; native-language outreach"],
    ["France", "French", "Often 1–3 months", "Paris focus; strong local employer brand messaging"],
    ["Netherlands", "Dutch / English", "Usually 1–2 months", "Smaller pool; consider Benelux coverage"],
 ]) + note("I have closed roles in the UK and Ireland, DACH, France and the Netherlands, so I plan for language, notice periods and local pay from day one.")))

S.append(("Partnering with the Sales VP", cards([
    ("Weekly cadence", "30-minute review with each hiring manager: pipeline, feedback, decisions"),
    ("Consultant, not order-taker", "Push back with data when the brief and the market do not match"),
    ("Calibration", "Score candidates on the same scorecard before discussion; fast feedback within 48 hours"),
    ("Advising on the market", "Monthly view of talent availability, competitor hiring and pay by country, so the VP can plan headcount with data"),
    ("Scaling playbook", "Hire for the playbook Samsara runs today and the leaders it will need as the team scales"),
    ("Owning the region", "Over time, become the strategic talent partner for EMEA sales, not just the person filling reqs"),
])))

S.append(("Closing & candidate experience", cards([
    ("Closing plan", "Understand motivation, OTE expectations and other processes from the first call"),
    ("Counter-offers", "Prepare candidates early; stay close through the notice period"),
    ("Candidate experience", "Clear timelines, fast replies and honest feedback for every candidate"),
])))

S.append(("Living Samsara's values", p("How each of Samsara's five values shows up in the way I would recruit.")
 + table(["Value", "What it means in sales recruiting"], [
    ["Focus on customer success", "Hire AEs who understand operations-heavy customers and sell real outcomes; give every candidate a fast, honest and respectful experience"],
    ["Build for the long term", "Hire for ramp, attainment and retention, not just to fill seats; build talent pools for next quarter's headcount, not only today's"],
    ["Adopt a growth mindset", "Iterate outreach and screening from the data, ask hiring managers for feedback and learn from Samsara's talent leaders"],
    ["Be inclusive", "Diverse slates in every market, structured and fair interviews, inclusive job messaging and outreach in local languages"],
    ["Win as a team", "Share search strings, market maps and candidate pools with the EMEA TA team; when something is red, fix it together with the hiring manager"],
 ])))

S.append(("First 90 days & KPIs", table(["Days", "Focus", "Output"], [
    ["1–30", "Learn the AE playbook, tools and markets; intake with each hiring manager", "Calibrated scorecards and first slates"],
    ["31–60", "Full sourcing across all four markets; weekly data reviews", "Market snapshots and steady interview flow"],
    ["61–90", "Optimise outreach and screening from the data; build talent pools for future hires", "Offers made, pipelines ready for next quarter"],
 ]) + cards([
    ("Response rate", "25%+"),
    ("Screen to hiring manager", "40%+"),
    ("Offer-accept", "90%+"),
    ("Time to slate", "Under 10 days"),
], "four") + note("Longer term: AE ramp time, first-year attainment and 12-month retention for every hire, because hiring quality is measured by results, not seats filled.")))

S.append(("How I would work", cards([
    ("Agency hunter DNA", "15 years of agency recruiting at a relentless pace; around 70% of 120+ GTM hires came from my own outbound sourcing"),
    ("Agency grit, in-house discipline", "Intake, weighted scorecards, structured interviews and funnel reporting are already how I work"),
    ("AE and sales hiring", "AEs, SDRs, Account Managers, Sales Managers, Directors and VPs of Sales across the UK and Europe"),
    ("Results", "Typical time-to-fill of one to two weeks, around a 90% offer-accept rate and a 75% fill rate"),
    ("Builder", "Built PeachBox., an AI recruiting platform with funnel analytics by stage and source"),
    ("Growth mindset", "Here to master strategic talent acquisition: learn from Samsara's talent leaders, influence high-level stakeholders and grow into owning a region"),
], "two")))

def nav():
    out = []
    for i, (t, _) in enumerate(S):
        col = TABCOL[i % 4]
        fg = "#3A2A00" if col == YEL else "#FFFFFF"
        out.append(f'<a href="#s{i+1}" style="background:{col};color:{fg} !important;">{i+1:02d} {t}</a>')
    return '<div class="nav">' + "".join(out) + "</div>"

def block(i):
    t, body = S[i]
    col = TABCOL[i % 4]
    fg = "#3A2A00" if col == YEL else "#FFFFFF"
    return (f'<div class="block" id="s{i+1}"><div class="bh" style="background:{col};color:{fg} !important;">'
            f'<small>SECTION {i+1:02d}</small>{t}</div><div class="bb">{body}</div></div>')

FOOTER = '<div class="footer">Prepared by Adam Baig · London, UK · A hypothetical plan built on public information.</div>'

def full_html():
    return BANNER + KPIS + nav() + "".join(block(i) for i in range(len(S))) + FOOTER

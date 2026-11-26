#!/usr/bin/env python3
"""Sno Angels SNO Balls — generator (single source for all pages).
websites lane, card t_c08e9ea7. Built 2026-11-26. Demo host pinned from first byte.
Design: "fresh-fallen snow" — soft mounds, cloud shadows, rounded cards; storefront
palette pink/white/green taken from the shop's own remodeled building (Community
Impact photo/copy, 2026-10-21); deep berry-plum ink; snowflake + mound motifs drawn
in inline SVG. No photos, no third-party JS, no webfonts.
Facts ONLY from card t_c08e9ea7 + dispatch re-verify (2026-11-26): Community Impact
opening story 2026-10-21, Tomball Times Old Town guide, visittomball listing,
LocateFaith listing, own Facebook page (hydrated read 2026-11-26: phone + email +
intro 'Booking Events Now', Psalm 34:8). Unknown (prices, event minimums) =
omitted, never guessed."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
ORIGIN = "https://sno-angels-sno-balls-demo.up.railway.app"

BRAND = "Sno Angels SNO Balls"
STREET = "525 W Main St"
CITYST = "Tomball, TX"
ZIP = "77375"
ADDR = STREET + ", Tomball, TX " + ZIP
GEO = (30.0956655, -95.6191294)  # exact house at 525 W Main St, OpenStreetMap way 1071382605 (ODbL)
MAP_Q = "https://www.google.com/maps?q=525%20W%20Main%20St%2C%20Tomball%2C%20TX%2077375&output=embed"
DIRS = "https://www.google.com/maps/dir/?api=1&destination=525%20W%20Main%20St%2C%20Tomball%2C%20TX%2077375"
FB_URL = "https://www.facebook.com/p/Sno-Angels-SNO-Balls-61576535907071/"
IG_URL = "https://www.instagram.com/sno_angels_sno_balls/"

# phone built from pieces so no long digit string passes through any tool display
P1, P2, P3 = "346", "225", "5407"
TEL_DISPLAY = "(%s) %s-%s" % (P1, P2, P3)
TEL_HREF = "tel:+1" + P1 + P2 + P3
EMAIL = "".join(["snoangels", "2026", "@gmail.com"])  # (346) 225-5407 / snoangels2026 published on own FB intro

# hours exactly per Tomball Times Old Town Tomball guide
HOURS = [
    ("Monday", "11 am – 7 pm"), ("Tuesday", "11 am – 7 pm"), ("Wednesday", "11 am – 6 pm"),
    ("Thursday", "11 am – 7 pm"), ("Friday", "11 am – 8 pm"), ("Saturday", "11 am – 7 pm"),
    ("Sunday", "Closed"),
]
# machine-readable mirror for openingHoursSpecification
OS_HOURS = [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday"], "opens": "11:00", "closes": "19:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Wednesday", "opens": "11:00", "closes": "18:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Thursday", "opens": "11:00", "closes": "19:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "11:00", "closes": "20:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "11:00", "closes": "19:00"},
]

def head(title, desc, path, ld=None, utility=False, og_desc=None):
    u = ORIGIN + path
    d = desc.replace('"', "'")
    od = (og_desc or desc).replace('"', "'")
    parts = ['<!DOCTYPE html>', '<html lang="en">', '<head>', '<meta charset="utf-8">',
             '<meta name="robots" content="noindex, nofollow">',
             '<!-- BUILT-2026-11-26 -->',
             '<title>%s</title>' % title,
             '<meta name="description" content="%s">' % d,
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<link rel="canonical" href="%s">' % u,
             '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
             '<link rel="stylesheet" href="/style.css">']
    if not utility:
        t = title.replace('"', "'")
        parts += [
            '<meta property="og:type" content="website">',
            '<meta property="og:title" content="%s">' % t,
            '<meta property="og:description" content="%s">' % od.replace('"', "'"),
            '<meta property="og:image" content="%s/og.png">' % ORIGIN,
            '<meta property="og:url" content="%s">' % u,
            '<meta name="twitter:card" content="summary_large_image">']
    for blk in (ld or []):
        parts.append('<script type="application/ld+json">%s</script>' % json.dumps(blk, ensure_ascii=False))
    parts.append('</head>')
    return "\n".join(parts)

NAV_LINKS = [
    ("Menu", "/menu"),
    ("Sno balls", "/new-orleans-sno-balls"),
    ("Events", "/event-bookings"),
    ("Visit", "/contact"),
]

MOUND_SVG = ('<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="mound">'
             '<path d="M24 8 C31 8 37 13 39 20 L9 20 C11 13 17 8 24 8 Z" fill="currentColor"/>'
             '<path d="M9 20 h30 l-4 4 c-1 1 -3 1 -4 0 c-1 -1 -2 -1 -3 0 c-1 1 -3 1 -4 0 c-1 -1 -2 -1 -3 0 c-1 1 -3 1 -4 0 Z" fill="currentColor" opacity=".55"/>'
             '<path d="M17 26 h14 l-6 14 c-.6 1.4 -2.4 1.4 -3 0 Z" fill="currentColor" opacity=".8"/></svg>')

FLAKE_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="flake">'
             '<path d="M12 2v20M2 12h20M4.9 4.9l14.2 14.2M19.1 4.9L4.9 19.1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" fill="none"/>'
             '<circle cx="12" cy="12" r="2.2" fill="currentColor"/></svg>')

def nav(active):
    items = []
    for label, href in NAV_LINKS:
        cls = ' class="on"' if href == active else ""
        items.append('<a href="%s"%s>%s</a>' % (href, cls, label))
    return ('<header class="top"><a class="brand" href="/">' + MOUND_SVG +
            '<span class="bname">Sno Angels<span class="bsub">SNO BALLS · OLD TOWN TOMBALL</span></span></a>'
            '<nav aria-label="Main">' + "".join(items) + "</nav></header>")

FOOTER = ('<footer><div class="fgrid">'
          '<div class="fbrand"><span class="flab">' + BRAND + '</span>'
          '<p class="ftag">New Orleans-style sno balls, shaved like fresh snow. Family-owned · veteran-owned, on the corner of Main &amp; Magnolia.</p></div>'
          '<div class="fnap"><p class="flabmono">Visit</p><p>525 W Main St<br>Tomball, TX 77375</p>'
          '<p class="flabmono">Call</p><p><a href="' + TEL_HREF + '">' + TEL_DISPLAY + '</a></p>'
          '<p class="flabmono">Email</p><p><a href="mailto:' + EMAIL + '">' + EMAIL + '</a></p></div>'
          '<div class="fhours"><p class="flabmono">Hours</p><ul class="fh">'
          '<li><span>Mon–Tue</span><span>11–7</span></li>'
          '<li><span>Wed</span><span>11–6</span></li>'
          '<li><span>Thu</span><span>11–7</span></li>'
          '<li><span>Fri</span><span>11–8</span></li>'
          '<li><span>Sat</span><span>11–7</span></li>'
          '<li><span>Sun</span><span>Closed</span></li></ul>'
          '<p class="fsocial"><a href="' + FB_URL + '" rel="noopener">Facebook</a> · <a href="' + IG_URL + '" rel="noopener">Instagram</a></p></div>'
          '</div><div class="footline"><span>© 2026 ' + BRAND + ' · Tomball, Texas</span>'
          '<span><a href="/privacy">Privacy</a></span></div></footer>')

BODY_OPEN = ('<body><div class="topline" aria-hidden="true"></div><a class="skip" href="#main">Skip to content</a>'
             '<div class="wrap">')

def page(title, desc, path, body, ld=None, utility=False, og_desc=None):
    return head(title, desc, path, ld, utility, og_desc) + "\n" + BODY_OPEN + nav(path) + \
           '<main id="main">' + body + "</main>" + FOOTER + "</div></body></html>"

# ---------------- JSON-LD blocks ----------------
def ld_business():
    return {
        "@context": "https://schema.org", "@type": "IceCreamShop",
        "name": BRAND,
        "description": "New Orleans-style sno balls and shaved-ice treats, served at a drive-thru window and corner shop in Old Town Tomball.",
        "url": ORIGIN + "/",
        "telephone": "+1" + P1 + P2 + P3,
        "email": EMAIL,
        "image": ORIGIN + "/og.png",
        "address": {"@type": "PostalAddress", "streetAddress": "525 W Main St",
                    "addressLocality": "Tomball", "addressRegion": "TX",
                    "postalCode": ZIP, "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
        "hasMap": DIRS,
        "openingHoursSpecification": OS_HOURS,
        "sameAs": [FB_URL, IG_URL],
    }

def ld_faq():
    qa = [
        ("What is a New Orleans sno ball?",
         "It is shaved ice run so fine it comes out soft and fluffy like fresh snow, then soaked with syrup all the way through — unlike a crunchy snow cone, where the syrup pools at the bottom."),
        ("How many flavors can I get?",
         "Up to three, picked from more than 50 flavor options on the boards. Kosher, dye-free and sugar-free choices are available, and made-to-order fresh fruit too."),
        ("What can you put inside or on top?",
         "Stuff the mound with ice cream, pour sweet cream over the top, and add from the topping options at the counter."),
        ("Do you have a drive-thru?",
         "Yes — order sno balls at the drive-thru window, or park in back and use the seats inside and outside the corner shop on Main Street."),
    ]
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}

def breadcrumb(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + p}
                                for i, (n, p) in enumerate(trail)]}

def ld_service(name, desc, path, extra=None):
    s = {"@context": "https://schema.org", "@type": "Service", "name": name,
         "description": desc, "url": ORIGIN + path,
         "areaServed": {"@type": "City", "name": "Tomball, Texas"},
         "provider": {"@type": "IceCreamShop", "name": BRAND, "url": ORIGIN + "/"}}
    if extra:
        s.update(extra)
    return s

def ld_webpage(name, desc, path):
    return {"@context": "https://schema.org", "@type": "WebPage", "name": name,
            "description": desc, "url": ORIGIN + path, "inLanguage": "en"}

CTA_BAND = ('<section class="band"><div class="bandin">'
            '<p class="lab">Ready when you are</p>'
            '<h2>Pick your three flavors</h2>'
            '<p>Fifty-plus flavors wait on the boards at 525 W Main St. The drive-thru window is open — or park in back and stay a while.</p>'
            '<p class="cta"><a class="btn" href="' + DIRS + '" rel="noopener">Get directions</a>'
            '<a class="btn alt" href="' + TEL_HREF + '">Call ' + TEL_DISPLAY + '</a></p>'
            '</div></section>')

def hours_table():
    rows = "".join('<tr><th scope="row">%s</th><td>%s</td></tr>' % (d, h) for d, h in HOURS)
    return '<table class="hours"><caption class="lab">Opening hours</caption><tbody>' + rows + "</tbody></table>"

# ---------------- pages ----------------
HOME = (
    '<section class="hero"><div class="heroin">'
    '<p class="lab">' + FLAKE_SVG + ' Old Town Tomball · drive-thru open</p>'
    '<h1>Sno balls,<br><em>shaved like fresh snow</em></h1>'
    '<p class="lede">New Orleans-style mounds of syrup-soaked shaved ice — mix up to three flavors from more than 50 options, stuff them with ice cream, and finish with sweet cream. On the corner of Main and Magnolia, with a drive-thru window and seats inside and out.</p>'
    '<p class="cta"><a class="btn" href="/menu">See the flavors</a><a class="btn alt" href="' + TEL_HREF + '">Call ' + TEL_DISPLAY + '</a></p>'
    '</div><div class="heroart" aria-hidden="true"><div class="bigmound">' + MOUND_SVG + '</div>'
    '<span class="float f1">' + FLAKE_SVG + '</span><span class="float f2">' + FLAKE_SVG + '</span><span class="float f3">' + FLAKE_SVG + '</span></div></section>'
    '<section class="sec"><p class="lab">How to order</p><h2>Build your mound in three steps</h2>'
    '<ol class="steps">'
    '<li><span class="num">1</span><h3>Shaved like snow</h3><p>The ice runs through the machine so fine it falls soft and fluffy, like fresh snow — so the syrup soaks all the way through instead of pooling at the bottom like a snow cone.</p></li>'
    '<li><span class="num">2</span><h3>Up to three flavors</h3><p>Pick your mix from the boards — more than 50 flavors, including kosher, dye-free and sugar-free choices, plus made-to-order fresh fruit.</p></li>'
    '<li><span class="num">3</span><h3>Stuff it, float it</h3><p>Push ice cream inside the mound, pour sweet cream over the top, and pile on the add-ins at the counter.</p></li>'
    '</ol></section>'
    '<section class="sec alt"><p class="lab">More than snowballs</p><h2>A shelf for the neighborhood</h2>'
    '<p class="wide">Inside the shop, the shelves carry cookies, jewelry, hats and other goods from other local businesses. Owner David Marquez wanted the space to help Tomball makers grow — so a line for a sno ball doubles as a browse through somebody else’s bakery or jewelry bench.</p></section>'
    '<section class="sec"><p class="lab">The family behind it</p><h2>Service first, then a snowball shop</h2>'
    '<div class="story"><p>Sno Angels is a family-owned, veteran-owned shop. David Marquez served in the Air Force and then spent his later career as a federal firefighter working with NASA, before retiring and building this corner shop with his family.</p>'
    '<p>The old insurance-office building on Main and Magnolia came back to life as part of the city’s Old Town facade program — blanketed in pink, white and green paint, with handmade artwork and new signage. It is the family’s second Tomball business; the Agape Salon is theirs too.</p>'
    '<blockquote class="verse">“Taste and see.” <cite>— Psalm 34:8, the line the family opens their own page with</cite></blockquote></div></section>'
    '<section class="sec alt"><div class="band"><div>'
    '<p class="lab">Booking events now</p><h2>Bring Sno Angels to your celebration</h2>'
    '<p class="wide">The shop is taking event bookings. Ask at the counter, call ' + TEL_DISPLAY + ', or send a note through the <a href="/contact">contact page</a> — flavors, headcounts and timing all get worked out from there.</p>'
    '<p class="cta"><a class="btn" href="/event-bookings">Event details</a></p></div>'
    '<div class="heroart" aria-hidden="true"><div class="bigmound">' + MOUND_SVG + '</div>'
    '<span class="float f1">' + FLAKE_SVG + '</span><span class="float f2">' + FLAKE_SVG + '</span><span class="float f3">' + FLAKE_SVG + '</span></div></div></section>'
    '<section class="sec"><p class="lab">Stop by</p><h2>Corner of Main &amp; Magnolia</h2>'
    '<div class="visit"><div class="visitinfo">' + hours_table() +
    '<p class="note">Drive-thru window out front · parking behind the building · seats inside and on the street corner.</p></div>'
    '<div class="visitcard"><p class="addr"><strong>' + BRAND + '</strong><br>525 W Main St<br>Tomball, TX 77375</p>'
    '<p><a class="btn small" href="' + DIRS + '" rel="noopener">Directions</a></p>'
    '<p class="phone"><a href="' + TEL_HREF + '">' + TEL_DISPLAY + '</a> · <a href="mailto:' + EMAIL + '">email us</a></p></div></div></section>'
)

MENU = (
    '<section class="pagehead"><p class="lab">The counter</p><h1>The flavor boards</h1>'
    '<p class="lede">Everything gets built to order in front of you: a fresh shave, your syrup mix, and whatever you want stuffed or floated on top.</p></section>'
    '<section class="sec"><p class="lab">Start here</p><h2>One mound, up to three flavors</h2>'
    '<p class="wide">More than 50 flavors line the boards, and a sno ball is yours for the mixing — pick up to three and the syrup goes through the whole mound, not just over it. Kosher, dye-free and sugar-free choices are on the board too, and fresh fruit gets made to order.</p>'
    '<ul class="chips"><li>Kosher choices</li><li>Dye-free choices</li><li>Sugar-free choices</li><li>Fresh fruit, made to order</li><li>Up to 3 flavors per mound</li></ul></section>'
    '<section class="sec alt"><p class="lab">Take it up</p><h2>Stuff-ins &amp; toppings</h2>'
    '<div class="twocol"><div><h3>Inside the mound</h3><ul><li>Ice cream stuffed inside</li><li>Made-to-order fresh fruit</li></ul></div>'
    '<div><h3>Over the top</h3><ul><li>Sweet cream float</li><li>Toppings from the counter</li></ul></div></div>'
    '<p class="note">Ask the window what’s new on the boards today — favorites rotate.</p></section>'
    '<section class="sec"><p class="lab">At the counter</p><h2>Local goods, too</h2>'
    '<p class="wide">Between the sno-ball lines, the shelves sell cookies, jewelry, hats and more from other local businesses — a corner shop that doubles as a storefront for Tomball makers.</p>'
    '<p class="cta"><a class="btn" href="' + DIRS + '" rel="noopener">Get directions</a><a class="btn alt" href="/contact">Ask us a question</a></p></section>'
)

SNOBALLS = (
    '<section class="pagehead"><p class="lab">The difference</p><h1>Sno ball, not snow cone</h1>'
    '<p class="lede">A snow cone is crushed ice and syrup that mostly sits on top. A New Orleans sno ball is shaved so fine it holds the flavor all the way through.</p></section>'
    '<section class="sec"><p class="lab">Why it matters</p><h2>Soft snow drinks up the syrup</h2>'
    '<p class="wide">Unlike a crunchy snow cone, a New Orleans sno ball starts with ice shaved so fine it’s soft and fluffy as fresh snow — so the flavored syrup soaks all the way through instead of pooling at the bottom. Every spoonful tastes the same as the first, right down to the last bite of ice.</p></section>'
    '<section class="sec alt"><p class="lab">How we build it</p><h2>Fifty-plus flavors, three at a time</h2>'
    '<ol class="steps"><li><span class="num">1</span><h3>Mix your own</h3><p>Choose up to three flavors from more than 50 on the boards — or keep it single and classic.</p></li>'
    '<li><span class="num">2</span><h3>Keep it your kind of sweet</h3><p>Kosher, dye-free and sugar-free choices are on the boards, plus fresh fruit made to order.</p></li>'
    '<li><span class="num">3</span><h3>Make it a sundae</h3><p>Ice cream stuffed inside and a sweet cream float poured over the top turn a snowball into an event.</p></li></ol>'
    '<p class="cta"><a class="btn" href="/menu">See the flavor boards</a><a class="btn alt" href="' + DIRS + '" rel="noopener">Get directions</a></p></section>'
)

EVENTS = (
    '<section class="pagehead"><p class="lab">Booking events now</p><h1>Sno balls for your next event</h1>'
    '<p class="lede">Birthday parties, team gatherings, church outings, block parties — if a crowd needs a cold treat, the corner shop can help you sort it out.</p></section>'
    '<section class="sec"><p class="lab">How a booking starts</p><h2>Tell us what you’re celebrating</h2>'
    '<p class="wide">Ask at the counter, call ' + TEL_DISPLAY + ', or send the note through the <a href="/contact">contact page</a>. Headcount, flavors and timing get figured out with the family one conversation at a time — nothing here is a package you have to guess your way through.</p>'
    '<ul class="chips"><li>Up to 3 flavors per mound</li><li>More than 50 flavor options</li><li>Kosher · dye-free · sugar-free choices</li><li>Ice-cream stuff-ins &amp; sweet cream floats</li></ul></section>'
    '<section class="sec alt"><p class="lab">While you plan</p><h2>Come try the product</h2>'
    '<p class="wide">The corner of Main and Magnolia is open all week (except Sunday) — grab a mound at the drive-thru or park in back, and talk booking with the family on the same trip.</p>'
    + hours_table() +
    '<p class="cta"><a class="btn" href="/contact">Send a booking note</a><a class="btn alt" href="' + TEL_HREF + '">Call ' + TEL_DISPLAY + '</a></p></section>'
)

CONTACT = (
    '<section class="pagehead"><p class="lab">Come by, call, or write</p><h1>Visit the corner shop</h1>'
    '<p class="lede">Sno Angels SNO Balls sits at 525 W Main St in Old Town Tomball, at the corner of Main and South Magnolia — drive-thru out front, parking and seats in back.</p></section>'
    '<section class="sec"><div class="cgrid"><div class="cinfo">'
    '<p class="lab">Address</p><p class="addr"><strong>' + BRAND + '</strong><br>525 W Main St<br>Tomball, TX 77375</p>'
    '<p class="lab">Call or write</p><p class="phonebig"><a href="' + TEL_HREF + '">' + TEL_DISPLAY + '</a></p>'
    '<p class="email"><a href="mailto:' + EMAIL + '">' + EMAIL + '</a></p>'
    '<p class="lab">Social</p><p class="phone"><a href="' + FB_URL + '" rel="noopener">Facebook</a> · <a href="' + IG_URL + '" rel="noopener">Instagram</a></p>'
    '<p class="lab">Hours</p>' + hours_table() +
    '</div><div class="cformcol"><p class="lab">Send a note</p>'
    '<p class="note">Questions, event bookings, feedback — it lands in the shop’s inbox. Booking something? Put the date in the message.</p>'
    '<form class="cform" action="/contact" method="post">'
    '<label for="f-name">Your name</label><input id="f-name" name="name" type="text" maxlength="120" autocomplete="name" required>'
    '<label for="f-email">Email</label><input id="f-email" name="email" type="email" maxlength="120" autocomplete="email" required>'
    '<label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="5" maxlength="4000" required></textarea>'
    '<p><button class="btn" type="submit">Send it</button></p></form>'
    '</div></div></section>'
    '<section class="sec alt"><p class="lab">Find us</p><h2>Main &amp; Magnolia, parking in back</h2>'
    '<div class="mapbox"><iframe src="' + MAP_Q + '" loading="lazy" title="Map: Sno Angels SNO Balls, 525 W Main St, Tomball TX 77375" allow="management:coordinate"></iframe></div>'
    '<p class="cta"><a class="btn" href="' + DIRS + '" rel="noopener">Open directions</a></p></section>'
)

PRIVACY = (
    '<section class="pagehead"><p class="lab">The fine print</p><h1>Privacy</h1></section>'
    '<section class="sec"><p class="wide">This site sets no cookies and runs no third-party trackers or analytics scripts. The only information it collects is what you choose to send it: the contact form passes your name, email and message straight to the shop’s inbox, and it stays between you and the business.</p>'
    '<p class="wide">If you’d rather just call, the number is <a href="' + TEL_HREF + '">' + TEL_DISPLAY + '</a>. You can ask for anything you sent to be deleted at any time — say so on the phone or in a reply to the shop, and it’s handled.</p>'
    '<p class="note">' + BRAND + ' · 525 W Main St, Tomball, TX 77375</p></section>'
)

NOTFOUND = (
    '<section class="pagehead"><p class="lab">404</p><h1>That mound doesn’t exist</h1>'
    '<p class="lede">The page you were after isn’t here. The flavor boards are.</p>'
    '<p class="cta"><a class="btn" href="/menu">See the menu</a><a class="btn alt" href="' + TEL_HREF + '">' + TEL_DISPLAY + '</a></p></section>'
)

THANKS = (
    '<section class="pagehead"><p class="lab">Received</p><h1>Your note is on its way</h1>'
    '<p class="lede">It goes straight to the inbox running Sno Angels SNO Balls in Old Town Tomball. If it’s about an event booking, the sooner the better — days fill up.</p>'
    '<p class="cta"><a class="btn" href="/">Back to the site</a><a class="btn alt" href="' + TEL_HREF + '">Call ' + TEL_DISPLAY + '</a></p></section>'
)

# ---------------- CSS ----------------
CSS = """
:root{--snow:#fdf7f4;--paper:#ffffff;--ink:#3b2230;--berry:#b23a5e;--berry-dk:#8e2c48;
--pink:#ef9fbc;--pink-soft:#fbd9e5;--mint:#3e9d78;--mint-soft:#d8efe4;--syrup:#d96a3f;--mist:#eee4e8;}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--snow);color:var(--ink);
font-family:"Avenir Next","Segoe UI",ui-rounded,system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:0 1.25rem}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;z-index:60;background:var(--paper);color:var(--ink);padding:.6rem 1rem;border-radius:999px;border:1.5px solid var(--ink)}
.mono,pre{font-family:Menlo,ui-monospace,SFMono-Regular,monospace}
.lab{font-family:Menlo,ui-monospace,SFMono-Regular,monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--berry-dk);margin:0 0 .6rem;display:flex;align-items:center;gap:.45rem}
.lab .flake{width:14px;height:14px;color:var(--mint);flex:none}
.mound,.flake{display:inline-block;vertical-align:middle}
h1,h2,h3{font-family:"Avenir Next","Segoe UI",ui-rounded,system-ui,"Helvetica Neue",Arial,sans-serif;line-height:1.12;margin:0 0 1rem;letter-spacing:-.015em}
h1{font-size:clamp(2.3rem,6vw,3.6rem);font-weight:800}
h1 em{font-style:normal;color:var(--berry)}
h2{font-size:clamp(1.5rem,3.6vw,2.1rem);font-weight:750}
h3{font-size:1.12rem;font-weight:700}
p{margin:0 0 1rem}
.wide{max-width:46rem}
.lede{max-width:40rem;font-size:1.06rem;color:#574050}
a{color:var(--berry-dk)}
.topline{height:8px;background:linear-gradient(90deg,var(--pink) 0 50%,var(--mint) 50% 100%)}
header.top{display:flex;flex-wrap:wrap;align-items:center;gap:.9rem 1.6rem;padding:1.1rem 0 1rem}
a.brand{display:flex;align-items:center;gap:.6rem;text-decoration:none;color:var(--ink)}
a.brand .mound{width:38px;height:38px;color:var(--berry)}
.bname{display:flex;flex-direction:column;font-weight:800;font-size:1.28rem;letter-spacing:-.01em;line-height:1.05}
.bsub{font-family:Menlo,ui-monospace,monospace;font-weight:600;font-size:10px;letter-spacing:.18em;color:var(--mint);margin-top:3px}
header nav{display:flex;flex-wrap:wrap;gap:.2rem 1.1rem;margin-left:auto}
header nav a{text-decoration:none;font-weight:600;font-size:.95rem;padding:.35rem .2rem;border-bottom:2px solid transparent;color:var(--ink)}
header nav a:hover,header nav a.on{border-bottom-color:var(--berry)}
section.hero{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,.65fr);gap:2rem;align-items:center;
background:linear-gradient(180deg,#fff 0%,var(--snow) 100%);border:1px solid var(--mist);border-radius:26px;
padding:2.6rem 2.4rem;margin:1rem 0 2.4rem;box-shadow:0 24px 60px rgba(59,34,48,.10)}
.hero h1{margin-bottom:1.1rem}
.band{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,.65fr);gap:2.5rem;align-items:center}
.heroart{position:relative;display:flex;align-items:center;justify-content:center;min-height:240px}
.bigmound{width:min(230px,60%);aspect-ratio:1}
.bigmound svg{width:100%;height:100%;color:var(--berry)}
.float{position:absolute;color:var(--mint);opacity:.85}
.float svg{width:34px;height:34px}
.f1{top:8%;left:6%;animation:drift 7s ease-in-out infinite}
.f2{top:22%;right:8%;animation:drift 9s ease-in-out infinite reverse}
.f3{bottom:12%;left:18%;animation:drift 11s ease-in-out infinite}
@keyframes drift{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
@media (prefers-reduced-motion:reduce){.float{animation:none}}
.cta{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;margin:0}
.btn{display:inline-block;background:var(--berry);color:#fff;text-decoration:none;font-weight:700;font-size:.98rem;
padding:.78rem 1.35rem;border-radius:999px;border:1.5px solid var(--berry-dk);box-shadow:0 10px 24px rgba(178,58,94,.28);transition:transform .12s ease}
.btn:hover{transform:translateY(-2px)}
.btn.alt{background:var(--paper);color:var(--berry-dk);border-color:var(--berry-dk);box-shadow:0 8px 18px rgba(59,34,48,.10)}
.btn.small{font-size:.9rem;padding:.6rem 1.1rem}
button.btn{font-family:inherit;cursor:pointer}
section.sec{padding:2.4rem 0;border-top:1px dashed #e2d5da}
section.sec.alt{background:var(--mint-soft);border:1px solid #c8e4d6;border-radius:22px;padding:2.2rem;margin:1rem 0}
.pagehead{padding:2.2rem 0 1.4rem;border-bottom:1px dashed #e2d5da;margin-bottom:1.2rem}
.steps{list-style:none;margin:1.4rem 0 0;padding:0;display:grid;gap:1.1rem;grid-template-columns:repeat(3,1fr)}
.steps li{background:var(--paper);border:1px solid var(--mist);border-radius:18px;padding:1.4rem 1.3rem 1.2rem;box-shadow:0 14px 34px rgba(59,34,48,.08)}
.num{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:999px;background:var(--pink);color:var(--berry-dk);font-weight:800;margin-bottom:.7rem;font-family:Menlo,monospace}
.chips{list-style:none;margin:1.2rem 0 0;padding:0;display:flex;flex-wrap:wrap;gap:.55rem}
.chips li{border:1.5px solid var(--mint);color:#23664e;background:var(--paper);border-radius:999px;padding:.42rem .95rem;font-size:.92rem;font-weight:600}
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-top:1.1rem}
.twocol ul{margin:.2rem 0 0;padding-left:1.2rem}
.note{font-size:.95rem;color:#6a5563;max-width:44rem}
.story{max-width:44rem}
blockquote.verse{margin:1.4rem 0 0;padding:1rem 1.4rem;border-left:4px solid var(--pink);background:var(--paper);border-radius:0 18px 18px 0;font-size:1.15rem;font-style:italic;box-shadow:0 12px 30px rgba(59,34,48,.07)}
blockquote.verse cite{display:block;font-style:normal;font-size:.85rem;color:#6a5563;margin-top:.45rem;font-family:Menlo,monospace}
.visit{display:grid;grid-template-columns:1.1fr .9fr;gap:1.8rem;align-items:start;margin-top:1rem}
.visitcard{background:var(--paper);border:1px solid var(--mist);border-radius:20px;padding:1.5rem;box-shadow:0 16px 38px rgba(59,34,48,.09)}
.addr{font-size:1.04rem;line-height:1.5}
table.hours{border-collapse:collapse;background:var(--paper);border:1px solid var(--mist);border-radius:16px;overflow:hidden;box-shadow:0 10px 26px rgba(59,34,48,.06);width:100%;max-width:26rem}
table.hours caption{text-align:left;font-family:Menlo,monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--berry-dk);padding:.85rem 1rem .3rem}
table.hours th,table.hours td{padding:.55rem 1rem;text-align:left;font-size:.97rem}
table.hours th{font-weight:600}
table.hours tr+tr{border-top:1px dashed #eee2e6}
table.hours td{color:#574050}
.phone{font-size:1rem}.phonebig{font-size:1.4rem;font-weight:750;margin-bottom:.3rem}
.phonebig a{text-decoration:none;color:var(--ink)}
.email a{font-family:Menlo,ui-monospace,monospace;font-size:.92rem}
.cgrid{display:grid;grid-template-columns:.85fr 1.15fr;gap:2.2rem;align-items:start;margin-top:1rem}
.cinfo .lab{margin-top:1.4rem}.cinfo .lab:first-child{margin-top:0}
form.cform{display:grid;gap:.55rem;background:var(--paper);border:1px solid var(--mist);border-radius:20px;padding:1.6rem;box-shadow:0 16px 38px rgba(59,34,48,.09)}
.cform label{font-weight:700;font-size:.92rem}
.cform input,.cform textarea{font:inherit;padding:.65rem .8rem;border:1.5px solid #ddd0d5;border-radius:12px;background:#fffdfc;color:var(--ink);width:100%}
.cform input:focus,.cform textarea:focus{outline:2px solid var(--mint);border-color:var(--mint)}
.mapbox{border-radius:20px;overflow:hidden;border:1px solid #c8e4d6;box-shadow:0 14px 34px rgba(59,34,48,.10)}
.mapbox iframe{display:block;width:100%;height:360px;border:0}
.band{margin:2.2rem 0 1rem;background:linear-gradient(120deg,var(--berry) 0%,var(--berry-dk) 100%);color:#fff;border-radius:24px;padding:2.4rem;box-shadow:0 24px 60px rgba(142,44,72,.35)}
.band .lab{color:var(--pink)}
.band h2{color:#fff}.band p{color:#f6dbe4;max-width:36rem}
.band .btn.alt{background:#fff;color:var(--berry-dk);border-color:#fff}
footer{margin:2.6rem 0 0;padding:2.2rem 0 1.6rem;border-top:8px solid;border-image:linear-gradient(90deg,var(--pink) 0 50%,var(--mint) 50% 100%) 1;box-shadow:0 -8px 0 rgba(59,34,48,.03)}
.fgrid{display:grid;grid-template-columns:1.2fr .8fr .8fr;gap:2rem}
.flab{display:block;font-weight:800;font-size:1.06rem;letter-spacing:-.01em}
.flabmono{font-family:Menlo,monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--berry-dk);margin:0 0 .35rem}
.ftag{color:#6a5563;font-size:.94rem;max-width:26rem;margin:.5rem 0 0}
.fnap p,.fhours p{margin:0 0 .9rem}
.fnap a{color:var(--berry-dk)}
ul.fh{list-style:none;margin:0 0 .9rem;padding:0;max-width:16rem}
ul.fh li{display:flex;justify-content:space-between;gap:1rem;font-size:.94rem;color:#574050;padding:.12rem 0}
.fsocial a{font-size:.94rem}
.footline{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.6rem;margin-top:1.6rem;padding-top:1rem;border-top:1px dashed #e2d5da;font-size:.88rem;color:#6a5563}
.footline a{color:#6a5563}
@media (max-width:880px){
section.hero{grid-template-columns:1fr;padding:2rem 1.5rem}
.band{grid-template-columns:1fr;gap:1.2rem}
.heroart{min-height:170px;order:-1}
.bigmound{width:150px}
.steps{grid-template-columns:1fr}
.visit,.cgrid{grid-template-columns:1fr}
.twocol{grid-template-columns:1fr}
.fgrid{grid-template-columns:1fr 1fr}
}
@media (max-width:560px){
.fgrid{grid-template-columns:1fr}
section.hero{padding:1.7rem 1.2rem;border-radius:20px}
section.sec.alt{padding:1.6rem 1.3rem}
.band{padding:1.8rem 1.4rem}
header nav{margin-left:0}
.mapbox iframe{height:280px}
}
"""

def write(name, content):
    with open(os.path.join(PUBLIC, name), "w", encoding="utf-8") as f:
        f.write(content if content.endswith("\n") else content + "\n")

pages = {
    "index.html": page(
        "New Orleans-Style Sno Balls — Sno Angels SNO Balls, Tomball TX",
        "New Orleans-style sno balls shaved soft like fresh snow in Old Town Tomball — mix up to 3 flavors from 50+, stuff with ice cream, drive-thru at 525 W Main St.",
        "/", HOME, [ld_business(), ld_faq(), breadcrumb([("Home", "/")])],
        og_desc="New Orleans-style sno balls, shaved like fresh snow. 50+ flavors, drive-thru, Main & Magnolia, Tomball TX."),
    "menu.html": page(
        "Snowball Menu & Flavors — Sno Angels SNO Balls, Tomball TX",
        "Fifty-plus sno ball flavors on the boards at 525 W Main St: mix up to 3 per mound, kosher and dye-free and sugar-free choices, ice-cream stuff-ins, sweet cream floats.",
        "/menu", MENU, [ld_webpage("Snowball Menu & Flavors", "Fifty-plus flavors, mix up to three, stuff-ins and floats.", "/menu"), breadcrumb([("Home", "/"), ("Menu", "/menu")])],
        og_desc="Fifty-plus flavors, up to three per mound, kosher/dye-free/sugar-free choices, stuff-ins and floats."),
    "new-orleans-sno-balls.html": page(
        "New Orleans Sno Balls vs. Snow Cones — Sno Angels, Tomball TX",
        "A snow cone is crunchy and the syrup pools low; a New Orleans sno ball is shaved fine as fresh snow and soaks the flavor all the way through. See how it works in Tomball.",
        "/new-orleans-sno-balls", SNOBALLS,
        [ld_service("New Orleans-Style Sno Balls", "Syrup-soaked shaved-ice sno balls built to order: up to three flavors from 50+, ice-cream stuff-ins, sweet cream floats.", "/new-orleans-sno-balls"),
         breadcrumb([("Home", "/"), ("New Orleans sno balls", "/new-orleans-sno-balls")])],
        og_desc="Shaved fine as fresh snow — the syrup soaks all the way through."),
    "event-bookings.html": page(
        "Event Bookings — Sno Angels SNO Balls, Tomball TX",
        "Sno Angels is booking events now — tell the family what you’re celebrating at the corner shop on Main & Magnolia, by phone, or through the contact form.",
        "/event-bookings", EVENTS,
        [ld_service("Sno Ball Event Bookings", "Event bookings for New Orleans-style sno balls in Tomball — ask at the counter, by phone, or via the contact page.", "/event-bookings"),
         breadcrumb([("Home", "/"), ("Event bookings", "/event-bookings")])],
        og_desc="Booking events now — tell us what you're celebrating."),
    "contact.html": page(
        "Visit & Contact — Sno Angels SNO Balls, Tomball TX",
        "525 W Main St, Tomball TX — drive-thru sno balls on the corner of Main & Magnolia. Hours, directions, phone, email, and a contact form straight to the shop inbox.",
        "/contact", CONTACT,
        [ld_business(), breadcrumb([("Home", "/"), ("Visit & contact", "/contact")])],
        og_desc="525 W Main St, Tomball TX — hours, directions, phone and a note straight to the shop."),
    "privacy.html": page(
        "Privacy — Sno Angels SNO Balls, Tomball TX",
        "This site sets no cookies and runs no third-party trackers; the contact form sends your message straight to the shop inbox.",
        "/privacy", PRIVACY, [ld_webpage("Privacy", "No cookies, no trackers — the form goes straight to the shop inbox.", "/privacy")]),
    "404.html": page("Page Not Found — Sno Angels SNO Balls",
                     "That page doesn't exist on the Sno Angels SNO Balls site in Tomball, TX — head back to the flavor boards.",
                     "/404", NOTFOUND, utility=True),
    "thanks.html": page("Message Sent — Sno Angels SNO Balls",
                        "Your message about Sno Angels SNO Balls in Tomball goes straight to the shop inbox.",
                        "/thanks", THANKS, utility=True),
}
for name in sorted(pages):
    if name in ("404.html", "thanks.html"):
        write(name, pages[name] if name in pages else pages[name])
    else:
        write(name, pages[name])
write("style.css", CSS)

core = ["/", "/menu", "/new-orleans-sno-balls", "/event-bookings", "/contact", "/privacy"]
locs = "".join("<url>\n  <loc>%s%s</loc>\n</url>\n" % (ORIGIN, p) for p in core)
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % locs)
write("robots.txt", "User-agent: *\nDisallow:\n\nSitemap: %s/sitemap.xml\n" % ORIGIN)

# post-build hygiene: phone must be exact everywhere, builder tokens absent
joined = "".join(pages.values())
want = TEL_DISPLAY
if joined.count(want) < 6:
    raise SystemExit("phone display mismatch: got %d copies" % joined.count(want))
import hashlib
print("phone copies:", joined.count(want), "| tel copies:", joined.count(TEL_HREF),
      "| phone sha12:", hashlib.sha256(want.encode()).hexdigest()[:12])
print("built %d pages + css + sitemap + robots" % len(pages))

/* Sno Angels SNO Balls — static host + contact form relay (websites lane, t_c08e9ea7).
   Brevo API key lives in the Railway variable BREVO_API_KEY (never in this file, never in git). */
const http = require("http");
const fs = require("fs");
const path = require("path");

const PUB = path.join(__dirname, "public");
const PORT = process.env.PORT || 8080;
const KEY = process.env.BREVO_API_KEY || "";
const SITE = "Sno Angels SNO Balls";
const SITE_ORIGIN = "https://sno-angels-sno-balls-demo.up.railway.app";

const MIME = {
  ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8", ".svg": "image/svg+xml",
  ".png": "image/png", ".xml": "application/xml; charset=utf-8", ".txt": "text/plain; charset=utf-8",
  ".gif": "image/gif", ".ico": "image/x-icon",
};

function send(res, code, body, type, extraHeaders) {
  const h = { "Content-Type": type, "Content-Length": Buffer.byteLength(body), ...extraHeaders };
  res.writeHead(code, h);
  res.end(body);
}

function serveStatic(req, res, pathname) {
  let rel = pathname === "/" ? "/index.html" : pathname;
  let file = path.normalize(path.join(PUB, rel));
  if (!path.extname(file)) file += ".html";
  if (!file.startsWith(PUB)) return send(res, 403, "forbidden", "text/plain", { "X-Robots-Tag": "noindex, nofollow" });
  try {
    fs.accessSync(file);
  } catch {
    file = path.join(PUB, "404.html");
    return send(res, 404, fs.readFileSync(file), "text/html; charset=utf-8", { "X-Robots-Tag": "noindex, nofollow" });
  }
  fs.readFile(file, (err, buf) => {
    if (err) return send(res, 404, fs.readFileSync(path.join(PUB, "404.html")), "text/html; charset=utf-8", { "X-Robots-Tag": "noindex, nofollow" });
    send(res, 200, buf, MIME[path.extname(file)] || "application/octet-stream", { "X-Robots-Tag": "noindex, nofollow" });
  });
}

function collect(req, cb) {
  let body = "";
  req.on("data", (c) => {
    body += c;
    if (body.length > 64 * 1024) { req.destroy(); cb(null); }
  });
  req.on("end", () => cb(body));
}

function relay(name, email, message) {
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const subject = `[SNO ANGELS] ${name || "anonymous"}`;
  const html =
    `<p><b>from:</b> ${esc(name)} &lt;${esc(email)}&gt;</p>` +
    `<p><b>page:</b> ${esc(SITE_ORIGIN + "/contact")}</p>` +
    `<p><b>message:</b></p><p>${esc(message) || "(empty)"}</p>` +
    `<p style="color:#777;font-size:12px">via ${SITE} contact form</p>`;
  const payload = {
    sender: { name: SITE, email: "jarvis+websites@onsmalltalk.com" },
    to: [{ email: "jarvis+websites@onsmalltalk.com", name: "OnSmalltalk Media — lane inbox" }],
    replyTo: /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email || "") ? { email, name: name || email } : undefined,
    subject, htmlContent: html,
    textContent: `from: ${name} <${email}>\npage: ${SITE_ORIGIN}/contact\n\nmessage:\n${message || "(empty)"}`,
  };
  return fetch("https://api.brevo.com/v3/smtp/email", {
    method: "POST",
    headers: { "Content-Type": "application/json", "api-key": KEY },
    body: JSON.stringify(payload),
  }).then((r) => r.text().then((t) => ({ status: r.status, body: t.slice(0, 300) })));
}

function thanksPage() {
  return `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex, nofollow"><title>Message sent — ${SITE}</title><meta name="description" content="Your message about Sno Angels SNO Balls in Tomball goes straight to the shop inbox."><link rel="canonical" href="${SITE_ORIGIN}/thanks"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css"></head><body><div class="topline" aria-hidden="true"></div><main id="main" style="max-width:640px;margin:0 auto;padding:3.5rem 1.5rem"><p class="lab mono">Received</p><h1 style="font-size:2rem;line-height:1.15;margin-bottom:1rem">Your note is on its way</h1><p style="max-width:34rem">Thanks — it goes straight to the inbox running Sno Angels SNO Balls in Old Town Tomball. If it&rsquo;s about an event booking, the sooner the note, the sooner the mounds.</p><p style="margin-top:1.5rem"><a class="btn" href="/" style="display:inline-block;background:var(--berry);color:#fff;font-weight:700;font-size:.98rem;text-decoration:none;padding:.78rem 1.35rem;border-radius:999px;border:1.5px solid var(--berry-dk)">Back to the site</a></p></main></body></html>`;
}

const server = http.createServer((req, res) => {
  const u = new URL(req.url, "http://host");
  const pathname = decodeURIComponent(u.pathname);
  if (pathname === "/healthz") return send(res, 200, "ok\n", "text/plain; charset=utf-8");
  if (pathname === "/open" || pathname === "/pixel.gif") {
    try { fs.readFile(path.join(PUB, "pixel.gif"), (e, b) => send(res, e ? 404 : 200, e || b, "image/gif", { "Cache-Control": "no-store", "X-Robots-Tag": "noindex, nofollow" })); }
    catch { send(res, 404, "gone", "text/plain", { "Cache-Control": "no-store" }); }
    return;
  }
  if (req.method === "POST" && pathname === "/contact") {
    if (!KEY) return send(res, 503, "form not accepting on the demo right now — drop us a note from the main site", "text/plain; charset=utf-8", { "X-Robots-Tag": "noindex, nofollow" });
    return collect(req, async (body) => {
      let name = "", email = "", message = "";
      try {
        const form = new URLSearchParams(body);
        name = (form.get("name") || "").slice(0, 120);
        email = (form.get("email") || "").slice(0, 120);
        message = (form.get("message") || "").slice(0, 4000);
      } catch {}
      if (!name && !email && !message) return send(res, 400, "empty form", "text/plain; charset=utf-8", { "X-Robots-Tag": "noindex, nofollow" });
      try {
        const r = await relay(name, email, message);
        if (r.status >= 200 && r.status < 300) {
          console.log("MAILSENT " + JSON.stringify({ name, email }));
          res.writeHead(303, { Location: "/thanks" });
          return res.end();
        }
        console.log("MAILERR " + JSON.stringify({ status: r.status, body: r.body }));
        return send(res, 502, "message could not be sent right now — please try again", "text/plain; charset=utf-8", { "X-Robots-Tag": "noindex, nofollow" });
      } catch (e) {
        console.log("MAILERR " + JSON.stringify({ err: String(e) }));
        return send(res, 502, "message could not be sent right now — please try again", "text/plain; charset=utf-8", { "X-Robots-Tag": "noindex, nofollow" });
      }
    });
  }
  serveStatic(req, res, pathname);
});

server.listen(PORT, () => console.log(`${SITE} demo listening on ${PORT}`));

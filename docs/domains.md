# Domain checklist: many domains, one main site

Use this when you own several domains and want them to lead to one main site under your own name. Work through it in order and write the answers down. A spreadsheet or a plain text file is enough.

## 1. List every domain you own

For each one, write down:

- the domain name
- where it is registered (the registrar) and which account holds it
- the renewal date, and whether auto-renew is on
- what it points to now (a website, a parked page, nothing)
- whether any email addresses use it
- whether people link to it (search for the name, check old business cards, social profiles and other sites)

Check your email for registrar receipts to find domains you forgot about.

## 2. Pick the main domain

Choose the one that is under your own name, or the one you want people to remember. This is the domain whose pages you build and promote. Everything else either forwards to it, serves a separate purpose, or is let go.

## 3. Decide what happens to each other domain

| Choice | Use it when |
| --- | --- |
| Forward to the main site | People may type or link to it. This is the usual choice. |
| Keep as its own site | It is a real, separate project, such as a company or foundation, with its own audience. |
| Keep only for email | Addresses on that domain are in use. Do not touch its mail settings until you have a replacement. |
| Let it expire | Nobody links to it, you do not use it, and you will not want it back. |

Cost is a small part of the decision. At about $10 a year per domain, the bigger cost is the time spent keeping each one up.

## 4. Put the domains in one place

Cloudflare is free for this and can also be the registrar.

1. Add the domain to Cloudflare at https://dash.cloudflare.com and choose the free plan.
2. Cloudflare reads the existing DNS records. Compare them with what the old registrar shows, and add anything missing. Pay particular attention to `MX` records, which carry email.
3. At the registrar, change the nameservers to the two Cloudflare gives you.
4. Wait until Cloudflare shows the domain as active. This usually takes minutes to a few hours.

Optional: transfer the registration itself to Cloudflare Registrar. The domain must be unlocked at the old registrar, you need its authorization code, and a domain cannot be transferred within 60 days of being registered or last transferred. Transfers usually add a year to the registration.

## 5. Forward the extra domains

For each domain that should forward to the main site:

1. Make sure it is in Cloudflare and active.
2. Add a DNS record for it that is proxied (the orange cloud). An `A` record for the name `@` with the placeholder address `192.0.2.1` works, because Cloudflare answers the redirect itself and never reaches that address. Do the same for `www`.
3. Open **Rules**, then **Redirect Rules**, and create a rule that matches the domain and redirects to your main domain with a 301 (permanent) status. Keep the path, so `old-domain.com/about` goes to `main-domain.com/about`.
4. Open the old address in a browser and check that it lands on the right page and shows the lock icon for HTTPS.

Cloudflare's current instructions are at https://developers.cloudflare.com/rules/url-forwarding/.

## 6. Check email before and after

- Send a test message to and from every address that uses a domain you changed.
- If an old domain still receives email, keep its `MX` records, or set up forwarding with Cloudflare Email Routing (free) at https://developers.cloudflare.com/email-routing/.

## 7. Keep it from breaking

- Turn on auto-renew for every domain you keep, and use an email address you read for the renewal notices.
- Put the renewal dates in your calendar.
- Turn on two-factor sign-in for the registrar and for Cloudflare.
- When a forwarded domain's renewal comes up, ask again whether anyone still uses it.

# Optional ChordCrack email updates

## Status

Prepared as a review branch, not published to GitHub Pages. The static website
uses GitHub Pages `main` / root. There is no existing website submission backend;
the app's Supabase authentication data is separate and is not a mailing list.

`updates.html` implements a manual email-request flow using the support address
already published on the website. It does not pretend to save a submission.
The visitor must send the email from their own email client. The page includes
fixed consent wording, a manual confirmation step, copyable fallback instructions,
an unsubscribe email link, and a dedicated privacy explanation. It has no scripts,
address input, form endpoint, tracking, local storage, or third-party embed.
The homepage navigation and release section link to it. The privacy page has an
email-updates addendum; the existing app-policy text has not been rewritten.

The domain's MX record points to Microsoft 365. This confirms routing only,
not that `support@chordcrack.com` exists or receives mail. No mailbox was accessed,
no email was sent, and no real subscriber data was used. Browser account checks
showed login screens for Brevo, EmailOctopus and Buttondown; no usable authenticated
account was available in that browser session. Accounts elsewhere may exist.

**Not verified end to end:** receipt in the support inbox, confirmation replies,
and actual unsubscribe processing. Do not merge until the owner verifies the
inbox and adopts the manual workflow below, or replaces it with a verified hosted
form. The current draft creates no service account, credential, database change,
or billable subscription.

## Owner workflow required for the manual option

1. Keep requests in the existing private support mailbox. Do not create public
   issues, repository CSVs, website JSON files, or public spreadsheets for contacts.
2. Treat every request as pending. Send a plain confirmation reply only in response
   to the request, to its sender address. Restate the updates purpose and ask the
   person to reply to confirm. Do not automatically trust a differing Reply-To or
   an address typed into the body. Do not bulk-confirm old app accounts or support
   contacts. No confirmation or marketing messages were sent by this change.
3. Only after a positive reply, mark the private thread as confirmed. Keep the
   original request and confirmation, with sender, received timestamps, purpose,
   and consent version `website-updates-2026-11-04`. Those messages are the consent
   record; a click on the website is not evidence of consent. Collect no profile
   name, password, demographics, analytics identifier, or game data for this list.
4. Process withdrawals before sending any further updates. Remove the address
   from the active audience, retain a minimal private suppression record, and
   never resubscribe it from an older request. Rejoining needs a new request and
   new confirmation. Also honor plain-language unsubscribe requests and replies,
   not just the exact suggested subject. No login or reason is required.
5. For any future, separately authorized update, use only currently confirmed,
   nonsuppressed addresses. Do not reveal recipients to each other. Include a
   reply-to unsubscribe route and the website unsubscribe link in every update.
   Review stale pending requests and unnecessary email signatures for deletion;
   retain only records needed to administer consent and suppression. Process
   access/correction/deletion requests through the same support inbox.

This is intentionally manual and suitable only for a small audience that the
owner can maintain. A hosted provider is preferable as the audience grows.
Before launch, an owner-controlled test mailbox should exercise request receipt,
confirmation, withdrawal, and attempted re-add from an old request. Such a test
needs authorization to send the confirmation email; it has not been performed.

## Costs and hosted alternatives checked November 4, 2026

The manual implementation adds **$0 in new platform/service fees**. Existing
GitHub Pages/domain/Microsoft 365 costs continue; their invoices were not inspected.
The implementation itself sends no email, so there are no send charges from it.

| Option | Published free allowance | Considerations before activation |
| --- | --- | --- |
| EmailOctopus | $0; 2,500 subscribers and 10,000 emails/month; one form and one landing page | Provider branding. Double opt-in is off by default and must be enabled. Verify sender/domain. Imports can bypass confirmation and must not be used for existing app accounts. |
| Brevo | $0; up to 100,000 stored contacts and 300 sends/day | The daily cap limits a same-day launch update to a larger list. Configure double confirmation, verified sender, and unsubscribe behavior. Provider branding remains on the free tier. |
| Buttondown | $0 for the first 100 subscribers | Straightforward HTML/hosted signup; default double opt-in. Smaller free audience. Verify sender/account and unsubscribe behavior before use. |

For an automated public signup, EmailOctopus offers the most useful free starting
capacity for this small app, provided double opt-in is enabled and sending remains
within the free limits. Buttondown is the simplest small-list alternative. No
provider was selected or activated for the user. Recheck limits at activation;
do not add payment details or accept a paid upgrade without authorization.

All require an accessible existing account or explicitly authorized account
creation, any required sender/domain verification, a genuine hosted form URL,
and a controlled subscribe/confirm/unsubscribe test. No frontend API key is needed
for a hosted signup form; do not expose a provider API key or Supabase service-role
key in this static repository. Keep contacts and suppression records private.

Official sources:

- [EmailOctopus pricing](https://emailoctopus.com/pricing)
- [EmailOctopus double opt-in](https://help.emailoctopus.com/article/36-how-to-edit-double-opt-in)
- [EmailOctopus sender reputation and verification](https://help.emailoctopus.com/article/105-maintaining-your-sender-reputation)
- [EmailOctopus suppression](https://help.emailoctopus.com/article/213-how-to-switch-to-emailoctopus)
- [Brevo plans](https://help.brevo.com/hc/en-us/articles/208589409-About-Brevo-s-pricing-plans)
- [Brevo free-plan limits](https://help.brevo.com/hc/en-us/articles/208580669-FAQs-What-are-the-limits-of-the-Free-plan)
- [Brevo double opt-in forms](https://help.brevo.com/hc/en-us/articles/208771869-Create-a-sign-up-form-in-Brevo)
- [Buttondown pricing](https://buttondown.com/pricing)
- [Buttondown signup options](https://docs.buttondown.com/building-your-subscriber-base)
- [Buttondown default double opt-in](https://docs.buttondown.com/api-subscribers-create)

## Validation

Run `python3 scripts/verify-email-updates.py` for offline checks of explicit consent,
identical fallback wording, fixed-recipient/encoded email links, withdrawal text,
absence of capture endpoints/tracking scripts, and local assets/anchors. It never
sends email or reads subscriber data. All content checked is synthetic/static.

Chrome review passed at 320, 768 and 1200 CSS pixels. The homepage and updates
page had no horizontal overflow at 320px, including the expanded fallback at
200% root text size. Keyboard navigation from the mobile menu and activation of
the fallback passed with a visible focus outline. The unsubscribe anchor and
encoded destinations were checked. The updates page has zero script/form
elements. JavaScript syntax and Git whitespace checks passed. A temporary large-
text fixture was removed after review. Neither a server database nor an actual
hosted signup service is part of this implementation.

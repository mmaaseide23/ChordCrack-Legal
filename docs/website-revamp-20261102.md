# ChordCrack website revamp — November 2, 2026

The landing page now introduces guitar ear training through the actual product and a silent chord-shape explorer. It keeps the original green pick and navy/green palette, and replaces decorative gradients and repeated feature cards with a clearer progression through chord recognition, daily practice, the library and practical questions.

## Changes

- Bricolage Grotesque display typography, locally hosted with its SIL Open Font License; no font service requests.
- Actual iOS development screenshots, explicitly labeled as development previews with fictional progress, not a release announcement.
- Accessible A/Am/E/Em chord-shape comparison, with native radio controls, screen-reader diagram descriptions and polite feedback. No audio, autoplay, account access or backend calls.
- Short press and note-position feedback. Keyboard selection is immediate; CSS honors Reduce Motion.
- Responsive navigation with Escape handling, native FAQ disclosures and intact App Store, support, privacy and terms destinations.
- Existing analytics remain restricted to the two production hostnames. No collection added to local or review hosts.

## Reference and provenance

The requested Instagram reel, https://www.instagram.com/reel/DerxrOmTkCt/, was inspected muted: its caption and the visible Impeccable segment identify Emil Kowalski’s Design Skills, Impeccable and Taste, with Figma MCP and Playwright mentioned as tools. No full audio transcript was obtained. The implementation applies composition, typography, purposeful interaction and real-browser review guidance from these public sources:

- https://github.com/emilkowalski/skills/tree/f1090bec277140d02ed202440185ad9d02ac1490
- https://github.com/pbakaus/impeccable/tree/c3c94b960276a42a235d1ff68e9954a342e5407e
- https://github.com/Leonxlnx/taste-skill/tree/12af471f627f866411b4bd785b19646d3672784c

The third-party skill installers, binaries, random direction generators and browser scripts were not run. Browser checks used the supported local browser interface. No Figma design was supplied or used. Product truth and the established brand take precedence over a skill’s optional visual conventions.

Bricolage Grotesque was downloaded from the official Google Fonts repository: https://github.com/google/fonts/tree/main/ofl/bricolagegrotesque. Its license is in `fonts/OFL.txt`. The existing logo and three synthetic app screenshots are unchanged; no stock photography, fabricated testimonials or user statistics were added.

## Validation

- JavaScript syntax, local asset/link existence and Git whitespace checks passed.
- Actual Chrome layout inspected at 1440, 768, 390 and 320 CSS pixels. No horizontal document overflow in final measurements.
- A temporary 200% root-text fixture at 320 CSS pixels exposed overflow in the hero, controls and email address. Those were corrected; all seven FAQ answers open together without overflow.
- All four chord selections and their note positions/descriptions checked. Arrow-key selection is immediate. Mobile navigation, menu Escape and all FAQ disclosures checked.
- Keyboard focus was checked in-browser on the hero action, selected chord control
  and footer action. Outlines contrast with their surrounding solid surfaces.
- Privacy and Terms pages opened successfully; their legal content is unchanged.
- All product images loaded; local page had no Google Analytics script and no audio/video elements. Palette contrast checked numerically.
- Reduce Motion CSS reviewed; OS preference was not changed. No hardware screen-reader audit or independent Safari run was performed.

The existing GitHub Pages main/root deployment is unchanged. This is a review-branch source update only; publication still requires approval.

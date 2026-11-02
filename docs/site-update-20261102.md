# Initial website update

This records the initial factual update. The subsequent full redesign and its
validation are documented in `website-revamp-20261102.md`.

This change preserves the existing ChordCrack site, logo, navy/green palette,
App Store destination and legal documents. GitHub Pages publishes `main` at
`www.chordcrack.com`; this work is prepared on a separate review branch.

- Describes implemented individual practice, friends and leaderboard features;
  explicitly distinguishes them from unimplemented live multiplayer.
- Limits offline claims to downloaded audio and explains which services need a
  connection. Removes unsupported jazz, invitation-code, seamless-sync and
  subscription language.
- Adds three inspected native iOS Simulator screenshots of the development
  build. All progress is fictional. Labels distinguish these screens and the
  five-round prototype from the available App Store version.
- Uses native keyboard-accessible FAQ disclosures and mobile navigation, visible
  focus, reduced-motion styling, wrapping at large text sizes and valid icons.
- Keeps existing website Analytics limited to the two production hostnames so
  local/review previews do not send telemetry. No collection was added.

Validation: inspected desktop (1200/1280px) and phone (320px) views; no horizontal
overflow. A temporary 200% root-text fixture at 320px identified and resolved
navigation, long-heading and contact wrapping; it was removed after checking.
Menu and FAQ work with Enter; selecting a navigation item closes the menu.
HTML anchor/local-asset checks and all 13 native disclosure pairs passed.
All screenshot assets loaded; local page had no remote Analytics script.
No app sound or personal account data was used.

Screenshot provenance (unmodified, fictional iPhone 13 mini Simulator captures):

| Asset | SHA-256 |
| --- | --- |
| preview-home.png | 9ee4ad50dbfe811bd7997858b7b11d567f95c6cd5576ba02572620b5d6804596 |
| preview-daily.png | fb3d9351ae300757ebd1ab3e4c400b55c173c0e3ca6bb222d0261ebfbb176107 |
| preview-chord.png | 2c86ce83b3faa88d3eb968d8c47e302951f635e7038cfa897501ceb83c4b3c10 |

The app's Analytics audit confirms receipt of automatic events. Crashlytics and
Performance are now integrated in the reviewed app source with the existing
Analytics & Diagnostics preference. A synthetic symbol upload passed; actual
Performance trace receipt is now console-verified from an isolated synthetic
fixture. Crashlytics also received one synthetic nonfatal and resolved its app
stack frame; fatal-crash and released-binary reporting remain unverified. This website makes no
monitoring assurances or claims about a released binary.
The app privacy-policy migration is covered by its own source and tests, not
by promotional claims here. No legal terms were rewritten.

#!/usr/bin/env python3
"""Offline checks only. Never sends an email or reads subscriber records."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, name):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.text = []
        self.feed((ROOT / name).read_text())

    def handle_starttag(self, tag, attrs):
        self.nodes.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


class EmailUpdatesChecks(unittest.TestCase):
    def setUp(self):
        self.page = Page('updates.html')
        self.ids = {attrs['id']: attrs for _, attrs in self.page.nodes if 'id' in attrs}

    def message(self, link):
        url = urlsplit(self.ids[link]['href'])
        self.assertEqual(url.scheme, 'mailto')
        self.assertEqual(url.path, 'support@chordcrack.com')
        fields = parse_qs(url.query, strict_parsing=True)
        # No CC/BCC or user-supplied query values; fixed recipient only.
        self.assertEqual(set(fields), {'subject', 'body'})
        self.assertEqual(len(fields['subject']), 1)
        self.assertEqual(len(fields['body']), 1)
        self.assertNotIn('\n', fields['subject'][0])
        self.assertNotIn('\r', fields['subject'][0])
        return fields['subject'][0], fields['body'][0]

    def test_explicit_consent_and_copyable_fallback_match(self):
        subject, body = self.message('subscribe-email')
        self.assertEqual(subject, 'Subscribe to ChordCrack updates')
        for phrase in ('Please send me occasional emails', 'Michael Maaseide',
                       'releases, new features and beta opportunities',
                       'I can unsubscribe at any time',
                       'website-updates-2026-11-04',
                       'https://www.chordcrack.com/updates.html#privacy'):
            self.assertIn(phrase, body)
        # The copyable version must express the same consent as the mailto draft.
        self.assertIn(' '.join(body.split()), ' '.join(' '.join(self.page.text).split()))
        self.assertIn('\r\n', body)
        self.assertNotIn('\n', body.replace('\r\n', ''))

    def test_unsubscribe_has_no_login_or_confirmation_requirement(self):
        subject, body = self.message('unsubscribe-email')
        self.assertEqual(subject, 'Unsubscribe from ChordCrack updates')
        self.assertIn('Please stop ChordCrack update emails', body)
        text = ' '.join(self.page.text)
        self.assertIn('No account or explanation needed.', text)
        self.assertIn('before further updates are sent', text)

    def test_no_capture_endpoint_tracking_or_browser_storage(self):
        for tag, attrs in self.page.nodes:
            self.assertNotIn(tag, {'form', 'input', 'script', 'iframe', 'textarea'})
            self.assertFalse(any(key.startswith('on') for key in attrs))
            self.assertNotIn('action', attrs)
            for attribute in ('src', 'href'):
                if attribute in attrs:
                    self.assertIn(urlsplit(attrs[attribute]).scheme, {'', 'mailto'})
        text = ' '.join(self.page.text)
        self.assertIn('Opening this link does not subscribe you.', text)
        self.assertIn('Existing accounts and support conversations are not automatically subscribed.', text)

    def test_links_assets_and_anchor_destinations_exist(self):
        for name in ('index.html', 'updates.html', 'privacy.html'):
            for _, attrs in Page(name).nodes:
                for attribute in ('href', 'src'):
                    value = attrs.get(attribute)
                    if not value:
                        continue
                    url = urlsplit(value)
                    if url.scheme or url.netloc:
                        continue
                    target = unquote(url.path) or name
                    self.assertTrue((ROOT / target).is_file(), (name, value))
                    if url.fragment:
                        ids = {a.get('id') for _, a in Page(target).nodes}
                        self.assertIn(unquote(url.fragment), ids, (name, value))


if __name__ == '__main__':
    unittest.main()

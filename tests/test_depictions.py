"""Render the upstream term and list templates with flat depiction files.

Run with a supported Hugo on PATH: python -m unittest discover -s tests
"""

import re
import shutil
import struct
import subprocess
import tempfile
import unittest
import zlib
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[1]


def png():
    def chunk(kind, data):
        return (struct.pack('!I', len(data)) + kind + data
                + struct.pack('!I', zlib.crc32(kind + data)))

    return (b'\x89PNG\r\n\x1a\n'
            + chunk(b'IHDR', struct.pack('!2I5B', 2, 2, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress((b'\x00' + b'\xff\x00\x00' * 2) * 2))
            + chunk(b'IEND', b''))


class DepictionTests(unittest.TestCase):
    def test_flat_images_on_term_pages_and_both_lists(self):
        for variant in ('grid', 'vertical'):
            with self.subTest(variant=variant), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                shutil.copytree(SOURCE / 'layouts', root / 'layouts')
                # Exercise the real content templates without the unrelated theme shell.
                (root / 'layouts/baseof.html').write_text(
                    '<html><body>{{ block "main" . }}{{ end }}</body></html>')
                (root / 'layouts/single.html').write_text('{{ define "main" }}{{ .Content }}{{ end }}')
                (root / 'layouts/home.html').write_text('{{ define "main" }}Home{{ end }}')
                (root / 'hugo.toml').write_text('''baseURL = "https://example.org/lab/"
disableKinds = ["RSS", "sitemap", "robotsTXT"]
[taxonomies]
person = "persons"
project = "projects"
topic = "topics"
''')

                def write(name, text):
                    path = root / 'content' / name
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(text)

                for section, kind in [('persons', 'portrait'), ('projects', 'logo'),
                                      ('topics', 'depiction')]:
                    write(f'{section}/_index.md',
                          f'---\ntitle: {section}\nlist_variant: {variant}\n'
                          f'term:\n  depiction_type: {kind}\n---\n')
                    write(f'{section}/same_name/_index.md',
                          f'---\ntitle: A different display title\nurl: /{section}/different-url/\n---\n')
                    write(f'{section}/missing/_index.md', '---\ntitle: Missing image\n---\n')
                (root / 'content/persons/same_name_portrait.png').write_bytes(png())
                write('projects/same_name_logo.svg',
                      '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="2">'
                      '<rect width="2" height="2" fill="blue"/></svg>')
                (root / 'content/topics/same_name_depiction.png').write_bytes(png())
                # Register real Hugo taxonomy terms, including one without an authored page.
                write('entry.md', '---\ntitle: Entry\npersons: [same_name, missing, automatic]\n'
                      'projects: [same_name, missing]\ntopics: [same_name, missing]\n---\n')
                result = subprocess.run(['hugo', '--source', str(root)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                output = root / 'public'
                for section, kind in [('persons', 'portrait'), ('projects', 'logo'),
                                      ('topics', 'depiction')]:
                    for name in [f'{section}/different-url/index.html', f'{section}/index.html']:
                        self.assertTrue((output / name).exists(), result.stdout + result.stderr)
                        html = (output / name).read_text()
                        images = re.findall(r'<img\b[^>]*src="([^"]+)"', html)
                        depiction = [url for url in images if f'same_name_{kind}' in url]
                        self.assertEqual(len(depiction), 1, (name, images))
                        self.assertTrue(depiction[0].startswith(f'/lab/{section}/'))
                        self.assertTrue((output / depiction[0].removeprefix('/lab/')).is_file())
                    html = (output / section / 'missing/index.html').read_text()
                    self.assertNotIn('<img', html)
                automatic = (output / 'persons/automatic/index.html').read_text()
                self.assertNotIn('<img', automatic)


if __name__ == '__main__':
    unittest.main()

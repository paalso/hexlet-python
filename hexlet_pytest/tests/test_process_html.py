from hexlet_pytest.process_html import extract_links
import os


def test_extract_links():
    # HTML находится в файле withLinks.html в директории tests/fixtures
    with_links_path = 'tests/fixtures/withLinks.html'
    with open(with_links_path, encoding='utf8') as f:
        html = f.read()
        # Теперь с HTML удобно работать, он не загромождает тесты
        links = extract_links(html)
        assert links == ['/resumes/1', '/users/6']

import pytest
from bs4 import BeautifulSoup
from src.backend.checks.alt_text import AltTextCheck
from src.backend.checks.language_declared import LanguageDeclaredCheck
from src.backend.checks.heading_hierarchy import HeadingHierarchyCheck
from src.backend.checks.form_labels import FormLabelsCheck

def test_alt_text_check():
    html = '<img src="test.jpg"> <img src="test2.jpg" alt=""> <img src="test3.jpg" alt="Description">'
    soup = BeautifulSoup(html, "html.parser")
    check = AltTextCheck()
    results = check.run(soup)
    
    assert len(results) == 2
    assert results[0]["message_key"] == "issue_alt_text"
    assert results[1]["message_key"] == "issue_alt_empty"

def test_language_declared_check():
    html_no_lang = "<html><body></body></html>"
    soup = BeautifulSoup(html_no_lang, "html.parser")
    check = LanguageDeclaredCheck()
    results = check.run(soup)
    assert len(results) == 1
    assert results[0]["message_key"] == "issue_lang_missing"

def test_heading_hierarchy_check():
    html = "<h1>Title</h1><h3>Sub</h3>"
    soup = BeautifulSoup(html, "html.parser")
    check = HeadingHierarchyCheck()
    results = check.run(soup)
    assert len(results) == 1
    assert results[0]["message_key"] == "issue_headings_broken"
    assert results[0]["params"]["last"] == 1
    assert results[0]["params"]["current"] == 3

def test_form_labels_check():
    html = '<input id="test"> <label for="test">Label</label> <input id="no-label">'
    soup = BeautifulSoup(html, "html.parser")
    check = FormLabelsCheck()
    results = check.run(soup)
    assert len(results) == 1
    assert results[0]["message_key"] == "issue_form_label_missing"

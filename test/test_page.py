def test_text_is_show(driver, base_url):
    driver.get(base_url)
    assert 'This is just a demo.' in driver.page_source

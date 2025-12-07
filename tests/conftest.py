import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope='function')
def setup_browser():
    chrome_options = Options()

    # Определяем, запущены ли в CI (Jenkins)
    is_ci = os.getenv('JENKINS_HOME') is not None

    # Основные опции для скрытия автоматизации
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Дополнительные опции
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")

    if is_ci:
        # Для Jenkins/CI - headless режим
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        # Для локального запуска
        chrome_options.add_argument("--start-maximized")

    # ВАЖНО: Создаем драйвер с опциями
    browser.config.driver = webdriver.Chrome(options=chrome_options)
    browser.config.base_url = "https://demoqa.com"  # Исправьте на ваш URL

    # Скрипты для маскировки (раскомментируйте если нужно)
    # browser.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    yield browser

    # Очистка
    if browser.driver:
        browser.quit()
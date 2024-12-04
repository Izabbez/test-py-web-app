import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Configuração do serviço explicitamente
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_github_login_page(driver):
    driver.get("https://github.com/login")
    assert "Sign in" in driver.title, "Título da página não corresponde ao esperado!"
    print("Teste E2E passou com sucesso!")

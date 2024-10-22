import pytest
from playwright.sync_api import sync_playwright, expect
from pages import page_input_register, page_input_login

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_mensagem_erro_login(page):
    #Selecionando a classe e passando o parâmetro Page
    input_login = page_input_login.InputLogin(page)

    #Acessando o link de teste 
    page.goto("https://bugbank.netlify.app/")

    #Tentar fazer login sem preencher os campos
    input_login.login_submit()

    #Validando as mensagens de erro para o login
    input_login.assert_login_fields_alert()

def test_mensagem_erro_cadastro(page):
    #Selecionando a classe e passando o parâmetro Page
    input_register = page_input_register.InputRegister(page)
    input_login = page_input_login.InputLogin(page)
    
    #Acessando o link de teste 
    page.goto("https://bugbank.netlify.app/")

    #Acessando a tela de cadastro
    input_login.access_register()
    
    #Tentar fazer cadastro sem preencher os campos
    input_register.register_submit()

    #Validando as mensagens de erro para o Cadastro
    input_register.assert_register_fields_alert()
    
def test_cadastro_feliz(page):
    #Selecionando a classe a ser utilizada passando page
    input_register = page_input_register.InputRegister(page)
    input_login = page_input_login.InputLogin(page)

    #Acessando o link de teste    
    page.goto("https://bugbank.netlify.app/")

    #Acessando a tela de cadastro
    input_login.access_register()

    #Fornecendo as informações para cadastro
    INFO_SUBMIT = {
        "Informe seu e-mail" : "teste@teste.com.br",
        "Informe seu Nome" : "João Bonin",
        "Informe sua senha" : "123123123",
        "Informe a confirmação da senha" : "123123123"
        }

    #Cadastro completo da conta
    input_register.complete_register(INFO_SUBMIT)

    #Usando a função de preencher espaços no login
    input_login.fill_all_fields(INFO_SUBMIT)

    #Clicando para logar
    input_login.login_submit()

    #Validando que após o login o redirecionamento para a Home do site é feito
    expect(page).to_have_url("https://bugbank.netlify.app/home")
        
def test_cadastro_sem_info(page):
    #Selecionando a classe e passando o parâmetro da página
    input_register = page_input_register.InputRegister(page)
    input_login = page_input_login.InputLogin(page)

    #Acessando o link de teste
    page.goto("https://bugbank.netlify.app/")

    #Acessando a tela de cadastro
    input_login.access_register()

    #Fornecendo as informações para cadastro
    INFO_SUBMIT = {
        "Informe seu e-mail" : "teste@teste.com.br",
        "Informe seu Nome" : "João Bonin",
        "Informe sua senha" : "123123123",
        "Informe a confirmação da senha" : "123123123"
        }

    #Preenchendo todos os campos para dar início aos testes
    input_register.fill_all_fields(INFO_SUBMIT)

    #Função que popula e remove campos 
    input_register.assert_register_fields_missing(INFO_SUBMIT)
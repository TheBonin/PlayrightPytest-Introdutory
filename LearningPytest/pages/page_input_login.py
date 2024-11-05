from playwright.sync_api import expect

class InputLogin:
    def __init__(self,page) -> None:
        #Transforma page em uma variável compartilhada pela classe dentro de 'self'
        self.page = page
        self.locator_login = page.locator(".card__login")
        self.locator_register_button = page.locator(".login__buttons [type='button']")
        self.locator_submit_button = page.locator(".login__buttons [type='submit']")
        self.locator_warging = page.locator(".card__login .input__warging")

    def fill_all_fields(self, info : dict) -> None:
        #Pega o dicionário enviado na função e faz um loop por entrada, divindo a key e seu respectivo valor por iteração
        for key, value in info.items():
            #Só preenche os campos presentes na tela de login
            if key == "Informe seu e-mail" or key == "Informe sua senha":
                self.locator_login.get_by_placeholder(key, exact = True).fill(value)

    def access_register (self) -> None:
        self.locator_register_button.click()

    def login_submit (self) -> None:
        self.locator_submit_button.click()

    def complete_login(self,info : dict) -> None:
        #Usando a função de preencher espaços no login
        self.fill_all_fields(info)

        #Clicando para logar
        self.locator_submit_button.click()

    def assert_login_fields_alert(self) -> None:
        #Loop que será repetido duas vezes
        for i in range(2):
            #Verifica que em ambos os espaços, o texto "É campo obrigatório" é exibido
            expect(self.locator_warging.all()[i-1]).to_have_text("É campo obrigatório")    
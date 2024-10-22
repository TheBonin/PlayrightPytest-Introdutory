from playwright.sync_api import expect

class InputLogin:
    def __init__(self,page) -> None:
        #Transforma page em uma variável compartilhada pela classe dentro de 'self'
        self.page = page
    
    def fill_all_fields(self, info : dict) -> None:
        #Pega o dicionário enviado na função e faz um loop por entrada, divindo a key e seu respectivo valor por iteração
        for key, value in info.items():
            #Só preenche os campos presentes na tela de login
            if key == "Informe seu e-mail" or key == "Informe sua senha":
                self.page.locator(".card__login").get_by_placeholder(key, exact = True).fill(value)

    def access_register (self) -> None:
        self.page.locator(".login__buttons [type='button']").click()

    def login_submit (self) -> None:
        self.page.locator(".login__buttons [type='submit']").click()

    def complete_login(self,info : dict) -> None:
        #Usando a função de preencher espaços no login
        self.fill_all_fields(info)

        #Clicando para logar
        self.page.locator(".login__buttons [type='submit']").click()

    def assert_login_fields_alert(self) -> None:
        #locator a ser uzado futuramente
        locator = self.page.locator(".card__login .input__warging").all()

        #Loop que será repetido duas vezes
        for i in range(2):
            #Verifica que em ambos os espaços, o texto "É campo obrigatório" é exibido
            expect(locator[i-1]).to_have_text("É campo obrigatório")    
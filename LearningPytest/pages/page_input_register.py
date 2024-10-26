from playwright.sync_api import expect

class InputRegister:
    def __init__(self, page) -> None:
        #Transforma page em uma variável compartilhada pela classe dentro de 'self'
        self.page = page
        self.locator_register = page.locator(".card__register div")  
        self.locator_field_alert = page.locator("p.input__warging")
        self.locator_success_register = page.locator("[id = modalText]")
        self.locator_success_button = page.locator("[id='btnCloseModal']")
        self.locator_register_submit = page.locator(".card__register [type=submit]")
        self.locator_name_alert = page.locator("[id='btnCloseModal']")

    def fill_all_fields(self, info : dict) -> None:
        #Pega o dicionário enviado na função e faz um loop por entrada, divindo a key e seu respectivo valor por iteração
        for key, value in info.items():
            #Usa a key e seu valor para encontrar e preencher o campo
            self.locator_register.get_by_placeholder(key, exact = True).fill(value)

    def register_submit(self) -> None:
        self.locator_register_submit.click()

    def complete_register(self,info : dict) -> None:
        #Usando a função de preencher espaços no cadastro
        self.fill_all_fields(info)

        #Dando submit no cadastro
        self.locator_register_submit.click()
    
        #Fechando modal de conta criada
        self.locator_success_button.click()
from playwright.sync_api import expect

class InputRegister:
    def __init__(self, page) -> None:
        #Transforma page em uma variável compartilhada pela classe dentro de 'self'
        self.page = page
        self.locator_register = page.locator(".card__register")  
        self.locator_field_alert = page.locator(".card__register .input__warging")
        self.locator_success_register = page.locator("[id = modalText]")
        self.locator_success_button = page.locator("[id='btnCloseModal']")
        self.locator_register_submit = page.locator(".card__register [type=submit]")
        self.locator_name_alert = page.locator("[id='btnCloseModal']")

    def fill_all_fields(self, info : dict) -> None:
        #Pega o dicionário enviado na função e faz um loop por entrada, divindo a key e seu respectivo valor por iteração
        for key, value in info.items():
            #Usa a key e seu valor para encontrar e preencher o campo
            self.locator_register.get_by_placeholder(key, exact = True).fill(value)

    #Valida que a mensagem de erro seja ou não exibida
    def assert_register_fields_missing(self,info : dict) -> None:
        for key, value in info.items():
            #Esvaziar somente um dos campos
            self.locator_register.get_by_placeholder(key, exact = True).fill("")

            #Tenta efetuar o cadastro
            self.locator_register_submit.click()
            
            #Fecha o modal exibido para o nome
            if key == "Informe seu Nome":
                self.locator_name_alert.click()
            
            #Validar que a mensagem de "Conta cadastrada" não seja exibida
            expect(self.locator_success_register).not_to_be_visible()

            #Preenche todos os campos para a próxima iteração
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

    def assert_register_fields_alert(self) -> None:
        #locator a ser uzado futuramente
        locator = self.locator_field_alert.all()

        #Loop que será repetido quatro vezes
        for i in range(4):
            #Exclui o campo "Nome" da verificação
            if i != 1:
                #Verifica que em todos os espaços, o texto "É campo obrigatório" é exibido
                expect(locator[i]).to_have_text("É campo obrigatório")
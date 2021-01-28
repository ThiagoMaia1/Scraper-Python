import time
from selenium import webdriver

nota = 1231414

def selecionarElemento(id):
    def suprimir(funcao):
        elemento = None
        try: elemento = funcao(id)
        except: pass
        return elemento
    tentativas = 0
    elemento = None
    css = False
    if id[0] == '.' or id[0] == '#' or id.find(' ') > 0: css = True
    while elemento is None:
        if tentativas > 10: return
        if tentativas != 0: 
            time.sleep(1)
        tentativas += 1
        if css:
            elemento = suprimir(driver.find_element_by_css_selector)
        else:
            elemento = suprimir(driver.find_element_by_id)
    return elemento

def click_id(id):
    botao = selecionarElemento(id)
    botao.click()

def inserir(id, valor):
    input = selecionarElemento(id)
    input.send_keys(valor)

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://zeppelin10.ufop.br/minhaUfop/desktop/login.xhtml')
# time.sleep(5) # Let the user actually see something!
inserir('formLogin:inputIdentificacao', '04055316640')
inserir('formLogin:inputSenha', '2020Ufop')
click_id('.ui-button-text.ui-c')
click_id('formPrincipal:grupos:7:j_idt22_header')
click_id('#formPrincipal .ui-panelgrid-cell.ui-grid-col-8 li:first-child a')
click_id('sd1')
click_id('#barra > a:first-of-type')
inserir('formTemplate:empenho', nota)

time.sleep(60)
import time
from selenium import webdriver
import sys
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# LINK NTI TESTES: https://kiss.ufop.br:8181/Almoxarifado/?idUsuario=47c37828e7eab47a28f696980b69803a&frs=0.9704407878468361

notaEmpenho = '2020NE800689'
notaFiscal = '000162108'
dataNF = '14/01/2021'
valor = 117060


def selecionarElemento(id, selector = False):
    def suprimir(func):
        elemento = None
        try: elemento = func(id)
        except: pass
        return elemento
    tentativas, elemento = 0, None
    funcao = selector
    if not funcao: 
        if id[0] == '.' or id[0] == '#' or id.find(' ') > 0: funcao = 'css_selector'
    if not funcao: 
        if id[0] == '/': funcao = 'xpath'
    if not funcao: funcao = 'id'
    while elemento is None:
        if tentativas > 10: return
        if tentativas != 0: 
            time.sleep(0.2)
        tentativas += 1
        elemento = suprimir(getattr(driver, 'find_element_by_' + funcao))
    return elemento

def click_id(id, selector = False):
    botao = selecionarElemento(id, selector)
    botao.click()
    return botao

def inserir(id, valor, selector = False):
    input = selecionarElemento(id, selector)
    input.send_keys(valor)
    return input

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://zeppelin10.ufop.br/minhaUfop/desktop/login.xhtml')
# time.sleep(5) # Let the user actually see something!
inserir('formLogin:inputIdentificacao', '416.810.188-61')
inserir('formLogin:inputSenha', '0327')
click_id('.ui-button-text.ui-c')
click_id('formPrincipal:grupos:7:j_idt22_header')
click_id('#formPrincipal .ui-panelgrid-cell.ui-grid-col-8 li:first-child a')
# print(driver.find_element_by_css_selector('.ui-button-text.ui-c'))
driver.switch_to.window(driver.window_handles[1])
click_id('sd1')
click_id('#barra > a:first-of-type')
inserir('formTemplate:empenho', notaEmpenho)
click_id('//input[@id="formTemplate:empenho"]/following-sibling::a')
# click_id('sd2')
inserir('formTemplate:j_id52', notaFiscal, 'name')
inserir('formTemplate:j_id56', dataNF.replace('/', ''), 'name')
time.sleep(1)
checkBoxes = driver.find_elements_by_css_selector('tbody .check_table input[type="checkbox"')

for c in checkBoxes:
    c.click()
click_id('formTemplate:salvar')

valorNTI = selecionarElemento('formTemplate:lista:totalNota').get_attribute('value').split(' ')[-1]
if valor != valorNTI: 
    driver.alert('Valor não bate')
    sys.exit(0)

campos = driver.find_elements_by_css_selector('#conteudo tbody span.campo')
ano = campos[0].getAttribute('innerText')
numeroNTI = campos[1].getAttribute('innerText')

driver.alert(ano, numeroNTI)
time.sleep(60)
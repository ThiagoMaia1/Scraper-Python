import time
from typing import Pattern
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
import sys
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# LINK NTI TESTES: https://kiss.ufop.br:8181/Almoxarifado/?idUsuario=47c37828e7eab47a28f696980b69803a&frs=0.9704407878468361

notaEmpenho = '2020NE800689'
notaFiscal = '000162108'
dataNF = '14/01/2021'
valor = 117060.0

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

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\\Users\\UFOP\Desktop\\NEs\\",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome(options=options)
driver.get('https://zeppelin10.ufop.br/minhaUfop/desktop/login.xhtml')
inserir('formLogin:inputIdentificacao', '416.810.188-61')
inserir('formLogin:inputSenha', '0327')
click_id('.ui-button-text.ui-c')
click_id('formPrincipal:grupos:7:j_idt22_header')
click_id('#formPrincipal .ui-panelgrid-cell.ui-grid-col-8 li:first-child a')

# ### CADASTRAR NOTA ###

# click_id('sd1')
# click_id('#barra > a:first-of-type')
# inserir('formTemplate:empenho', notaEmpenho)
# click_id('//input[@id="formTemplate:empenho"]/following-sibling::a')
# inserir('formTemplate:j_id52', notaFiscal, 'name')
# inserir('formTemplate:j_id56', dataNF.replace('/', ''), 'name')

# # checkBoxes = driver.find_elements_by_css_selector('')

# for i in range(500):
#     selectorCheckbox = (By.NAME, 'formTemplate:lista:%s:j_id64' % i)
#     try: driver.find_element(*selectorCheckbox)
#     except: break
#     checkBox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(selectorCheckbox))
#     checkBox.click()
#     time.sleep(0.5)


# time.sleep(1)

# strValorNTI = selecionarElemento('formTemplate:lista:totalNota').get_attribute('value')
# valorNTI = strValorNTI.split(' ')[-1]
# if valor != valorNTI: 
#     print(strValorNTI, valorNTI, valor)
#     print('Valor não bate')
#     sys.exit(0)
# click_id('formTemplate:salvar')

# campos = driver.find_elements_by_css_selector('#conteudo tbody span.campo')
# ano = campos[0].get_attribute('innerText')
# numeroNTI = campos[1].get_attribute('innerText')  

# print(ano, numeroNTI)

# click_id('//*[@title="Imprimir Nota Fiscal"]')

### Cadastrar 

ano = 2021
nota = 30

driver.switch_to.window(driver.window_handles[0])
click_id('.ui-dialog-titlebar-icon.ui-dialog-titlebar-close.ui-corner-all .ui-icon.ui-icon-closethick')
click_id('formPrincipal:grupos:0:j_idt27')
time.sleep(1)
click_id('#formPrincipal\\:painelArea_content li:first-child a')
driver.switch_to.window(driver.window_handles[2])
time.sleep(2)
inserir('txtPesquisaRapida', notaEmpenho)
inserir('txtPesquisaRapida', Keys.ENTER)
resultadosSEI = driver.find_elements_by_css_selector('td.resTituloEsquerda')

for r in resultadosSEI:
    pattern = re.compile("Orçamento")
    if pattern.search(r.get_attribute('innerText')) is not None:
        r.find_element_by_css_selector('.arvore').click()
        break
        
time.sleep(1)
click_id('#topmenu a:first-child')
click_id('#divArvoreAcoes > a:nth-child(2')

click_id('#divArvoreAcoes > a:first-child')
click_id('#tblSeries > tbody > tr:first-child')

# click_id('sd2')

# time.sleep(60)
# driver.close()
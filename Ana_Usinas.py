from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date, timedelta

data_atual = date.today()
semana = date.weekday(data_atual)
dias = (8, 9, 10, 11, 12)
data_anterior = data_atual - timedelta(days = dias[semana])

usinas = ("código das usinas")

chromedrive_path = 'chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedrive_path)
sleep(2)
webdriver.get('https://www.snirh.gov.br/hidrotelemetria/serieHistorica.aspx')

AcessoMapa = webdriver.find_element_by_css_selector('#lnkMapa')
AcessoMapa.click()
sleep(2)
webdriver.get('https://www.snirh.gov.br/hidrotelemetria/serieHistorica.aspx')

for i in usinas:
    webdriver.find_element_by_xpath('/html/body/form/div[5]/div[2]/div[8]/div[2]/div[1]/div[1]/div/input[1]').clear()
    webdriver.find_element_by_xpath('/html/body/form/div[5]/div[2]/div[8]/div[2]/div[1]/div[1]/div/input[1]').click()
    pesquisarpor = webdriver.find_element_by_xpath('/html/body/form/div[5]/div[2]/div[8]/div[2]/div[1]/div[1]/div/input[1]')
    pesquisarpor.send_keys(i)
    pesquisarpor.send_keys(Keys.ENTER)
    sleep(2)

    webdriver.find_element_by_xpath('/html/body/form/div[5]/div[2]/div[8]/div[2]/div[3]/div/table[1]/tbody/tr[1]/td[2]/input').clear()
    campo_de = webdriver.find_element_by_xpath('/html/body/form/div[5]/div[2]/div[8]/div[2]/div[3]/div/table[1]/tbody/tr[1]/td[2]/input')
    campo_de.send_keys(data_anterior.strftime('%d/%m/%Y'))
    sleep(2)

    confirma = webdriver.find_element_by_css_selector('#cphCorpo_ctl01_imbAplicarDrHr')
    confirma.click()
    sleep(2)

    sel_estacao = webdriver.find_element_by_xpath('/html/body/form/div[5]/div[2]/div[8]/div[1]/div/select/option')
    sel_estacao.click()
    sleep(2)

    relatorio = webdriver.find_element_by_css_selector('#cphCorpo_btExportar')
    relatorio.click()
    sleep(2)

webdriver.close()
webdriver.quit()
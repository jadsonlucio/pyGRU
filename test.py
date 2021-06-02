"""import requests

data_json = {
    "codigo_favorecido": "153037",
    "gestao": "15222",
    "codigo_correlacao": "904",
    "nome_favorecido": "UNIVERSIDADE FEDERAL DE ALAGOAS",
    "codigo_recolhimento": "28830-6",
    "nome_recolhimento": "SERVIçOS ADMINISTRATIVOS",
    "referencia": "153037152221714",
    "competencia": "",
    "vencimento": "04/06/2021",
    "cnpj_cpf": "112.930.944-47",
    "nome_contribuinte": "Jadson Lucio dos Santos",
    "valorPrincipal": "1,11",
    "descontos": "0,00",
    "deducoes": "0,00",
    "multa": "0,00",
    "juros": "0,00",
    "acrescimos": "0,00",
    "valorTotal": "0,00",
    "impressao": "SA",
    "pagamento": "1",
    "campo": "NRCR",
    "ind": "0",
}

resp = requests.post(
    "https://consulta.tesouro.fazenda.gov.br/gru_novosite/gerarHTML.asp", data=data_json, verify=False
)

print(resp.status_code)

with open("file.html", "w") as f:
    f.write(resp.text)"""

from pyGRU.core import GRUPDF

data_json = {
    "codigo_favorecido": "153037",
    "gestao": "15222",
    "codigo_correlacao": "904",
    "nome_favorecido": "UNIVERSIDADE FEDERAL DE ALAGOAS",
    "codigo_recolhimento": "28830-6",
    "nome_recolhimento": "SERVIçOS ADMINISTRATIVOS",
    "referencia": "153037152221714",
    "competencia": "",
    "vencimento": "04/06/2021",
    "cnpj_cpf": "112.930.944-47",
    "nome_contribuinte": "Jadson Lucio dos Santos",
    "valorPrincipal": "1,11",
    "descontos": "0,00",
    "deducoes": "0,00",
    "multa": "0,00",
    "juros": "0,00",
    "acrescimos": "0,00",
    "valorTotal": "0,00",
    "impressao": "SA",
    "pagamento": "1",
    "campo": "NRCR",
    "ind": "0",
}

gru = GRUPDF(**data_json)
print(gru.get_barcode())
gru.save_pdf("test.pdf")

"""import PyPDF2

pdfFileObj = open("pdf.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)

print("\n".join(pageObj.extractText()))"""

import io
import os
import requests
import PyPDF2


BASE_REQUEST_URL = "https://consulta.tesouro.fazenda.gov.br/gru_novosite"
HTML_URL = os.path.join(BASE_REQUEST_URL, "gerarHTML.asp")
PDF_URL = os.path.join(BASE_REQUEST_URL, "gerarPDF.asp")


class GRUPDF:
    def __init__(
        self,
        codigo_favorecido,
        gestao,
        codigo_correlacao,
        nome_favorecido,
        codigo_recolhimento,
        nome_recolhimento,
        referencia,
        vencimento,
        cnpj_cpf,
        nome_contribuinte,
        valorPrincipal,
        valorTotal,
        descontos=0,
        deducoes=0,
        multa=0,
        juros=0,
        acrescimos=0,
        impressao="SA",
        competencia="",
        pagamento=1,
        campo="NRCR",
        ind=0,
    ) -> None:
        self.data = {
            "codigo_favorecido": codigo_favorecido,
            "gesta": gestao,
            "codigo_correlacao": codigo_correlacao,
            "nome_favorecido": nome_favorecido,
            "codigo_recolhimento": codigo_recolhimento,
            "nome_recolhimento": nome_recolhimento,
            "referencia": referencia,
            "vencimento": vencimento,
            "cnpj_cpf": cnpj_cpf,
            "nome_contribuinte": nome_contribuinte,
            "valorPrincipal": valorPrincipal,
            "valorTotal": valorTotal,
            "descontos": descontos,
            "deducoes": deducoes,
            "multa": multa,
            "juros": juros,
            "acrescimos": acrescimos,
            "impressao": impressao,
            "competencia": competencia,
            "pagamento": pagamento,
            "campo": campo,
            "ind": ind,
        }

        self.pdf_obj = None

    def get_pdf_obj(self):
        if self.pdf_obj is None:
            resp = requests.post(PDF_URL, self.data, verify=False)
            self.pdf_obj = resp.content

        return self.pdf_obj

    def save_pdf(self, path):
        with open(path, "wb") as f:
            f.write(self.get_pdf_obj())

    def get_barcode(self):
        pdfReader = PyPDF2.PdfFileReader(io.BytesIO(self.get_pdf_obj()))
        pageObj = pdfReader.getPage(0)
        barcode = pageObj.extractText()[-54:]
        return barcode

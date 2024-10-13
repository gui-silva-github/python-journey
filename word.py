from docx import Document
from datetime import datetime
import pandas as pd

tabela = pd.read_excel(r"P:/Guilherme/Python/Informações.xlsx")

    for linha in tabela.index:
        documento = Document(r"P:/Guilherme/Python/Contrato.docx")

        nome = tabela.loc[linha, "Nome"]
        item1 = tabela.loc[linha, "Item1"]
        item2 = tabela.loc[linha, "Item2"]
        item3 = tabela.loc[linha, "Item3"]

        referencias = {
            "XXXX": nome,
            "YYYY": item1,
            "ZZZZ": item2,
            "WWWW": item3,
            "DD": str(datetime.now().day),
            "MM": str(datetime.now().month),
            "AAAA": str(datetime.now().year),
        }

        for paragrafo in documento.paragraphs:
            for codigo in referencias:
                valor = referencias[codigo]
                paragrafo.text = paragrafo.text.replace(codigo, valor)

        documento.save(f"P:\Guilherme\Python\Contrato - {nome}.docx")
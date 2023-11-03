import logging
from time import sleep
import openpyxl
from playwright.sync_api import sync_playwright
import flet as ft

# Constants
URL_ERROR_TEXT = "URL do formulário não foi inserido"
FILE_ERROR_TEXT = "Selecione um arquivo"
NO_FILE_SELECTED = "Nenhum arquivo selecionado"
URL_SUCCESS_TEXT = "URL inserida com sucesso"
FILLING_TEXT = "Preenchimento em andamento"
COMPLETION_TEXT = "Preenchimento concluído"

# Magic Numbers
PAGE_LOAD_TIME = 2
FORM_SUBMIT_TIME = 3

# Set up logging
logging.basicConfig(level=logging.ERROR)


def main(page: ft.Page):
    """Main function to handle form filling"""
    page.title = "Preenchedor de Formulários"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def executar_script(e):
        """Function to execute the script"""
        if not fldURL.value:
            fldURL.error_text = URL_ERROR_TEXT
            page.update()
        elif not txtCaminhoArquivo.value:
            fldURL.error_text = FILE_ERROR_TEXT
            txtCaminhoArquivo.value = NO_FILE_SELECTED
            page.update()
            txtCaminhoArquivo.value = ""
        else:
            url = fldURL.value
            caminhoArquivo = txtCaminhoArquivo.value
            fldURL.error_text = URL_SUCCESS_TEXT
            fldURL.error_style = ft.TextStyle(color="green")
            page.update()
            logging.info(f"URL: {url}")
            logging.info(f"File Path: {caminhoArquivo}")
            fill_form(url, caminhoArquivo)

    def fill_form(url: str, caminhoArquivo: str):
        """Function to fill the form"""
        txtConclusao.value = FILLING_TEXT
        txtConclusao.color = ft.colors.ORANGE
        page.update()
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context()
            webPage = context.new_page()
            try:
                wb = openpyxl.load_workbook(caminhoArquivo)
                sh_users = wb['data']
                for linha in sh_users.iter_rows(min_row=2):
                    webPage.goto(url)
                    sleep(PAGE_LOAD_TIME)
                    fill_fields(webPage, linha)
                    webPage.get_by_role("button", name="Enviar").click()
                    sleep(FORM_SUBMIT_TIME)
            except Exception as e:
                logging.error(f"Error: {e}")
            finally:
                context.close()
                browser.close()
        txtConclusao.value = COMPLETION_TEXT
        page.update()

    def fill_fields(webPage, linha):
        """Function to fill the form fields"""
        webPage.get_by_label("Nome *").fill(linha[0].value)
        webPage.get_by_label("E-mail *").fill(linha[1].value)
        webPage.get_by_label("Endereço *").fill(linha[2].value)
        webPage.get_by_label("Número de telefone").fill(linha[3].value)
        webPage.get_by_label("Comentários").fill(linha[4].value)

    def dialog_picker(e: ft.FilePickerResultEvent):
        """Function to handle file picker dialog"""
        txtCaminhoArquivo.value = e.files[0].path
        txtCaminhoArquivo.update()

    txtTitulo = ft.Text(
        value="Preenchedor de Formulários",
        color="yellow",
        size=30,
    )

    fldURL = ft.TextField(
        label="Cole aqui a URL do seu formulário",
        text_align=ft.TextAlign.RIGHT,
        width=1000,
    )

    txtCaminhoArquivo = ft.Text("")
    meuArquivo = ft.FilePicker(on_result=dialog_picker)
    page.overlay.append(meuArquivo)
    btnSelecionarArquivo = ft.ElevatedButton(
        "Selecionar Arquivo", on_click=lambda _: meuArquivo.pick_files()
    )

    btnExecutar = ft.ElevatedButton(
        "Iniciar Preenchimento Automático", on_click=executar_script
    )

    txtConclusao = ft.Text(
        value="",
        color="green",
        size=15,
    )

    page.add(
        ft.Column(
            [
                txtTitulo,
                fldURL,
                btnSelecionarArquivo,
                txtCaminhoArquivo,
                btnExecutar,
                txtConclusao,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)

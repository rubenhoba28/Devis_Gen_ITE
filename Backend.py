
import typer
import requests
import os
from dataclasses import dataclass
from typing import List
from datetime import datetime, timedelta
import random
import string
import fitz #PyMuPdf

import sys
import os

def resource_path(relative_path):
    """ Obtenez le chemin d'accès aux ressources, fonctionne pour le développement et pour l'exécutable unique."""
    try:
        # Si l'application est compilée, le chemin d'accès est relatif au dossier temporaire _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Sinon, le chemin d'accès est relatif au dossier actuel
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

@dataclass
class Invoice:
    from_who: str
    to_who: str
    logo: str
    number: str
    date: str
    due_date: str
    items: List[dict]
    notes: str
    header: str
    quantity_header: str
    unit_cost_header: str
    currency: str
    amount_header: str
    fields: {}
    tax: int
    subtotal_title: str
    tax_title: str
    total_title: str


class InfoParser:
    def __init__(self):
        self.field_names = (
            'from_who',
            'to_who',
            'logo',
            'number',
            'date',
            'due_date',
            'items',
            'notes',
            'header',
            'quantity_header',
            'unit_cost_header',
            'currency',
            'amount_header',
            'fields'
            'tax',
            'subtotal_title',
            'tax_title',
            'total_title'

        )

    def get_invoices(self, nom_client_value, superficie_value, adresse_value, telephone_value, logement_value,
                     chauffage_value,prix_value,produits):

        invoice_item = Invoice("", "", "", "", "", "", [], "", "", "", "", "", "", {}, 0, "", "", "")
        invoice_item.from_who = ("SAS SENERGIE\n 38 Avenue du 8 Mai 95200 SARCELLES\n Tél : 01 76 42 10 58\n "
                                 "contact@senergie.fr")
        invoice_item.to_who = (nom_client_value +
                               "\n" + adresse_value +
                               "\n Tél : " + telephone_value +
                               "\n Type de chauffage : " + chauffage_value +
                               "\n Type de logement : " + logement_value)
        invoice_item.logo = ("https://encrypted-tbn0.gstatic.com/images?q=tbn"
                             ":ANd9GcTSoSn3trOczwYhC3FAOGVwQN_B3V48NSnSgFqJOhtdog&s")
        invoice_item.number = ''.join(random.choices(
                    string.digits, k=6))
        invoice_item.fields = {"tax": "%", "discounts": False, "shipping": False}
        invoice_item.tax = 5.5
        invoice_item.date = str(datetime.today().strftime("%d/%m/%Y"))
        invoice_item.due_date = str((datetime.today() + timedelta(days=60)).strftime("%d/%m/%Y"))
        invoice_item.items = [{"name": "Montage - Démontage de l'echafaudage mise en securité du chantier"
                                       "\nProtection du sol et des ouvrants"
                                       "\nRespect des normes de securité", "quantity": int(superficie_value),
                               "unit_cost": float(prix_value) * 0.017 / float(superficie_value)
                               },
                              {
                                  "name": "Fourniture et pose de panneaux de polystyrène expanse (PSE),\n spécialement "
                                          "conçus pour l'isolation thermique par l'extérieur"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.472 / float(superficie_value)
                              }, {
                                  "name": "Rails de départs pour soubassement et chevilles pour fixations des rails"
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.027 / float(superficie_value)
                              },
                              {
                                  "name": "Pack de chevilles à frapper pour EPS"
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.032 / float(superficie_value)
                              },
                              {
                                  "name": "Rouleaux d'armature - Fibre verre"
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.032 / float(superficie_value)
                              },
                              {
                                  "name": "Colle et sous enduit."
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.137 / float(superficie_value)
                              },
                              {
                                  "name": "Cornières d'angles entoilées pour ouverture et goutte"
                                          " d'eau PVC avec trame de verre"
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.032 / float(superficie_value)
                              },
                              {
                                  "name": "Fourniture et pose d’appuis de fenêtres en aluminium et rails de couronnement."
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.032 / float(superficie_value)
                              },
                              {
                                  "name": "Tube acrylique pour les jonctions bois et menuiseries."
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.008 / float(superficie_value)
                              },
                              {
                                  "name": "Régulateur de fond avant l'enduit final"
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.024 / float(superficie_value)
                              },
                              {
                                  "name": "Enduit final - Finition en gréser taloché sur toute la surface des panneaux"
                                          "\nNécessaire à l’intégralité de l'ensemble"
                                  , "quantity": int(superficie_value), "unit_cost": float(prix_value) * 0.187 / float(superficie_value)
                              }
                              ]

        # Affichage des produits et de leurs prix
        print("Produits et prix saisis :")
        for nom, prix,quantity in produits:
            item = {"name" : nom + "\nNécessaire à l’intégralité de l'ensemble", "quantity": int(quantity), "unit_cost": float(prix)}
            invoice_item.items.append(item)
            print(f"Nom du produit: {nom}, Prix: {prix}")

        invoice_item.header = "DEVIS"
        invoice_item.quantity_header = "Quantité"
        invoice_item.unit_cost_header = "Prix unitaire"
        invoice_item.subtotal_title = "Total HT"
        invoice_item.tax_title = "TVA"
        invoice_item.total_title = "Total TTC"
        invoice_item.currency = "EUR"
        invoice_item.amount_header = "Montant HT"

        return invoice_item


class MakeInvoice:
    def __init__(self):
        self.endpoint = "https://invoice-generator.com"
        self.download_dir = os.path.join(os.path.expanduser("~"), "Downloads")  # Répertoire de téléchargement
        self.headers = {'Content-Type': 'application/json', 'Accept-Language': 'fr-FR'}

    def convertJSON(self, invoice: Invoice):
        parsed = {
            'header': invoice.header,
            'quantity_header': invoice.quantity_header,
            'unit_cost_header': invoice.unit_cost_header,
            'from': invoice.from_who,
            'to': invoice.to_who,
            'logo': invoice.logo,
            'number': invoice.number,
            'date': invoice.date,
            'due_date': invoice.due_date,
            'items': invoice.items,
            'notes': invoice.notes,
            'currency': invoice.currency,
            'amount_header': invoice.amount_header,
            'fields': invoice.fields,
            'tax': invoice.tax,
            'subtotal_title': invoice.subtotal_title,
            'tax_title': invoice.tax_title,
            'total_title': invoice.total_title

        }
        return parsed

    def save_to_pdf(self, content, invoice: Invoice):
        invoice_name = f"{invoice.number}_invoice.pdf"
        invoice_path = os.path.join(self.download_dir,invoice_name)  # Chemin complet pour enregistrer l'invoice dans le dossier de téléchargement
        with open(invoice_path, 'wb') as f:
            typer.echo(f"Making invoice {invoice_name}")
            f.write(content)
        # Ouvrir le PDF principal et le PDF à insérer

        pdf = fitz.open(invoice_path)
        page = pdf[-1]
        page.clean_contents()
        text = "m²"
        page.insert_text(fitz.Point(391, 31),  # bottom-left of 1st char
                         text,  # the text (honors '\n')
                         fontname="helv",  # the default font
                         fontsize=10,  # the default font size
                         rotate=0,  # also available: 90, 180, 270
                         )
        page.insert_text(fitz.Point(391, 69),  # bottom-left of 1st char
                         text,  # the text (honors '\n')
                         fontname="helv",  # the default font
                         fontsize=10,  # the default font size
                         rotate=0,  # also available: 90, 180, 270
                         )
        page.insert_text(fitz.Point(391, 107.5),  # bottom-left of 1st char
                         text,  # the text (honors '\n')
                         fontname="helv",  # the default font
                         fontsize=10,  # the default font size
                         rotate=0,  # also available: 90, 180, 270
                         )

        pdf.save(invoice_path, deflate=True, deflate_images=True, deflate_fonts=True, incremental=True,
                 encryption=fitz.PDF_ENCRYPT_KEEP)
        pdf.close()
        fin_de_page = resource_path("fin_de_page.pdf")
        doc_principal = fitz.open(invoice_path)
        doc_a_inserer = fitz.open(fin_de_page)

        # Sélectionner la dernière page du document principal
        derniere_page = doc_principal[-1]

        # Sélectionner la première page du PDF à insérer (ajustez si nécessaire)
        page_a_inserer = doc_a_inserer[0]

        # Déterminer la nouvelle taille et la position pour l'insertion
        # Exemple : réduire et déplacer plus bas
        largeur_image, hauteur_image = 600, 300  # Nouvelles dimensions souhaitées
        position_bas = 0  # Combien de pixels du bas de la page

        # Calculer la position pour mettre le contenu en bas à gauche
        x0, y0 = 20, derniere_page.rect.height - position_bas - hauteur_image
        x1, y1 = largeur_image, derniere_page.rect.height - position_bas

        # Créer un rectangle pour définir où et comment le PDF sera inséré
        rect_insertion = fitz.Rect(x0, y0, x1, y1)

        # Insérer le contenu du PDF à la position spécifiée
        derniere_page.show_pdf_page(rect_insertion, doc_a_inserer, 0)  # 0 est l'indice de la page à insérer

        # Sauvegarder le PDF modifié
        doc_principal.save(invoice_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)

        pdf = fitz.open(invoice_path)
        page = pdf[-1]
        largeur_page, hauteur_page = page.rect.width, page.rect.height
        hauteur_widget = 15  # Exemple : 15 points de haut
        self.create_widget_text(220, hauteur_page - hauteur_widget - 255, 270, hauteur_page - 255, page, "montant paiement comptant")
        self.create_widget_text(230, hauteur_page - hauteur_widget - 240, 280, hauteur_page - 240, page, "montant financement")
        self.create_widget_text(380, hauteur_page - hauteur_widget - 240, 450, hauteur_page - 240, page, "oragnisme")
        self.create_widget_text(390, hauteur_page - 10 - 227, 450, hauteur_page - 227, page, "TAEG")
        self.create_widget_text(260, hauteur_page - 10 - 227, 310, hauteur_page - 227, page, "mensualite")
        self.create_widget_text(150, hauteur_page - 10 - 227, 200, hauteur_page - 227, page, "remboursement")
        self.create_widget_text(390, hauteur_page - 10 - 215, 450, hauteur_page - 215, page, "report")
        self.create_widget_text(260, hauteur_page - 10 - 215, 310, hauteur_page - 215, page, "cout total")
        self.create_widget_text(130, hauteur_page - 10 - 215, 170, hauteur_page - 215, page, "taux debiteur")
        self.create_widget_text(75, hauteur_page - 40 - 75, 160, hauteur_page - 75, page, "sign client")
        self.create_widget_text(450, hauteur_page - 14 - 98, 570, hauteur_page - 98, page, "name conseiller")
        self.create_widget_text(430, hauteur_page - 18 - 45, 590, hauteur_page - 45, page, "sign conseiller")
        self.create_widget_text(73, hauteur_page - 10 - 147, 150, hauteur_page - 147, page, "Date")
        self.create_widget_checkbox(57, hauteur_page - hauteur_widget - 255, 76, hauteur_page - 255, page, "check paiement comptant")
        self.create_widget_checkbox(57, hauteur_page - hauteur_widget - 237, 76, hauteur_page - 237, page, "check financement")
        page = pdf[0]
        page.clean_contents()
        text = "m²"
        self.add_text(page, fitz.Point(391, 352.5), text)
        self.add_text(page, fitz.Point(391, 421), text)
        self.add_text(page, fitz.Point(391, 459), text)
        self.add_text(page, fitz.Point(391, 512.5), text)
        self.add_text(page, fitz.Point(391, 550.5), text)
        self.add_text(page, fitz.Point(391, 588.5), text)
        self.add_text(page, fitz.Point(391, 627), text)
        self.add_text(page, fitz.Point(391, 680), text)
        pdf.save(invoice_path, deflate=True, deflate_images=True, deflate_fonts=True, incremental=True,
                 encryption=fitz.PDF_ENCRYPT_KEEP)

    def add_text(self, page, point, text):
        page.insert_text(point,  # bottom-left of 1st char
                         text,  # the text (honors '\n')
                         fontname="helv",  # the default font
                         fontsize=10,  # the default font size
                         rotate=0,  # also available: 90, 180, 270
                         )


    def create_widget_text(self, x0, y0, x1, y1, page, name):
        form_field_rect = fitz.Rect(x0, y0, x1, y1)  # Créer le rectangle pour le champ de formulaire
        form_field_rect = form_field_rect * page.derotation_matrix
        widget = fitz.Widget()
        widget.rect = form_field_rect
        widget.field_type = fitz.PDF_WIDGET_TYPE_TEXT
        widget.field_name = name
        widget.field_value = ""
        page.add_widget(widget)

    def create_widget_checkbox(self, x0, y0, x1, y1, page, name):
        form_field_rect = fitz.Rect(x0, y0, x1, y1)  # Créer le rectangle pour le champ de formulaire
        form_field_rect = form_field_rect * page.derotation_matrix
        widget = fitz.Widget()
        widget.rect = form_field_rect
        widget.field_type = fitz.PDF_WIDGET_TYPE_CHECKBOX
        widget.field_name = name
        page.add_widget(widget)

    def get_invoice(self, invoice):
            r = requests.post(self.endpoint,
                              json=self.convertJSON(invoice),
                              headers=self.headers)

            if r.status_code == 200:
                self.save_to_pdf(r.content, invoice)
                typer.echo("File Saved!")
            else:
                typer.echo(f"Fail: {r.text}")




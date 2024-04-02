import tkinter as tk
from tkinter import Frame, Label, Entry, OptionMenu

import typer
import requests
import os
from dataclasses import dataclass
from typing import List
from datetime import datetime, timedelta
import random
import string
import sys


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

    def create_sign_box(self):
        rectangle = ("\n_________________________\n\n\n"
                     "\n\n_________________________")

        return rectangle

    def get_invoices(self, nom_client_value, superficie_value, adresse_value, telephone_value, logement_value,
                     chauffage_value,prix_value):

        percentages_price = [0.017, 0.473, 0.027, 0.032, 0.032, 0.137, 0.032, 0.032, 0.008, 0.024, 0.187]
        invoice_item = Invoice("", "", "", "", "", "", [], "", "", "", "", "", "", {}, 0, "", "", "")
        invoice_item.from_who = ("SAS SENERGIE\n 3 BOULEVARD ALBERT CAMUS 95200 SARCELLES\n Tél : 01 76 42 10 58\n "
                                 "contact@senergie.fr")
        invoice_item.to_who = (nom_client_value +
                               "\n" + adresse_value +
                               "\n Tél : " + telephone_value +
                               "\n Zone : H2 Précarité : Modeste\n Type de chauffage : " + chauffage_value +
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
        invoice_item.notes = (
                "Pour être accepté, le devis doit être daté, signé et suivi de la mention manuscrite « Bon pour accord »\n"
                "Le: \n Signature:" + self.create_sign_box()
        )
        invoice_item.header = "DEVIS"
        invoice_item.quantity_header = "Quantité (m²)"
        invoice_item.unit_cost_header = "Prix au m²"
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
        invoice_path = os.path.join(self.download_dir,
                                    invoice_name)  # Chemin complet pour enregistrer l'invoice dans le dossier de téléchargement
        with open(invoice_path, 'wb') as f:
            typer.echo(f"Making invoice {invoice_name}")
            f.write(content)

    def get_invoice(self, invoice):
        r = requests.post(self.endpoint,
                          json=self.convertJSON(invoice),
                          headers=self.headers)

        if r.status_code == 200:
            self.save_to_pdf(r.content, invoice)
            typer.echo("File Saved!")
        else:
            typer.echo(f"Fail: {r.text}")



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Devis Client ITE")
        self.configure(bg='white')
        self.geometry("550x710")  # Largeur x Hauteur

        # Variables pour stocker les valeurs des champs du formulaire
        self.nom_client = tk.StringVar()
        self.superficie = tk.StringVar()
        self.prix = tk.StringVar()
        self.adresse = tk.StringVar()
        self.telephone = tk.StringVar()
        self.email = tk.StringVar()
        self.type_logement = tk.StringVar()
        self.type_chauffage = tk.StringVar()

        # Charger et afficher le logo
        logo_path = 'logo_senergie_final.png'
        self.logo_image = tk.PhotoImage(file=logo_path).subsample(1, 1)  # Ajuster selon vos besoins
        logo_label = tk.Label(self, image=self.logo_image, bg='white')
        logo_label.pack(anchor='nw', padx=10, pady=10)  # Ajouter un padding pour l'espace autour du logo
        logo_label.config(width=self.logo_image.width(),
                          height=self.logo_image.height())  # Définir la taille maximale du logo

        # Cadre pour les entrées
        entries_frame = Frame(self, bg='white')
        entries_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Superficie en m²
        Label(entries_frame, text="Nom du client:", bg='white').grid(row=0, column=0, sticky='w')
        Entry(entries_frame, textvariable=self.nom_client).grid(row=0, column=1, pady=5)

        # Superficie en m²
        Label(entries_frame, text="Superficie en m²:", bg='white').grid(row=1, column=0, sticky='w')
        Entry(entries_frame, textvariable=self.superficie).grid(row=1, column=1, pady=5)

        # Prix total hors taxe
        Label(entries_frame, text="Prix total hors taxe:", bg='white').grid(row=2, column=0, sticky='w')
        Entry(entries_frame, textvariable=self.prix).grid(row=2, column=1, pady=5)

        # Informations du client
        Label(entries_frame, text="Adresse:", bg='white').grid(row=3, column=0, sticky='w')
        Entry(entries_frame, textvariable=self.adresse).grid(row=3, column=1, pady=5)

        Label(entries_frame, text="Téléphone:", bg='white').grid(row=4, column=0, sticky='w')
        Entry(entries_frame, textvariable=self.telephone).grid(row=4, column=1, pady=5)

        # Type de logement
        Label(entries_frame, text="Type de logement:", bg='white').grid(row=5, column=0, sticky='w')
        logement_options = ["Appartement", "Maison Individuelle"]
        OptionMenu(entries_frame, self.type_logement, *logement_options).grid(row=5, column=1, pady=5)

        # Type de chauffage
        Label(entries_frame, text="Type de chauffage:", bg='white').grid(row=6, column=0, sticky='w')
        chauffage_options = ["Electrique", "Gaz", "Fioul", "Bois", "Autre"]
        OptionMenu(entries_frame, self.type_chauffage, *chauffage_options).grid(row=6, column=1, pady=5)

        # Bouton Submit
        submit_button = tk.Button(self, text="Submit", command=self.main)
        submit_button.pack(pady=10)

        self.message_label = Label(self, text="", bg='white')
        self.message_label.pack(pady=10)

        # Bouton "Faire un devis à nouveau"
        new_quote_button = tk.Button(self, text="Faire un devis à nouveau", command=self.clear_form)
        new_quote_button.pack(pady=5)

    def clear_form(self):
        # Effacer les valeurs des champs du formulaire
        self.nom_client.set('')  # Effacer le champ du nom du client
        self.superficie.set('')
        self.prix.set('')
        self.adresse.set('')
        self.telephone.set('')
        self.type_logement.set('')
        self.type_chauffage.set('')
        self.message_label.config(text="")


    def main(self):
        # Récupérer les valeurs des champs
        nom_client_value = self.nom_client.get()
        superficie_value = self.superficie.get()
        prix_value = self.prix.get()
        prix_value =prix_value.replace(',','.')
        adresse_value = self.adresse.get()
        telephone_value = self.telephone.get()
        logement_value = self.type_logement.get()
        chauffage_value = self.type_chauffage.get()

        maker = MakeInvoice()
        parser = InfoParser()
        invoice = parser.get_invoices(nom_client_value, superficie_value, adresse_value, telephone_value,
                                      logement_value, chauffage_value,prix_value)
        maker.get_invoice(invoice)
        self.message_label.config(text="Le devis est disponible dans vos téléchargements.")


if __name__ == "__main__":
    app = Application()
    app.mainloop()

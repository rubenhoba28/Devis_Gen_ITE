import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from Backend import *

class Application():
    def __init__(self):
        self.root = tb.Window(themename='sandstone')
        self.root.title("Devis Client ITE")
        self.root.geometry("700x900")
        self.root.resizable(True, True)  # Autoriser la redimensionnement de la fenêtre


        # Variables pour stocker les valeurs des champs du formulaire
        self.nom_client = tk.StringVar()
        self.superficie = tk.StringVar()
        self.prix = tk.StringVar()
        self.adresse = tk.StringVar()
        self.telephone = tk.StringVar()
        self.email = tk.StringVar()
        self.type_logement = tk.StringVar()
        self.type_chauffage = tk.StringVar()

        # Frame qui sera ajouté au Canvas
        self.scrollable_frame = ScrolledFrame(self.root, autohide=True)
        self.scrollable_frame.pack(fill='both', expand=True)

        # Charger et afficher le logo (Assurez-vous d'ajuster le chemin d'accès selon vos besoins)
        logo_path = 'logo_senergie_final.png'
        self.logo_image = tk.PhotoImage(file=logo_path)
        logo_label = ttk.Label(self.scrollable_frame, image=self.logo_image)
        logo_label.pack(padx=10, pady=10)

        entries_frame = ttk.Frame(self.scrollable_frame)
        entries_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Superficie en m²
        ttk.Label(entries_frame, text="Nom du client:").grid(row=0, column=0, sticky='w')
        ttk.Entry(entries_frame, textvariable=self.nom_client).grid(row=0, column=1, pady=5)

        # Superficie en m²
        ttk.Label(entries_frame, text="Superficie en m²:").grid(row=1, column=0, sticky='w')
        ttk.Entry(entries_frame, textvariable=self.superficie).grid(row=1, column=1, pady=5)

        # Prix total hors taxe
        ttk.Label(entries_frame, text="Prix total hors taxe:").grid(row=2, column=0, sticky='w')
        ttk.Entry(entries_frame, textvariable=self.prix).grid(row=2, column=1, pady=5)

        # Informations du client
        ttk.Label(entries_frame, text="Adresse:").grid(row=3, column=0, sticky='w')
        ttk.Entry(entries_frame, textvariable=self.adresse).grid(row=3, column=1, pady=5)

        ttk.Label(entries_frame, text="Téléphone:").grid(row=4, column=0, sticky='w')
        ttk.Entry(entries_frame, textvariable=self.telephone).grid(row=4, column=1, pady=5)

        # Type de logement
        logement_label = ttk.Label(entries_frame, text="Type de logement:")
        logement_label.grid(row=5, column=0, sticky='w')
        logement_options = ["Appartement", "Maison Individuelle"]
        logement_combobox = ttk.Combobox(entries_frame, textvariable=self.type_logement, values=logement_options)
        logement_combobox.grid(row=5, column=1, pady=5)

        # Type de chauffage
        chauffage_label = ttk.Label(entries_frame, text="Type de chauffage:")
        chauffage_label.grid(row=6, column=0, sticky='w')
        chauffage_options = ["Electrique", "Gaz", "Fioul", "Bois", "Autre"]
        chauffage_combobox = ttk.Combobox(entries_frame, textvariable=self.type_chauffage, values=chauffage_options)
        chauffage_combobox.grid(row=6, column=1, pady=5)

        # Sélection du nombre de produits à ajouter
        self.nombre_produits = tk.IntVar()
        ttk.Label(entries_frame, text="Nombre de produits à ajouter:").grid(row=7, column=0, sticky='w')
        spinbox = ttk.Spinbox(entries_frame, from_=1, to=10, textvariable=self.nombre_produits)
        spinbox.grid(row=7, column=1, pady=5)

        # Cadre pour les produits
        self.produits_frame = ttk.Frame(self.scrollable_frame)
        self.produits_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Bouton "Entrer"
        enter_button = ttk.Button(entries_frame, text="Entrer", command=self.update_produit_entries,
                                  bootstyle="success")
        enter_button.grid(row=7, column=2, padx=5)

        # Bouton Submit
        submit_button = ttk.Button(self.scrollable_frame, text="Submit", command=self.main, bootstyle="success")
        submit_button.pack(pady=10)

        self.message_label = ttk.Label(self.scrollable_frame, text="")
        self.message_label.pack(pady=10)

        # Bouton "Faire un devis à nouveau"
        new_quote_button = ttk.Button(self.scrollable_frame, text="Faire un devis à nouveau", command=self.clear_form)
        new_quote_button.pack(pady=5)

        self.produit_entries = []
    def update_produit_entries(self):
        # Efface les anciens champs de produit s'ils existent
        for widget in self.produits_frame.winfo_children():
            widget.destroy()

        # Réinitialise la liste des références aux champs d'entrée
        self.produit_entries.clear()

        # Crée de nouveaux champs de produit en fonction du nombre spécifié
        for i in range(self.nombre_produits.get()):
            row = i
            nom_label = ttk.Label(self.produits_frame, text=f"Nom du produit {i + 1}:")
            nom_label.grid(row=row, column=0, sticky='w', pady=5)  # Ajouté pady pour l'espacement vertical
            nom_entry = ttk.Entry(self.produits_frame)
            nom_entry.grid(row=row, column=1, pady=5, padx=5)  # Ajouté padx pour l'espacement horizontal

            prix_label = ttk.Label(self.produits_frame, text="Prix:")  # Texte simplifié pour "Prix"
            prix_label.grid(row=row, column=2, sticky='w', pady=5)

            prix_entry = ttk.Entry(self.produits_frame)
            prix_entry.grid(row=row, column=3, pady=5)

            # Stocker les références aux champs d'entrée dans la liste
            self.produit_entries.append((nom_entry, prix_entry))


    def recuperer_produits(self):
        """Récupère les noms et les prix des produits à partir des champs d'entrée."""
        produits = []
        for nom_entry, prix_entry in self.produit_entries:
            nom = nom_entry.get()
            prix = prix_entry.get()
            produits.append((nom, prix))
        return produits

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
        prix_value = prix_value.replace(',', '.')
        adresse_value = self.adresse.get()
        telephone_value = self.telephone.get()
        logement_value = self.type_logement.get()
        chauffage_value = self.type_chauffage.get()
        produits = self.recuperer_produits()

        maker = MakeInvoice()
        parser = InfoParser()
        invoice = parser.get_invoices(nom_client_value, superficie_value, adresse_value, telephone_value,
                                      logement_value, chauffage_value, prix_value, produits)
        maker.get_invoice(invoice)
        self.message_label.config(text="Le devis est disponible dans vos téléchargements.")

if __name__ == '__main__':
    app = Application()
    app.root.mainloop()

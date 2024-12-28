import matplotlib.pyplot as plt
import csv

# Descrizione iniziale
print("Questo script calcola la distribuzione delle tue entrate settimanali includendo tutte le spese, un risparmio suggerito e un costo aggiuntivo per benzina, spesa e utenza telefonica. Genera un grafico a barre e salva i dati in un file CSV.")

# Dati aggiornati
costi_annuali = {
    "condominio": 1021.14,
    "luce_elettrica": 900,
    "gas": 460,
    "acqua": 280,
    "compas": 1080,
    "agos": 384,
    "utenza_telefonica": 372
}

# Calcolo dei costi settimanali
costo_benzina_e_spesa = 70
costi_settimanali_base = sum(costi_annuali.values()) / 52
risparmio_suggerito = 20
costo_totale_settimanale = costi_settimanali_base + costo_benzina_e_spesa

# Entrate settimanali
entrate_settimanali = 250
resto_aggiornato = entrate_settimanali - costo_totale_settimanale - risparmio_suggerito

# Calcolo dei costi settimanali per le utenze
costi_settimanali_utenze = sum(costi_annuali.values()) / 52

# Dati per il grafico
labels = ["Costi Settimanali", "Risparmio Suggerito", "Benzina e Spesa", "Resto", "Utenze Settimanali"]
valori = [costo_totale_settimanale, risparmio_suggerito, costo_benzina_e_spesa, resto_aggiornato, costi_settimanali_utenze]
colori = ["red", "green", "orange", "blue", "purple"]

# Salvataggio dati in un file CSV
csv_file = "dati_finanziari.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Categoria", "Importo (€)"])
    for label, valore in zip(labels, valori):
        writer.writerow([label, f"{valore:.2f}"])

print(f"Dati salvati nel file CSV: {csv_file}")

# Creazione del grafico a barre
plt.figure(figsize=(12, 8))
bars = plt.bar(labels, valori, color=colori, edgecolor="black", linewidth=1.2)

# Aggiunta di valori sopra le barre
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height + 2, f"{height:.2f} €", ha="center", fontsize=10)

# Dettagli del grafico
plt.title("Distribuzione delle Entrate Settimanali con Dettagli Aggiuntivi", fontsize=16)
plt.ylabel("Euro", fontsize=12)
plt.xlabel("Categorie", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.axhline(entrate_settimanali, color='black', linestyle='--', label="Entrate Totali (250 €)")
plt.legend(fontsize=12)

# Aggiunta di una descrizione sotto il grafico
plt.figtext(0.1, -0.1, (
    "Descrizione del Grafico:\n"
    "1. Costi Settimanali: Include le spese per utenze, benzina e spesa.\n"
    "2. Risparmio Suggerito: Un importo consigliato da mettere da parte ogni settimana.\n"
    "3. Benzina e Spesa: Spese specifiche settimanali.\n"
    "4. Resto: La somma che rimane dopo tutte le spese e il risparmio.\n"
    "5. Utenze Settimanali: Importo settimanale calcolato dalle spese annuali per utenze.\n"
    "Suggerimento: Mantieni monitorate le spese non essenziali per incrementare il risparmio."),
    fontsize=10, ha="left")

# Salvataggio del grafico come file immagine
grafico_file = "grafico_finanziario.png"
plt.savefig(grafico_file, bbox_inches="tight")
print(f"Grafico salvato come immagine: {grafico_file}")

# Mostra il grafico
plt.tight_layout()
plt.show()

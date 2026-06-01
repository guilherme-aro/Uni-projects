#=========================================
# CREATED BY: GUILHERME ARO
# DATE: 06/01/2026
# CONTACT MANAGEMENT SYSTEM
#=========================================

import os

ARQUIVO = "contatos.txt"
SEP = ";"

# =========================================
# Initialization
# =========================================

def inicializar():
    """Creates the file if it doesn't exist yet."""
    try:
        with open(ARQUIVO, "x", encoding="utf-8") as f:
            print(f"File '{ARQUIVO}' created successfully.")
    except FileExistsError:
        pass

# =========================================
# Validation Functions
# =========================================

def validar_nome(nome):
    """Validates if the name contains only letters."""
    return bool(nome.strip()) and nome.replace(" ", "").isalpha()

def validar_email(email):
    """Validates basic email format."""
    if not email:
        return True
    return "@" in email and "." in email

# =========================================
# Input Functions
# =========================================

def obter_nome():
    """Gets and validates the contact name."""
    while True:
        nome = input("Name: ").strip()
        if not nome:
            print("Name cannot be empty!")
            continue
        if not validar_nome(nome):
            print("Please enter only letters!")
            continue
        return nome

def obter_telefone():
    """Gets the phone number."""
    while True:
        telefone = input("Phone: ").strip()
        if not telefone:
            print("Phone cannot be empty!")
            continue
        return telefone

def obter_email():
    """Gets and validates the email."""
    while True:
        email = input("Email: ").strip()
        if email and not validar_email(email):
            print("Invalid email format!")
            continue
        return email

# =========================================
# File Operations
# =========================================

def carregar_contatos():
    """Loads all contacts from file."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def salvar_contatos(linhas):
    """Saves contacts back to file."""
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            f.writelines(linhas)
        return True
    except Exception as e:
        print(f"Error saving: {e}")
        return False

# =========================================
# Display Functions
# =========================================

def listar():
    """Displays all saved contacts."""
    print("\n--- CONTACT LIST ---")

    linhas = carregar_contatos()

    if not linhas:
        print("No contacts registered yet.")
        return

    linhas_ordenadas = sorted(linhas, key=lambda x: x.split(SEP)[0].lower())

    contador = 0
    for linha in linhas_ordenadas:
        campos = linha.strip().split(SEP)
        if len(campos) == 3:
            nome, tel, email = campos
            contador += 1
            print(f"[{contador:02d}] {nome:20} | {tel:16} | {email}")

    print(f"\nTotal: {contador} contact(s).\n")

# =========================================
# Search
# =========================================

def buscar():
    """Searches for contacts by name."""
    print("\n--- SEARCH CONTACT ---")
    
    termo = input("Enter the name to search: ").strip().lower()
    
    if not termo:
        print("Please enter a name!")
        return
    
    linhas = carregar_contatos()
    encontrados = 0
    
    for linha in linhas:
        if termo in linha.lower():
            campos = linha.strip().split(SEP)
            if len(campos) == 3:
                nome, tel, email = campos
                print(f"Name: {nome} | Phone: {tel} | Email: {email}")
                encontrados += 1
    
    if encontrados == 0:
        print("No contacts found.")
    else:
        print(f"\n{encontrados} result(s) found.\n")

# =========================================
# Create
# =========================================

def cadastrar():
    """Creates a new contact."""
    print("\n--- REGISTER CONTACT ---")
    
    nome = obter_nome()
    telefone = obter_telefone()
    email = obter_email()
    
    try:
        linha = f"{nome}{SEP}{telefone}{SEP}{email}\n"
        
        with open(ARQUIVO, "a", encoding="utf-8") as f:
            f.write(linha)
        
        print(f"Contact '{nome}' registered successfully!\n")
    except Exception as e:
        print(f"Error registering: {e}\n")

# =========================================
# Edit
# =========================================

def editar():
    """Edits an existing contact."""
    print("\n--- EDIT CONTACT ---")
    
    nome_busca = input("Contact name to edit: ").strip().lower()
    
    if not nome_busca:
        print("Please enter a name!")
        return
    
    linhas = carregar_contatos()
    novas_linhas = []
    editado = False
    
    for linha in linhas:
        campos = linha.strip().split(SEP)
        
        if len(campos) == 3 and nome_busca in campos[0].lower():
            print(f"Contact found: {campos[0]} | Phone: {campos[1]}")
            print("\nWhat do you want to edit?")
            print("(1) Phone")
            print("(2) Email")
            opcao = input("Choose: ").strip()
            
            if opcao == "1":
                campos[1] = input("New phone: ").strip()
            elif opcao == "2":
                campos[2] = input("New email: ").strip()
            else:
                print("Invalid option!")
                novas_linhas.append(linha)
                continue
            
            linha = SEP.join(campos) + "\n"
            editado = True
        
        novas_linhas.append(linha)
    
    if not editado:
        print("Contact not found.\n")
        return
    
    if salvar_contatos(novas_linhas):
        print("Contact updated successfully!\n")

# =========================================
# Delete
# =========================================

def excluir():
    """Deletes one or more contacts by name."""
    print("\n--- DELETE CONTACT ---")
    
    nome_del = input("Contact name to delete: ").strip().lower()
    
    if not nome_del:
        print("Please enter a name!")
        return
    
    linhas = carregar_contatos()
    indices_remover = []
    
    for i, linha in enumerate(linhas):
        campos = linha.strip().split(SEP)
        if len(campos) == 3 and nome_del in campos[0].lower():
            indices_remover.append(i)
            print(f"   • {campos[0]}")
    
    if not indices_remover:
        print("No contacts found.\n")
        return
    
    print(f"\nTotal of {len(indices_remover)} contact(s) to delete.")
    conf = input("Continue? (yes/no): ").strip().lower()
    
    if conf not in ["yes", "s", "y"]:
        print("Operation cancelled.\n")
        return
    
    for i in sorted(indices_remover, reverse=True):
        del linhas[i]
    
    if salvar_contatos(linhas):
        print(f"{len(indices_remover)} contact(s) deleted.\n")

# =========================================
# Menu
# =========================================

def menu():
    """Displays the menu and returns the chosen option."""
    print("""
==================================
   CONTACT MANAGEMENT SYSTEM
==================================
  1. Register contact
  2. List contacts
  3. Search contact
  4. Edit contact
  5. Delete contact
  0. Exit
==================================
""")
    return input("Choose an option: ").strip()

# =========================================
# Main
# =========================================

def main():
    """Main program function."""
    inicializar()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            editar()
        elif opcao == "5":
            excluir()
        elif opcao == "0":
            print("See you later!")
            break
        else:
            print("Invalid option. Try again.\n")
        
        input("Press Enter to continue...")

# =========================================
# Entry Point
# =========================================

if __name__ == "__main__":
    main()
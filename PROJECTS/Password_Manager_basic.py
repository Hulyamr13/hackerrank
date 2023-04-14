import os
import random
import string
import pandas as pd
import pyperclip

# Set default encoding
encoding = 'utf-8'

# Define path for password storage
password_file = 'passwords.csv'

# Check if password file exists, otherwise create one
if not os.path.exists(password_file):
    with open(password_file, 'w', encoding=encoding) as f:
        f.write('Website,Username,Password\n')

# Load passwords into dataframe
df = pd.read_csv(password_file)


# Define functions for password management

def search_password(website):
    """
    Search for a password by website.
    """
    try:
        return df.loc[df['Website'] == website]
    except KeyError:
        print(f"No password found for {website}.")
        return None


def show_all_passwords():
    """
    Display all passwords in the password manager.
    """
    print(df)


def copy_password(website):
    """
    Copy a password to the clipboard by double-clicking on the cell.
    """
    password = df.loc[df['Website'] == website, 'Password'].item()
    pyperclip.copy(password)  # copy to clipboard
    print(f"Password for {website} has been copied to clipboard.")


def generate_password(length=12):
    """
    Generate a random password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def add_password(website, username, password=None):
    """
    Add a new password to the password manager.
    """
    if password is None:
        password = generate_password()
    df.loc[len(df.index)] = [website, username, password]
    print(f"Password added for {website} with username {username} and password {password}.")


def delete_password(website):
    """
    Delete a password from the password manager.
    """
    try:
        df.drop(df[df['Website'] == website].index, inplace=True)
        print(f"Password for {website} has been deleted.")
    except KeyError:
        print(f"No password found for {website}.")


def config_language(language):
    """
    Configure the language setting.
    """
    # TODO: Implement language configuration.


def config_encoding(encoding):
    """
    Configure the encoding setting.
    """
    # TODO: Implement encoding configuration.


def export_cleaned_passwords(file_name):
    """
    Export all cleaned passwords to an Excel file.
    """
    df.to_excel(file_name, index=False)
    print(f"Passwords have been exported to {file_name}.")


def export_encrypted_backup(file_name, master_password):
    """
    Export an encrypted backup of the password manager.
    """
    # TODO: Implement encryption backup functionality.


def import_encrypted_backup(file_name, master_password):
    """
    Import an encrypted backup of the password manager.
    """
    # TODO: Implement encryption backup functionality.


def reset_all_passwords():
    """
    Reset all passwords to a random value.
    """
    df['Password'] = df['Password'].apply(lambda x: generate_password())
    print("All passwords have been reset.")


def change_master_password(old_password, new_password):
    """
    Change the master password for the password manager.
    """
    # TODO: Implement master password change functionality.
    if old_password == 'password123':  # replace with actual master password check
        # update password in password file
        df.to_csv(password_file, index=False)
        print("Master password has been updated.")
    else:
        print("Incorrect old master password.")

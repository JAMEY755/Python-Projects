import re
import tkinter as tk
from tkinter import messagebox, ttk

class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.current_id = 1

    def _validate_phone(self, phone):
        pattern = r"^\+?[0-9\-]+$"
        return bool(re.match(pattern, phone))

    def _validate_email(self, email):
        if not email:
            return True
        return "@" in email and "." in email

    def add_contact(self, name, phone, email=""):
        if not name.strip():
            return False, "Name cannot be empty."

        if not self._validate_phone(phone):
            return False, "Phone number can only contain digits, hyphens, and an optional leading '+'."

        if not self._validate_email(email):
            return False, "Invalid email format. Must contain '@' and '.'."

        self.contacts[self.current_id] = {
            "name": name.strip(),
            "phone": phone.strip(),
            "email": email.strip()
        }
        created_id = self.current_id
        self.current_id += 1
        return True, f"Contact added successfully with ID: {created_id}."

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        if contact_id not in self.contacts:
            return False, "Contact ID not found."

        contact = self.contacts[contact_id]
        new_name = name if name is not None else contact["name"]
        new_phone = phone if phone is not None else contact["phone"]
        new_email = email if email is not None else contact["email"]

        if not new_name.strip():
            return False, "Name cannot be empty."

        if phone is not None and not self._validate_phone(new_phone):
            return False, "Phone number can only contain digits, hyphens, and an optional leading '+'."

        if email is not None and not self._validate_email(new_email):
            return False, "Invalid email format. Must contain '@' and '.'."

        contact["name"] = new_name.strip()
        contact["phone"] = new_phone.strip()
        contact["email"] = new_email.strip()
        return True, f"Contact ID {contact_id} updated successfully."

    def delete_contact(self, contact_id):
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            return True, f"Contact ID {contact_id} deleted successfully."
        return False, "Contact ID not found."

    def search_contacts(self, query):
        query = query.lower().strip()
        results = []
        for cid, info in self.contacts.items():
            if (query in info["name"].lower() or
                query in info["phone"] or
                query in info["email"].lower()):
                results.append((cid, info["name"], info["phone"], info["email"]))
        return results


class ContactManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("820x560")
        self.root.configure(bg="#f4f7ff")
        self.root.resizable(False, False)

        self.manager = ContactManager()
        self.manager.add_contact("Sam Kutesa", "+256-701", "sam.kutesa@example.com")
        self.manager.add_contact("Mary Bata", "0772-111222", "mary.bata@ug.org")

        self._create_widgets()
        self._refresh_contacts()

    def _create_widgets(self):
        header = tk.Label(self.root, text="Contact Manager", bg="#f4f7ff", fg="#2e4f7b",
                          font=("Segoe UI", 20, "bold"))
        header.pack(pady=(16, 6))

        subtitle = tk.Label(self.root, text="GUI for managing contacts", bg="#f4f7ff",
                            fg="#556e8c", font=("Segoe UI", 10))
        subtitle.pack(pady=(0, 18))

        content = tk.Frame(self.root, bg="#f4f7ff")
        content.pack(fill=tk.BOTH, expand=True, padx=16)

        left_panel = tk.Frame(content, bg="#f4f7ff")
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 12))

        form_frame = tk.LabelFrame(left_panel, text="Contact Details", bg="#f4f7ff",
                                   fg="#2e4f7b", font=("Segoe UI", 10, "bold"), padx=12, pady=12)
        form_frame.pack(fill=tk.X, pady=(0, 12))

        tk.Label(form_frame, text="Name:", bg="#f4f7ff", font=("Segoe UI", 10)).grid(row=0, column=0, sticky=tk.W, pady=6)
        tk.Label(form_frame, text="Phone:", bg="#f4f7ff", font=("Segoe UI", 10)).grid(row=1, column=0, sticky=tk.W, pady=6)
        tk.Label(form_frame, text="Email:", bg="#f4f7ff", font=("Segoe UI", 10)).grid(row=2, column=0, sticky=tk.W, pady=6)

        self.name_entry = tk.Entry(form_frame, width=30, font=("Segoe UI", 10))
        self.phone_entry = tk.Entry(form_frame, width=30, font=("Segoe UI", 10))
        self.email_entry = tk.Entry(form_frame, width=30, font=("Segoe UI", 10))

        self.name_entry.grid(row=0, column=1, pady=6, padx=(8, 0))
        self.phone_entry.grid(row=1, column=1, pady=6, padx=(8, 0))
        self.email_entry.grid(row=2, column=1, pady=6, padx=(8, 0))

        action_frame = tk.Frame(left_panel, bg="#f4f7ff")
        action_frame.pack(fill=tk.X)

        self.add_button = tk.Button(action_frame, text="Add Contact", command=self._add_contact,
                                    bg="#4d7cff", fg="white", font=("Segoe UI", 10, "bold"), width=20)
        self.update_button = tk.Button(action_frame, text="Update Contact", command=self._update_contact,
                                       bg="#2e8b57", fg="white", font=("Segoe UI", 10, "bold"), width=20)
        self.delete_button = tk.Button(action_frame, text="Delete Contact", command=self._delete_contact,
                                       bg="#d9534f", fg="white", font=("Segoe UI", 10, "bold"), width=20)
        self.clear_button = tk.Button(action_frame, text="Clear Fields", command=self._clear_fields,
                                      bg="#6c757d", fg="white", font=("Segoe UI", 10), width=20)

        self.add_button.grid(row=0, column=0, pady=6, sticky=tk.W)
        self.update_button.grid(row=1, column=0, pady=6, sticky=tk.W)
        self.delete_button.grid(row=2, column=0, pady=6, sticky=tk.W)
        self.clear_button.grid(row=3, column=0, pady=6, sticky=tk.W)

        right_panel = tk.Frame(content, bg="#f4f7ff")
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        search_frame = tk.Frame(right_panel, bg="#f4f7ff")
        search_frame.pack(fill=tk.X, pady=(0, 12))

        tk.Label(search_frame, text="Search:", bg="#f4f7ff", font=("Segoe UI", 10)).pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame, width=28, font=("Segoe UI", 10))
        self.search_entry.pack(side=tk.LEFT, padx=(8, 6))
        self.search_entry.bind("<Return>", lambda event: self._search_contacts())

        search_button = tk.Button(search_frame, text="Search", command=self._search_contacts,
                                  bg="#4d7cff", fg="white", font=("Segoe UI", 10, "bold"), width=12)
        show_all_button = tk.Button(search_frame, text="Show All", command=self._refresh_contacts,
                                    bg="#5a6268", fg="white", font=("Segoe UI", 10, "bold"), width=12)
        search_button.pack(side=tk.LEFT, padx=(0, 6))
        show_all_button.pack(side=tk.LEFT)

        table_frame = tk.Frame(right_panel, bg="#f4f7ff")
        table_frame.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=26, background="#ffffff", fieldbackground="#ffffff")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#e2e8f0")
        style.map("Treeview", background=[("selected", "#4d7cff")], foreground=[("selected", "white")])

        columns = ("id", "name", "phone", "email")
        self.contact_table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        self.contact_table.heading("id", text="ID")
        self.contact_table.heading("name", text="Name")
        self.contact_table.heading("phone", text="Phone")
        self.contact_table.heading("email", text="Email")
        self.contact_table.column("id", width=50, anchor=tk.CENTER)
        self.contact_table.column("name", width=220)
        self.contact_table.column("phone", width=180)
        self.contact_table.column("email", width=260)

        self.contact_table.bind("<<TreeviewSelect>>", self._on_select)

        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.contact_table.yview)
        self.contact_table.configure(yscroll=scroll_y.set)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_table.pack(fill=tk.BOTH, expand=True)

        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bg="#e8efff", fg="#27374d",
                              font=("Segoe UI", 10), anchor=tk.W, padx=12)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(8, 0))

    def _set_status(self, message, color="#27374d"):
        self.status_var.set(message)

    def _clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.contact_table.selection_remove(self.contact_table.selection())
        self._set_status("Fields cleared.")

    def _refresh_contacts(self):
        self.contact_table.delete(*self.contact_table.get_children())
        for cid, info in sorted(self.manager.contacts.items()):
            email = info["email"] or "N/A"
            self.contact_table.insert("", tk.END, values=(cid, info["name"], info["phone"], email))
        self._set_status("Showing all contacts.")

    def _add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        ok, message = self.manager.add_contact(name, phone, email)
        if ok:
            self._refresh_contacts()
            self._clear_fields()
            messagebox.showinfo("Success", message)
            self._set_status(message)
        else:
            messagebox.showwarning("Add failed", message)
            self._set_status(message)

    def _update_contact(self):
        selection = self.contact_table.selection()
        if not selection:
            messagebox.showwarning("No selection", "Select a contact to update.")
            return
        contact_id = int(self.contact_table.item(selection[0], "values")[0])
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        ok, message = self.manager.update_contact(contact_id, name=name, phone=phone, email=email)
        if ok:
            self._refresh_contacts()
            messagebox.showinfo("Updated", message)
            self._set_status(message)
        else:
            messagebox.showwarning("Update failed", message)
            self._set_status(message)

    def _delete_contact(self):
        selection = self.contact_table.selection()
        if not selection:
            messagebox.showwarning("No selection", "Select a contact to delete.")
            return
        contact_id = int(self.contact_table.item(selection[0], "values")[0])
        if not messagebox.askyesno("Confirm delete", f"Delete contact ID {contact_id}?"):
            return
        ok, message = self.manager.delete_contact(contact_id)
        if ok:
            self._refresh_contacts()
            self._clear_fields()
            messagebox.showinfo("Deleted", message)
            self._set_status(message)
        else:
            messagebox.showerror("Delete failed", message)
            self._set_status(message)

    def _search_contacts(self):
        query = self.search_entry.get().strip()
        self.contact_table.delete(*self.contact_table.get_children())
        if not query:
            self._refresh_contacts()
            return
        results = self.manager.search_contacts(query)
        for cid, name, phone, email in results:
            self.contact_table.insert("", tk.END, values=(cid, name, phone, email or "N/A"))
        self._set_status(f"{len(results)} result(s) for '{query}'.")

    def _on_select(self, event):
        selection = self.contact_table.selection()
        if not selection:
            return
        cid, name, phone, email = self.contact_table.item(selection[0], "values")
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, phone)
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, email if email != "N/A" else "")


def main():
    root = tk.Tk()
    ContactManagerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

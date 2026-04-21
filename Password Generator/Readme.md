#  Password Generator (Python)

A simple and customizable **command-line password generator** built with Python.
Generate secure passwords with options for uppercase letters, numbers, and special characters.

---

##  Features

* Custom password length
* Include/exclude:

  * Uppercase letters (A–Z)
  * Numbers (0–9)
  * Special characters (!@#$%^&*)
* Ensures at least one character from each selected category
* Randomized and shuffled output

---

##  Built With

* Python 3
* Built-in modules:

  * `string`
  * `random`

---


##  Usage Example

```
Enter password length: 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y
```

**Output:**

```
A9!kLp#2xQ@1
```

---

##  Error Handling

If the password length is too short for the selected options:

```
Password length is too short for the specified criteria.
```

---

##  Security Note

This project uses Python’s `random` module, which is **not cryptographically secure**.
For better security, consider using the `secrets` module:

---

##  Future Improvements

* [ ] Switch to `secrets` module
* [ ] Add GUI (Tkinter or PyQt)
* [ ] Password strength checker
* [ ] Export passwords to file

---

## Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

##  License

This project is licensed under the **MIT License**.

---


GitHub: https://github.com/Shujaa93

**Introduction to Python Bytecode**
Python bytecode asal mai Python code ka ek *intermediate form* hota hai jo Python compiler generate karta hai. Jab hum Python code likhte hain, wo sabse pehle bytecode mai compile hota hai — phir Python interpreter use execute karta hai.

---

### **Python Code Kese Compile Hota Hai:**

1. **Lexical Analysis:** Code ko chhote parts (tokens) mai tod diya jata hai jaise keywords, identifiers, aur literals.
2. **Syntax Analysis:** Dekha jata hai ke code sahi syntax follow kar raha hai ya nahi.
3. **Semantic Analysis:** Code ka matlab aur logic check hota hai.
4. **Bytecode Generation:** Ab code compile hoke bytecode mai convert ho jata hai.

---

### **Python Bytecode Kya Hai?**

Python bytecode ek *platform-independent* representation hoti hai jo Python interpreter chala sakta hai. Ye ek binary instructions ka sequence hota hai jo kisi machine ke liye specific nahi hota.

Ye bytecode `.pyc` files mai store hoti hai (jo Python module import karne par banti hain). Ye files interpreter ke through directly run ho sakti hain.

---

### **Example:**

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("Arif Rozani", 20)
person.greet()
```

**Output:**
Hello, my name is Arif Rozani and I am 20 years old.

---

### **Bytecode Dekhne ke Liye:**

```python
import dis
dis.dis(Person)
```

Yahan tumhe har line ka *bytecode instruction* milega — jaise `LOAD_FAST`, `STORE_ATTR`, `RETURN_VALUE`, etc. Ye sab wo commands hain jo interpreter background mai execute karta hai.

---

### **dis Module Kya Hai?**

`dis` module Python ka ek built-in module hai jo bytecode ko *disassemble* (tod kar samjhaane) ke liye use hota hai. Isse tum dekh sakte ho ke Python interpreter tumhara code kis tarah run karta hai.

---

### **Python Bytecode Kyu Important Hai?**

1. **Platform Independent:** Same bytecode kisi bhi OS (Windows, Linux, macOS) par chal sakta hai.
2. **Dynamic Typing:** Variable ka type run time par decide hota hai.
3. **Flexibility:** Bytecode ko modify karna easy hota hai, jisse interpreter ko enhance karna possible hai.

---

### **Python Bytecode Kaise Use Hota Hai:**

1. **Compilation:** Python script ko interpreter compile karta hai bytecode mai.
2. **Execution:** Ye bytecode *Python Virtual Machine (PVM)* ke through run hota hai.
3. **Caching:** Compiled bytecode ko `__pycache__` folder mai store kar diya jata hai taake next time fast chale.

---

### **Kya Bytecode Har OS Par Chal Sakta Hai?**

Haan ✅ — Python bytecode *platform-independent* hota hai. Matlab ek `.pyc` file har OS par chal sakti hai, lekin **Python version same hona chahiye.**

**Lekin kuch limitations hain:**

* `.pyc` file Python version ke saath dependent hoti hai (Python 3.10 ka bytecode Python 3.8 par nahi chalega).
* Kuch OS-specific modules (jaise `os`, `sys`) alag behave karte hain.

---

### **Kya Bytecode Direct Run Kar Sakte Hain?**

Nahi — tumhe Python interpreter ki zarurat hoti hai. Ye Java ke JVM jaisa nahi hai.

---

### **Bytecode Manually Run Karne Ka Tareeqa:**

1. **Compile Code:**

   ```
   python -m compileall TestP.py
   ```

   Ye `__pycache__` folder mai bytecode create karega.
2. **Run Bytecode:**

   ```
   cd __pycache__
   python TestP.cpython-312.pyc
   ```

---

## **Indentation in Python**

### **Introduction:**

Python mai indentation *bahut zaruri* hoti hai. Ye batata hai ke code kaunsa block mai belong karta hai — jaise `if`, `for`, `function`, ya `class`.

### **Indentation Kya Hai?**

Indentation matlab line ke start mai spaces (ya tabs) lagana taake Python ko pata chale ke ye line kis block se related hai.

---

### **Indentation Important Kyu Hai?**

* Code ka structure clear karta hai
* Relationship between lines show karta hai
* Code readable banata hai
* Syntax errors se bachata hai

---

### **Rules of Indentation:**

1. **Consistent raho:** Ya to spaces use karo ya tabs — dono mix mat karo.
2. **4 spaces per level:** Ye standard Python style hai.
3. **Colon (:) ke baad indent karo:** Jaise `if`, `for`, `def` ke baad.
4. **Function aur class ke andar indent zarur do.**

---

### **Examples:**

**✅ Correct:**

```python
if True:
    print("Hello, World!")
    print("This is a block of code")
```

**❌ Incorrect:**

```python
if True:
print("Hello, World!")
  print("This is a block of code")
```

---

### **Best Practices:**

* Hamesha same number of spaces use karo.
* Auto-indentation wali IDE use karo (VSCode, PyCharm).
* Tabs avoid karo (kyunke system ke hisaab se alag size ke ho sakte hain).



# โปรแกรมแปลง PDF เป็น Word แบบง่าย

โปรแกรมนี้เป็นสคริปต์ Python สำหรับแปลงไฟล์ PDF เป็นไฟล์ Word (DOCX) แบบง่าย ๆ ใช้ไลบรารี `pdf2docx` ในการแปลง

## วิธีใช้งาน

1. ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

2. รันคำสั่งแปลงไฟล์

```bash
python pdf_to_word.py path/to/input.pdf
```

ถ้าต้องการระบุชื่อไฟล์ผลลัพธ์เอง

```bash
python pdf_to_word.py path/to/input.pdf -o path/to/output.docx
```

## หมายเหตุ

- ไฟล์ผลลัพธ์จะถูกสร้างในโฟลเดอร์เดียวกับไฟล์ต้นฉบับ หากไม่ระบุ `-o`.
- การแปลง PDF ที่มีรูปแบบซับซ้อนมากอาจได้ผลลัพธ์ไม่สมบูรณ์ขึ้นอยู่กับไฟล์ต้นฉบับ.

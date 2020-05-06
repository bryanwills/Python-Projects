import pdftotext
with open("test.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

print(len(pdf))

for page in pdf:
    print(page)

print(pdf[0])
print(pdf[1])

print("\n\n".join(pdf))

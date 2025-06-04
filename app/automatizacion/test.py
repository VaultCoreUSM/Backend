import os
import shutil




print("📍 Directorio actual:", os.getcwd())
print("📄 Archivo ejecutándose:", __file__)

# Ruta esperada en Linux para wkhtmltopdf
linux_path = "/usr/bin/wkhtmltopdf"

# Alternativamente, usar shutil.which() para buscarlo en PATH
found_path = shutil.which("wkhtmltopdf")

print(f"🔍 Buscando wkhtmltopdf en {linux_path}")
if os.path.exists(linux_path):
    print("✅ wkhtmltopdf ENCONTRADO en /usr/bin/wkhtmltopdf")
else:
    print("❌ wkhtmltopdf NO encontrado en /usr/bin/wkhtmltopdf")

if found_path:
    print(f"✅ wkhtmltopdf también encontrado con shutil: {found_path}")
else:
    print("❌ shutil.which no encontró wkhtmltopdf en PATH")

from PIL import Image
import os

# Папки для входных и выходных файлов
input_folder = "jpeg"
output_folder = "png"

def convert_images():
    # Создаем выходную папку, если её нет
    os.makedirs(output_folder, exist_ok=True)

    # Перебираем все файлы в папке jpeg
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")

            try:
                img = Image.open(input_path)
                img.save(output_path, format="PNG")
                print(f"Конвертировано: {output_path}")
            except Exception as e:
                print(f"Ошибка с файлом {filename}: {e}")

if __name__ == "__main__":
    convert_images()
    print("Конвертация завершена!")

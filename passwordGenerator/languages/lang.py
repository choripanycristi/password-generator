# lang.py

translations = {
    "en": {
        "title": "Password Generator v1.0",
        "password_length": "Password length:",
        "length_12": "12 characters",
        "length_16": "16 characters",
        "length_20": "20 characters",
        "generate": "Generate"
    },
    "es": {
        "title": "Generador de Contraseñas v1.0",
        "password_length": "Longitud de la contraseña:",
        "length_12": "12 caracteres",
        "length_16": "16 caracteres",
        "length_20": "20 caracteres",
        "generate": "Generar"
    },
    "cn": {
        "title": "密码生成器 v1.0",
        "password_length": "密码长度：",
        "length_12": "12个字符",
        "length_16": "16个字符",
        "length_20": "20个字符",
        "generate": "生成"
    }
}

def get_translation(language_code):
    return translations.get(language_code, translations["en"])
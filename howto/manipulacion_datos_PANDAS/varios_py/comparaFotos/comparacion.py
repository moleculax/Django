from deepface import DeepFace

# Compara dos imágenes
resultado = DeepFace.verify(img1_path="images2.jpeg", img2_path="images1.jpeg")

# El resultado es un diccionario con la clave 'verified'
if resultado['verified']:
    print("✅ Las fotos son de la misma persona")
else:
    print("❌ Las fotos son de personas diferentes")
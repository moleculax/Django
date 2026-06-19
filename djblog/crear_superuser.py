# crear_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djblog.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def crear_superusuario():
    email = 'pdfhand@gmail.com'
    password = 'admin123'
    
    # Verificar si ya existe
    if User.objects.filter(email=email).exists():
        print(f"⚠️ El usuario con email {email} ya existe")
        user = User.objects.get(email=email)
        print(f"📧 Email: {user.email}")
        print(f"👑 Es superusuario: {user.is_superuser}")
        return
    
    # Crear superusuario con todos los campos
    user = User.objects.create_superuser(
        email=email,
        password=password,
        first_name='Admin',
        last_name='User',
        phone_number='123456789',
        web_site='https://moleculax.com',
        linkedin='https://linkedin.com/in/tuprofile',
        twitter='https://twitter.com/tuprofile',
        instagram='https://instagram.com/tuprofile'
    )
    
    print("✅ SUPERUSUARIO CREADO EXITOSAMENTE")
    print("=" * 50)
    print(f"📧 Email: {user.email}")
    print(f"👤 Nombre: {user.first_name} {user.last_name}")
    print(f"🔑 Password: {password}")
    print(f"👑 Superusuario: {user.is_superuser}")
    print(f"💼 Staff: {user.is_staff}")
    print("=" * 50)
    print("\n🔗 Accede al admin en: http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    crear_superusuario()

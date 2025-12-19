#!/usr/bin/env python3
"""
Script básico para probar conexión con AWS usando Boto3
"""

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def verificar_conexion():
    """Verifica la conexión con AWS"""
    try:
        # Crear cliente STS para obtener identidad
        sts = boto3.client('sts')
        
        
        identidad = sts.get_caller_identity()
        
        print("✅ Conexión exitosa con AWS")
        print(f"\nDetalles de la cuenta:")
        print(f"  Account ID: {identidad['Account']}")
        print(f"  User ARN:   {identidad['Arn']}")
        print(f"  User ID:    {identidad['UserId']}")
        
        session = boto3.session.Session() # Obtiene región configurada

        region = session.region_name or 'No configurada'
        print(f"  Región:     {region}")
        
        return True
        
    except NoCredentialsError:
        print("❌ Error: No se encontraron credenciales de AWS")
        print("Ejecuta: aws configure")
        return False
        
    except ClientError as e:
        print(f"❌ Error al conectar con AWS: {e}")
        return False

    

if __name__ == "__main__":
    print("=" * 50)
    print("Verificación de Conexión AWS con Boto3")
    print("=" * 50)
    verificar_conexion()

    
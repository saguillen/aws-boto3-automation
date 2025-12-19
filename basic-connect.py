#!/usr/bin/env python3
"""
Script básico para probar conexión con AWS usando Boto3
"""

import boto3
import logging
from botocore.exceptions import ClientError, NoCredentialsError

# Configure logging
logger = logging.getLogger(__name__)

def verificar_conexion():
    """Verifica la conexión con AWS"""
    try:
        # Crear cliente STS para obtener identidad
        sts = boto3.client('sts')
        
        
        identidad = sts.get_caller_identity()
        
        logger.info("✅ Conexión exitosa con AWS")
        logger.info(f"Detalles de la cuenta:")
        logger.info(f"  Account ID: {identidad['Account']}")
        logger.info(f"  User ARN:   {identidad['Arn']}")
        logger.info(f"  User ID:    {identidad['UserId']}")


        
        session = boto3.session.Session() # Obtiene región configurada

        region = session.region_name or 'No configurada'
        logger.info(f"  Región:     {region}")
        
        return True
        
    except NoCredentialsError:
        logger.error("No se encontraron credenciales de AWS")
        logger.error("Ejecuta: aws configure")
        return False
        
    except ClientError as e:
        logger.error(f"Error al conectar con AWS: {e}")
        return False

    

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    logger.info("=" * 50)
    logger.info("Verificación de Conexión AWS con Boto3")
    logger.info("=" * 50)
    verificar_conexion()


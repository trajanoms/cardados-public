from django.core.exceptions import ValidationError

    
def validate_item_group(inspection_group):
    from.models import InspectionItem

    valid_groups = {
        InspectionItem.PLACA: inspection_group.PIV,
        InspectionItem.TRASEIRA_ESQUERDA: inspection_group.REPAROS_ESTRUTURAIS,
        InspectionItem.TRASEIRA_DIREITA: inspection_group.REPAROS_ESTRUTURAIS,
        InspectionItem.FRENTE_ESQUERDA: inspection_group.REPAROS_ESTRUTURAIS,
        InspectionItem.FRENTE_DIREITA: inspection_group.REPAROS_ESTRUTURAIS,
        InspectionItem.GRAV_VIDRO_FRONTAL: inspection_group.VIS_VIDROS,
        InspectionItem.GRAV_VIDRO_DIANTEIRO_ESQUERDO: inspection_group.VIS_VIDROS,
        InspectionItem.GRAV_VIDRO_DIANTEIRO_DIREITO: inspection_group.VIS_VIDROS,
        InspectionItem.GRAV_VIDRO_TRASEIRO_ESQUERDO: inspection_group.VIS_VIDROS,
        InspectionItem.GRAV_VIDRO_TRASEIRO_DIREITO: inspection_group.VIS_VIDROS,
        InspectionItem.GRAV_VIDRO_TRASEIRO: inspection_group.VIS_VIDROS,
        InspectionItem.PAINEL_HODOMETRO: inspection_group.REGISTRO_KM,
        InspectionItem.COLUNA_DIANTEIRA_ESQUERDA: inspection_group.GRUPO_EXTRA,
        InspectionItem.COLUNA_CENTRAL_ESQUERDA: inspection_group.GRUPO_EXTRA,
        InspectionItem.COLUNA_TRASEIRA_ESQUERDA: inspection_group.GRUPO_EXTRA,
        InspectionItem.COLUNA_TRASEIRA_DIREITA: inspection_group.GRUPO_EXTRA,
        InspectionItem.COLUNA_CENTRAL_DIREITA: inspection_group.GRUPO_EXTRA,
        InspectionItem.COMPARTIMENTO_MOTOR: inspection_group.GRUPO_EXTRA,
        InspectionItem.GRAVACAO_MOTOR: inspection_group.GRUPO_EXTRA,
        InspectionItem.GRAVACAO_CAMBIO: inspection_group.GRUPO_EXTRA,
        InspectionItem.ETIQUETA_VIS_COMP_MOTOR: inspection_group.GRUPO_EXTRA,
        InspectionItem.ETIQUETA_VIS_PORTA: inspection_group.GRUPO_EXTRA,
        InspectionItem.GRAVACAO_CHASSI: inspection_group.GRUPO_EXTRA,
        InspectionItem.LONGARINA_DIANTEIRA_ESQUERDA: inspection_group.GRUPO_EXTRA,
        InspectionItem.LONGARINA_TRASEIRA_ESQUERDA: inspection_group.GRUPO_EXTRA,
        InspectionItem.LONGARINA_TRASEIRA_DIREITA: inspection_group.GRUPO_EXTRA,
        InspectionItem.LONGARINA_DIANTEIRA_DIREITA: inspection_group.GRUPO_EXTRA,
        InspectionItem.DOCUMENTO: inspection_group.GRUPO_EXTRA,
        InspectionItem.AVARIAS_ESTETICAS: inspection_group.GRUPO_EXTRA,
        InspectionItem.AVARIAS_ESTRUTURAIS: inspection_group.GRUPO_EXTRA,
        InspectionItem.PROBLEMAS_MECANICOS: inspection_group.GRUPO_EXTRA,
        InspectionItem.PROBLEMAS_ELETRICOS: inspection_group.GRUPO_EXTRA,
    }

    if (
        InspectionItem.item in valid_groups and 
        inspection_group.group not in 
        valid_groups[inspection_group.item]
    ):
        raise ValidationError(
            f'''
                O item "{InspectionItem.item}" não pode ser associado ao grupo 
                "{InspectionItem.group.group}".
            '''
        )


def validate_classification_item(inspection_response):
    from .models import InspectionItem

    valid_items = {
        inspection_response.PERFEITO_ESTADO: (
            InspectionItem.PLACA, 
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.DANIFICADA: (
            InspectionItem.PLACA,
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
            InspectionItem.GRAVACAO_CHASSI,
            InspectionItem.PAINEL_HODOMETRO,

        ),
        inspection_response.AUSENTE: (
            InspectionItem.PLACA,
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.SEM_REPARO_APARENTE: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
            InspectionItem.FRENTE_ESQUERDA,
            InspectionItem.FRENTE_DIREITA,
            InspectionItem.COLUNA_DIANTEIRA_ESQUERDA,
            InspectionItem.COLUNA_TRASEIRA_ESQUERDA,
            InspectionItem.COLUNA_TRASEIRA_DIREITA,
            InspectionItem.COLUNA_CENTRAL_ESQUERDA,
            InspectionItem.COLUNA_CENTRAL_DIREITA,
            InspectionItem.LONGARINA_DIANTEIRA_DIREITA,
            InspectionItem.LONGARINA_TRASEIRA_DIREITA,
            InspectionItem.LONGARINA_TRASEIRA_ESQUERDA,
            InspectionItem.LONGARINA_DIANTEIRA_ESQUERDA,
        ),
        inspection_response.POSSUI_AVARIA: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
            InspectionItem.FRENTE_ESQUERDA,
            InspectionItem.FRENTE_DIREITA,
            InspectionItem.COLUNA_DIANTEIRA_ESQUERDA,
            InspectionItem.COLUNA_CENTRAL_ESQUERDA,
            InspectionItem.COLUNA_TRASEIRA_ESQUERDA,
            InspectionItem.COLUNA_TRASEIRA_DIREITA,
            InspectionItem.COLUNA_CENTRAL_DIREITA,
            InspectionItem.LONGARINA_DIANTEIRA_ESQUERDA,
            InspectionItem.LONGARINA_TRASEIRA_ESQUERDA,
            InspectionItem.LONGARINA_TRASEIRA_DIREITA,
            InspectionItem.LONGARINA_DIANTEIRA_DIREITA,
        ),
        inspection_response.REPARO_ASSOALHO: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_PORTA_TRASEIRA: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_CAIXA_AR: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_CAIXA_RODAS: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_CAIXA_STEP: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_LANTERNA: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_PARALAMAS: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
            InspectionItem.FRENTE_ESQUERDA,
            InspectionItem.FRENTE_DIREITA,
        ),
        inspection_response.REPARO_PARACHOQUE: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
            InspectionItem.FRENTE_ESQUERDA,
            InspectionItem.FRENTE_DIREITA,
        ),
        inspection_response.REPARO_TAMPA_MALA: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_TETO: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_COLUNA_TRASEIRA: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_PAINEL_TRASEIRO: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
        ),
        inspection_response.REPARO_LONGARINA: (
            InspectionItem.TRASEIRA_ESQUERDA,
            InspectionItem.TRASEIRA_DIREITA,
            InspectionItem.FRENTE_ESQUERDA,
            InspectionItem.FRENTE_DIREITA,
        ),
        inspection_response.ORIGINAL: (
            InspectionItem.GRAV_VIDRO_FRONTAL,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO,
        ),
        inspection_response.NAO_ORIGINAL: (
            InspectionItem.GRAV_VIDRO_FRONTAL,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO,
        ),
        inspection_response.INEXISTENTE: (
            InspectionItem.GRAV_VIDRO_FRONTAL,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO,
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.ILEGIVEL: (
            InspectionItem.GRAV_VIDRO_FRONTAL,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO,
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.DIVERGENTE: (
            InspectionItem.GRAV_VIDRO_FRONTAL,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO,
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.ADULTERADA: (
            InspectionItem.GRAV_VIDRO_FRONTAL,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_DIANTEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_ESQUERDO,
            InspectionItem.GRAV_VIDRO_TRASEIRO_DIREITO,
            InspectionItem.GRAV_VIDRO_TRASEIRO,
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.APAGADO: (
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.LUZ_AIRBAG_ACESA: (
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.LUZ_DIRECAO_ASSISTIDA: (
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.LUZ_FREIO_ESTACIONAMENTO: (
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.LUZ_OLEO_ACESA: (
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.REPETIDOR_SETA_DIREITA: (
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.REPETIDOR_SETA_ESQUERDA: (
            InspectionItem.PAINEL_HODOMETRO,
        ),
        inspection_response.POSSUI_REPARO: (
            InspectionItem.COLUNA_DIANTEIRA_ESQUERDA,
            InspectionItem.COLUNA_TRASEIRA_ESQUERDA,
            InspectionItem.COLUNA_TRASEIRA_DIREITA,
            InspectionItem.COLUNA_CENTRAL_ESQUERDA,
            InspectionItem.COLUNA_CENTRAL_DIREITA,
            InspectionItem.LONGARINA_DIANTEIRA_DIREITA,
            InspectionItem.LONGARINA_TRASEIRA_DIREITA,
            InspectionItem.LONGARINA_TRASEIRA_ESQUERDA,
            InspectionItem.LONGARINA_DIANTEIRA_ESQUERDA,
        ),
        inspection_response.DENTRO_DOS_PADROES: (
            InspectionItem.COMPARTIMENTO_MOTOR,
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
        ),
        inspection_response.FORA_DOS_PADROES: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
        ),
        inspection_response.MOTOR_AUSENTE: (
            InspectionItem.COMPARTIMENTO_MOTOR,
        ),
        inspection_response.MOTOR_NAO_LIGA: (
            InspectionItem.COMPARTIMENTO_MOTOR,
        ),
        inspection_response.SEM_BATERIA: (
            InspectionItem.COMPARTIMENTO_MOTOR,
        ),
         inspection_response.COM_VAZAMENTO: (
            InspectionItem.COMPARTIMENTO_MOTOR,
        ),
        inspection_response.OBSTRUIDA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.REMARCADA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.RESTAURADA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.LIXADA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.CORROIDA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.INICIO_OXIDACAO: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.OXIDADA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.OBLITERADA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.REMOVIDA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.INCOMPLETA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
        ),
        inspection_response.IMPLATADA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.PARALELA: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CAMBIO,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.GRAVACAO_REGULARIZADA_REM: (
            InspectionItem.GRAVACAO_MOTOR,
            InspectionItem.GRAVACAO_CHASSI,
        ),
        inspection_response.FALSIFICADA: (
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
        ),
        inspection_response.TRANSPLANTADA: (
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
        ),
        inspection_response.NUCLEO_IMPLATADO: (
            InspectionItem.ETIQUETA_VIS_COMP_MOTOR,
            InspectionItem.ETIQUETA_VIS_PORTA,
        )



    }

    if (
        inspection_response.classification in valid_items and 
        inspection_response.item.item not in 
        valid_items[inspection_response.classification]
    ):
        raise ValidationError(
            f'''
                A classificação "{inspection_response.classification}" não pode 
                ser associada ao item "{inspection_response.item.item}".
            '''
        )
    
def validate_image(file):
    file_size = file.size
    limit_kb = 1024  # Limite de tamanho do arquivo em KB
    if file_size > limit_kb * 1024:
        raise ValidationError(f"O tamanho máximo do arquivo é {limit_kb} KB.")
    
    valid_extensions = ['jpg', 'jpeg', 'png']
    extension = file.name.split('.')[-1].lower()
    if extension not in valid_extensions:
        raise ValidationError(
            f"Extensão de arquivo não suportada. Use: {', '.join(valid_extensions)}"
        )

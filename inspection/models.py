import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .validators import (
    validate_item_group, validate_classification_item, validate_image,
)


class InspectionItem(models.Model):
    PLACA = "placa"
    TRASEIRA_ESQUERDA = "traseira_esquerda"
    TRASEIRA_DIREITA = "traseira_direita"
    FRENTE_DIREITA = "frente_direita"
    FRENTE_ESQUERDA = "frente_esquerda"
    GRAV_VIDRO_FRONTAL = "grav_vidro_frontal"
    GRAV_VIDRO_DIANTEIRO_ESQUERDO = "grav_vidro_dianteiro_esquerdo"
    GRAV_VIDRO_DIANTEIRO_DIREITO = "grav_vidro_dianteiro_direito"
    GRAV_VIDRO_TRASEIRO_ESQUERDO = "grav_vidro_traseiro_esquerdo"
    GRAV_VIDRO_TRASEIRO_DIREITO = "grav_vidro_traseiro_direito"
    GRAV_VIDRO_TRASEIRO = "grav_vidro_traseiro"
    PAINEL_HODOMETRO = "painel_hodometro"
    COLUNA_DIANTEIRA_ESQUERDA = "coluna_dianteira_esquerda"
    COLUNA_CENTRAL_ESQUERDA = "coluna_central_esquerda"
    COLUNA_TRASEIRA_ESQUERDA = "coluna_traseira_esquerda"
    COLUNA_TRASEIRA_DIREITA = "coluna_traseira_direita"
    COLUNA_CENTRAL_DIREITA = "coluna_central_direita"
    COMPARTIMENTO_MOTOR = "compartimento_do_motor"
    GRAVACAO_MOTOR = "gravacao_motor"
    GRAVACAO_CAMBIO = "gravacao_cambio"
    ETIQUETA_VIS_COMP_MOTOR = "etiqueta_vis_comp_motor"
    ETIQUETA_VIS_PORTA = "etiqueta_vis_porta"
    GRAVACAO_CHASSI = "gravacao_chassi"
    LONGARINA_DIANTEIRA_ESQUERDA = "longarina_dianteira_esquerda"
    LONGARINA_TRASEIRA_ESQUERDA = "longarina_traseira_esquerda"
    LONGARINA_TRASEIRA_DIREITA = "longarina_traseira_direita"
    LONGARINA_DIANTEIRA_DIREITA = "longarina_dianteira_direita"
    DOCUMENTO = "documento"
    AVARIAS_ESTETICAS = "avarias_esteticas"
    AVARIAS_ESTRUTURAIS = "avarias_estruturais"
    PROBLEMAS_MECANICOS = "problemas_mecanicos"
    PROBLEMAS_ELETRICOS = "problemas_eletricos"

    ITEMS = (
        (PLACA, PLACA,),
        (TRASEIRA_ESQUERDA, TRASEIRA_ESQUERDA,),
        (TRASEIRA_DIREITA, TRASEIRA_DIREITA,),
        (FRENTE_ESQUERDA, FRENTE_ESQUERDA,),
        (FRENTE_DIREITA, FRENTE_DIREITA,),
        (GRAV_VIDRO_FRONTAL, GRAV_VIDRO_FRONTAL,),
        (GRAV_VIDRO_DIANTEIRO_ESQUERDO, GRAV_VIDRO_DIANTEIRO_ESQUERDO,),
        (GRAV_VIDRO_DIANTEIRO_DIREITO, GRAV_VIDRO_DIANTEIRO_DIREITO,),
        (GRAV_VIDRO_TRASEIRO_ESQUERDO, GRAV_VIDRO_TRASEIRO_ESQUERDO,),
        (GRAV_VIDRO_TRASEIRO_DIREITO, GRAV_VIDRO_TRASEIRO_DIREITO,),
        (GRAV_VIDRO_TRASEIRO, GRAV_VIDRO_TRASEIRO,),
        (PAINEL_HODOMETRO, PAINEL_HODOMETRO,),
        (COLUNA_DIANTEIRA_ESQUERDA, COLUNA_DIANTEIRA_ESQUERDA,),
        (COLUNA_CENTRAL_ESQUERDA, COLUNA_CENTRAL_ESQUERDA,),
        (COLUNA_TRASEIRA_ESQUERDA, COLUNA_TRASEIRA_ESQUERDA,),
        (COLUNA_TRASEIRA_DIREITA, COLUNA_TRASEIRA_DIREITA,),
        (COLUNA_CENTRAL_DIREITA, COLUNA_CENTRAL_DIREITA,),
        (COMPARTIMENTO_MOTOR, COMPARTIMENTO_MOTOR,),
        (GRAVACAO_MOTOR, GRAVACAO_MOTOR,),
        (GRAVACAO_CAMBIO, GRAVACAO_CAMBIO,),
        (ETIQUETA_VIS_COMP_MOTOR, ETIQUETA_VIS_COMP_MOTOR,),
        (ETIQUETA_VIS_PORTA, ETIQUETA_VIS_PORTA,),
        (GRAVACAO_CHASSI, GRAVACAO_CHASSI,),
        (LONGARINA_DIANTEIRA_ESQUERDA, LONGARINA_DIANTEIRA_ESQUERDA,),
        (LONGARINA_TRASEIRA_ESQUERDA, LONGARINA_TRASEIRA_ESQUERDA,),
        (LONGARINA_TRASEIRA_DIREITA, LONGARINA_TRASEIRA_DIREITA,),
        (LONGARINA_DIANTEIRA_DIREITA, LONGARINA_DIANTEIRA_DIREITA,),
        (DOCUMENTO, DOCUMENTO,),
        (AVARIAS_ESTETICAS, AVARIAS_ESTETICAS,),
        (AVARIAS_ESTRUTURAIS, AVARIAS_ESTRUTURAIS,),
        (PROBLEMAS_MECANICOS, PROBLEMAS_MECANICOS,),
        (PROBLEMAS_ELETRICOS, PROBLEMAS_ELETRICOS,),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=255, choices=ITEMS, verbose_name="Item do grupo")
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class InspectionGroup(models.Model):
    PIV = "piv"
    REPAROS_ESTRUTURAIS = "reparos_estruturais"
    VIS_VIDROS = "vis_vidros"
    REGISTRO_KM = "registro_km"
    GRUPO_EXTRA = "grupo_extra"

    GROUPS = (
        (PIV, PIV,),
        (REPAROS_ESTRUTURAIS, REPAROS_ESTRUTURAIS),
        (VIS_VIDROS, VIS_VIDROS),
        (REGISTRO_KM, REGISTRO_KM),
        (GRUPO_EXTRA, GRUPO_EXTRA),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.CharField(max_length=255, choices=GROUPS, verbose_name="Grupo")
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(
        InspectionItem, 
        related_name="group",
        verbose_name="Itens"
    )

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        validate_item_group(self)
    

class InspectionTemplate(models.Model):
    CARRO = "carro"
    MOTO = "moto"

    VEHICLES = (
        (CARRO, CARRO,),
        (MOTO, MOTO,),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome do template")
    vehicle = models.CharField(max_length=255, choices=VEHICLES, verbose_name="Tipo de veículo")
    inspection_groups = models.ManyToManyField(
        InspectionGroup, 
        related_name="templates",
        verbose_name="Grupos"
    )

    def __str__(self):
        return self.name


class InspectionResponse(models.Model):
    PERFEITO_ESTADO = "perfeito_estado"
    DANIFICADA = "danificada"
    AUSENTE = "ausente"
    POSSUI_REPARO = "possui_reparo"
    SEM_REPARO_APARENTE = "sem_reparo_aparente"
    POSSUI_AVARIA = "possui_avaria"
    REPARO_ASSOALHO = "reparo_assoalho"
    REPARO_PORTA_TRASEIRA = "reparo_porta_traseira"
    REPARO_CAIXA_AR = "reparo_caixa_ar"
    REPARO_CAIXA_RODAS = "reparo_caixa_rodas"
    REPARO_CAIXA_STEP = "reparo_caixa_step"
    REPARO_LANTERNA = "reparo_lanterna"
    REPARO_PARALAMAS = "reparo_paralamas"
    REPARO_PARACHOQUE = "reparo_parachoque"
    REPARO_TAMPA_MALA = "reparo_tampa_mala"
    REPARO_TETO = "reparo_teto"
    REPARO_COLUNA_TRASEIRA = "reparo_coluna_traseira"
    REPARO_PAINEL_TRASEIRO = "reparo_painel_traseiro"
    REPARO_LONGARINA = "reparo_longarina"
    ORIGINAL = "original"
    NAO_ORIGINAL = "nao_original"
    INEXISTENTE = "inexistente"
    ILEGIVEL = "ilegivel"
    DIVERGENTE = "divergente"
    ADULTERADA = "adulterada"
    APAGADO = "apagado"
    LUZ_AIRBAG_ACESA = "luz_airbag_acesa"
    LUZ_DIRECAO_ASSISTIDA = "luz_direcao_assistida"
    LUZ_FREIO_ESTACIONAMENTO = "luz_freio_estacionamento"
    LUZ_OLEO_ACESA = "luz_oleo_acesa"
    REPETIDOR_SETA_DIREITA = "repetidor_seta_direita"
    REPETIDOR_SETA_ESQUERDA = "repetidor_seta_esquerda"
    DENTRO_DOS_PADROES = "dentro_dos_padroes"
    FORA_DOS_PADROES = "fora_dos_padroes"
    MOTOR_AUSENTE = "motor_ausente"
    MOTOR_NAO_LIGA = "motor_nao_liga"
    SEM_BATERIA = "sem_bateria"
    COM_VAZAMENTO = "com_vazamento"
    OBSTRUIDA = "obstruida"
    REMARCADA = "remarcada"
    RESTAURADA = "restaurada"
    LIXADA = "lixada"
    CORROIDA = "corroida"
    INICIO_OXIDACAO = "inicio_oxidacao"
    OXIDADA = "oxidada"
    OBLITERADA = "obliterada"
    REMOVIDA = "removida"
    INCOMPLETA = "incompleta"
    IMPLATADA = "implatada"
    PARALELA = "paralela"
    GRAVACAO_REGULARIZADA_REM = "gravacao_regularizada_rem"
    FALSIFICADA = "falsificada"
    TRANSPLANTADA = "transplantada"
    NUCLEO_IMPLATADO = "nucleo_implatado"

    CLASSIFICATIONS = (
        (PERFEITO_ESTADO, PERFEITO_ESTADO,),
        (DANIFICADA, DANIFICADA,),
        (AUSENTE, AUSENTE,),
        (POSSUI_REPARO, POSSUI_REPARO,),
        (SEM_REPARO_APARENTE, SEM_REPARO_APARENTE,),
        (POSSUI_AVARIA, POSSUI_AVARIA,),
        (REPARO_ASSOALHO, REPARO_ASSOALHO,),
        (REPARO_PORTA_TRASEIRA, REPARO_PORTA_TRASEIRA,),
        (REPARO_CAIXA_AR, REPARO_CAIXA_AR,),
        (REPARO_CAIXA_RODAS, REPARO_CAIXA_RODAS,),
        (REPARO_CAIXA_STEP, REPARO_CAIXA_STEP,),
        (REPARO_LANTERNA, REPARO_LANTERNA,),
        (REPARO_PARALAMAS, REPARO_PARALAMAS,),
        (REPARO_PARACHOQUE, REPARO_PARACHOQUE,),
        (REPARO_TAMPA_MALA, REPARO_TAMPA_MALA,),
        (REPARO_TETO, REPARO_TETO,),
        (REPARO_COLUNA_TRASEIRA, REPARO_COLUNA_TRASEIRA,),
        (REPARO_PAINEL_TRASEIRO, REPARO_PAINEL_TRASEIRO,),
        (REPARO_LONGARINA, REPARO_LONGARINA,),
        (ORIGINAL, ORIGINAL,),
        (NAO_ORIGINAL, NAO_ORIGINAL,),
        (INEXISTENTE, INEXISTENTE,),
        (ILEGIVEL, ILEGIVEL,),
        (DIVERGENTE, DIVERGENTE,),
        (ADULTERADA, ADULTERADA,),
        (APAGADO, APAGADO,),
        (LUZ_AIRBAG_ACESA, LUZ_AIRBAG_ACESA,),
        (LUZ_DIRECAO_ASSISTIDA, LUZ_DIRECAO_ASSISTIDA,),
        (LUZ_FREIO_ESTACIONAMENTO, LUZ_FREIO_ESTACIONAMENTO,),
        (LUZ_OLEO_ACESA, LUZ_OLEO_ACESA,),
        (REPETIDOR_SETA_DIREITA, REPETIDOR_SETA_DIREITA,),
        (REPETIDOR_SETA_ESQUERDA, REPETIDOR_SETA_ESQUERDA,),
        (DENTRO_DOS_PADROES, DENTRO_DOS_PADROES,),
        (FORA_DOS_PADROES, FORA_DOS_PADROES,),
        (MOTOR_AUSENTE, MOTOR_AUSENTE,),
        (MOTOR_NAO_LIGA, MOTOR_NAO_LIGA,),
        (SEM_BATERIA, SEM_BATERIA,),
        (COM_VAZAMENTO, COM_VAZAMENTO,),
        (OBSTRUIDA, OBSTRUIDA,),
        (REMARCADA, REMARCADA,),
        (RESTAURADA, RESTAURADA,),
        (LIXADA, LIXADA,),
        (CORROIDA, CORROIDA,),
        (INICIO_OXIDACAO, INICIO_OXIDACAO,),
        (OXIDADA, OXIDADA,),
        (OBLITERADA, OBLITERADA,),
        (REMOVIDA, REMOVIDA,),
        (INCOMPLETA, INCOMPLETA,),
        (IMPLATADA, IMPLATADA,),
        (PARALELA, PARALELA,),
        (GRAVACAO_REGULARIZADA_REM, GRAVACAO_REGULARIZADA_REM,),
        (FALSIFICADA, FALSIFICADA,),
        (TRANSPLANTADA, TRANSPLANTADA,),
        (NUCLEO_IMPLATADO, NUCLEO_IMPLATADO,),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        InspectionItem,
        related_name="response", 
        on_delete=models.SET_NULL,
        null=True,
    )
    classification = models.CharField(max_length=255, choices=CLASSIFICATIONS, verbose_name="Classificação")
    photo = models.ImageField(
        upload_to='images/', 
        verbose_name="Foto do item",
        null=True,
        validators=[validate_image]
    )

    def clean(self):
        super().clean()
        validate_classification_item(self)


class Inspection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    template = models.ForeignKey(
        InspectionTemplate, 
        related_name="inspection", 
        on_delete=models.SET_NULL,
        null=True,
    )
    responses = models.ManyToManyField(
        InspectionResponse, 
        related_name="inspection", 
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

@receiver(post_save, sender=Inspection)
def create_inspection_responses(sender, instance, created, **kwargs):
    if created:
        try:
            groups = instance.template.inspection_groups.all()
            for group in groups:
                for item in group.items.all():
                    inspection_response = InspectionResponse.objects.create(item=item)
                    instance.responses.add(inspection_response)
        except Exception as e:
            raise Exception(e)
            






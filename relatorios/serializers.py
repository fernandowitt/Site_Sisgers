from rest_framework import serializers
from models import Vistoria


class VistoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    #tem como fazer com choice
    cobrad = serializers.CharField(required=True, allow_blank=False, max_length=200)
    municipio = serializers.CharField(required=True, allow_blank=False, max_length=200)
    #tem como fazer com choice

    descricao = serializers.CharField()
    data = serializers.DateField()
    endereco = serializers.CharField()
    #latitude e longitude com FloatField ou DecimalField?

    #Danos humanos:

    danos_humanos_desalojados = serializers.IntegerField(required=True)
    danos_humanos_desabrigados = serializers.IntegerField(required=True)
    danos_humanos_desaparecidos = serializers.IntegerField(required=True)
    danos_humanos_feridos = serializers.IntegerField(required=True)
    danos_humanos_enfermos = serializers.IntegerField(required=True)
    danos_humanos_mortos = serializers.IntegerField(required=True)
    danos_humanos_isolados = serializers.IntegerField(required=True)
    danos_humanos_atingidos = serializers.IntegerField(required=True)
    danos_humanos_afetados = serializers.IntegerField(required=True)

    danos_humanos_observacoes = serializers.CharField()

    #Danos materiais:

    unidades_habitacionais_atingidas = serializers.IntegerField(required=True)
    unidades_habitacionais_danificads = serializers.IntegerField(required=True)
    unidades_habitacionais_interditadas = serializers.IntegerField(required=True)
    unidades_habitacionais_destruidas = serializers.IntegerField(required=True)
    instalacoes_publicas_saude_atingidas = serializers.IntegerField(required=True)
    instalacoes_publicas_ensino_atingidas = serializers.IntegerField(required=True)
    instalacoes_comunitarias_atingidas = serializers.IntegerField(required=True)
    obras_atingidas = serializers.IntegerField(required=True)
    interrupcoes_servicos_essenciais = serializers.IntegerField(required=True)

    danos_materiais_observacoes = serializers.CharField()

    #Danos ambientais:

    contaminacao_solo = serializers.IntegerField(required=True)
    contaminacao_agua = serializers.IntegerField(required=True)
    contaminacao_ar = serializers.IntegerField(required=True)

    danos_ambientais_observacoes = serializers.CharField()

    #Danos econômicos:

    danos_agricultura = serializers.IntegerField(required=True)
    danos_pecuaria = serializers.IntegerField(required=True)
    danos_industria = serializers.IntegerField(required=True)
    danos_comercio = serializers.IntegerField(required=True)
    danos_prestacao_de_servicos = serializers.IntegerField(required=True)

    danos_economicos_observacoes = serializers.CharField()

    #IAH

    iah_cestas_de_alimentos = serializers.IntegerField(required=True)
    iah_agua_potavel = serializers.IntegerField(required=True)
    iah_colchoes = serializers.IntegerField(required=True)
    iah_kit_higiene_pessoal = serializers.IntegerField(required=True)
    iah_kit_limpeza = serializers.IntegerField(required=True)
    iah_telhas = serializers.IntegerField(required=True)
    iah_lona_plastica = serializers.IntegerField(required=True)
    iah_outros = serializers.IntegerField(required=True)

    iah_fornecidos_outros_observacoes = serializers.CharField()
    iah_vias_publicas_totalmente_desobistruidas = serializers.BooleanField(required=True)
    iah_reestabelecimento_servicos_essenciais = serializers.BooleanField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Vistoria` instance, given the validated data.
        """
        return Vistoria.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Vistoria` instance, given the validated data.
        """
        instance.cobrad = validated_data.get('cobrad', instance.cobrad)
        instance.municipio = validated_data.get('municipio', instance.municipio)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.data = validated_data.get('data', instance.data)
        instance.endereco = validated_data.get('endereco', instance.endereco)
        instance.danos_humanos_desalojados = validated_data.get('danos_humanos_desalojados', instance.danos_humanos_desalojados)
        instance.danos_humanos_desabrigados = validated_data.get('danos_humanos_desabrigados', instance.danos_humanos_desabrigados)
        instance.danos_humanos_desaparecidos = validated_data.get('danos_humanos_desaparecidos', instance.danos_humanos_desaparecidos)
        instance.danos_humanos_feridos = validated_data.get('danos_humanos_feridos', instance.danos_humanos_feridos)
        instance.danos_humanos_enfermos = validated_data.get('danos_humanos_enfermos', instance.danos_humanos_enfermos)
        instance.danos_humanos_mortos = validated_data.get('danos_humanos_mortos', instance.danos_humanos_mortos)
        instance.danos_humanos_isolados = validated_data.get('danos_humanos_isolados', instance.danos_humanos_isolados)
        instance.danos_humanos_atingidos = validated_data.get('danos_humanos_atingidos', instance.danos_humanos_atingidos)
        instance.danos_humanos_afetados = validated_data.get('danos_humanos_afetados', instance.danos_humanos_afetados)
        instance.danos_humanos_observacoes = validated_data.get('danos_humanos_observacoes', instance.danos_humanos_observacoes)
        instance.unidades_habitacionais_atingidas = validated_data.get('unidades_habitacionais_atingidas', instance.unidades_habitacionais_atingidas)
        instance.unidades_habitacionais_danificads = validated_data.get('unidades_habitacionais_danificads', instance.unidades_habitacionais_danificads)
        instance.unidades_habitacionais_interditadas = validated_data.get('unidades_habitacionais_interditadas', instance.unidades_habitacionais_interditadas)
        instance.unidades_habitacionais_destruidas = validated_data.get('unidades_habitacionais_destruidas', instance.unidades_habitacionais_destruidas)
        instance.instalacoes_publicas_saude_atingidas = validated_data.get('instalacoes_publicas_saude_atingidas', instance.instalacoes_publicas_saude_atingidas)
        instance.instalacoes_publicas_ensino_atingidas = validated_data.get('instalacoes_publicas_ensino_atingidas', instance.instalacoes_publicas_ensino_atingidas)
        instance.instalacoes_comunitarias_atingidas = validated_data.get('instalacoes_comunitarias_atingidas', instance.instalacoes_comunitarias_atingidas)
        instance.obras_atingidas = validated_data.get('obras_atingidas', instance.obras_atingidas)
        instance.interrupcoes_servicos_essenciais = validated_data.get('interrupcoes_servicos_essenciais', instance.interrupcoes_servicos_essenciais)
        instance.danos_materiais_observacoes = validated_data.get('danos_materiais_observacoes', instance.danos_materiais_observacoes)
        instance.contaminacao_solo = validated_data.get('contaminacao_solo', instance.contaminacao_solo)
        instance.contaminacao_agua = validated_data.get('contaminacao_agua', instance.contaminacao_agua)
        instance.contaminacao_ar = validated_data.get('contaminacao_ar', instance.contaminacao_ar)
        instance.danos_ambientais_observacoes = validated_data.get('danos_ambientais_observacoes', instance.danos_ambientais_observacoes)
        instance.danos_agricultura = validated_data.get('danos_agricultura', instance.danos_agricultura)
        instance.danos_pecuaria = validated_data.get('danos_pecuaria', instance.danos_pecuaria)
        instance.danos_industria = validated_data.get('danos_industria', instance.danos_industria)
        instance.danos_comercio = validated_data.get('danos_comercio', instance.danos_comercio)
        instance.danos_prestacao_de_servicos = validated_data.get('danos_prestacao_de_servicos', instance.danos_prestacao_de_servicos)
        instance.danos_economicos_observacoes = validated_data.get('danos_economicos_observacoes', instance.danos_economicos_observacoes)
        instance.iah_cestas_de_alimentos = validated_data.get('iah_cestas_de_alimentos', instance.iah_cestas_de_alimentos)
        instance.iah_agua_potavel = validated_data.get('iah_agua_potavel', instance.iah_agua_potavel)
        instance.iah_colchoes = validated_data.get('iah_colchoes', instance.iah_colchoes)
        instance.iah_kit_higiene_pessoal = validated_data.get('iah_kit_higiene_pessoal', instance.iah_kit_higiene_pessoal)
        instance.iah_kit_limpeza = validated_data.get('iah_kit_limpeza', instance.iah_kit_limpeza)
        instance.iah_telhas = validated_data.get('iah_telhas', instance.iah_telhas)
        instance.iah_lona_plastica = validated_data.get('iah_lona_plastica', instance.iah_lona_plastica)
        instance.iah_outros = validated_data.get('iah_outros', instance.iah_outros)
        instance.iah_fornecidos_outros_observacoes = validated_data.get('iah_fornecidos_outros_observacoes', instance.iah_fornecidos_outros_observacoes)
        instance.iah_vias_publicas_totalmente_desobistruidas = validated_data.get('iah_vias_publicas_totalmente_desobistruidas', instance.iah_vias_publicas_totalmente_desobistruidas)
        instance.iah_reestabelecimento_servicos_essenciais = validated_data.get('iah_reestabelecimento_servicos_essenciais', instance.iah_reestabelecimento_servicos_essenciais)

        instance.save()
        return instance
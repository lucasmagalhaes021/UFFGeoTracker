# UFFGeoTracker

Este projeto Python é uma ferramenta de visualização de traceroute que mostra a rota dos pacotes até um destino especificado em um arquivo KML. Abaixo estão as bibliotecas utilizadas e suas funcionalidades específicas no contexto do projeto.

## Diagrama do Processo:
![UffGeoTracker_2](https://github.com/lucasmagalhaes021/redes_2024_1/assets/148398476/c05d2629-6e02-471d-b059-6a04ad455b7f)

## Bibliotecas Utilizadas

### `subprocess`
- **Utilidade**: Permite executar novos aplicativos ou programas através de comandos, capturando os resultados de saída. No contexto deste projeto, é usado para executar o comando `tracert` para rastrear a rota dos pacotes até um destino de rede especificado.
- **Documentação**: [subprocess](https://docs.python.org/3/library/subprocess.html)

### `requests`
- **Utilidade**: Biblioteca para fazer solicitações HTTP em Python. Aqui, é usada para fazer uma solicitação GET a uma API (`ip-api.com`) para obter informações detalhadas sobre cada IP encontrado no resultado do traceroute.
- **Documentação**: [requests](https://docs.python-requests.org/en/latest/)

### `re`
- **Utilidade**: Oferece operações com expressões regulares em Python. Neste script, é utilizado para encontrar todos os endereços IP válidos na saída do comando `tracert`.
- **Documentação**: [re](https://docs.python.org/3/library/re.html)

### `threading`
- **Utilidade**: Facilita a execução de múltiplas operações ao mesmo tempo sem interrupção, usando threads. No código, duas threads são criadas: uma para realizar o traceroute e outra para mostrar uma animação de carregamento enquanto o traceroute está sendo executado.
- **Documentação**: [threading](https://docs.python.org/3/library/threading.html)

### `time`
- **Utilidade**: Usada para manipular funções relacionadas ao tempo. No script, é utilizada para controlar o intervalo de atualização da animação de carregamento durante a execução do traceroute.
- **Documentação**: [time](https://docs.python.org/3/library/time.html)

### `simplekml`
- **Utilidade**: Permite a criação de arquivos KML com uma interface simples. É usada para criar um arquivo KML que mapeia a rota de traceroute com detalhes geográficos, incluindo pontos e linhas entre as localizações dos IPs.
- **Documentação**: [simplekml](https://simplekml.readthedocs.io/en/latest/)

## Funcionalidades do Script

1. **traceroute**: Rastreia a rota que os pacotes seguem até o destino especificado e coleta os IPs dos hops intermediários.
2. **spinnerAnimation**: Exibe uma animação em terminal enquanto o traceroute está sendo processado.
3. **getIpDetails**: Obtém informações geográficas e outras de cada IP na rota usando uma API externa.
4. **createKML**: Gera um arquivo KML que pode ser aberto em aplicativos como Google Earth para visualizar a rota de traceroute.

## Como Usar

1. Execute o script.
2. Forneça uma URL ou um endereço IP para rastrear.
3. O resultado será salvo em arquivo KML e será gerado se houver IPs válidos na rota.

---

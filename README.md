# UFFGeoTracker

Este projeto Python é uma ferramenta de visualização de **Traceroute** que mostra a rota dos pacotes até um destino especificado em um arquivo KML. Abaixo estão as bibliotecas utilizadas e suas funcionalidades específicas no contexto do projeto.

## Traceroute
![Traceroute_Cartaz](https://github.com/lucasmagalhaes021/redes_2024_1/assets/148398476/69b77cf6-2917-4250-90c7-1d917ee286f4)

## Diagrama do Processo
![UffGeoTracker_2](https://github.com/lucasmagalhaes021/redes_2024_1/assets/148398476/c05d2629-6e02-471d-b059-6a04ad455b7f)

## Funcionalidades do Script

1. **Traceroute**: Rastreia a rota que os pacotes seguem até o destino especificado e coleta os IPs dos hops intermediários.
2. **SpinnerAnimation**: Exibe uma animação em terminal enquanto o traceroute está sendo processado.
3. **GetIpDetails**: Obtém informações geográficas e outras de cada IP na rota usando uma API externa.
4. **CreateKML**: Gera um arquivo KML que pode ser aberto em aplicativos como Google Earth para visualizar a rota de traceroute.

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

## Comandos para Configuração do Script
<details>
  <summary>Processo de configuração (CMD Windows)</summary>

  #### Verificar se o Python está instalado
  ```bash
  python --version
  ```

  #### Verificar se o pip está instalado
  ```bash
  pip --version
  ```

  #### Caso o pip não esteja instalado, siga estas etapas para instalá-lo:
  1. Baixe o script get-pip.py usando curl:
  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  ```

  2. Execute o script para instalar o pip:
  ```bash
  python get-pip.py
  ```

  #### Verificar novamente se o pip está instalado
  ```bash
  pip --version
  ```

  #### Instalar a biblioteca externa "simplekml"
  ```bash
  pip install simplekml
  ```

  #### Instalar a biblioteca "requests"
  ```bash
  pip install requests
  ```

</details>

<details>
  <summary>Processo de configuração (Terminal Linux)</summary>

  #### Verificar se o Python está instalado
  ```bash
  python3 --version
  ```

  #### Verificar se o pip está instalado
  ```bash
  pip3 --version
  ```

  #### Caso o pip não esteja instalado, siga estas etapas para instalá-lo:
  1. Baixe o script get-pip.py usando curl:
  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  ```

  2. Execute o script para instalar o pip:
  ```bash
  python3 get-pip.py
  ```

  #### Verificar novamente se o pip está instalado
  ```bash
  pip3 --version
  ```

  #### Instalar a biblioteca externa "simplekml"
  ```bash
  pip3 install simplekml
  ```

  #### Instalar a biblioteca "requests"
  ```bash
  pip3 install requests
  ```

</details>



{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "F4nzcTjmt8ij"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt #importa bibliotecas que serão utilizadas\n",
        "import numpy as np\n",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive #trecho de código carrega google drive\n",
        "drive.mount('/content/drive')#utiliza método mount para carregar conteúdo do google drive"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LYeZ3uB_uXzf",
        "outputId": "d5a51e65-f77a-480c-e6f2-327bd02809da"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "WFa0LZpkP7uZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **COTAÇÃO DÓLAR**"
      ],
      "metadata": {
        "id": "1--41X9tiZYl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"TRATANDO DADOS\n",
        "arrumando datasets para manipulação\"\"\"\n",
        "\n",
        "dolar= pd.read_csv('/content/drive/MyDrive/TDE/Cotação do Dólar por período.csv')#instancia um objeto da classe pandas.core.frame.DataFrame pelo método read_csv\n",
        "# capaz de ler arquivos .csv, recebe path do dataset no drive como parâmetro\n",
        "\n",
        "\n",
        "dolar = dolar.replace(',','.',regex = True).astype(float)#método replace substitui valores do dataset de maneira dinâmica, no caso transfomando valores \n",
        "#de String para float. Recebe como parêmetro os valores a serem susbstitídos, e método astype muda o tipo de uma série de dados\n",
        "\n",
        "dolar = dolar.reset_index()#método reset_index cria uma nova coluna a partir do índice anterior com o numero de dias\n",
        "\n",
        "dolar = dolar.rename({'index': 'Dias'},axis=1)#método rename renomeia a nova coluna criada recebendo um dicionário como parâmetro\n",
        "\n",
        "print(dolar.info())#método info não recebe parâmetros e retorna um sumário conciso sobre o dataset instanciado \n",
        "\n",
        "print(\"\\ntipo do objeto dolar: \", type(dolar))# função type retorna o tipo do objeto dolar, no caso sua classe"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8cKOVI1oe364",
        "outputId": "54866625-5943-44b8-b329-0beaf7a3f5f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 756 entries, 0 to 755\n",
            "Data columns (total 3 columns):\n",
            " #   Column         Non-Null Count  Dtype  \n",
            "---  ------         --------------  -----  \n",
            " 0   Dias           756 non-null    int64  \n",
            " 1   cotacaoCompra  756 non-null    float64\n",
            " 2   cotacaoVenda   756 non-null    float64\n",
            "dtypes: float64(2), int64(1)\n",
            "memory usage: 17.8 KB\n",
            "None\n",
            "\n",
            "tipo do objeto dolar:  <class 'pandas.core.frame.DataFrame'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dolar.head() #método head retorna 5 primeiras linhas do dataset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "9pu-UeirZyeS",
        "outputId": "eaf972f7-a077-41b3-a8e3-c0f2832deb7d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Dias  cotacaoCompra  cotacaoVenda\n",
              "0     0         3.7670        3.7676\n",
              "1     1         3.7364        3.7370\n",
              "2     2         3.7145        3.7151\n",
              "3     3         3.6513        3.6519\n",
              "4     4         3.6688        3.6694"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-16466b08-90e1-4ad0-b53b-ca451bfc872d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Dias</th>\n",
              "      <th>cotacaoCompra</th>\n",
              "      <th>cotacaoVenda</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>3.7670</td>\n",
              "      <td>3.7676</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3.7364</td>\n",
              "      <td>3.7370</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>3.7145</td>\n",
              "      <td>3.7151</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3</td>\n",
              "      <td>3.6513</td>\n",
              "      <td>3.6519</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>3.6688</td>\n",
              "      <td>3.6694</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-16466b08-90e1-4ad0-b53b-ca451bfc872d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-16466b08-90e1-4ad0-b53b-ca451bfc872d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-16466b08-90e1-4ad0-b53b-ca451bfc872d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = np.array(dolar[\"cotacaoCompra\"])#  instancia um objeto da classe numpy.ndarray, recebe como parâmetro o objeto dataframe instanciado anteriormente\n",
        "#com a coluna da cotacao do dólar.\n",
        "\n",
        "#modulo plt\n",
        "plt.title('Dólar entre janeiro de 2019 e 2022')# utiliza método title para plotar título do gráfico\n",
        "\n",
        "plt.xlabel('Dias') #metodo xlabel define nome para eixo x\n",
        "\n",
        "plt.ylabel('Variação')# metodo ylabel define nome para eixo y\n",
        "\n",
        "plt.plot(a,color = 'green')# método plot cria gráfico, recebendo; x = dias; y = dólar "
      ],
      "metadata": {
        "id": "u9Mb6R2yeZyZ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 312
        },
        "outputId": "577444fd-e2a9-42a6-b859-3c9926574a7d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f447666f280>]"
            ]
          },
          "metadata": {},
          "execution_count": 5
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dolar['cotacaoCompra'].describe() # método describe do pandas retorna informações estatisticas"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_XiD9y-VKIbW",
        "outputId": "61bdacfa-67e9-4406-dd69-50185e41481e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "count    756.000000\n",
              "mean       4.874085\n",
              "std        0.695159\n",
              "min        3.651300\n",
              "25%        4.100250\n",
              "50%        5.196650\n",
              "75%        5.444075\n",
              "max        5.936600\n",
              "Name: cotacaoCompra, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **IPCA**"
      ],
      "metadata": {
        "id": "LeSqQ4T1csRP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ipca = pd.read_csv('/content/drive/MyDrive/TDE/IPCA_arrumado.csv',sep=';', names = [\"Data\", \"Taxa\"])#instancia um objeto da classe pandas.core.frame.DataFrame pelo método read_csv\n",
        "#recebe path do dataset no drive como parâmetro, também um caractere separador de colunas e os nomes das colunas\n",
        "\n",
        "\n",
        "ipca = ipca.reset_index()# método reset_index cria uma nova coluna a partir do índice anterior com o numero de meses\n",
        "\n",
        "ipca = ipca.rename({'index': 'Meses'},axis=1)# método rename renomeia a nova coluna criada recebendo um dicionário como parâmetro, e o eixo da coluna\n",
        "\n",
        "ipca = ipca.iloc[295:332] # método iloc de seleção de dados em lista\n",
        "\n",
        "data_types_dict = {'Taxa': float}# cria dicionario para mudar o tipo de dado da coluna selecionada\n",
        "\n",
        "ipca = ipca.astype(data_types_dict)# método astype do pandas altera o tipo de dado de uma séria, recebe um dicionário como parâmetro\n",
        "\n",
        "ipca.head()#método head retorna 5 primeiras linhas da base de dados sobre índice IPCA"
      ],
      "metadata": {
        "id": "F2B7B9bHbs_P",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "outputId": "a3ce111f-96ce-4572-b06a-65789fc45b1a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     Meses            Data  Taxa\n",
              "295    295    janeiro 2019  0.32\n",
              "296    296  fevereiro 2019  0.43\n",
              "297    297      março 2019  0.75\n",
              "298    298      abril 2019  0.57\n",
              "299    299       maio 2019  0.13"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bf3169af-e09f-41ee-b4d8-72cefc602c9e\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Meses</th>\n",
              "      <th>Data</th>\n",
              "      <th>Taxa</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>295</th>\n",
              "      <td>295</td>\n",
              "      <td>janeiro 2019</td>\n",
              "      <td>0.32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>296</th>\n",
              "      <td>296</td>\n",
              "      <td>fevereiro 2019</td>\n",
              "      <td>0.43</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>297</th>\n",
              "      <td>297</td>\n",
              "      <td>março 2019</td>\n",
              "      <td>0.75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>298</th>\n",
              "      <td>298</td>\n",
              "      <td>abril 2019</td>\n",
              "      <td>0.57</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>299</th>\n",
              "      <td>299</td>\n",
              "      <td>maio 2019</td>\n",
              "      <td>0.13</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bf3169af-e09f-41ee-b4d8-72cefc602c9e')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-bf3169af-e09f-41ee-b4d8-72cefc602c9e button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-bf3169af-e09f-41ee-b4d8-72cefc602c9e');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "taxa = np.array(ipca[\"Taxa\"])#  instancia um objeto da classe numpy.ndarray, recebe como parâmetro o objeto dataframe instanciado anteriormente\n",
        "#com a coluna do IPCA.\n",
        "plt.title('IPCA entre janeiro de 2019 e 2022')# utiliza método title para plotar título do gráfico\n",
        "\n",
        "plt.xlabel('Meses')# metodo xlabel define nome para eixo x\n",
        "\n",
        "\n",
        "plt.ylabel('Variação')# metodo ylabel define nome para eixo y\n",
        "\n",
        "\n",
        "plt.plot(taxa,color = 'blue',marker = 'o')# método plot cria gráfico, recebe um objeto numpy.ndarray, uma cor e um marcador como parâmetros;\n",
        "# x = meses; y = IPCA\n",
        "\n",
        "plt.grid('True') # método grid cria uma grade no plano de fundo do gráfico, default = 'False', recebe parâmetro String 'True' ou 'False'.\n",
        "\n",
        "plt.show()# método show apresenta último gráfico criado com o módulo plt"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "ebmW6L-hsa7P",
        "outputId": "e316e73b-71f5-480d-a585-d46a658c4b9a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "display(ipca['Taxa'].describe())# método describe do pandas retorna informações estatisticas"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 173
        },
        "id": "0ci1DGMS4rg7",
        "outputId": "74311f5b-c96c-4835-a5e4-cacf0ba2433f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "count    37.000000\n",
              "mean      0.509189\n",
              "std       0.430054\n",
              "min      -0.380000\n",
              "25%       0.210000\n",
              "50%       0.510000\n",
              "75%       0.860000\n",
              "max       1.350000\n",
              "Name: Taxa, dtype: float64"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **TAXA SELIC**"
      ],
      "metadata": {
        "id": "hZzxRueuLiKO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "selic = pd.read_csv('/content/drive/MyDrive/TDE/taxa_selic.csv',sep=';') # instancia um objeto da classe pandas.core.frame.DataFrame pelo método read_csv\n",
        "#recebe path do dataset no drive como parâmetro, também um caractere separador de colunas\n",
        "\n",
        "\n",
        "selic = selic.rename({'11 - Taxa de juros - Selic - % a.d.': 'Taxa Selic'},axis=1)# método rename renomeia a nova coluna criada recebendo um dicionário como parâmetro\n",
        "\n",
        "selic = selic.drop([776],axis=0)# método drop retira linha ou coluna do dataframe e recebe como parâmetro uma seleção e um eixo, foi removida a última linha.\n",
        "\n",
        "selic['Taxa Selic'] = selic['Taxa Selic'].replace(',','.',regex = True).astype(float)#método replace substitui valores do dataset de maneira dinâmica, no caso transfomando valores \n",
        "#de String para float. Recebe como parêmetro os valores a serem susbstitídos, e método astype muda o tipo da série de dados\n",
        "\n",
        "selic = selic.reset_index()# método reset_index cria uma nova coluna a partir do índice anterior com o numero de dias\n",
        "\n",
        "selic = selic.rename({'index': 'Dias'},axis=1)# método rename renomeia a nova coluna criada recebendo um dicionário como parâmetro\n",
        "\n",
        "selic = selic[0:757]# seleciona os 756 dias"
      ],
      "metadata": {
        "id": "sFL62gOZWuKo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Gráfico de Barras\n",
        "c=np.array(selic['Dias'])#  instancia um objeto da classe numpy.ndarray, recebe como parâmetro o objeto dataframe instanciado anteriormente\n",
        "#com a coluna do IPCA. c = dias\n",
        "\n",
        "d=np.array(selic[\"Taxa Selic\"])#  instancia um objeto da classe numpy.ndarray, recebe como parâmetro o objeto dataframe instanciado anteriormente\n",
        "#com a coluna do IPCA. d = variação selic\n",
        "\n",
        "plt.title('Selic entre janeiro de 2019 e 2022')# utiliza método title para plotar título do gráfico\n",
        "\n",
        "plt.xlabel('Dias')# metodo xlabel define nome para eixo x\n",
        "\n",
        "plt.ylabel('Variação')# metodo ylabel define nome para eixo y\n",
        "\n",
        "plt.bar(c,d,width=1,color='red')# método bar cria um gráfico de barras recebe como parâmetros os eixos x,y; a largura das barras, e a cor\n",
        "\n",
        "plt.grid('True')# método grid cria uma grade no plano de fundo\n",
        "\n",
        "plt.show()# método show apresenta último gráfico criado com o módulo plt\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "uq-uC9BoKuFO",
        "outputId": "e43b3e51-dc3b-4b54-87c3-7d0b3c988057"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "display(selic['Taxa Selic'].describe())# método describe do pandas retorna informações estatisticas"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 173
        },
        "id": "-LaiRQapumMa",
        "outputId": "67904ed9-1af8-4fa0-b741-c8bbffc97217"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "count    757.000000\n",
              "mean       0.017053\n",
              "std        0.007390\n",
              "min        0.007469\n",
              "25%        0.010379\n",
              "50%        0.017089\n",
              "75%        0.024620\n",
              "max        0.034749\n",
              "Name: Taxa Selic, dtype: float64"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}
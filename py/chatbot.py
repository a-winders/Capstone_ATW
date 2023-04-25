{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [
        "RDRNBrQlKQ-K",
        "gS1PZp408ckK"
      ],
      "authorship_tag": "ABX9TyO1JVgvU62CKq4hRxAnu0b6",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/a-winders/Capstone_ATW/blob/main/Chatbot.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Importing Libraries"
      ],
      "metadata": {
        "id": "KIJR4GFVJl8H"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 101,
      "metadata": {
        "id": "XNwjpc-nJUTO"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Mounts Google Drive"
      ],
      "metadata": {
        "id": "9DGxCsWUJtFV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/gdrive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zSbhLEYrJvZU",
        "outputId": "e859d1f8-6a58-4657-8299-2fcb52294dd3"
      },
      "execution_count": 102,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/gdrive; to attempt to forcibly remount, call drive.mount(\"/content/gdrive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Importing Datasets"
      ],
      "metadata": {
        "id": "RDRNBrQlKQ-K"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Imports different scraped .csv movie files"
      ],
      "metadata": {
        "id": "NcOWTGXT12Aa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "metadata = pd.read_csv('/content/gdrive/MyDrive/Bellarmine/CS430_Data_Files/archive/movies_metadata.csv')\n",
        "ratings = pd.read_csv('/content/gdrive/MyDrive/Bellarmine/CS430_Data_Files/archive/ratings.csv')\n",
        "credits = pd.read_csv('/content/gdrive/MyDrive/Bellarmine/CS430_Data_Files/archive/credits.csv')\n",
        "keywords = pd.read_csv('/content/gdrive/MyDrive/Bellarmine/CS430_Data_Files/archive/keywords.csv')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3o1RYxOoxull",
        "outputId": "46155e0b-5843-449e-8c92-f813d94fbfb7"
      },
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-103-94022b624a60>:1: DtypeWarning: Columns (10) have mixed types. Specify dtype option on import or set low_memory=False.\n",
            "  metadata = pd.read_csv('/content/gdrive/MyDrive/Bellarmine/CS430_Data_Files/archive/movies_metadata.csv')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Displays first row from each imported dataset"
      ],
      "metadata": {
        "id": "rv7xK_CG46Gs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "metadata.head(1)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 261
        },
        "id": "pjqzJ9st4i3n",
        "outputId": "3de96eaa-60f2-4c7f-fd67-d03696d4ec89"
      },
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   adult                              belongs_to_collection    budget  \\\n",
              "0  False  {'id': 10194, 'name': 'Toy Story Collection', ...  30000000   \n",
              "\n",
              "                                              genres  \\\n",
              "0  [{'id': 16, 'name': 'Animation'}, {'id': 35, '...   \n",
              "\n",
              "                               homepage   id    imdb_id original_language  \\\n",
              "0  http://toystory.disney.com/toy-story  862  tt0114709                en   \n",
              "\n",
              "  original_title                                           overview  ...  \\\n",
              "0      Toy Story  Led by Woody, Andy's toys live happily in his ...  ...   \n",
              "\n",
              "  release_date      revenue runtime                          spoken_languages  \\\n",
              "0   1995-10-30  373554033.0    81.0  [{'iso_639_1': 'en', 'name': 'English'}]   \n",
              "\n",
              "     status  tagline      title  video vote_average vote_count  \n",
              "0  Released      NaN  Toy Story  False          7.7     5415.0  \n",
              "\n",
              "[1 rows x 24 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-88bfcf2e-915f-4868-b4de-ea34c7acd9d7\">\n",
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
              "      <th>adult</th>\n",
              "      <th>belongs_to_collection</th>\n",
              "      <th>budget</th>\n",
              "      <th>genres</th>\n",
              "      <th>homepage</th>\n",
              "      <th>id</th>\n",
              "      <th>imdb_id</th>\n",
              "      <th>original_language</th>\n",
              "      <th>original_title</th>\n",
              "      <th>overview</th>\n",
              "      <th>...</th>\n",
              "      <th>release_date</th>\n",
              "      <th>revenue</th>\n",
              "      <th>runtime</th>\n",
              "      <th>spoken_languages</th>\n",
              "      <th>status</th>\n",
              "      <th>tagline</th>\n",
              "      <th>title</th>\n",
              "      <th>video</th>\n",
              "      <th>vote_average</th>\n",
              "      <th>vote_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>False</td>\n",
              "      <td>{'id': 10194, 'name': 'Toy Story Collection', ...</td>\n",
              "      <td>30000000</td>\n",
              "      <td>[{'id': 16, 'name': 'Animation'}, {'id': 35, '...</td>\n",
              "      <td>http://toystory.disney.com/toy-story</td>\n",
              "      <td>862</td>\n",
              "      <td>tt0114709</td>\n",
              "      <td>en</td>\n",
              "      <td>Toy Story</td>\n",
              "      <td>Led by Woody, Andy's toys live happily in his ...</td>\n",
              "      <td>...</td>\n",
              "      <td>1995-10-30</td>\n",
              "      <td>373554033.0</td>\n",
              "      <td>81.0</td>\n",
              "      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>\n",
              "      <td>Released</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Toy Story</td>\n",
              "      <td>False</td>\n",
              "      <td>7.7</td>\n",
              "      <td>5415.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1 rows × 24 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-88bfcf2e-915f-4868-b4de-ea34c7acd9d7')\"\n",
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
              "          document.querySelector('#df-88bfcf2e-915f-4868-b4de-ea34c7acd9d7 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-88bfcf2e-915f-4868-b4de-ea34c7acd9d7');\n",
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
          "execution_count": 104
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ratings.head(1)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "zwuhfWNt4yl3",
        "outputId": "5307a6b7-8bdf-4d5c-855f-22a83386013c"
      },
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   userId  movieId  rating   timestamp\n",
              "0       1      110     1.0  1425941529"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2be13584-aead-4cf8-a745-487d91e226f4\">\n",
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
              "      <th>userId</th>\n",
              "      <th>movieId</th>\n",
              "      <th>rating</th>\n",
              "      <th>timestamp</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>110</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1425941529</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2be13584-aead-4cf8-a745-487d91e226f4')\"\n",
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
              "          document.querySelector('#df-2be13584-aead-4cf8-a745-487d91e226f4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-2be13584-aead-4cf8-a745-487d91e226f4');\n",
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
          "execution_count": 105
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "credits.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "p9OMqrFN40aq",
        "outputId": "45bae2a9-6b69-4e9b-dd33-ce4f15e894ce"
      },
      "execution_count": 106,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                                cast  \\\n",
              "0  [{'cast_id': 14, 'character': 'Woody (voice)',...   \n",
              "1  [{'cast_id': 1, 'character': 'Alan Parrish', '...   \n",
              "2  [{'cast_id': 2, 'character': 'Max Goldman', 'c...   \n",
              "3  [{'cast_id': 1, 'character': \"Savannah 'Vannah...   \n",
              "4  [{'cast_id': 1, 'character': 'George Banks', '...   \n",
              "\n",
              "                                                crew     id  \n",
              "0  [{'credit_id': '52fe4284c3a36847f8024f49', 'de...    862  \n",
              "1  [{'credit_id': '52fe44bfc3a36847f80a7cd1', 'de...   8844  \n",
              "2  [{'credit_id': '52fe466a9251416c75077a89', 'de...  15602  \n",
              "3  [{'credit_id': '52fe44779251416c91011acb', 'de...  31357  \n",
              "4  [{'credit_id': '52fe44959251416c75039ed7', 'de...  11862  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e0c9617e-bfe5-43b2-b09a-712e57223176\">\n",
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
              "      <th>cast</th>\n",
              "      <th>crew</th>\n",
              "      <th>id</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>[{'cast_id': 14, 'character': 'Woody (voice)',...</td>\n",
              "      <td>[{'credit_id': '52fe4284c3a36847f8024f49', 'de...</td>\n",
              "      <td>862</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>[{'cast_id': 1, 'character': 'Alan Parrish', '...</td>\n",
              "      <td>[{'credit_id': '52fe44bfc3a36847f80a7cd1', 'de...</td>\n",
              "      <td>8844</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>[{'cast_id': 2, 'character': 'Max Goldman', 'c...</td>\n",
              "      <td>[{'credit_id': '52fe466a9251416c75077a89', 'de...</td>\n",
              "      <td>15602</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>[{'cast_id': 1, 'character': \"Savannah 'Vannah...</td>\n",
              "      <td>[{'credit_id': '52fe44779251416c91011acb', 'de...</td>\n",
              "      <td>31357</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>[{'cast_id': 1, 'character': 'George Banks', '...</td>\n",
              "      <td>[{'credit_id': '52fe44959251416c75039ed7', 'de...</td>\n",
              "      <td>11862</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e0c9617e-bfe5-43b2-b09a-712e57223176')\"\n",
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
              "          document.querySelector('#df-e0c9617e-bfe5-43b2-b09a-712e57223176 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e0c9617e-bfe5-43b2-b09a-712e57223176');\n",
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
          "execution_count": 106
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "keywords.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "nrVA2n6n43jw",
        "outputId": "b5bef1c1-7473-4cdf-fe31-9e4ef75bcb7c"
      },
      "execution_count": 107,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      id                                           keywords\n",
              "0    862  [{'id': 931, 'name': 'jealousy'}, {'id': 4290,...\n",
              "1   8844  [{'id': 10090, 'name': 'board game'}, {'id': 1...\n",
              "2  15602  [{'id': 1495, 'name': 'fishing'}, {'id': 12392...\n",
              "3  31357  [{'id': 818, 'name': 'based on novel'}, {'id':...\n",
              "4  11862  [{'id': 1009, 'name': 'baby'}, {'id': 1599, 'n..."
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-68e6996c-0f7c-463d-b8f3-c3b75bb0b6f8\">\n",
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
              "      <th>id</th>\n",
              "      <th>keywords</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>862</td>\n",
              "      <td>[{'id': 931, 'name': 'jealousy'}, {'id': 4290,...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>8844</td>\n",
              "      <td>[{'id': 10090, 'name': 'board game'}, {'id': 1...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>15602</td>\n",
              "      <td>[{'id': 1495, 'name': 'fishing'}, {'id': 12392...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>31357</td>\n",
              "      <td>[{'id': 818, 'name': 'based on novel'}, {'id':...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>11862</td>\n",
              "      <td>[{'id': 1009, 'name': 'baby'}, {'id': 1599, 'n...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-68e6996c-0f7c-463d-b8f3-c3b75bb0b6f8')\"\n",
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
              "          document.querySelector('#df-68e6996c-0f7c-463d-b8f3-c3b75bb0b6f8 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-68e6996c-0f7c-463d-b8f3-c3b75bb0b6f8');\n",
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
          "execution_count": 107
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Trimming data"
      ],
      "metadata": {
        "id": "gS1PZp408ckK"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Prints the number of rows for each column in each dataset"
      ],
      "metadata": {
        "id": "Dbs_5BFf2Eyc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"metadata shape:\",metadata.shape)\n",
        "print(\"metadata columns name:\", metadata.columns)\n",
        "\n",
        "print(\"ratings shape:\",ratings.shape)\n",
        "print(\"ratings columns name:\", list(ratings.columns))\n",
        "\n",
        "print(\"credits shape:\",credits.shape)\n",
        "print(\"columns name:\", list(credits.columns))\n",
        "\n",
        "print(\"keywords shape:\",keywords.shape)\n",
        "print(\"columns name:\", list(keywords.columns))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q0Rx4hyr4CrC",
        "outputId": "d89df372-5bb1-4a9f-dff6-bc4ec6915d97"
      },
      "execution_count": 108,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "metadata shape: (45466, 24)\n",
            "metadata columns name: Index(['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id',\n",
            "       'imdb_id', 'original_language', 'original_title', 'overview',\n",
            "       'popularity', 'poster_path', 'production_companies',\n",
            "       'production_countries', 'release_date', 'revenue', 'runtime',\n",
            "       'spoken_languages', 'status', 'tagline', 'title', 'video',\n",
            "       'vote_average', 'vote_count'],\n",
            "      dtype='object')\n",
            "ratings shape: (26024289, 4)\n",
            "ratings columns name: ['userId', 'movieId', 'rating', 'timestamp']\n",
            "credits shape: (45476, 3)\n",
            "columns name: ['cast', 'crew', 'id']\n",
            "keywords shape: (46419, 2)\n",
            "columns name: ['id', 'keywords']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Removes some of the dataframes to save processing time"
      ],
      "metadata": {
        "id": "VxCZobgW2mB0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "metadata = pd.read_csv('/content/gdrive/MyDrive/Bellarmine/CS430_Data_Files/archive/movies_metadata.csv') \n",
        "metadata = metadata.iloc[0:10000,:]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "myZ1AY4D2ldA",
        "outputId": "5b665c2e-f9e1-4548-bedf-c2e3e9d3298e"
      },
      "execution_count": 109,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-109-f7602ee0df36>:1: DtypeWarning: Columns (10) have mixed types. Specify dtype option on import or set low_memory=False.\n",
            "  metadata = pd.read_csv('/content/gdrive/MyDrive/Bellarmine/CS430_Data_Files/archive/movies_metadata.csv')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Converts *id* in the listed columns to **int** data type"
      ],
      "metadata": {
        "id": "GzmbNQh52y59"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "keywords['id'] = keywords['id'].astype('int')\n",
        "credits['id'] = credits['id'].astype('int')\n",
        "metadata['id'] = metadata['id'].astype('int')"
      ],
      "metadata": {
        "id": "ok8GleaQ2yV9"
      },
      "execution_count": 110,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Consolidates the **keywords** and **credits** dataframes"
      ],
      "metadata": {
        "id": "4oL8Fc903ZNR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "metadata = metadata.merge(credits, on='id')\n",
        "metadata = metadata.merge(keywords, on='id')\n",
        "metadata.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "THPLWtOe5s7a",
        "outputId": "608b799c-8b19-42aa-d24c-09c1974df087"
      },
      "execution_count": 111,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10048, 27)"
            ]
          },
          "metadata": {},
          "execution_count": 111
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Saves **cast**, **crew**, **keywords**, and **genres** columns into a new variable called **features**\n",
        "<br> Changes dataype of **features** to allow for easier parsing"
      ],
      "metadata": {
        "id": "a0rqVC-X6CLx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from ast import literal_eval\n",
        "features = ['cast', 'crew', 'keywords', 'genres']\n",
        "for feature in features:\n",
        "  metadata[feature] = metadata[feature].apply(literal_eval)"
      ],
      "metadata": {
        "id": "ULurRS0O6IyD"
      },
      "execution_count": 112,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Grabs the name of the director for each movie from **crew**"
      ],
      "metadata": {
        "id": "BJJBHFEK52I4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def get_director(x):\n",
        "    for i in x:\n",
        "        if i['job'] == 'Director':\n",
        "            return i['name']\n",
        "    return np.nan"
      ],
      "metadata": {
        "id": "u92kWsBE7Mgq"
      },
      "execution_count": 113,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Returns a list of actors, genres, and keywords"
      ],
      "metadata": {
        "id": "0tQc8XHE7Ngi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def get_list(x):\n",
        "    if isinstance(x, list): \n",
        "        names = [i['name'] for i in x] \n",
        "\n",
        "        if len(names) > 3:\n",
        "            names = names[:3]\n",
        "        return names\n",
        "\n",
        "    return []"
      ],
      "metadata": {
        "id": "Qt3APR4G7VX-"
      },
      "execution_count": 114,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Adds the parsed data back into the dataframe"
      ],
      "metadata": {
        "id": "5rbnqVRZ7agJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "metadata['director'] = metadata['crew'].apply(get_director)\n",
        "\n",
        "features = ['cast', 'keywords', 'genres']\n",
        "for feature in features:\n",
        "    metadata[feature] = metadata[feature].apply(get_list)\n",
        "\n",
        "metadata[['title', 'cast', 'director', 'keywords', 'genres']].head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "h5pP_SsE6M-m",
        "outputId": "886a743e-afc7-4e61-f2e4-cb648ecf0170"
      },
      "execution_count": 115,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                         title  \\\n",
              "0                    Toy Story   \n",
              "1                      Jumanji   \n",
              "2             Grumpier Old Men   \n",
              "3            Waiting to Exhale   \n",
              "4  Father of the Bride Part II   \n",
              "\n",
              "                                                cast         director  \\\n",
              "0                [Tom Hanks, Tim Allen, Don Rickles]    John Lasseter   \n",
              "1     [Robin Williams, Jonathan Hyde, Kirsten Dunst]     Joe Johnston   \n",
              "2         [Walter Matthau, Jack Lemmon, Ann-Margret]    Howard Deutch   \n",
              "3  [Whitney Houston, Angela Bassett, Loretta Devine]  Forest Whitaker   \n",
              "4         [Steve Martin, Diane Keaton, Martin Short]    Charles Shyer   \n",
              "\n",
              "                                            keywords  \\\n",
              "0                               [jealousy, toy, boy]   \n",
              "1  [board game, disappearance, based on children'...   \n",
              "2       [fishing, best friend, duringcreditsstinger]   \n",
              "3  [based on novel, interracial relationship, sin...   \n",
              "4                 [baby, midlife crisis, confidence]   \n",
              "\n",
              "                         genres  \n",
              "0   [Animation, Comedy, Family]  \n",
              "1  [Adventure, Fantasy, Family]  \n",
              "2             [Romance, Comedy]  \n",
              "3      [Comedy, Drama, Romance]  \n",
              "4                      [Comedy]  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-7a4d72f4-8283-46c5-9892-6832459f61a2\">\n",
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
              "      <th>title</th>\n",
              "      <th>cast</th>\n",
              "      <th>director</th>\n",
              "      <th>keywords</th>\n",
              "      <th>genres</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Toy Story</td>\n",
              "      <td>[Tom Hanks, Tim Allen, Don Rickles]</td>\n",
              "      <td>John Lasseter</td>\n",
              "      <td>[jealousy, toy, boy]</td>\n",
              "      <td>[Animation, Comedy, Family]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Jumanji</td>\n",
              "      <td>[Robin Williams, Jonathan Hyde, Kirsten Dunst]</td>\n",
              "      <td>Joe Johnston</td>\n",
              "      <td>[board game, disappearance, based on children'...</td>\n",
              "      <td>[Adventure, Fantasy, Family]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Grumpier Old Men</td>\n",
              "      <td>[Walter Matthau, Jack Lemmon, Ann-Margret]</td>\n",
              "      <td>Howard Deutch</td>\n",
              "      <td>[fishing, best friend, duringcreditsstinger]</td>\n",
              "      <td>[Romance, Comedy]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Waiting to Exhale</td>\n",
              "      <td>[Whitney Houston, Angela Bassett, Loretta Devine]</td>\n",
              "      <td>Forest Whitaker</td>\n",
              "      <td>[based on novel, interracial relationship, sin...</td>\n",
              "      <td>[Comedy, Drama, Romance]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Father of the Bride Part II</td>\n",
              "      <td>[Steve Martin, Diane Keaton, Martin Short]</td>\n",
              "      <td>Charles Shyer</td>\n",
              "      <td>[baby, midlife crisis, confidence]</td>\n",
              "      <td>[Comedy]</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7a4d72f4-8283-46c5-9892-6832459f61a2')\"\n",
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
              "          document.querySelector('#df-7a4d72f4-8283-46c5-9892-6832459f61a2 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-7a4d72f4-8283-46c5-9892-6832459f61a2');\n",
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
          "execution_count": 115
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Wordsoup"
      ],
      "metadata": {
        "id": "e4tdai5a8XSG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Converts all words to lowercase and removes all spaces between them"
      ],
      "metadata": {
        "id": "UGpHScoj--mZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def clean_data(x):\n",
        "    if isinstance(x, list):\n",
        "        return [str.lower(i.replace(\" \", \"\")) for i in x] \n",
        "    else:\n",
        "        \n",
        "        if isinstance(x, str):\n",
        "            return str.lower(x.replace(\" \", \"\"))\n",
        "        else:\n",
        "            return ''\n",
        "          \n",
        "         \n",
        "\n",
        "features = ['cast', 'keywords', 'director', 'genres']\n",
        "\n",
        "for feature in features:\n",
        "  metadata[feature] = metadata[feature].apply(clean_data)"
      ],
      "metadata": {
        "id": "Ngw0dm3S6Xgy"
      },
      "execution_count": 117,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Consolidates **features** into a wordsoup by iterating through each row of the dataframe and adding a space inbetween words"
      ],
      "metadata": {
        "id": "BnmeKSAT_h2v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def create_soup(x):\n",
        "    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])\n",
        "\n",
        "metadata['soup'] = metadata.apply(create_soup, axis=1)\n",
        "metadata[['title', 'soup', 'cast', 'director', 'keywords', 'genres']].head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 250
        },
        "id": "z6T8vR_j6hN6",
        "outputId": "19173072-dc91-476b-93a0-1ffc58de9d41"
      },
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                         title  \\\n",
              "0                    Toy Story   \n",
              "1                      Jumanji   \n",
              "2             Grumpier Old Men   \n",
              "3            Waiting to Exhale   \n",
              "4  Father of the Bride Part II   \n",
              "\n",
              "                                                soup  \\\n",
              "0  jealousy toy boy tomhanks timallen donrickles ...   \n",
              "1  boardgame disappearance basedonchildren'sbook ...   \n",
              "2  fishing bestfriend duringcreditsstinger walter...   \n",
              "3  basedonnovel interracialrelationship singlemot...   \n",
              "4  baby midlifecrisis confidence stevemartin dian...   \n",
              "\n",
              "                                             cast        director  \\\n",
              "0                [tomhanks, timallen, donrickles]    johnlasseter   \n",
              "1     [robinwilliams, jonathanhyde, kirstendunst]     joejohnston   \n",
              "2        [waltermatthau, jacklemmon, ann-margret]    howarddeutch   \n",
              "3  [whitneyhouston, angelabassett, lorettadevine]  forestwhitaker   \n",
              "4         [stevemartin, dianekeaton, martinshort]    charlesshyer   \n",
              "\n",
              "                                            keywords  \\\n",
              "0                               [jealousy, toy, boy]   \n",
              "1  [boardgame, disappearance, basedonchildren'sbook]   \n",
              "2        [fishing, bestfriend, duringcreditsstinger]   \n",
              "3  [basedonnovel, interracialrelationship, single...   \n",
              "4                  [baby, midlifecrisis, confidence]   \n",
              "\n",
              "                         genres  \n",
              "0   [animation, comedy, family]  \n",
              "1  [adventure, fantasy, family]  \n",
              "2             [romance, comedy]  \n",
              "3      [comedy, drama, romance]  \n",
              "4                      [comedy]  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-6be46343-4488-4320-a0cf-b84233e4fd19\">\n",
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
              "      <th>title</th>\n",
              "      <th>soup</th>\n",
              "      <th>cast</th>\n",
              "      <th>director</th>\n",
              "      <th>keywords</th>\n",
              "      <th>genres</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Toy Story</td>\n",
              "      <td>jealousy toy boy tomhanks timallen donrickles ...</td>\n",
              "      <td>[tomhanks, timallen, donrickles]</td>\n",
              "      <td>johnlasseter</td>\n",
              "      <td>[jealousy, toy, boy]</td>\n",
              "      <td>[animation, comedy, family]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Jumanji</td>\n",
              "      <td>boardgame disappearance basedonchildren'sbook ...</td>\n",
              "      <td>[robinwilliams, jonathanhyde, kirstendunst]</td>\n",
              "      <td>joejohnston</td>\n",
              "      <td>[boardgame, disappearance, basedonchildren'sbook]</td>\n",
              "      <td>[adventure, fantasy, family]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Grumpier Old Men</td>\n",
              "      <td>fishing bestfriend duringcreditsstinger walter...</td>\n",
              "      <td>[waltermatthau, jacklemmon, ann-margret]</td>\n",
              "      <td>howarddeutch</td>\n",
              "      <td>[fishing, bestfriend, duringcreditsstinger]</td>\n",
              "      <td>[romance, comedy]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Waiting to Exhale</td>\n",
              "      <td>basedonnovel interracialrelationship singlemot...</td>\n",
              "      <td>[whitneyhouston, angelabassett, lorettadevine]</td>\n",
              "      <td>forestwhitaker</td>\n",
              "      <td>[basedonnovel, interracialrelationship, single...</td>\n",
              "      <td>[comedy, drama, romance]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Father of the Bride Part II</td>\n",
              "      <td>baby midlifecrisis confidence stevemartin dian...</td>\n",
              "      <td>[stevemartin, dianekeaton, martinshort]</td>\n",
              "      <td>charlesshyer</td>\n",
              "      <td>[baby, midlifecrisis, confidence]</td>\n",
              "      <td>[comedy]</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6be46343-4488-4320-a0cf-b84233e4fd19')\"\n",
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
              "          document.querySelector('#df-6be46343-4488-4320-a0cf-b84233e4fd19 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-6be46343-4488-4320-a0cf-b84233e4fd19');\n",
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
          "execution_count": 118
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Captures user input and and creates wordsoup for building recommendations"
      ],
      "metadata": {
        "id": "gxYDriBaAIJz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def get_genres():\n",
        "  genres = input(\"What movie genre would you like to watch? (type 'skip' to skip) \")\n",
        "  return genres\n",
        "\n",
        "def get_actors():\n",
        "  actors = input(\"What actor would you like to see? (type 'skip' to skip) \")\n",
        "  return actors\n",
        "\n",
        "def get_directors():\n",
        "  directors = input(\"Write the name of a director that you like. (type 'skip' to skip) \")\n",
        "  return directors\n",
        "\n",
        "def get_keywords():\n",
        "  keywords = input(\"What are some keywords that describe your ideal movie? (e.g. crime, romance, action) (type 'skip' to skip) \")\n",
        "  keywords = \" \".join([\"\".join(n.split()) for n in keywords.lower().split(',')])\n",
        "  return keywords\n",
        "\n",
        "def get_searchTerms():\n",
        "  searchTerms = [] \n",
        "  genres = get_genres()\n",
        "  if genres != 'skip':\n",
        "    searchTerms.append(genres)\n",
        "\n",
        "  actors = get_actors()\n",
        "  if actors != 'skip':\n",
        "    searchTerms.append(actors)\n",
        "\n",
        "  directors = get_directors()\n",
        "  if directors != 'skip':\n",
        "    searchTerms.append(directors)\n",
        "\n",
        "  keywords = get_keywords()\n",
        "  if keywords != 'skip':\n",
        "    searchTerms.append(keywords)\n",
        "  \n",
        "  return searchTerms"
      ],
      "metadata": {
        "id": "I-JZWOdp6tvF"
      },
      "execution_count": 126,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Executes machine learning function and returns recommendations"
      ],
      "metadata": {
        "id": "D0iiIILdBafp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "\n",
        "def make_recommendation(metadata=metadata):\n",
        "  new_row = metadata.iloc[-1,:].copy() \n",
        "  \n",
        "\n",
        "  searchTerms = get_searchTerms()  \n",
        "  new_row.iloc[-1] = \" \".join(searchTerms) \n",
        "  \n",
        "  metadata = metadata.append(new_row)\n",
        "  \n",
        "  count = CountVectorizer(stop_words='english')\n",
        "  count_matrix = count.fit_transform(metadata['soup'])\n",
        "\n",
        "  cosine_sim2 = cosine_similarity(count_matrix, count_matrix) \n",
        "  \n",
        "  sim_scores = list(enumerate(cosine_sim2[-1,:]))\n",
        "  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)\n",
        "\n",
        "  ranked_titles = []\n",
        "  for i in range(1, 11):\n",
        "    indx = sim_scores[i][0]\n",
        "    ranked_titles.append([metadata['title'].iloc[indx], metadata['imdb_id'].iloc[indx]])\n",
        "  \n",
        "  return ranked_titles\n",
        "\n",
        "make_recommendation()"
      ],
      "metadata": {
        "id": "IOyqRGLa7Cj7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "28022f61-9bbe-4354-f822-561ee1fc6a83"
      },
      "execution_count": 127,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "What movie genre would you like to watch? (type 'skip' to skip) drama\n",
            "What actor would you like to see? (type 'skip' to skip) leonardo dicaprio\n",
            "Write the name of a director that you like. (type 'skip' to skip) martin scorsese\n",
            "What are some keywords that describe your ideal movie? (e.g. crime, romance, action) (type 'skip' to skip) skip\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-127-633133e52cf2>:13: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  metadata = metadata.append(new_row)\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['Ill Gotten Gains', 'tt0119352'],\n",
              " ['Jails, Hospitals & Hip-Hop', 'tt0210130'],\n",
              " ['Lotto Land', 'tt0113695'],\n",
              " ['Other Voices Other Rooms', 'tt0119845'],\n",
              " ['Went to Coney Island on a Mission from God... Be Back by Five',\n",
              "  'tt0157182'],\n",
              " ['Cremaster 2', 'tt0214605'],\n",
              " ['Little Boy Blue', 'tt0119547'],\n",
              " ['Salsa', 'tt0096030'],\n",
              " ['The Town Is Quiet', 'tt0234988'],\n",
              " ['Behind the Sun', 'tt0291003']]"
            ]
          },
          "metadata": {},
          "execution_count": 127
        }
      ]
    }
  ]
}
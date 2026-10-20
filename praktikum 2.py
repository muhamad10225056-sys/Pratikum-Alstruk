{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMy6FLptqlKGFkRtCHLcnHX",
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
        "<a href=\"https://colab.research.google.com/github/muhamad10225056-sys/Pratikum-Alstruk/blob/main/praktikum%202.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vjFtX8ooryue",
        "outputId": "e22e7494-f316-4d97-8cb6-ce517379a3c5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Harga per buku       : Rp12500\n",
            "Jumlah beli          : 4\n",
            "Total harga          : Rp50000\n",
            "Sisa pembagian % 2000: 0\n",
            "Total setelah diskon : Rp45000\n"
          ]
        }
      ],
      "source": [
        "harga = 12500\n",
        "jumlah = 4\n",
        "\n",
        "total_harga = harga * jumlah\n",
        "sisa_pembagian = total_harga % 2000\n",
        "total_diskon = total_harga - 5000\n",
        "\n",
        "print(f\"Harga per buku       : Rp{harga}\")\n",
        "print(f\"Jumlah beli          : {jumlah}\")\n",
        "print(f\"Total harga          : Rp{total_harga}\")\n",
        "print(f\"Sisa pembagian % 2000: {sisa_pembagian}\")\n",
        "print(f\"Total setelah diskon : Rp{total_diskon}\")"
      ]
    }
  ]
}
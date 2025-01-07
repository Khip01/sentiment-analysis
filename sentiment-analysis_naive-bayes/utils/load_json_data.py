# ini untuk memuat data json 
# yang diubah menjadi sekumpulan data sesuai model data.py

import json

from models.data import Data


def load_data_from_json(data_path: str) -> list[Data]:
    # membuka data json
    j = open(data_path)

    datas_json = json.load(j)

    # mengubah data json ke model data
    datas_model: list[Data] = [Data(d["sentence"], d["label"]) for d in datas_json]

    return datas_model